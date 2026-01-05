from langdetect import detect

SEXUAL_KEYWORDS = {
    "fa": [
        ("فیلم خصوصی", 30),
        ("سکسی", 20),
        ("پورن", 30),
        ("برهنه", 25),
        ("دیپ فیک", 40),
        ("بدون رضایت", 40),
        ("نود", 25),
    ],
    "en": [
        ("non consensual", 40),
        ("deepfake", 40),
        ("nude", 25),
        ("porn", 30),
        ("leaked", 30),
        ("explicit", 20),
        ("sex tape", 35),
    ],
}

PRIVACY_KEYWORDS = {
    "fa": [
        ("شماره", 20),
        ("آدرس", 25),
        ("کد ملی", 40),
        ("عکس خصوصی", 35),
        ("اطلاعات شخصی", 30),
    ],
    "en": [
        ("phone number", 25),
        ("address", 25),
        ("id card", 40),
        ("private photo", 35),
        ("personal data", 30),
    ],
}


def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "unknown"


def analyze_keywords(text, keyword_map):
    score = 0
    for keyword, weight in keyword_map:
        if keyword in text:
            score += weight
    return score


def classify(text):
    if not text or len(text.strip()) < 3:
        return {
            "violation": "Unknown",
            "confidence": 0,
            "severity": "Low",
            "language": "Unknown",
        }

    text_lower = text.lower()
    lang = detect_language(text_lower)

    sexual_score = 0
    privacy_score = 0

    if lang.startswith("fa"):
        sexual_score = analyze_keywords(text_lower, SEXUAL_KEYWORDS["fa"])
        privacy_score = analyze_keywords(text_lower, PRIVACY_KEYWORDS["fa"])
    else:
        sexual_score = analyze_keywords(text_lower, SEXUAL_KEYWORDS["en"])
        privacy_score = analyze_keywords(text_lower, PRIVACY_KEYWORDS["en"])

    if sexual_score >= 60:
        return {
            "violation": "Non-consensual sexual content / Deepfake",
            "confidence": min(sexual_score, 100),
            "severity": "Critical",
            "language": lang,
        }

    if privacy_score >= 40:
        return {
            "violation": "Privacy violation / Doxxing",
            "confidence": min(privacy_score, 100),
            "severity": "High",
            "language": lang,
        }

    if sexual_score > 0 or privacy_score > 0:
        return {
            "violation": "Suspicious content",
            "confidence": max(sexual_score, privacy_score),
            "severity": "Medium",
            "language": lang,
        }

    return {
        "violation": "No clear violation detected",
        "confidence": 10,
        "severity": "Low",
        "language": lang,
    }
