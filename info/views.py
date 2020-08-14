from django.shortcuts import render

#from .form import UserForm

from django.contrib.auth.forms import UserCreationForm

from .form import CreateUserForm

# Create your views here.


def home(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            
            form.save()

    context={
        'form':form,
    }

    return render(request,'info/base.html',context)