from django import forms
from .models import Contact
from .models import note

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]

    class note(forms.ModelForm):
        class Meta:
            model = note
            fields = [
                'time',
                'text',
                'note'
            ]