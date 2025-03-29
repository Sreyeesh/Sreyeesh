import os
import markdown

# Read the README.md file
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_content = f.read()

# Convert Markdown to HTML
html_content = markdown.markdown(readme_content)

# Material Theme Dark CSS
css = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        line-height: 1.6;
        color: #e0e0e0;
        background-color: #0f111a;
        padding: 20px;
    }
    h1, h2, h3 { color: #ffffff; }
    a { color: #82aaff; font-weight: bold; text-decoration: none; }
    a:hover { text-decoration: underline; }
    code, pre {
        background-color: #1e212b;
        color: #e0e0e0;
        padding: 5px;
        border-radius: 3px;
    }
    blockquote {
        border-left: 5px solid #89ddff;
        padding: 10px;
        background-color: #1e212b;
    }
</style>
"""

# Create HTML template
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>README</title>
    {css}
</head>
<body>
    <div class="markdown-body">
        {html_content}
    </div>
</body>
</html>
"""

# Save to dist/index.html
os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w", encoding='utf-8') as f:
    f.write(html)

print("✅ Generated dist/index.html")
