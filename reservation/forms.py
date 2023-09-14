from django import forms
from .models import trains
class BookingForm(forms.Form):
    # ... other fields ...
    num_people = forms.IntegerField(label='Number of People', min_value=1)
