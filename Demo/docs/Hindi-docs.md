
---

# 📘 Django + TailwindCSS Template System

## (Complete Hindi Documentation)

यह documentation एक ऐसे Django + TailwindCSS setup को explain करती है जिसमें:

* TailwindCSS एक reusable Django app के रूप में है
* User सिर्फ folder copy करके Tailwind use कर सकता है
* User चाहे तो अपनी **खुद की base.html** बना सकता है
* `core.html` और `base.html` का clear separation है
* Development और Production दोनों flow defined हैं

---

## 📂 Overall Architecture

```text
My_Project/
│
├── My_Project/                # Django project settings
├── Applection/                # Your Django app
│   └── templates/
│       └── Applection/
│           └── base.html      # (User custom base)
│
├── tailwindcss/               # Tailwind Django App
│   ├── templates/
│   │   └── tailwindcss/
│   │       ├── core.html
│   │       ├── base.html
│   │       └── includes/
│   │           ├── header.html
│   │           ├── footer.html
│   │           └── scripts.html
│   │
│   └── static/
│       └── tailwindcss/
│           └── css/
│               ├── main.css
│               └── style.css
│
├── z_dev/                     # Tailwind build tool (Node.js)
└── manage.py
```

---

# 1️⃣ `tailwindcss/core.html`

## (Root / Skeleton Template)

### 🔹 यह file क्या है?

`core.html` **पूरे template system की नींव (foundation)** है।

* इसमें सिर्फ HTML structure होता है
* कोई UI design नहीं
* कोई header/footer नहीं
* सिर्फ blocks (hooks) दिए जाते हैं

👉 **Rule:**

> इस file को direct page के लिए use नहीं किया जाता
> यह सिर्फ extend करने के लिए है

---

## 🧱 `core.html` का काम

* `<html>`, `<head>`, `<body>` define करना
* Tailwind का `main.css` load करना
* SEO, CSS, JS, Layout के लिए blocks देना

---

## 🔹 HTML Level Blocks

```django
<html lang="{% block html_lang %}en{% endblock %}"
      class="{% block html_class %}{% endblock %}">
```

### Explanation:

* `html_lang`
  → Website की language
  → Example: `hi`, `en-IN`

* `html_class`
  → `<html>` tag पर class
  → Dark mode, theme switch के लिए useful

---

## 🔹 `<head>` Section

```django
{% block head %}
```

पूरा head section wrapper।

### Meta Block

```django
{% block meta %}
```

* Charset
* Viewport
* Base SEO tags

---

### Title Block

```django
{% block title %}{% endblock %}
```

* Browser tab का title
* हर page में override हो सकता है

---

### Tailwind CSS (Mandatory)

```django
<link rel="stylesheet" href="{% static 'tailwindcss/css/main.css' %}">
```

* `npm run dev` / `npm run build` से generate होती है
* Production में यही CSS use होती है

---

### Extra Head Blocks

| Block   | उपयोग                     |
| ------- | ------------------------- |
| `seo`   | Meta description, OG tags |
| `css`   | Extra CSS files           |
| `style` | Inline CSS                |

---

## 🔹 `<body>` Section

```django
<body class="{% block body_class %}{% endblock %}">
```

* `body_class`
  → Body पर Tailwind classes
  → Example: `bg-gray-100 text-gray-900`

---

### Body Layout Blocks

```django
{% block body %}
    {% block header %}{% endblock %}
    {% block layout %}{% endblock %}
    {% block footer %}{% endblock %}
{% endblock %}
```

* `header` → Navbar / Top section
* `layout` → Main content
* `footer` → Footer section

---

## 🔹 JavaScript Blocks

| Block    | Purpose          |
| -------- | ---------------- |
| `js`     | JS files include |
| `script` | Inline JS        |

---

## ✅ `core.html` Summary

* यह framework है
* यह design नहीं करता
* सिर्फ structure देता है
* Advanced users के लिए powerful है

---

# 2️⃣ `tailwindcss/base.html`

## (Default Ready Layout)

### 🔹 यह file क्या है?

`base.html` एक **ready-to-use layout** है जो `core.html` पर based है।

👉 यही file **normally user extend करता है**

---

## 🧱 `base.html` का काम

* Header / Footer include करना
* SEO default set करना
* Content area define करना
* Easy inheritance देना

---

## 🔹 Core Extend

```django
{% extends "tailwindcss/core.html" %}
```

इसका मतलब:

* HTML skeleton core से आएगा
* अब हम blocks fill कर रहे हैं

---

## 🔹 Title

```django
{% block title %}My Site{% endblock %}
```

* Default title
* Page level override possible

---

## 🔹 SEO Block

```django
{% block seo %}
<meta name="description" content="{% block meta_description %}Default website description{% endblock %}">
<link rel="icon" href="{% static 'tailwindcss/images/favicon.ico' %}">
{% endblock %}
```

* Default meta description
* Nested block `meta_description`
* Favicon included

---

## 🔹 Extra CSS

```django
{% block css %}
<link rel="stylesheet" href="{% static 'tailwindcss/css/style.css' %}">
{% endblock %}
```

* Tailwind के ऊपर custom CSS

---

## 🔹 Header Include

```django
{% include "tailwindcss/includes/header.html" %}
```

* Common header
* Single place maintenance

---

## 🔹 Main Content Area

```django
{% block layout %}
<main id="content">
    {% block content %}{% endblock %}
</main>
{% endblock %}
```

👉 `content` block सबसे ज्यादा use होता है

---

## 🔹 Footer & JS

* Footer common
* Scripts centralized

---

## ✅ `base.html` Summary

* Ready layout
* SEO + Tailwind ready
* 90% projects के लिए best

---

# 3️⃣ User अपनी खुद की `base.html` कैसे बनाए

User के पास **दो valid तरीके** हैं।

---

## 🥇 Method 1: `core.html` से

### (Full Control)

```django
{% extends "tailwindcss/core.html" %}

{% block header %}
<header class="bg-black text-white p-4">My Header</header>
{% endblock %}

{% block layout %}
<main class="p-6">
    {% block content %}{% endblock %}
</main>
{% endblock %}
```

✔ जब design पूरी तरह custom हो

---

## 🥈 Method 2: `tailwindcss/base.html` से

### (Recommended)

```django
{% extends "tailwindcss/base.html" %}

{% block title %}Dashboard{% endblock %}
{% block body_class %}bg-gray-100{% endblock %}

{% block content %}
<h1 class="text-2xl font-bold">Welcome</h1>
{% endblock %}
```

✔ Fast
✔ Clean
✔ Maintainable

---

## 🔍 Comparison

| Point       | core.html | base.html  |
| ----------- | --------- | ---------- |
| Control     | Full      | Limited    |
| Speed       | Slow      | Fast       |
| Recommended | Advanced  | Most users |

---

# 4️⃣ Development vs Production

## 🔧 Development

* New terminal:

```bash
npm run dev
```

* Another terminal:

```bash
python manage.py runserver
```

---

## 🏗️ Production

```bash
npm run build
```

* CSS generate होगी
* उसके बाद `z_dev/` delete कर सकते हैं

---

# 5️⃣ Git / Commit Rules

### ✅ Commit करें

* `tailwindcss/core.html`
* `tailwindcss/base.html`
* `tailwindcss/includes/*`
* `main.css`

### ❌ Commit न करें

* `z_dev/`
* `node_modules/`

---

# 🏁 Final Conclusion

* ✔ User अपनी base.html बना सकता है
* ✔ core से भी
* ✔ base से भी
* ✔ दोनों सही हैं

**Architecture Philosophy:**

> core.html = framework
> base.html = default layout
> app base.html = customization

---
