import webbrowser
import urllib.parse

def build_mailto(report_text):
    """
    ساخت لینک ایمیل آماده برای Telegram Abuse
    متن در بدنه ایمیل چند خطی و خواناست
    """
    to = "abuse@telegram.org"
    subject = "Telegram Abuse Report - Privacy / Sexual Content"

    # بدنه ایمیل: لینک، تخلف، متن، درصد اعتماد
    body_lines = [
        "📧 ایمیل گیرنده: abuse@telegram.org",
        "",
        "📄 متن گزارش:",
        report_text,
        "",
        "💡 اعتماد سیستم: طبق تحلیل PARS"
    ]

    # ترکیب خطوط با newline
    body = "\n".join(body_lines)

    # urlencode برای استفاده در mailto
    params = {
        "subject": subject,
        "body": body
    }

    query = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    mailto_link = f"mailto:{to}?{query}"
    return mailto_link


def open_email_client(report_text):
    """
    باز کردن ایمیل در مرورگر یا کلاینت پیش‌فرض
    """
    link = build_mailto(report_text)
    print("\n📨 ایمیل آماده شد. اگر خودکار باز نشد، می‌توانید لینک زیر را کپی کرده و در مرورگر باز کنید:\n")
    print(link)
    webbrowser.open(link)
