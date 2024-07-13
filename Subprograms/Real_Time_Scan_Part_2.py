import os
import hashlib
import sqlite3
import shutil
import getpass
import psutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from concurrent.futures import ThreadPoolExecutor
from plyer import notification
from winotify import Notification, audio  # type: ignore

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
directory = os.path.join(parent_dir, 'Logo')
logo_path = os.path.join(directory, "Logo.ico")

# Define file extension categories
file_categories = {
    "Executable Files": [".exe", ".com", ".bat", ".msi", ".scr"],
    "Script Files": [".js", ".vbs", ".wsf", ".ps1"],
    "Document Files": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".rtf", ".pdf"],
    "Compressed Files": [".zip", ".rar", ".7z"],
    "Macro Files": [".mde", ".mdb", ".xla", ".xlam"],
    "Email Files": [".eml", ".msg"],
    "Image Files": [".jpg", ".jpeg", ".png", ".gif"],
    "Media Files": [".mp3", ".mp4"],
    "System Files": [".dll", ".sys", ".drv", ".ocx"],
    "Database Files": [".sql", ".db", ".sqlite"],
    "Web Files": [".html", ".htm", ".php", ".asp", ".aspx"],
    "Configuration Files": [".ini", ".cfg", ".inf"],
    "Virtual Machine Files": [".vmdk", ".vdi", ".vhd"],
    "Font Files": [".ttf", ".otf"],
    "CAD Files": [".dwg", ".dxf"],
    "Scripting Files": [".sh", ".csh", ".ksh", ".bash"],
    "Template Files": [".dotx", ".xltx", ".potx"],
    "Installer Files": [".apk", ".dmg", ".pkg"],
    "Specialized Files": [".reg", ".url", ".lnk"],
    "3D Model Files": [".obj", ".fbx"],
    "Binary and Game Files": [".bin", ".rom"],
    "Log and Presentation Files": [".log", ".prs"],
    "C/C++ Source Files": [".cpp", ".c", ".h"],
    "Python Script": [".py"],
    "Ruby Script": [".rb"],
    "Perl Script": [".pl"],
    "Swift Source File": [".swift"],
    "C# Source File": [".cs"],
    "Lua Script": [".lua"],
    "Tcl Script": [".tcl"],
    "R Script": [".r"],
    "Mathematical and Statistical Files": [".mat", ".rdata"],
    "Adobe Flash Files": [".swf", ".fla"],
    "Font Files": [".fon", ".fnt"],
    "Financial Files": [".qbw", ".qbb", ".qfx"],
    "Email Data Files": [".pst", ".ost"],
    "Virtualization Files": [".vhdx", ".ova"],
    "Game Files": [".pak", ".wad"],
    "GIS Files": [".shp", ".gpx"],
    "Presentation Files": [".key", ".odp"],
    "Font Files": [".ttf", ".fnt"],
    "Log and Report Files": [".dmp", ".rpt"],
    "Developer Project Files": [".proj", ".sln"],
    "Archive Files": [".tar.gz", ".tar.bz2"],
    "Scripting and Automation Files": [".ahk", ".scpt"],
    "Executable Files on Unix-like Systems": [".run", ".app"],
    "Configuration Files": [".env", ".yaml", ".yml"],
    "Text and Source Code Files": [".json", ".xml"],
    "Engineering Files": [".sldprt", ".sldasm"],
    "Graphical Files": [".svg", ".eps"],
    "Spreadsheets and Databases": [".ods", ".accdb"],
    "Miscellaneous Files": [".cfg", ".properties", ".toml", ".conf"]
}

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_ext = os.path.splitext(file_path)[1].lower()
            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    self.process_file_async(file_path)
                    break

    def process_file_async(self, file_path):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(process_file, file_path)

def process_file(file_path):
    time.sleep(1.5)  # Simulate processing time
    hashes, file_path = get_file_hashes(file_path)
    if hashes:
        check_hashes_in_db(file_path, hashes)

def get_file_hashes(file_path):
    hashes = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256()}
    
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                for hash_obj in hashes.values():
                    hash_obj.update(chunk)
    except (FileNotFoundError, PermissionError) as e:
        return None, file_path
    except Exception as e:
        return None, file_path
    
    return {name: hash_obj.hexdigest() for name, hash_obj in hashes.items()}, file_path

def check_hashes_in_db(file_path, hashes):
    parent_dir = os.path.dirname(script_dir)
    directory = os.path.join(parent_dir, 'Hash Database')
    db_file = os.path.join(directory, "hashes.db")
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    found = False
    
    for hash_type, hash_value in hashes.items():
        cursor.execute(f"SELECT * FROM {hash_type} WHERE hash = ?", (hash_value,))
        result = cursor.fetchone()
        
        if result:
            quarantine_file(file_path)
            found = True
            break
    
    conn.close()

def quarantine_file(file_path):
    toast = Notification(app_id="Secure Drive",
                         title="🚨 Virus Detected!",
                         msg="The file has been placed in quarantine.",
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
    
    shutil.move(file_path, new_path)
    print(f"🚩 File '{file_name}' Quarantined Successfully!")
    print(f"🔒 The file contains a virus and has been placed in quarantine.")

def get_all_drives():
    partitions = psutil.disk_partitions()
    drives = [partition.mountpoint for partition in partitions]
    return drives

if __name__ == "__main__":
    drives_to_watch = get_all_drives()

    event_handler = NewFileHandler()
    observer = Observer()

    for drive in drives_to_watch:
        observer.schedule(event_handler, drive, recursive=True)

    observer.start()
    try:
        print("🔍 Real-time file monitoring started.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("⏹️ Monitoring stopped by user.")
    observer.join()
