from django.shortcuts import render


def landing(request):
    return render(
        request,
        'single_page/landing.html'
    )


def about_us(request):
    return render(
        request,
        'single_page/about.html'
    )


def mypage(request):
    return render(
        request,
        'single_page/mypage.html'
    )


def login(request):
    return render(
        request,
        'single_page/login.html'
    )