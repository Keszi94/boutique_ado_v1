from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            # list comprehension -
            # - shorthand way of for loop to add items to a list
            friendly_names = [
                (c.id, c.get_friendly_name()) for c in categories
            ]

            # instead of cat.id or name we will see the friendly name
            self.fields['caregory'].choices = friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'
