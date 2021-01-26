from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "太郎"
        return ctxt

class AboutView(TemplateView):
    template_name = "app/about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 12345678
        ctxt["skills"] = [
            "Python",
            "Django",
            "Javascript",
            "Html"
        ]
        return ctxt
