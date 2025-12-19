# Project Nexus

**Project Nexus** is a multi-functional Python application integrating various tools and utilities into a single, cohesive interface. Built with Tkinter, it serves as a personal assistant dashboard.

## 🚀 Features

*   **Security**: Encrypt and Decrypt text using Fernet encryption.
*   **Voice Integration**: Text-to-Speech (TTS) and Speech-to-Text (STT) capabilities.
*   **Utilities**:
    *   Weather Information (OpenWeatherMap API)
    *   Calculator
    *   Sticky Notes
    *   To-Do List
    *   Quick Notes
    *   Expense Tracker
    *   Password Generator
    *   Stopwatch
    *   Random Number Generator
*   **Entertainment**:
    *   Dual Player Snake Game
    *   Typing Speed Challenge
    *   YouTube Search Helper
*   **Global**:
    *   Language Translator (Google Translate)

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Tarunpathak001/Project-Nexus.git
    cd Project-Nexus
    ```

2.  **Create a virtual environment (Recommended)**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Setup**:
    *   Copy `.env.example` to `.env`
    *   Add your OpenWeatherMap API key if you want weather functionality.
    ```bash
    # Windows (PowerShell)
    Copy-Item .env.example .env
    ```

## ▶️ Usage

Run the main application:
```bash
python main.py
```

## 📂 Project Structure

```
Project-Nexus/
├── assets/             # Images and static resources
├── src/
│   └── project_nexus/
│       ├── core/       # Business logic (API, Encryption, TTS)
│       ├── ui/         # GUI Components
│       │   ├── frames/ # Individual feature screens
│       │   └── app.py  # Main Application Controller
│       └── config.py   # Configuration
├── main.py             # Entry point
└── requirements.txt    # Dependencies
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request.

## 📄 License

This project is open-source.
# Project-Nexus
