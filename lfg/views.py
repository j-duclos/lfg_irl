from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


#@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'lfg/profile.html', {'form': form, 'user_profile': user_profile})        