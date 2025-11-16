# 🔍 Website Technology Analyzer

Detect and analyze technologies, frameworks, and tools used by any website.

## Features

- 🎯 Accurate technology detection
- 📊 Comprehensive technology listing
- 💾 JSON export for further analysis
- ⚡ Fast and simple to use
- 🌐 Works with any website

## Installation

```bash
pip install python-Wappalyzer
```

## Usage

### Command Line

```bash
python tech_detector.py
```

Then enter the target URL when prompted.

### As a Module

```python
from Wappalyzer import Wappalyzer, WebPage

wappalyzer = Wappalyzer.latest()
webpage = WebPage.new_from_url('https://example.com')
technologies = wappalyzer.analyze(webpage)

print(technologies)
```

## Example Output

```
============================================================
🔍 WEBSITE TECHNOLOGY DETECTOR
============================================================

🌐 Analyzing: https://example.com

✅ TECHNOLOGIES DETECTED
============================================================

📊 Found 12 technologies:

   1. Apache
   2. Bootstrap
   3. Cloudflare
   4. Font Awesome
   5. Google Analytics
   6. jQuery
   7. MySQL
   8. Nginx
   9. PHP
  10. React
  11. Webpack
  12. WordPress

💾 Results saved to: technologies.json
```

## Output File

The tool saves results in `technologies.json`:

```json
{
  "url": "https://example.com",
  "technologies": [
    "Apache",
    "Bootstrap",
    "jQuery",
    ...
  ],
  "count": 12
}
```

## What Can Be Detected?

- **Web Servers:** Apache, Nginx, IIS
- **Frameworks:** React, Angular, Vue.js, Django, Laravel
- **CMS:** WordPress, Drupal, Joomla
- **Analytics:** Google Analytics, Matomo
- **CDN:** Cloudflare, Akamai
- **JavaScript Libraries:** jQuery, Bootstrap
- **And much more!**

## Use Cases

- 🔒 Security assessment
- 🔍 Competitor analysis
- 📊 Market research
- 🛠️ Technology stack discovery
- 📈 Web development insights

## Requirements

- Python 3.7+
- python-Wappalyzer
- Internet connection

## Troubleshooting

**Error: "No technologies detected"**
- Check if the website is accessible
- Some websites block automated analysis
- Try with a different URL

**Error: "Connection failed"**
- Verify internet connection
- Check if the URL is correct
- Some websites may be behind firewall

## Credits

Powered by [Wappalyzer](https://www.wappalyzer.com/) - the leading technology profiler.

## License

MIT License

