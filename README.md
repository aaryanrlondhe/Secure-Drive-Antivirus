# Secure Drive Antivirus

## Overview
Secure Drive Antivirus is a comprehensive open-source antivirus solution designed to provide robust real-time protection against malware and other malicious threats. This project includes several key features that ensure the safety and security of your files and system. Among these features are real-time file scanning, which continuously monitors your system for potential threats; full system scans, which thoroughly check every file and folder on your device for malicious software; and virus detection for particular files, allowing you to target specific areas of concern. Additionally, the quarantine functionality isolates infected files, preventing them from causing further harm while allowing you to review and address them safely. Developed with the goal of providing reliable and effective protection, Secure Drive Antivirus aims to mitigate the impact of various types of malware, ensuring that your system remains secure and your data stays protected. 

## Features
Secure Drive Antivirus offers a robust suite of features designed to protect your system from malicious threats:

- **Real-Time File Monitoring** <a name="real-time-file-monitoring"></a>: This feature monitors file creation events in real-time using watchdog, detecting newly created files and scanning them for potential threats to ensure immediate protection.

- **Full System Scan** <a name="full-system-scan"></a>: This functionality allows for the scanning of all files and directories on specified drives or the entire system. It provides comprehensive scanning reports and progress indicators, ensuring thorough and transparent protection.

- **Virus Detection for a Particular File** <a name="virus-detection-for-a-particular-file"></a>: This feature checks individual files against a database of known virus signatures. It notifies users of detected threats and provides options for quarantine, allowing for targeted security measures.

- **Quarantine Functionality** <a name="quarantine-functionality"></a>: Infected files are quarantined to a secure directory. Users receive notifications when files are quarantined, preventing their execution and ensuring that threats are contained.

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

## About Malware Hash Database
Secure Drive Antivirus uses a malware hash database from the GitHub repository [Malware-Hash-Database](https://github.com/aaryanrlondhe/Malware-Hash-Database). This repository is regularly updated with the latest malware hashes to ensure that Secure Drive Antivirus can detect the most recent threats effectively. The database is maintained by the same person who created Secure Drive Antivirus, ensuring seamless integration and consistent updates. The database contains a collection of known malware signatures, which the antivirus software uses to identify and quarantine infected files. By leveraging this continuously updated repository, Secure Drive Antivirus stays current with emerging threats and enhances its capability to protect your system.

## Contributing

We welcome contributions to improve Secure Drive Antivirus. You can fork the repository, make your changes, and submit a pull request. To contribute, follow these steps:

#### 1. Fork the Repository
Click the "Fork" button at the top right of the repository page to create a copy of the repository under your GitHub account.

#### 2. Clone the Repository
Clone your forked repository to your local machine using
```bash
git clone https://github.com/aaryanrlondhe/Secure-Drive-Antivirus.git
```

#### 3. Create a Branch
Create a new branch for your feature or bug fix using
```bash
git checkout -b feature-branch-name.
```

#### 4. Make Changes
Implement your changes in your local repository.

#### 5. Commit Changes
Commit your changes with a clear and descriptive message using
```bash
git commit -m "Description of your changes".
```

#### 6. Push Changes
Push your changes to your forked repository on GitHub using git push origin feature-branch-name.

#### 7. Submit a Pull Request
Go to the original repository on GitHub and click "New Pull Request." Compare your feature branch with the base branch, add relevant comments, and submit the pull request.

## License
Secure Drive Antivirus is licensed under the MIT License. See the [LICENSE file](https://github.com/aaryanrlondhe/Secure-Drive-Antivirus/blob/main/LICENSE) for more details.

