import os
from flask import Flask
import markdown

app = Flask(__name__)

def generate_html():
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
    html_content = markdown.markdown(readme_content)
    with open("static/style.css") as style_file:
        css_styles = f"<style>{style_file.read()}</style>"
    return f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Sreyeesh Garimella – DevOps</title>
    {css_styles}
</head>
<body>
    <div class='markdown-body'>{html_content}</div>
</body>
</html>"""

@app.route('/')
def home():
    return generate_html()

@app.route('/notion')
def notion_embed():
    return """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Notion Portfolio</title>
</head>
<body style="margin:0; padding:0;">
    <iframe src="https://stump-principle-4a6.notion.site/Sreyeesh-Garimella-DevOps-Engineer-Data-Engineer-Pipeline-Technical-Director-1d7c1e24aece808c8f02ecf255287e1c?pvs=74"
            width="100%" height="100%" style="border:none; position:absolute; top:0; left:0; bottom:0; right:0;"></iframe>
</body>
</html>"""

if __name__ == "__main__":
    if os.environ.get("FLASK_RUN_MODE") == "export-only":
        os.makedirs("dist", exist_ok=True)
        with open("dist/index.html", "w", encoding="utf-8") as f:
            f.write(generate_html())
        print("✅ Exported to dist/index.html")
    else:
        app.run(debug=True, host="0.0.0.0", port=5000)
