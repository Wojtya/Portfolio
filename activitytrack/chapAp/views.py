from django.shortcuts import render, redirect
from .models import Member, Association, Ministry, Scc
from .forms import MemberForm

# Create your views here.s

def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = MemberForm()
    return render(request, 'reg.html', {'form': form})



def homeView(request):
    return render(request, 'chapap/home.html')
