from django.shortcuts import render



def about_view(request):
    template_name = "about.html"
    return render(request, template_name)