import os
from flask import Flask, render_template_string
import markdown

app = Flask(__name__)

@app.route('/')
def serve_readme():
    # Path to README.md (must be in the same directory as this file)
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')

    try:
        with open(readme_path, 'r') as f:
            readme_content = f.read()
    except FileNotFoundError:
        return "README.md not found. Please ensure the file exists in the same directory."

    # Convert Markdown to HTML
    html_content = markdown.markdown(readme_content)

    # Material Theme (Dark) inspired CSS
    css_styles = """
    <style>
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

        a {
            color: #82aaff;
            text-decoration: none;
            font-weight: bold;
        }

        a:hover {
            text-decoration: underline;
        }

        ul, ol {
            margin: 20px 0;
            padding-left: 20px;
        }

        li {
            margin-bottom: 10px;
        }

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

        .badge:hover {
            opacity: 0.8;
        }

        .badge-section {
            margin: 20px 0;
        }

        .badge-section h3 {
            margin-bottom: 10px;
        }

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
    </style>
    """

    # Render HTML with injected CSS
    return render_template_string("""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project README</title>
        {{ css | safe }}
    </head>
    <body>
        <div class="markdown-body">
            <div>{{ content | safe }}</div>
        </div>
    </body>
    </html>
    """, content=html_content, css=css_styles)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
