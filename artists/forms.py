from django import forms
from products.models import Artist, Category


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'