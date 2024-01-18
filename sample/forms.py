from django.forms import ModelForm
from sample.models import *


class SampleForm(ModelForm):
    class Meta:
        model = SampleModel
        fields = ["name"]
