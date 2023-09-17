from django import forms
from mainApp.models import CompClub


class CompClubForm(forms.ModelForm):
    class Meta:
        model = CompClub
        fields = [
            "name",
            "surname",
            "middlename",
            "email",
            "desired_place",
            "time_in",
            "time_out",
            "vip",
            "promo_code",
            "commentaries"
        ]