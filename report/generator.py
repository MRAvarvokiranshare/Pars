def generate_report(link, analysis, policy):
    return f"""
TELEGRAM ABUSE REPORT

Link:
{link}

Violation:
{analysis['violation']}

Severity:
{analysis['severity']}

Confidence:
{analysis['confidence']}%

Policy:
{policy}

Description:
This content appears to contain non-consensual sexual material
and violates Telegram rules.

Please review and take action.
"""
