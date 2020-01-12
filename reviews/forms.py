from reviews.models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        fields = ('rating', 'review', 'reported_feelings',
                  'reported_activities', 'reported_reliefs')
