from django import forms
from .models import Booking  # Import your Booking model


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['book_name', 'book_email', 'book_date', 'book_phn', 'book_dep', 'book_desc']
        widgets = {
            'book_name': forms.TextInput(attrs={
                "type": "text",
                "class": "form-control",
                "id": "name",
                "name": "name",
                "placeholder": "Full Name"
            }),
            'book_email': forms.EmailInput(attrs={
                "type": "email",
                "class": "form-control",
                "id": "email",
                "name": "email",
                "placeholder": "Your Email"
            }),
            'book_date': forms.TextInput(attrs={
                "type": "date",
                "class": "form-control",
                "name": "date",
            }),
            'book_phn': forms.TextInput(attrs={
                "type": "tel",
                "class": "form-control",
                "id": "phone",
                "name": "phone",
                "placeholder": "Phone"
            }),
            'book_dep': forms.Select(attrs={
                "class": "form-control",
            }),
            'book_desc': forms.Textarea(attrs={
                "class": "form-control",
                "id": "message",
                "name": "message",
                "placeholder": "Message",
                "rows": "5"
            })
        }


