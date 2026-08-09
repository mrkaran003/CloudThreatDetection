#  Cloud Threat Detection

A Flask-based cloud security application for uploading and analyzing security log files using a rule-based threat detection engine. The system calculates risk scores, classifies threat severity, stores analysis results, and displays security information through a web dashboard.

---

##  Project Overview

Cloud Threat Detection is a web-based security monitoring application developed using Python and Flask.

The application allows an authenticated user to upload supported security log files, analyze security-related information, calculate a risk score, determine threat severity, and store the analysis results in a database.

The project also provides dashboard, history, reporting, profile, settings, administration, and file-management functionality.

---

##  Objectives

- Upload and analyze security log files.
- Detect suspicious security activity.
- Calculate a threat risk score.
- Classify threats according to severity.
- Store uploaded-file and threat information.
- Display security statistics through a dashboard.
- Maintain analysis history.
- Provide report generation functionality.
- Provide user and administration features.

---

##  Main Features

###  Authentication

- User registration
- User login
- User logout
- Session-based authentication

###  File Upload

Supported security-file formats configured by the application include:

- CSV
- TXT
- LOG
- JSON
- PCAP

Uploaded files are validated before analysis.

###  Threat Detection

The current detection engine evaluates security-related fields such as:

- Failed login attempts
- Unknown IP activity
- Malware detection indicators

The system calculates a risk score and assigns a severity level.


### Risk Classification

| Risk Score | Severity |
| ---------- | -------- |
| 0-29       | Low      |
| 30-59      | Medium   |
| 60-79      | High     |
| 80-100     | Critical |

###  Dashboard

The dashboard provides security statistics such as:

- Uploaded files
- Detected threats
- High-risk activity
- Critical-risk activity
- Risk scores
- System status

###  Threat History

The application stores threat-analysis results so previous detections can be reviewed.

###  Reports

The application provides report-generation functionality, including PDF and Excel report routes.

###  User Management

The application includes:

- Profile management
- Settings
- Administration
- User-role management
- File management

---

## Threat Detection Workflow

```text
User Login
    |
Upload Security File
    |
File Validation
    |
Save Uploaded File
    |
Read Security Data
    |
Calculate Risk Score
    |
Determine Severity
    |
Generate Threat Prediction
    |
Store Result in Database
    |
Display Result on Dashboard