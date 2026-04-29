from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import Contactform
from django.contrib import messages

# Create your views here.
def home(request):
    contacts = Contact.objects.all()    
    return render(request,'home.html',{'contacts':contacts})

def createcontact(request):
    if request.method=='POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact uploaded successfuly!')
            return redirect('home')
    else:
        form = Contactform()
    return render(request, 'createcontact.html',{'form':form})
    
def allcontacts(request):
    contacts = Contact.objects.all()
    return render(request, 'allcontacts.html',{'contacts':contacts})

def updatecontact(request, cid):
    contact = get_object_or_404(Contact, id=cid)
    if request.method == 'POST':
        form=Contactform(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,'Contact updated successfully!')
            return redirect('contacts')
    else:
        form = Contactform(instance=contact)
    return render(request,'updatecontact.html',{'form':form})

def deletecontact(request,cid):
    contact=get_object_or_404(Contact, id=cid)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully')
        return redirect('contacts')
    return render(request, 'deletecontact.html',{'contact':contact})
        