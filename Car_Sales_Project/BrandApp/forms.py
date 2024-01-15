from django import forms 
from . models import BrandModel

class BranModelForm(forms.ModelForm): 
    class Meta:
        model = BrandModel 
        fields = '__all__'
        
