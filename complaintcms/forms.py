from django import forms

from complaintcms.models import Complaint

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Complaint
        field = '__all__'