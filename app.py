import os
from flask import Flask, render_template_string
import markdown

app = Flask(__name__)

def generate_html():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        return "README.md not found."

    html_content = markdown.markdown(readme_content)

    css_styles = """<style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            line-height: 1.6;
            color: #e0e0e0;
            background-color: #0f111a;
            padding: 20px;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
            font-weight: bold;
            margin-bottom: 10px;
        }
        h1 { font-size: 36px; }
        h2 { font-size: 30px; }
        h3 { font-size: 24px; }
        p { margin: 20px 0; }
        a { color: #82aaff; text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; }
        ul, ol { margin: 20px 0; padding-left: 20px; }
        li { margin-bottom: 10px; }
        code, pre {
            background-color: #1e212b;
            color: #e0e0e0;
            padding: 5px;
            border-radius: 3px;
        }
        pre {
            padding: 10px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        blockquote {
            margin: 20px 0;
            padding: 10px;
            background-color: #1e212b;
            border-left: 5px solid #89ddff;
        }
        .markdown-body {
            max-width: 900px;
            margin: 0 auto;
        }
        .markdown-body img {
            max-width: 100%;
            height: auto;
        }
        .badge {
            display: inline-block;
            margin-right: 10px;
            padding: 5px 10px;
            font-size: 14px;
            border-radius: 3px;
            color: white;
            background-color: #f07178;
        }
        .badge:hover { opacity: 0.8; }
        .badge-section { margin: 20px 0; }
        .badge-section h3 { margin-bottom: 10px; }
        .tech-table {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .tech-table .badge-column {
            display: flex;
            flex-direction: column;
            margin-right: 20px;
        }
        .tech-table .badge-column p {
            margin-bottom: 10px;
        }
    </style>"""

    html_page = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Project README</title>
        {css_styles}
    </head>
    <body>
        <div class="markdown-body">{html_content}</div>
    </body>
    </html>"""

    return html_page

@app.route('/')
def serve_readme():
    return generate_html()

if __name__ == "__main__":
    # If in CI/CD, export HTML to file instead of starting server
    if os.environ.get("FLASK_RUN_MODE") == "export-only":
        html = generate_html()
        os.makedirs("dist", exist_ok=True)
        with open("dist/index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ Static HTML generated in dist/index.html")
    else:
        app.run(debug=True, host="0.0.0.0", port=5000)
