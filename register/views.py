from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, FeedbackForm
from django.views.generic import UpdateView
from .models import UserProfile
from django.urls import reverse_lazy

from django.core.mail import mail_admins
# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form":form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            redirect('home')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


class ProfilePage(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserForm
    template_name = "profilepage.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        pk = self.request.user.userlink.id
        return reverse_lazy('account', kwargs={'pk':pk})

#---------------- feedback/contact us view --------------------------#
def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)

        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have been contact by {} - {}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)

            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('home')

    else:
        f = FeedbackForm()
    return render(request, 'feedback.html', {'form': f})