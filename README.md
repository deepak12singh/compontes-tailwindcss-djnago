# Django + TailwindCSS (Copy-Paste Setup)

This README is for developers who want to use **TailwindCSS in Django in the simplest possible way**, without rebuilding the setup for every new project.

👉 In this approach, you only need to **copy two folders**:

1. `tailwindcss/`
2. `z_dev/`
3. `templates`

That’s it. Tailwind is ready to use 🚀

---

## 🧩 Prerequisites

Make sure your system has the following installed:

* Python 3.10+
* Django 5.x
* Node.js (LTS recommended)
* npm (comes with Node.js)

---

## 📁 Project Creation (Base Steps)

```bash
django-admin startproject My_Project
cd My_Project
python manage.py startapp Applection
python manage.py runserver
```

If the server starts correctly, your base project is ready ✅

---

## 📂 Tailwind Integration (Core Idea)

### ✅ Step 1: Copy Required Folders

From any working project, copy these **two folders** into your Django project root:

```text
My_Project/
├── My_Project/
├── Applection/
├── templates     # templates
├── tailwindcss/   # Django app (templates + static)
├── z_dev/         # Node + Tailwind build tools
└── manage.py
```

> ⚠️ `tailwindcss` is a Django app. `z_dev` is only for building CSS.

---

### ✅ Step 2: Update `settings.py`

Open `My_Project/settings.py` and update the following:

#### Add Tailwind app

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tailwindcss',
    'Applection',
]
```

#### Ensure static files configuration

```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'tailwindcss' / 'static',
]
```

---

## ⚙️ Tailwind Build Setup (`z_dev`)

### ✅ Step 3: Install Node Modules

```bash
cd z_dev
npm install
```

This installs Tailwind CLI and required dependencies.

---

### ✅ Step 4: Run Tailwind in Watch Mode (IMPORTANT)

```bash
npm run dev
```

🔴 **Always run this command in a NEW / SEPARATE terminal**

* Terminal 1 → `npm run dev` (Tailwind live watcher)
* Terminal 2 → `python manage.py runserver` (Django server)

What this does:

```text
input.css
  ↓ (watch mode)
../tailwindcss/static/tailwindcss/css/main.css
```

* Any change in templates automatically regenerates CSS
* Keep this terminal running during development

---

## ▶️ Run Django Server

Open another terminal (or tab):

```bash
cd ..
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/Applection/
```

Tailwind styles should now load correctly 🎨

---

## 🏗️ Production Build (Before Deleting `z_dev`)

When your project is complete and you no longer need live Tailwind updates:

### ✅ Step 1: Generate Final CSS

```bash
cd z_dev
npm run build
```

This creates a **final, optimized CSS file**.

---

### ✅ Step 2: Delete `z_dev`

After running `npm run build`, you can safely delete:

```text
z_dev/
```

⚠️ Important rules:

* Never delete `z_dev` **before** running `npm run build`
* `tailwindcss/static/tailwindcss/css/main.css` must exist

---

## 🧬 Template Inheritance (How You Use It)

### 📌 Provided Base Components

The Tailwind system already includes:

* `tailwindcss/core.html` → HTML skeleton
* `tailwindcss/base.html` → Main layout
* `tailwindcss/includes/header.html`
* `tailwindcss/includes/footer.html`
* `tailwindcss/includes/scripts.html`

---

### 🧱 How Your App Uses It

Inside your app templates:

```django
{% extends "tailwindcss/base.html" %}
```

This automatically gives you:

* Tailwind CSS
* Header & Footer
* SEO and JS blocks

---

## 🧑‍💻 Example: Custom App Base Template

**Path:** `Applection/templates/Applection/base.html`

```django
{% extends "tailwindcss/base.html" %}

{% block title %}User Dashboard{% endblock %}

{% block body_class %}bg-gray-100 text-gray-900{% endblock %}

{% block content %}
<div class="max-w-6xl mx-auto p-6">
    <h1 class="text-3xl font-bold mb-4">Dashboard</h1>
    <p class="text-gray-600">Welcome to your application powered by TailwindCSS.</p>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        <div class="bg-white p-4 rounded shadow">Card 1</div>
        <div class="bg-white p-4 rounded shadow">Card 2</div>
        <div class="bg-white p-4 rounded shadow">Card 3</div>
    </div>
</div>
{% endblock %}
```

All your other pages can now extend this file.

---

## ❗ Common Notes

* `/` returning 404 is normal if no root view is defined
* `/Applection/` is the active route
* `npm run dev` is required only during development
* In production, only `main.css` is needed

---

## 🎯 Summary (Golden Rule)

For every new Django project with TailwindCSS:

1. Copy `tailwindcss/`
2. Copy `z_dev/`
3. Add `tailwindcss` to `INSTALLED_APPS`
4. Development → `npm run dev` (new terminal)
5. Production → `npm run build` → delete `z_dev`

Clean. Repeatable. Production-safe. ⚡
