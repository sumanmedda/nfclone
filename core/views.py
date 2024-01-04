from django.shortcuts import render
from django.views import View

# home / index page
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Index.html')

