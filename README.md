NETWORK PORT SCANNER V2.0

AUTHOR:
Thammineni Chidvila

PROJECT DESCRIPTION:
This project is a Python-based TCP Network Port Scanner developed for learning cybersecurity and network programming concepts.

The scanner accepts a target IP address and a custom port range from the user. It then scans each port within the specified range, determines whether the port is open or closed, identifies common services, and generates a scan report.

FEATURES:

* User-defined target IP address
* Custom port range scanning
* TCP port scanning using Python sockets
* Service identification for common ports
* Open port counting
* Scan start and end timestamps
* Results saved to a text report
* Error handling for invalid port input
* Modular code using functions

TECHNOLOGIES USED:

* Python 3
* Socket Programming
* Datetime Module

PROJECT STRUCTURE:

Network-Port-Scanner/
│
├── scanner.py
├── results.txt
└── README.txt

HOW TO RUN:

1. Open VS Code or Python IDLE.
2. Open scanner.py.
3. Run the program.

Command:

python scanner.py

4. Enter:

   * Target IP Address
   * Starting Port
   * Ending Port

Example:

Enter Target IP Address: 127.0.0.1
Enter Starting Port: 1
Enter Ending Port: 100

OUTPUT:
The program displays:

* Open ports found
* Total number of open ports
* Scan start and finish times

A report is also generated in:

results.txt

CONCEPTS LEARNED:

* Networking Fundamentals
* TCP/IP Communication
* Port Scanning
* Socket Programming
* Functions
* Loops
* Dictionaries
* File Handling
* Error Handling
* Cybersecurity Reconnaissance

FUTURE IMPROVEMENTS:

* Multithreaded Scanning
* Banner Grabbing
* Service Version Detection
* Ping Sweep Functionality
* GUI Interface using Tkinter
* Export Reports to PDF
* Vulnerability Detection Module

LEARNING OUTCOME:
This project helped in understanding how network scanners work and provided hands-on experience with Python programming, networking, and cybersecurity concepts.
