# 🎓 QR Code Linker

A secure, Azure-hosted web application that automates the process of linking student IDs to unique QR codes. Designed for educational environments, this system enables a professor to generate, print, and track QR codes, while students scan and submit their IDs through a simple web interface.

---

## 🚀 Project Goals

- Automate the lifecycle of QR code creation, printing, and linking
- Ensure secure, one-time association between QR codes and student IDs
- Prevent abuse through non-predictable URLs, CAPTCHA, and token expiry
- Deploy using CI/CD pipelines for rapid iteration and reliability

---

## 🧱 Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Frontend     | HTML/CSS/JavaScript (or React) |
| Backend      | Node.js / Python / .NET Core   |
| Database     | Azure SQL                      |
| Hosting      | Azure App Service              |
| DevOps       | GitHub Actions (CI/CD)         |

---

## 🔐 Security Features

- Non-guessable QR code URLs (UUID-based)
- CAPTCHA protection on student submission
- One-time-use tokens with expiry logic
- HTTPS enforced across all endpoints
- Input validation and audit logging

---

## 📦 Folder Structure
/frontend # Student-facing UI and admin dashboard
/backend # API endpoints and business logic
/docs # Architecture diagrams, user flows, etc. 
/infra # Azure deployment scripts and pipeline configs README.md


# Project overview and setup instructions

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/student-qr-linker.git
   cd student-qr-linker

2. Install dependencies

(Instructions will vary based on chosen backend and frontend stack)

3. Configure Azure SQL
- Create a database instance
- Add connection string to environment variables

4. Deploy to Azure
- Use Azure App Service
- Configure GitHub Actions for CI/CD

# MVP Scope
- QR code generation and status tracking
- Student scan and ID submission
- Admin login and dashboard
- Security features (CAPTCHA, token expiry, HTTPS)

# License
This project is open-source under the MIT License

# Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.