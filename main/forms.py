from django.forms import ModelForm
from main.models import Product

class GothEntryForm(ModelForm):
    class Meta:
        model = Product 
        fields = ["name", "price", "description", "gothness"]


