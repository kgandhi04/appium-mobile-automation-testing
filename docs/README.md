# Appium Mobile Automation Testing

This repository contains a detailed framework for mobile app automation using Appium. It supports testing for both Android and iOS applications.

---

## 🚀 Features
- Automated tests for login functionality (valid and invalid login scenarios).
- Configurable environment setup via `config.yaml`.
- Cross-platform support for Android and iOS.
- HTML and console test reports.

---

## 📂 Project Structure
```plaintext
appium-mobile-automation-testing/
├── tests/
│   ├── test_login.py          # Test cases for login functionality
├── config/
│   └── config.yaml            # Configuration file for environment setup
├── reports/                   # Test reports (generated dynamically)
└── docs/
    └── README.md              # Project documentation
```

---

## 🛠️ Setup Instructions

### Prerequisites
1. **Appium Server**:
   - Install Appium via npm:
     ```bash
     npm install -g appium
     ```

2. **Android SDK**:
   - Install Android Studio and set up the SDK.

3. **Python Environment**:
   - Python 3.7 or higher installed.

4. **Dependencies**:
   - Install required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

---

## ▶️ Running Tests

1. Start the Appium server:
   ```bash
   appium
   ```

2. Run the test cases:
   ```bash
   python -m unittest tests/test_login.py
   ```

3. View the results:
   - Reports will be saved in the `reports/` directory.

---

## 📝 Configuration

Update `config/config.yaml` to set your desired environment, app path, and device details:
```yaml
default:
  platformName: "Android"
  platformVersion: "11"
  deviceName: "emulator-5554"
  appPath: "/path/to/your-app.apk"
  automationName: "UiAutomator2"
```

---

## 🧩 Contributing

Contributions are welcome! Feel free to fork the repository and create pull requests.

---

## 📄 License
This project is licensed under the MIT License.
