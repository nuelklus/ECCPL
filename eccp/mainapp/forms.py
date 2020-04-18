from django import forms


# create ContactForm

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'contact_input',
                                      'placeholder': 'Enter your name'}))  # TODO: added contact_input class that is connected to custom.css
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput({'class': 'contact_input', 'placeholder': 'Enter your email'}))
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput({'class': 'contact_input', 'placeholder': 'Enter your subject'}))
    message = forms.CharField(
        max_length=4000,
        widget=forms.Textarea({'class': 'contact_input', 'placeholder': 'Write your message here!', 'rows': '20',
                               'style': 'height: 150px;'}),

    )
