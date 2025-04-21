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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sreyeesh Garimella – DevOps Portfolio</title>
    {css_styles}
</head>
<body>
    <div class="markdown-body">{html_content}</div>
</body>
</html>"""

@app.route('/')
def home():
    return generate_html()

if __name__ == "__main__":
    if os.environ.get("FLASK_RUN_MODE") == "export-only":
        os.makedirs("dist", exist_ok=True)
        with open("dist/index.html", "w", encoding="utf-8") as f:
            f.write(generate_html())
        print("✅ Exported to dist/index.html")
    else:
        app.run(debug=True, host="0.0.0.0", port=5000)
