# Secure Drive Antivirus

## Overview
Secure Drive Antivirus is a comprehensive open-source antivirus solution designed to provide robust real-time protection against malware and other malicious threats. This project includes several key features that ensure the safety and security of your files and system. Among these features are real-time file scanning, which continuously monitors your system for potential threats; full system scans, which thoroughly check every file and folder on your device for malicious software; and virus detection for particular files, allowing you to target specific areas of concern. Additionally, the quarantine functionality isolates infected files, preventing them from causing further harm while allowing you to review and address them safely. Developed with the goal of providing reliable and effective protection, Secure Drive Antivirus aims to mitigate the impact of various types of malware, ensuring that your system remains secure and your data stays protected. 

## Features
Secure Drive Antivirus offers a robust suite of features designed to protect your system from malicious threats:

- Real-time File Monitoring <a name="real-time-file-monitoring"></a>: This feature monitors file creation events in real-time using watchdog, detecting newly created files and scanning them for potential threats to ensure immediate protection.

- Full System Scan <a name="full-system-scan"></a>: This functionality allows for the scanning of all files and directories on specified drives or the entire system. It provides comprehensive scanning reports and progress indicators, ensuring thorough and transparent protection.

- Virus Detection for a Particular File <a name="virus-detection-for-a-particular-file"></a>: This feature checks individual files against a database of known virus signatures. It notifies users of detected threats and provides options for quarantine, allowing for targeted security measures.

- Quarantine Functionality <a name="quarantine-functionality"></a>: Infected files are quarantined to a secure directory. Users receive notifications when files are quarantined, preventing their execution and ensuring that threats are contained.

## Cloning the repository:
```bash
git clone https://github.com/aaryanrlondhe/Secure-Drive-Antivirus.git
```
Navigate to the project directory
```bash
cd Secure-Drive-Antivirus
```
## Installing Dependencies
To install the required dependencies, use the following command:
```bash
pip install -r requirements.txt
```
## Executing the Application
```bash
python main.py
```

## Contributing
We welcome contributions to enhance Secure Drive Antivirus. To contribute, follow these steps:

### Fork the repository.
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

