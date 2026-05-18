# 🔐 Secure Code Auditor

A professional Flask-based cybersecurity tool that performs static code analysis on Python files using Bandit.

The application scans uploaded Python files for common security vulnerabilities and generates detailed vulnerability reports with severity analysis and remediation guidance.

---

# 📌 Project Overview

Secure Code Auditor is a beginner-friendly cybersecurity project developed for:

- Internship submission
- College mini project
- GitHub portfolio
- Cybersecurity demonstrations

The system uses Bandit to identify insecure coding practices in Python source code and displays the results in a modern cybersecurity dashboard.

---

# 🚀 Features

## ✅ File Upload System

- Upload Python source files
- Validate `.py` files
- Temporary secure file handling

---

## ✅ Static Code Analysis

Uses **Bandit** to detect:

- Hardcoded passwords
- Weak hashing algorithms
- Command injection vulnerabilities
- Unsafe subprocess usage
- Dangerous Python functions
- Insecure coding practices

---

## ✅ Vulnerability Dashboard

Displays:

- Total vulnerabilities
- High severity issues
- Medium severity issues
- Low severity issues
- Security score

---

## ✅ Scan Results

Detailed results including:

- Vulnerability name
- Severity level
- Line number
- Description
- Recommended fixes

---

## ✅ Report Generation

Generate downloadable:

- JSON reports
- PDF security reports

---

## ✅ Professional UI

Modern dark-themed cybersecurity interface with:

- Sidebar navigation
- Dashboard cards
- Severity indicators
- Responsive layout
- Cybersecurity styling

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | Web Framework |
| HTML | Frontend Structure |
| CSS | Styling |
| JavaScript | Frontend Interaction |
| Bandit | Static Code Analysis |
| ReportLab | PDF Report Generation |

---

# 📁 Project Structure

```bash
secure-code-auditor/
│
├── app.py
├── requirements.txt
│
├── scanner/
│   └── scanner.py
│
├── uploads/
│
├── reports/
│
├── sample_files/
│   └── test_vulnerable.py
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── results.html
│   └── reports.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/secure-code-auditor.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd secure-code-auditor
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# 🧪 Testing The Application

Use the sample vulnerable Python file:

```bash
sample_files/test_vulnerable.py
```

The scanner should detect:

- Weak hashing
- Command injection
- Unsafe subprocess usage
- Dangerous system calls

---

# 📄 PDF Reports

The application can generate professional PDF vulnerability reports containing:

- Scan summary
- Vulnerability details
- Severity classification
- Risk explanation
- Security recommendations

---

# 🔒 Security Features

- Static code analysis
- Severity-based vulnerability classification
- Secure file validation
- Automated report generation
- Security score calculation

---



# 📚 Learning Outcomes

This project helped in understanding:

- Static Application Security Testing (SAST)
- Secure coding practices
- Python security vulnerabilities
- Flask web development
- Cybersecurity reporting
- Vulnerability assessment workflows

---

# 🎯 Internship Objective

This project was developed as part of a cybersecurity internship task to demonstrate:

- Python programming
- Secure code analysis
- Vulnerability detection
- Web application development
- Cybersecurity concepts

---

# 👨‍💻 Author

Pinninti Deekshith Redddy 

---

# 📜 License

This project is developed for educational and internship purposes.
