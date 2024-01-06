from django import forms
from chapAp.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'reg_no', 'Association', 'Ministry', 'Scc']
