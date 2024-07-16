import subprocess
import os
import sys

# Define functions for each case
def run_full_scan():
    try:
        # Execute the Python script using subprocess
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        sub_dir1 = "Subprograms"  
        file_name = "Full_Scan_Part_1.py" 
        file_path = os.path.join(script_dir, sub_dir1, file_name)
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"🚫 Error: Try Again! {e}")
    except FileNotFoundError:
        print("🚫 Error: Script Not Found! Please check the file path.")

def scan_file():
    try:
        # Execute the Python script using subprocess
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        sub_dir1 = "Subprograms"   
        file_name = "File_Scan.py" 
        file_path = os.path.join(script_dir, sub_dir1, file_name)
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"🚫 Error: Try Again! {e}")
    except FileNotFoundError:
        print("🚫 Error: Script Not Found! Please check the file path.")

def turn_on_real_time_scanning():
    try:
        # Execute the Python script using subprocess
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        sub_dir1 = "Subprograms"  
        file_name = "Real_Time_Scan_Part_1.py" 
        file_path = os.path.join(script_dir, sub_dir1, file_name)
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"🚫 Error: Try Again! {e}")
    except FileNotFoundError:
        print("🚫 Error: Script Not Found! Please check the file path.")

def turn_off_real_time_scanning():
    print("🛑 Turning off real-time scanning...")

def open_quarantine_folder():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    sub_dir1 = "Quarantine"   
    quarantine_folder = os.path.join(script_dir, sub_dir1)
    print("📂 Opening Quarantine Folder...")
    os.startfile(quarantine_folder)

def update_antivirus_signatures():
    try:
        # Execute the Python script using subprocess
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        sub_dir1 = "Subprograms"   
        file_name = "Update_Database.py" 
        file_path = os.path.join(script_dir, sub_dir1, file_name)
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"🚫 Error: Try Again! {e}")
    except FileNotFoundError:
        print("🚫 Error: Script Not Found! Please check the file path.")

def close_antivirus():
    print("🔒 Closing antivirus... See you again soon!")
    sys.exit()

# Define a function to simulate switch-case
def switch_case(case):
    switcher = {
        1: run_full_scan,
        2: scan_file,
        3: turn_on_real_time_scanning,
        4: open_quarantine_folder,
        5: update_antivirus_signatures,
        6: close_antivirus,
        # Add more cases as needed
    }
    # Get the function corresponding to the case
    func = switcher.get(case, lambda: print("❌ Invalid option"))
    # Execute the function
    func()

# Main program loop
while True:
    print("\n🔐 Secure Drive Options:")
    print("1. 🖥️ \t Run Full Scan on System")
    print("2. 📁 \tScan a File")
    print("3. 🟢 \tTurn On Real Time Scanning")
    print("4. 📂 \tOpen Quarantine Folder")
    print("5. 🔄 \tUpdate Antivirus Signatures")
    print("6. ❌ \tClose Antivirus")
    
    try:
        choice = input("Enter your choice (1-6): ")
        case_number = int(choice)
        
        if case_number == 6:
            print("🔒 Closing Antivirus... See you again soon!")
            break
        
        switch_case(case_number)
    except ValueError:
        print("❌ Invalid input. Please enter a number between 1 and 7.")
