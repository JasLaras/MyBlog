from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!", 
    "may": "Walk for at least 20 minutes every day!", 
    "june": "Learn Django for at least 20 minutes every day!", 
    "july": "Eat no meat for the entire month!", 
    "august": "Walk for at least 20 minutes every day!", 
    "september": "Learn Django for at least 20 minutes every day!", 
    "october": "Eat no meat for the entire month!", 
    "november": "Learn Django for at least 20 minutes every day!", 
    "december": None
}

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."
    # for month in months:
         # capitalized_month = month.capitalize()
        # month_path = reverse("month-challenge", args=[month])
        # list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        # raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

# FIRST METHOD

# def index():
    # return HttpResponse("This works!")

# def january(request):
    # return HttpResponse("Eat no meat for the entire month!")

# def february(request):
    # return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
    # return HttpResponse("Learn Django for at least 20 minutes every day!")

# def monthly_challenge(request, month):
    # SECOND METHOD

    # challenge_text = None
    # if month == "january": 
        # challenge_text = "Eat no meat for the entire month!"
    # elif month == "february":
        # challenge_text = "Walk for at least 20 minutes every day!"
    # elif month == "march":
        # challenge_text = "Learn Django for at least 20 minutes every day!"
    # else:
        # return HttpResponseNotFound("This month is not supported!")
    # return HttpResponse(challenge_text)