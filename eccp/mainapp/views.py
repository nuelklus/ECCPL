from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.


# class HomeView(TemplateView):
#     template_name = "mainapp/home-3.html"


class ContactFormView(FormView):
    template_name = "mainapp/home-3.html"
    form_class = ContactForm
    success_url = reverse_lazy('mainapp:homepage')

    def form_valid(self, form):
        clean_form = form.cleaned_data

        subject = clean_form.get('subject', '')
        message = clean_form.get('message', '')
        from_email = clean_form.get('email' '')
        print(from_email)
        send_mail(subject, message, from_email, ['nuelklus@gmail.com'])
        return super(ContactFormView, self).form_valid(form)

