# Django + TailwindCSS (Copy-Paste Setup)

यह README उन लोगों के लिए है जो **TailwindCSS को Django में सबसे आसान तरीके से** इस्तेमाल करना चाहते हैं, बिना हर project में पूरा setup दोबारा करने के।

👉 इस approach में आपको **सिर्फ 2 folder copy करने हैं**:

1. `tailwindcss/`
2. `z_dev/`

बस, Tailwind चालू 🚀

---

## 🧩 Prerequisites

सुनिश्चित करें कि आपके system में ये चीज़ें मौजूद हों:

* Python 3.10+
* Django 5.x
* Node.js (LTS recommended)
* npm (Node के साथ आता है)

---

## 📁 Project Creation (Base Steps)

```bash
django-admin startproject My_Project
cd My_Project
python manage.py startapp Applection
python manage.py runserver
```

अगर server सही से चल रहा है तो आप सही रास्ते पर हैं ✅

---

## 📂 Tailwind Integration (Core Idea)

### ✅ Step 1: Folder Copy

किसी working project से ये **दो folder** copy करके अपने Django project root में paste करें:

```text
My_Project/
├── My_Project/
├── Applection/
├── tailwindcss/   👈 (Django app)
├── z_dev/         👈 (Node + Tailwind build tool)
└── manage.py
```

> ⚠️ `tailwindcss` एक Django app है, और `z_dev` Tailwind build के लिए Node environment है।

---

### ✅ Step 2: settings.py Update

`My_Project/settings.py` में:

#### INSTALLED_APPS में add करें:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tailwindcss',  # 👈 required
    'Applection',
]
```

#### Static files ensure करें:

```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'tailwindcss' / 'static',
]
```

---

## ⚙️ Tailwind Build Setup (z_dev)

### ✅ Step 3: Node Modules Install

```bash
cd z_dev
npm install
```

यह Tailwind CLI और dependencies install करेगा।

---

### ✅ Step 4: Tailwind Watch Mode (IMPORTANT)

```bash
npm run dev
```

🔴 **यह command हमेशा NEW TERMINAL में run करें**

* एक terminal में: `npm run dev`
* दूसरे terminal में: `python manage.py runserver`

👉 `npm run dev` **live watch mode** में रहता है:

* HTML / template बदलते ही
* `main.css` auto regenerate होती है

```text
input.css
  ↓ (watch)
../tailwindcss/static/tailwindcss/css/main.css
```

⚠️ Development के दौरान इस terminal को बंद न करें।

---

### ✅ Step 4: Tailwind Watch Mode

```bash
npm run dev
```

यह command background में Tailwind को watch mode में रखेगा:

```text
input.css  →  ../tailwindcss/static/tailwindcss/css/main.css
```

> जैसे ही आप HTML बदलेंगे, CSS auto-update हो जाएगी ✨

---

## ▶️ Django Server Run

नया terminal खोलें (या दूसरा tab):

```bash
cd ..
python manage.py runserver
```

अब browser में खोलें:

```
http://127.0.0.1:8000/Applection/
```

Tailwind styles live load होंगी 🎨

---

## 🧱 Template Structure (Already Ready)

### `core.html`

यह base skeleton है जो Tailwind CSS load करता है:

* `main.css` auto include
* reusable blocks (`header`, `footer`, `layout`)

---

### `base.html`

```django
{% extends "tailwindcss/core.html" %}
```

यह main layout file है जिसे **हर app use कर सकता है**।

इसमें:

* SEO block
* Header / Footer includes
* Custom CSS support

👉 आपको सिर्फ `{% extends "tailwindcss/base.html" %}` करना है।

---

## 📦 Static Files Used

Tailwind files auto-generate होकर यहाँ जाते हैं:

```text
tailwindcss/static/tailwindcss/css/
├── main.css   👈 Tailwind output
├── style.css  👈 optional custom css
```

---

## 🏗️ Production Build (z_dev delete करने से पहले)

जब आपका project complete हो जाए और अब Tailwind live watch की ज़रूरत न हो:

### ✅ Step 1: Final CSS Build

```bash
cd z_dev
npm run build
```

👉 यह **final optimized CSS** generate करेगा।

---

### ✅ Step 2: z_dev Folder Delete

अब आप safely:

```text
z_dev/
```

folder **delete कर सकते हैं** ✅

⚠️ लेकिन ध्यान रखें:

* `npm run build` **चलाए बिना delete न करें**
* `tailwindcss/static/.../main.css` file रहनी चाहिए

---

## ❗ Common Notes

* `/` URL पर 404 normal है अगर root view define नहीं किया
* `/Applection/` सही route है
* Development में `npm run dev` चालू रहना चाहिए
* Production में सिर्फ `main.css` काफी है

---

## 🧬 Template Inheritance (How YOU use it)

### 📌 Given Base Files

Tailwind system आपको ये ready components देता है:

* `tailwindcss/core.html` → HTML skeleton
* `tailwindcss/base.html` → Full layout
* `tailwindcss/includes/header.html`
* `tailwindcss/includes/footer.html`
* `tailwindcss/includes/scripts.html`

---

### 🧱 How your App uses it

आपके app (`Applection`) में:

```django
{% extends "tailwindcss/base.html" %}
```

बस इतना करने से:

* Tailwind CSS load
* Header + Footer ready
* SEO + JS blocks ready

---

## 🧑‍💻 Example: User Custom base.html

**Applection/templates/Applection/base.html**

```django
{% extends "tailwindcss/base.html" %}

{% block title %}User Dashboard{% endblock %}

{% block body_class %}bg-gray-100 text-gray-900{% endblock %}

{% block content %}
<div class="max-w-6xl mx-auto p-6">
    <h1 class="text-3xl font-bold mb-4">Dashboard</h1>
    <p class="text-gray-600">Welcome to your application powered by Tailwind.</p>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        <div class="bg-white p-4 rounded shadow">Card 1</div>
        <div class="bg-white p-4 rounded shadow">Card 2</div>
        <div class="bg-white p-4 rounded shadow">Card 3</div>
    </div>
</div>
{% endblock %}
```

अब आपकी हर page सिर्फ इस file को extend करेगी।

---

## 🎯 Summary (Golden Rule)

हर नए Django project में Tailwind चाहिए?

1. `tailwindcss/` copy करो
2. `z_dev/` copy करो
3. `settings.py` में `tailwindcss` add करो
4. Dev में → `npm run dev` (NEW terminal)
5. Final में → `npm run build` → `z_dev` delete

Clean. Repeatable. Production-safe. ⚡🧠
