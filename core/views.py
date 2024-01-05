from django.shortcuts import render, redirect
from django.views import View
from core.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm

# home / index page
class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        else:
            return render(request, 'index.html')

# profile
method_decorator(login_required,name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request,'profileList.html',{'profiles':profiles})


# create profile
method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request, *args, **kwargs):
        form =ProfileForm()
        return render(request,'profileCreate.html',{'form':form})
    
    def post(self,request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
        return render(request,'profileCreate.html',{'form':form})
    

