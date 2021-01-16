from django import forms
from .models import Staff

class CreateUserForm(forms.ModelForm):
    #modelformを継承する
    class meta():
        model = Staff
        fields = ("name ", "password", "roll", "nyushabi", "taishabi", "hyoujijyun", "jikyu", "delete ")
