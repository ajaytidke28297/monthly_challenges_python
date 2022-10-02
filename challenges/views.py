from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
)

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Walk for at least 20 minutes every day",
    "april": "Walk for at least 20 minutes every day",
    "may": "Walk for at least 20 minutes every day",
    "june": "Walk for at least 20 minutes every day",
    "july": "Walk for at least 20 minutes every day",
    "august": "Walk for at least 20 minutes every day",
    "september": "Walk for at least 20 minutes every day",
    "october": "Walk for at least 20 minutes every day",
    "november": "Walk for at least 20 minutes every day",
    "december": "Walk for at least 20 minutes every day",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    return HttpResponsePermanentRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        HttpResponseNotFound("This month is not supported")
