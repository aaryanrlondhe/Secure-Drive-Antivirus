import os
import subprocess
import psutil

def real_time_scan():
    print("🛠️ Initializing real-time scan script...")
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(script_dir)
        sub_dir2 = "Subprograms"
        file_name = "Real_Time_Scan_Part_2.py"
        file_path = os.path.join(parent_dir, sub_dir2, file_name)
        
        # Run the script in the background using subprocess.Popen for Windows
        subprocess.Popen(['python', file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("🚀 Real-time scan initiated. Use 'q' to terminate the scan at any time.")

        while True:
            user_input = input()
            if user_input.lower() == 'q':
                print("🔄 Terminating scan process...")
                # Find and terminate the process by name
                for proc in psutil.process_iter():
                    if proc.name() == "python.exe" and file_name in " ".join(proc.cmdline()):
                        proc.terminate()
                        break
                print("✅ Real-time scan process successfully terminated.")
                break
            else:
                print("❓ Unknown command. Please use 'q' to terminate the scan.")

    except FileNotFoundError:
        print("🚫 Error: File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    real_time_scan()
