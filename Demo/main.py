import os
import re

APP_NAME = input("Enter the name off app: ")

def GetProjectName():
    root_folder = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if "settings.py" in filenames:
            return os.path.basename(dirpath)

PROJECT_NAME = GetProjectName()

BASE_DIR = os.path.abspath(APP_NAME)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates', APP_NAME)
STATIC_DIR = os.path.join(BASE_DIR, 'static', APP_NAME)
STATIC_CSS_DIR = os.path.join(STATIC_DIR, 'css')
STATIC_JS_DIR = os.path.join(STATIC_DIR, 'js')
MEDIA_DIR = os.path.abspath('media')

PROJECT_SETTINGS = os.path.join(PROJECT_NAME, 'settings.py')
PROJECT_URLS = os.path.join(PROJECT_NAME, 'urls.py')
VIEWS_FILE = os.path.join(BASE_DIR, 'views.py')
URLS_FILE = os.path.join(BASE_DIR, 'urls.py')

BASE_HTML = os.path.join(os.getcwd(), 'templates', 'base.html')
HOME_HTML = os.path.join(TEMPLATES_DIR, f'{APP_NAME}.html')
STYLE_CSS = os.path.join(STATIC_CSS_DIR, 'style.css')
SCRIPT_JS = os.path.join(STATIC_JS_DIR, 'script.js')

# Content for base.html
base_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {{% load static %}}
    <meta charset="UTF-8">
    <title>{{% block title %}}My Site{{% endblock %}}</title>
    {{% block style %}}{{% endblock style %}}
</head>
<body>
    
    {{% block header %}}
    <header>
        <h1>Welcome to My Site</h1>
    </header>
    {{% endblock header %}}

    <main>
        {{% block content %}}{{% endblock %}}
    </main>

    {{% block footer %}}
    <footer>
        <p>&copy; 2025 My Site</p>
    </footer>
    {{% endblock footer %}}
    
</body>
{{% block script %}} {{% endblock script %}}
</html>
"""

# Content for home.html
home_html_content = f"""{{% extends 'base.html' %}}
{{% load static %}}
{{% block title %}}{APP_NAME}{{% endblock %}}

{{% block style %}}
<link rel="stylesheet" href="{{% static '{APP_NAME}/css/style.css' %}}">
{{% endblock style %}}

{{% block header %}}
<header>
    <h1>Welcome to {APP_NAME}</h1>
</header>
{{% endblock header %}}

{{% block content %}}
<p>This is the {APP_NAME}content.</p>
{{% endblock %}}

{{% block script %}} 
<script src="{{% static '{APP_NAME}/js/script.js' %}}"></script>
{{% endblock script %}}
"""

# Content for style.css
style_css_content = """body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}
header, footer {
    background: #222;
    color: #fff;
    padding: 10px;
    text-align: center;
}
"""

# Content for script.js
script_js_content = "console.log('JavaScript Loaded!');"

# views.py content
views_py_content = f"""from django.shortcuts import render

def {APP_NAME}(request):
    return render(request, '{APP_NAME}/{APP_NAME}.html')
"""

# urls.py content
urls_py_content = f"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.{APP_NAME}, name='{APP_NAME}'),
]
"""


# Create folders
os.makedirs(os.path.dirname(BASE_HTML), exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(STATIC_CSS_DIR, exist_ok=True)
os.makedirs(STATIC_JS_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

# Write files
if not os.path.exists(BASE_HTML):
    with open(BASE_HTML, 'w') as f:
        f.write(base_html_content)
        print(f"✅ Created: {BASE_HTML}")
else:
    print(f"⚠️ Skipped: {BASE_HTML} already exists.")

with open(HOME_HTML, 'w') as f:
    f.write(home_html_content)
    print(f"✅ Created: {HOME_HTML}")

with open(STYLE_CSS, 'w') as f:
    f.write(style_css_content)
    print(f"✅ Created: {STYLE_CSS}")

with open(SCRIPT_JS, 'w') as f:
    f.write(script_js_content)
    print(f"✅ Created: {SCRIPT_JS}")

with open(VIEWS_FILE, 'w') as f:
    f.write(views_py_content)
    print(f"✅ Created: {VIEWS_FILE}")

if not os.path.exists(URLS_FILE):
    with open(URLS_FILE, 'w') as f:
        f.write(urls_py_content)
        print(f"✅ Created: {URLS_FILE}")
else:
    print(f"⚠️ Skipped: {URLS_FILE} already exists.")

if os.path.exists(PROJECT_SETTINGS):
    with open(PROJECT_SETTINGS, 'r') as f:
        settings = f.read()

    # ✅ Check if APP_NAME is already in INSTALLED_APPS
    if re.search(rf"['\"]{APP_NAME}['\"]", settings):
        print(f"⚠️ '{APP_NAME}' already in INSTALLED_APPS")
    else:
        pattern = r"(INSTALLED_APPS\s*=\s*\[\s*)(.*?)(\s*\])"
        match = re.search(pattern, settings, re.DOTALL)
        if match:
            before = match.group(1)
            body = match.group(2).rstrip().rstrip(',')
            after = match.group(3)

            new_body = f"{body},\n    '{APP_NAME}',"
            new_installed_apps = before + new_body + after
            settings = settings.replace(match.group(0), new_installed_apps)

            with open(PROJECT_SETTINGS, 'w') as f:
                f.write(settings)
            print(f"✅ '{APP_NAME}' added to INSTALLED_APPS")
        else:
            print("❌ INSTALLED_APPS not found!")

    # ✅ TEMPLATES['DIRS'] update
    if re.search(r"'DIRS':\s*\[\s*\]", settings):
        settings = re.sub(r"'DIRS':\s*\[\s*\]", "'DIRS': ['templates']", settings)
        with open(PROJECT_SETTINGS, 'w') as f:
            f.write(settings)
        print("✅ TEMPLATES['DIRS'] updated to ['templates']")
    else:
        print("⚠️ TEMPLATES['DIRS'] already configured or not found")

    # ✅ MEDIA settings
    if "MEDIA_URL" not in settings:
        with open(PROJECT_SETTINGS, 'a') as f:
            f.write("\n# Media configuration\n")
            f.write("MEDIA_URL = '/media/'\n")
            f.write("MEDIA_ROOT = BASE_DIR / 'media'\n")
        print("✅ MEDIA settings added to settings.py")
    else:
        print("⚠️ MEDIA settings already exist in settings.py")

    

# Add static media support in project-level urls.py
if os.path.exists(PROJECT_URLS):
    with open(PROJECT_URLS, 'r') as f:
        urls_content = f.read()

    include_import_needed = 'from django.urls import path, include' not in urls_content
    include_line_needed = f"include('{APP_NAME}.urls')" not in urls_content
        
    # ✅ Add path('', include(...)) if not present
    if include_line_needed:
        urlpatterns_pattern = r'urlpatterns\s*=\s*\[\s*(.*?)\s*\]'
        match = re.search(urlpatterns_pattern, urls_content, re.DOTALL)
        if match:
            body = match.group(1).rstrip().rstrip(',')
            new_body = body + f",\n    path('{APP_NAME}/', include('{APP_NAME}.urls'))"
            new_urlpatterns = f"urlpatterns = [\n    {new_body}\n]"
            urls_content = re.sub(urlpatterns_pattern, new_urlpatterns, urls_content, flags=re.DOTALL)
            print(f"✅ path('', include('{APP_NAME}.urls')) added to urlpatterns")
        else:
            print("❌ Could not find urlpatterns to modify")
    else:
        print("⚠️ App URL include already exists in urlpatterns")

    # ✅ Add `include` to imports if needed
    if include_import_needed:
        urls_content = re.sub(
            r'(from django\.urls import path)',
            r'\1, include',
            urls_content
        )
        print("✅ 'include' imported in urls.py")
    else:
        print("⚠️ 'include' already imported")

    # ✅ Add static media serving in debug mode
    if 'document_root=settings.MEDIA_ROOT' not in urls_content:
        urls_content += """\n
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
        print("✅ Media URL handler added to project-level urls.py")
    else:
        print("⚠️ Media URL handler already exists in urls.py")

    # Save final result
    with open(PROJECT_URLS, 'w') as f:
        f.write(urls_content)

else:
    print("❌ Project-level urls.py not found.")


print("\n🎉 Django app setup completed successfully!")
# print(f"1. Add `path('', include('{APP_NAME}.urls'))` to your project-level urls.py")
# print(f"2. Ensure `{APP_NAME}` is in INSTALLED_APPS")

