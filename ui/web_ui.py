import sys, os, zipfile
from datetime import datetime
from flask import Flask, request, render_template_string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.legal_mapper import map_to_policy
from report.pdf_generator import generate_pdf_report
from report.stats import collect_stats

app = Flask(__name__)

LANG = {
    "fa": {
        "title": "PARS – گزارش تخلف",
        "links": "لینک‌ها (هر خط یک لینک)",
        "violation": "نوع تخلف",
        "run": "🚀 اجرای گزارش انبوه",
        "done": "✅ عملیات انجام شد",
        "count": "📊 تعداد لینک‌ها",
        "saved": "📁 فایل‌ها ذخیره شدند",
        "email": "📧 ایمیل تلگرام",
        "zip": "📦 ساخت ZIP"
    },
    "en": {
        "title": "PARS – Abuse Reporting",
        "links": "Links (one per line)",
        "violation": "Violation type",
        "run": "🚀 Run Bulk Report",
        "done": "✅ Bulk completed",
        "count": "📊 Total links",
        "saved": "📁 Files saved",
        "email": "📧 Telegram email",
        "zip": "📦 Create ZIP"
    },
    "ar": {
        "title": "PARS – الإبلاغ عن الانتهاك",
        "links": "الروابط (كل رابط بسطر)",
        "violation": "نوع المخالفة",
        "run": "🚀 تنفيذ جماعي",
        "done": "✅ تم التنفيذ",
        "count": "📊 عدد الروابط",
        "saved": "📁 تم حفظ الملفات",
        "email": "📧 بريد تيليغرام",
        "zip": "📦 إنشاء ZIP"
    }
}

HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{{ t.title }}</title>
<style>
body { background:#1e1e1e; color:#ccc; font-family:Tahoma; }
h2 { color:#4da6ff; }
textarea, select { width:95%; padding:8px; margin:6px 0; }
button { background:#4da6ff; color:white; padding:10px; border:none; cursor:pointer; }
pre { background:#2b2b2b; padding:10px; }
.green { color:#33ff66; }
.blue { color:#4da6ff; }
</style>
</head>
<body>

<h2>{{ t.title }}</h2>

<form method="post">
<select name="lang">
<option value="fa">فارسی</option>
<option value="en">English</option>
<option value="ar">العربية</option>
</select><br>

<label>{{ t.links }}</label><br>
<textarea name="links" rows="7" required></textarea><br>

<label>{{ t.violation }}</label><br>
<select name="violation">
<option>Non-consensual sexual content</option>
<option>Impersonation / Deepfake</option>
<option>Privacy violation / Doxxing</option>
</select><br>

<button type="submit">{{ t.run }}</button>
</form>

{% if result %}
<hr>
<pre>
<span class="green">{{ t.done }}</span>

<span class="blue">{{ t.count }}:</span> {{ count }}

<span class="green">{{ t.saved }}</span>

<span class="green">{{ t.email }}:</span>
abuse@telegram.org
</pre>

<form method="get">
<button name="zip" value="1">{{ t.zip }}</button>
</form>
{% endif %}

{% if zipfile %}
<hr>
<pre class="green">
ZIP: {{ zipfile }}
</pre>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    lang = request.form.get("lang", "fa")
    t = LANG.get(lang, LANG["fa"])

    result = False
    count = 0
    zipfile_path = None

    if request.method == "POST":
        links = [l.strip() for l in request.form["links"].splitlines() if l.strip()]
        violation = request.form["violation"]
        policy = map_to_policy(violation)

        os.makedirs("Evidence", exist_ok=True)

        for link in links:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            pdf = f"Evidence/report_{ts}.pdf"
            generate_pdf_report(
                link,
                violation,
                "Critical",
                90,
                policy,
                collect_stats(),
                pdf
            )

        result = True
        count = len(links)

    if request.args.get("zip"):
        zipfile_path = "Evidence/reports.zip"
        with zipfile.ZipFile(zipfile_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in os.listdir("Evidence"):
                z.write(os.path.join("Evidence", f))

    return render_template_string(
        HTML,
        t=t,
        result=result,
        count=count,
        zipfile=zipfile_path
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
