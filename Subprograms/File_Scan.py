import hashlib
import sqlite3
import shutil
import os
from plyer import notification
import getpass
from winotify import Notification, audio  # type: ignore
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
import sys
import time

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
        return {name: hash_obj.hexdigest() for name, hash_obj in hashes.items()}
    except (FileNotFoundError, IOError) as e:
        print(f"🚫 Error reading file: {e}")
        return None

def select_file():
    try:
        app = QApplication(sys.argv)
        mainWin = QMainWindow()
        mainWin.setWindowTitle('File Selection')
        mainWin.setWindowIcon(QIcon(logo_path))  # Set the main window icon

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        dialog = QFileDialog(mainWin, "Select a File", "", "All Files (*);;Text Files (*.txt)", options=options)
        dialog.setFixedSize(1000, 800)  # Set the dialog size to 800x600 pixels

        if dialog.exec_():
            file_path = dialog.selectedFiles()[0]
            if file_path:
                hashes = get_file_hashes(file_path)
                if hashes:
                    return hashes, file_path
    except Exception as e:
        print(f"🚫 Error selecting file: {e}")
    return None, None

def check_hashes_in_db(hashes, file_path):
    try:
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
                found = True
                toast = Notification(app_id="Secure Drive",
                                     title="🚨 Virus Detected!",
                                     msg="The file has been placed in quarantine.",
                                     icon=logo_path)
                toast.set_audio(audio.Default, loop=False)
                toast.show()
                script1_dir = os.path.dirname(os.path.abspath(__file__))
                parent1_dir = os.path.dirname(script1_dir)
                quarantine_folder  = os.path.join(parent1_dir, 'Quarantine')
                if not os.path.exists(quarantine_folder):
                    os.makedirs(quarantine_folder)
            
                file_name = os.path.basename(file_path)
                new_path = os.path.join(quarantine_folder, file_name)
                shutil.move(file_path, new_path)
            
                print(f"🚩 File '{file_name}' Quarantined Successfully!")
                print(f"🔒 The file contains a virus and has been placed in quarantine.")
                time.sleep(2)
                        
        if not found:
            print("✅ The file is clean!")
            toast = Notification(app_id="Secure Drive",
                                 title="✅ No Virus Found",
                                 msg="The file is clean!",
                                 icon=logo_path)
            toast.set_audio(audio.Default, loop=False)
            toast.show()
            time.sleep(2)
            
        conn.close()
    except sqlite3.Error as e:
        print(f"🛑 Database error: {e}")
    except (shutil.Error, OSError) as e:
        print(f"🛑 File operation error: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_hashes, file_path = select_file()
    if file_hashes:
        check_hashes_in_db(file_hashes, file_path)
