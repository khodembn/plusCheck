def get_mood_feedback(score):

    if score <= 3:
        return {
            "show_support": True,
            "message": "به نظر می‌رسه امروز حال خوبی نداری. اگر نیاز داری با مشاورمون صحبت کن",
            "counselor_phone": "09123456789",
        }

    return {
        "show_support": False,
        "message": None,
        "counselor_phone": None,
    }