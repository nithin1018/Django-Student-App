from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.

def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username} You're Good to go")
            return redirect('users:login')
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

class Register(FormView):
    form_class=RegisterForm
    template_name='users/register.html'
    success_url=reverse_lazy('users:login')

    def form_valid(self, form):
        user=form.save()
        user_name=form.cleaned_data.get('username')
        messages.success(self.request,f"Welcome {user.username} {user_name}You're Good to go")
        return super().form_valid(form)

@login_required
def profile(request):
    return render(request,'users/profile.html')