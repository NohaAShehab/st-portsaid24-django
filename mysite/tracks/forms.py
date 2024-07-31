
from django import forms

from tracks.models import Track


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'