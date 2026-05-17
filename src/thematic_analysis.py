THEME_MAP = {

     "Login Issues": [
        "login",
        "password",
        "otp",
        "account",
        "signin",
        "verify"
    ],

    "Transaction Problems": [
        "transfer",
        "payment",
        "failed",
        "slow",
        "transaction",
        "loading"
    ],

    "User Experience": [
        "ui",
        "design",
        "interface",
        "easy",
        "navigation",
        "experience"
    ],

    "Performance Issues": [
        "crash",
        "bug",
        "freeze",
        "error",
        "stuck"
    ],

    "Customer Support": [
        "support",
        "help",
        "service",
        "response",
        "customer"
    ]
}


def identify_theme(text):
    """
    Identify business theme from review.
    """

    text = text.lower()

    for theme, keywords in THEME_MAP.items():

        if any(
            keyword in text
            for keyword in keywords
        ):

            return theme

    return "Other"