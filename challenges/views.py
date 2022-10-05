from django.http import Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

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
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponsePermanentRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
    except:
        raise Http404("This month is not supported")
