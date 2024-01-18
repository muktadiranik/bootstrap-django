from django.shortcuts import render
from django.views import View
from sample.forms import *


class IndexView(View):
    def get(self, request):
        form = SampleForm()
        return render(request, "sample/index.html", {
            "form": form
        })
