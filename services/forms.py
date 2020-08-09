from datetime import date

from django.forms import (
CharField, DateField, IntegerField, ModelForm, ImageField, ModelChoiceField, Textarea
)
from django.core.exceptions import ValidationError

from services.models import Category, Cities, Services

class FutureDateField(DateField):

    def validate(self, value):
        super().validate(value)
        if value <= date.today():
            raise ValidationError("Only future dates allowed here.")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=result.day)


class ServiceForm(ModelForm):

    class Meta:
        model = Services
        fields = '__all__'


class ServiceEditForm(ModelForm):
    class Meta:
        model = Services
        fields = ('title', 'photo', 'category', 'price', 'city', 'deadline', 'description')