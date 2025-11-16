import google.generativeai as genai

# إعداد API Key
API_KEY = "AIzaSyAk9XcBZ9vK3JZbyZutskVVrD7_7No02G0"
genai.configure(api_key=API_KEY)

# Create the model (Latest: Gemini 2.5 Flash - September 2025)
model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

# إرسال الرسالة
response = model.generate_content("hi, how are you?")

# طباعة الرد
print(response.text)

