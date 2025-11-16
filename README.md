# 🔍 Website Technology Analyzer

Detect technologies, frameworks, and tools used by any website using Wappalyzer.

## 📁 Structure

```
hack_tools/
├── README.md                          # Main documentation
└── website_analyzer/                  # Website analysis tool
    ├── README.md                      # Detailed guide
    ├── requirements.txt               # Dependencies
    └── tech_detector.py               # Main tool
```

## ✨ Features

- 🎯 Accurate technology detection
- 📊 Comprehensive technology listing
- 💾 JSON export for further analysis
- ⚡ Fast and simple to use
- 🌐 Works with any website

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/blackangiliq/hack_tools.git
cd hack_tools/website_analyzer

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python tech_detector.py
```

Then enter the target URL when prompted.

### Example

```
🔍 Website Technology Detector
   Powered by Wappalyzer

🎯 Enter website URL: example.com

============================================================
🔍 WEBSITE TECHNOLOGY DETECTOR
============================================================

🌐 Analyzing: https://example.com
⏳ Loading Wappalyzer database...
📡 Fetching website data...
🔍 Detecting technologies...

============================================================
✅ TECHNOLOGIES DETECTED
============================================================

📊 Found 12 technologies:

   1. Apache
   2. Bootstrap
   3. jQuery
   4. MySQL
   5. PHP
   ...

💾 Results saved to: technologies.json
```

## 📋 What Can Be Detected?

- **Web Servers:** Apache, Nginx, IIS
- **Frameworks:** React, Vue.js, Django, Laravel
- **CMS:** WordPress, Drupal, Joomla
- **Analytics:** Google Analytics
- **CDN:** Cloudflare, Akamai
- **JavaScript Libraries:** jQuery, Bootstrap
- **And much more!**

## 📋 Requirements

- Python 3.7+
- python-Wappalyzer
- Internet connection

## ⚠️ Disclaimer

This tool is for educational and authorized security testing purposes only.

## 📝 License

MIT License - Feel free to use and modify.

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests.

---

**Created with ❤️ for the cybersecurity community**
