from Wappalyzer import Wappalyzer, WebPage
import json

def analyze_website(url):
    """Detect website technologies"""
    print("\n" + "="*60)
    print("🔍 WEBSITE TECHNOLOGY DETECTOR")
    print("="*60 + "\n")
    
    try:
        # Add https if not present
        if not url.startswith('http'):
            url = 'https://' + url
        
        print(f"🌐 Analyzing: {url}\n")
        print("⏳ Loading Wappalyzer database...")
        
        # Initialize Wappalyzer
        wappalyzer = Wappalyzer.latest()
        
        print("📡 Fetching website data...")
        
        # Analyze webpage
        webpage = WebPage.new_from_url(url)
        
        print("🔍 Detecting technologies...\n")
        
        # Get technologies
        technologies = wappalyzer.analyze(webpage)
        
        # Display results
        print("="*60)
        print("✅ TECHNOLOGIES DETECTED")
        print("="*60 + "\n")
        
        if technologies:
            # Sort alphabetically
            tech_list = sorted(list(technologies))
            
            print(f"📊 Found {len(tech_list)} technologies:\n")
            
            for i, tech in enumerate(tech_list, 1):
                print(f"  {i:2d}. {tech}")
            
            # Save to file
            result = {
                "url": url,
                "technologies": tech_list,
                "count": len(tech_list)
            }
            
            with open("technologies.json", "w") as f:
                json.dump(result, f, indent=2)
            
            print(f"\n💾 Results saved to: technologies.json")
            
        else:
            print("❌ No technologies detected!")
            print("   The website might be blocking analysis or using unknown tech.")
        
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Check if the URL is correct")
        print("  2. Make sure you have internet connection")
        print("  3. Install: pip install python-Wappalyzer")

def main():
    """Main function"""
    print("\n🔍 Website Technology Detector")
    print("   Powered by Wappalyzer\n")
    
    url = input("🎯 Enter website URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    analyze_website(url)

if __name__ == "__main__":
    main()
    input("\n⏸️  Press Enter to exit...")

