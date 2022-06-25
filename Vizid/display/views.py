from django.shortcuts import render, redirect
from .models import Section as Sect
from django.views.generic import ListView, DetailView, CreateView
from .models import Comment
from .forms import UserCommentForm,UserContactForm,UserMeetingForm

global context
comment = Comment.objects.all()
context = {"comment": comment}


def home(request):
    comment = Comment.objects.all()

    if request.method=='POST':
        former=UserCommentForm(request.POST)
        if former.is_valid():
            former.save()
            return redirect("display/about.html")
    else:
        former = UserCommentForm()
    context = {"comment": comment,"former":former}
    return render(request,"display/index.html",context)

def about(request):
    return render(request, "display/about.html", context)


def contact(request):
    if request.method=='POST':
        form=UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = UserContactForm()

    if request.method == 'POST':
        mform=UserMeetingForm(request.POST)
        if mform.is_valid():
            mform.save()
            return redirect("contact")
    else:
        mform = UserMeetingForm()
    return render(request, "display/contact.html",{"former":form,"mform":mform})




class SectionView(ListView):
    model = Sect
    template_name = "display/section.html"
    context_object_name = "section"


class SectionDetails(DetailView):
    model = Sect
    template_name = "display/sectiondetails.html"

