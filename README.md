# Python Security Log Reader

The Python Security Log Reader is a beginner cybersecurity project designed to analyze login activity from a log file.

The program reads security log entries line by line and identifies successful and failed login attempts. It extracts IP addresses associated with failed logins and uses a Python dictionary to track how many failed attempts originate from each IP address.

If an IP address reaches a defined number of failed login attempts, the program generates a security alert to highlight potentially suspicious activity.

## Features

- Reads security logs from a text file
- Detects successful and failed login attempts
- Extracts IP addresses from log entries
- Counts failed login attempts for each IP address
- Identifies repeated failed login activity
- Generates alerts for potentially suspicious IP addresses
- Displays a simple security log analysis report

## Technologies Used

- Python
- File Handling
- Dictionaries
- For Loops
- Conditional Statements
- String Manipulation

## Example

The program can analyze log entries such as:

2026-09-29 10:02:20 LOGIN FAILED user=admin ip=192.168.1.20

If the same IP address generates multiple failed login attempts, the program tracks the activity and can generate an alert.

Example output:

===== SECURITY LOG REPORT =====

Successful logins: 2
Failed logins: 6

Failed attempts by IP:

192.168.1.20 : 5
10.0.0.5 : 1

===== SECURITY ALERTS =====

ALERT: 192.168.1.20 has 5 failed login attempts

## What I Learned

Through this project, I practised working with Python file handling, loops, conditional statements, dictionaries, string methods, and counters.

I also learned how basic Python programming concepts can be applied to cybersecurity tasks such as analyzing authentication logs and identifying repeated failed login attempts.

## Future Improvements

Future versions of this project could include:

- CSV and JSON log support
- Different alert severity levels
- Timestamp analysis
- Username-based failed login detection
- Configurable alert thresholds
- Exporting suspicious activity to a report
- Improved error handling
