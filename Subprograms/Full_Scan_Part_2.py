import os
import hashlib
import sqlite3
import shutil
import getpass
from plyer import notification
from winotify import Notification, audio  # type: ignore
import psutil
import concurrent.futures

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
directory = os.path.join(parent_dir, 'Logo')
global logo_path
logo_path = os.path.join(directory, "Logo.ico")

def get_file_hashes(file_path):
    hashes = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256()}
    
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                for hash_obj in hashes.values():
                    hash_obj.update(chunk)
    except PermissionError:
        print(f"🚫 Permission denied: '{file_path}'")
        return None
    except Exception as e:
        print(f"⚠️ Error reading file '{file_path}': {e}")
        return None
    
    return {name: hash_obj.hexdigest() for name, hash_obj in hashes.items()}

def check_hashes_in_db(hashes, file_path):
    username = getpass.getuser()
    parent_dir = os.path.dirname(script_dir)
    directory = os.path.join(parent_dir, 'Hash Database')
    db_file = os.path.join(directory, "hashes.db")

    if not os.path.exists(db_file):
        raise FileNotFoundError(f"🚫 Database file '{db_file}' not found.")

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    found = False
    
    for hash_type, hash_value in hashes.items():
        cursor.execute(f"SELECT * FROM {hash_type} WHERE hash = ?", (hash_value,))
        result = cursor.fetchone()
        
        if result:
            print(f"🔍 Hash of type {hash_type.upper()} found in the database for file: {file_path}")
            found = True
            toast = Notification(app_id="Secure Drive",
                                 title="🚨 Virus Detected!",
                                 msg=f"The File '{file_path}' Contains Virus and is Placed in Quarantine",
                                 icon=logo_path)
            toast.set_audio(audio.Default, loop=False)
            toast.show()
            
            script1_dir = os.path.dirname(os.path.abspath(__file__))
            parent1_dir = os.path.dirname(script1_dir)
            quarantine_folder = os.path.join(parent1_dir, 'Quarantine')
            if not os.path.exists(quarantine_folder):
                os.makedirs(quarantine_folder)
        
            file_name = os.path.basename(file_path)
            new_path = os.path.join(quarantine_folder, file_name)
        
            try:
                shutil.move(file_path, new_path)
                print(f"🔒 File '{file_name}' quarantined successfully to '{quarantine_folder}'.")
            except Exception as e:
                print(f"⚠️ Error quarantining file '{file_name}': {e}")
        
    conn.close()

def list_all_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            yield file_path

def get_all_drives():
    partitions = psutil.disk_partitions()
    drives = [partition.device for partition in partitions if partition.fstype != '']
    return drives

def main():
    root_dirs = get_all_drives()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(list_all_files, root_dir): root_dir for root_dir in root_dirs if os.path.exists(root_dir)}
        for future in concurrent.futures.as_completed(futures):
            try:
                for file_path in future.result():
                    print(f"🔍 Processing file: {file_path}")
                    hashes = get_file_hashes(file_path)
                    if hashes:
                        check_hashes_in_db(hashes, file_path)
            except Exception as e:
                print(f"⚠️ Error processing {futures[future]}: {e}")

if __name__ == "__main__":
    main()
