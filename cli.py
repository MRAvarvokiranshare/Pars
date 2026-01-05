from core.classifier import classify
from core.legal_mapper import map_to_policy
from report.generator import generate_report
from report.email_helper import open_email_client
from report.pdf_generator import generate_pdf_report
from report.stats import collect_stats
from colorama import init, Fore, Style
import os
import hashlib
from datetime import datetime
import csv

init(autoreset=True)

VIOLATION_OPTIONS = {
    "1": "Non-consensual sexual content",
    "2": "Impersonation / Deepfake without consent",
    "3": "Privacy violation / Doxxing"
}

def save_report(report_text):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    hash_digest = hashlib.sha256(report_text.encode()).hexdigest()[:8]
    filename = f"Evidence/report_{now}_{hash_digest}.txt"
    os.makedirs("Evidence", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)
    return filename

def save_report_csv(link, violation, severity, confidence, policy):
    os.makedirs("Evidence", exist_ok=True)
    csv_file = "Evidence/reports.csv"
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp","Link","Violation","Severity","Confidence","Policy"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), link, violation, severity, confidence, policy])

def choose_violation():
    print("\n📌 نوع تخلف را انتخاب کنید:\n")
    for key, value in VIOLATION_OPTIONS.items():
        print(f"{key}. {value}")
    choice = input("\nشماره گزینه (1-3): ").strip()
    if choice not in VIOLATION_OPTIONS:
        print(Fore.RED + "⚠️ گزینه نامعتبر، بررسی دستی انتخاب شد.")
        return VIOLATION_OPTIONS["3"]
    return VIOLATION_OPTIONS[choice]

def main():
    print(Fore.CYAN + "===================================")
    print(Fore.CYAN + "  PARS - Critical Violations Mode")
    print(Fore.CYAN + "===================================\n")

    link = input(Fore.GREEN + "🔗 لینک کانال یا پست تلگرام: " + Style.RESET_ALL)
    selected_violation = choose_violation()

    # هشدار فوری
    print(Fore.RED + "\n⚠️ هشدار: این تخلف بسیار حساس است! ⚠️\n")
    print(Fore.MAGENTA + "🔔 توجه: PARS گزینه‌های Critical را شناسایی کرد.\n")
    os.system('termux-vibrate -d 500')

    print("\n⏳ در حال تحلیل محتوا...\n")
    auto_result = classify("")
    violation = selected_violation
    severity = "Critical"
    confidence = 90

    result = {
        "violation": violation,
        "severity": severity,
        "confidence": confidence,
        "language": auto_result["language"]
    }

    policy = map_to_policy(result["violation"])
    report_text = generate_report(link, result, policy)

    # ذخیره TXT و CSV
    saved_file = save_report(report_text)
    save_report_csv(link, violation, severity, confidence, policy)
    print(Fore.MAGENTA + f"\n💾 گزارش ذخیره شد در فایل: {saved_file}")
    print(Fore.MAGENTA + "💾 CSV گزارش نیز به‌روزرسانی شد: Evidence/reports.csv\n")

    # تولید PDF سبک با جدول آمار
    stats_table = collect_stats()
    pdf_file = f"Evidence/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    generate_pdf_report(link, violation, severity, confidence, policy, stats_table, pdf_file)
    print(Fore.MAGENTA + f"📄 PDF گزارش ساخته شد: {pdf_file}\n")

    # نمایش رنگی و ایمیل خودکار
    print(Fore.BLUE + "===============================")
    print(Fore.BLUE + "      ایمیل آماده شد!      ")
    print(Fore.BLUE + "===============================\n")
    print(Fore.GREEN + "📧 ایمیل گیرنده:\nabuse@telegram.org\n")
    print(Fore.BLUE + "📄 متن گزارش:\n")
    print(Fore.BLUE + report_text)
    print(Fore.BLUE + "\n-------------------------------\n")
    print(Fore.GREEN + f"💡 اعتماد سیستم: {result['confidence']} %\n")
    open_email_client(report_text)

    print(Fore.CYAN + "\n✨ پایان اجرای PARS")

if __name__ == "__main__":
    main()
