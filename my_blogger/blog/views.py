from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Jasmine",
        "date": date(2024, 3, 29),
        "title": "Nature at its best",
        "excerpt": "Why are all our AI voices female? Siri, Alexa, ... And all the intelligent and fictional AI voices male? Jarvis (Iron Man 2), Sully (I, Robot), ...",
        "content": "lorem ipsum"
    },
    {
        "slug": "ai-voices",
        "image": "Capture1.JPG",
        "author": "Jasmine",
        "date": date(2024, 4, 29),
        "title": "AI Voices",
        "excerpt": "Why are all our AI voices female? Siri, Alexa, ... And all the intelligent and fictional AI voices male? Jarvis (Iron Man 2), Sully (I, Robot), ...",
        "content": "lorem ipsum"
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Jasmine",
        "date": date(2024, 5, 29),
        "title": "Programming!",
        "excerpt": "Why are all our AI voices female? Siri, Alexa, ... And all the intelligent and fictional AI voices male? Jarvis (Iron Man 2), Sully (I, Robot), ...",
        "content": "lorem ipsum"
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")