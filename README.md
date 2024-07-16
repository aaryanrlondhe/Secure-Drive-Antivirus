# Secure Drive Antivirus

## Overview
Secure Drive Antivirus is a comprehensive open spourcev antivirus solution designed to provide real-time protection against malware and other malicious threats. This project includes features such as real-time file scanning, full system scan, virus detection for particular files, and quarantine functionalities.Secure Drive Antivirus is developed to ensure the safety and security of your files and system by providing robust protection against various types of malware. With features like real-time scanning and quarantine, it aims to prevent and mitigate the impact of malicious software.


## Features
Secure Drive Antivirus offers the following features:

- Real-time File Monitoring <a name="real-time-file-monitoring"></a>
Monitors file creation events in real-time using watchdog.
Detects newly created files and scans them for potential threats.
- Full System Scan <a name="full-system-scan"></a>
Allows scanning of all files and directories on specified drives or the entire system.
Provides comprehensive scanning reports and progress indicators.
- Virus Detection for a Particular File <a name="virus-detection-for-a-particular-file"></a>
Checks individual files against a database of known virus signatures.
Notifies users of detected threats and provides options for quarantine.
- Quarantine Functionality <a name="quarantine-functionality"></a>
Quarantines infected files to a secure directory.
Displays notifications when files are quarantined and prevents their execution.
Installation
To install Secure Drive Antivirus, follow these steps:

## Clone the repository:
'''
git clone https://github.com/aaryanrlondhe/Secure-Drive-Antivirus.git
'''
cd Secure-Drive-Antivirus
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python main.py
Usage
Real-time Scanning
Real-time scanning is enabled by default. It continuously monitors the system and alerts the user if any threat is detected. The system tray icon indicates the current status of the antivirus.

Full System Scan
To perform a full system scan, use the following command in the application interface:

bash
Copy code
python main.py --full-scan
This command initiates a comprehensive scan of all files and directories on the system.

File Scan
To scan a specific file, use the following command:

bash
Copy code
python main.py --scan-file <path_to_file>
Replace <path_to_file> with the path of the file you wish to scan.

Quarantine
Suspicious files detected during scans are moved to a quarantine folder. This folder is located inside the "Secure Drive" directory. To create a quarantine folder, you can use:

bash
Copy code
mkdir -p "C:/Secure Drive/quarantine"
Quarantined files can be reviewed and restored if found to be safe.

Configuration
Configuration settings for Secure Drive Antivirus can be found in the config.json file. This file allows you to customize various parameters, including:

Scan intervals
Log file locations
Quarantine folder path
Notification settings
To modify the settings, open config.json in a text editor and adjust the values as needed.

Contributing
We welcome contributions to enhance Secure Drive Antivirus. To contribute, follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-branch
Make your changes and commit them:
bash
Copy code
git commit -m "Description of changes"
Push to the branch:
bash
Copy code
git push origin feature-branch
Create a pull request on GitHub.
License
Secure Drive Antivirus is licensed under the MIT License. See the LICENSE file for more details.

