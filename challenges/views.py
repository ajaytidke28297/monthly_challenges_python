from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    if month == "january":
        challenge_text = "Eat no meat"
    else:
        return HttpResponseNotFound("This month challenge not configured")
    return HttpResponse(challenge_text)
