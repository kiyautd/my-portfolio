import sys
import os
import urllib.parse

# 1. ኮምፒውተሩ አማርኛን (UTF-8) ያለችግር ፕሪንት እንዲያደርግ የሚያዝ መፍትሄ!
sys.stdout.reconfigure(encoding='utf-8')

# 2. የብሮውዘር መታወቂያ 
print("Content-type: text/html; charset=utf-8")
print()

try:
    from google import genai

    # 3. የ API ቁልፍህን እዚህ አስገባ
    api_key = "YOUR_API_KEY_HERE" 
    client = genai.Client(api_key=api_key)

    # 4. የመረጃ መቀበያ አሰራር
    env_length = os.environ.get('CONTENT_LENGTH', '0')
    content_length = int(env_length) if env_length else 0
    
    post_data = sys.stdin.read(content_length)
    form = urllib.parse.parse_qs(post_data)

    message = form.get("message", [""])[0]

    # 5. መረጃው ወደ AI ተልኮ መልሱ ይወጣል
    if message:
        ai_reply = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=message
        )
        # መልሱን ቆንጆ አድርጎ ያወጣል
        print(f"<h3>የ AI መልስ:</h3> <p>{ai_reply.text}</p>")
    else:
        print("ምንም መልዕክት አላገኘሁም!")

except Exception as e:
    print(f"<h3>ይቅርታ፣ ስህተት አጋጥሟል:</h3> <p>{e}</p>")