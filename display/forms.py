from django import forms
from .models import Comment,Contact,Meeting



class UserCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','comment']

class UserContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email',"phone","message"]

class UserMeetingForm(forms.ModelForm):
    date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model=Meeting
        fields=['name','email',"phone","date","reason"]
