from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.models import Doctor,Comment
from django.core.paginator import Paginator
from .forms import AddComment
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect 
from .filter import CFilter,DFilter
# Create your views here.

@login_required
def home(request):
    doc_list = Doctor.objects.all()
    myfilter=DFilter(request.GET,queryset=doc_list)
    doc_list=myfilter.qs
    paginator = Paginator(doc_list, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{"docs":page_obj,"filter":myfilter})


@csrf_exempt
@login_required
def detail(request,slug):
    docs=Doctor.objects.get(name=slug)
    w=str(request)
    where=w.split("'")
    comms=Comment.objects.filter(where=where[1])
    if request.method == 'POST':
        form = AddComment(request.POST)
        print(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.name=str(request.user)
            myform.comment=form.cleaned_data['comment']
            myform.where=where[1]
            myform.save()
            form=AddComment()
            return redirect("/")

    else:
        form=AddComment()
    return render(request,'detail.html',{"docs":docs,"form":form,"comms":comms})


def view_404(request,exception):
    return render(request,'404.html')