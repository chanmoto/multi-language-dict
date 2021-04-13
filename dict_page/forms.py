from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField
from django.db.models import Q
from .models import Dictionary
import pdb

class AddForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["word","def1","def2","def3","def4","def5","def6","def7","def8","def9","def10",]

class InputForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["word",]

    def validate_word(self):
        word = self.cleaned_data['word']
        if len(word) > 50:
            raise ValidationError("The length of the word is more than 50 characters!")
            # word = word[:50]
        return word
