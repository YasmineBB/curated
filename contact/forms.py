from django import forms
from .models import ContactForm


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = (
            'contact_name',
            'contact_email',
            'contact_subject',
            'contact_message',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders,
        remove auto-generated labels,
        set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_subject': 'Subject',
            'contact_message': 'Your Message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False