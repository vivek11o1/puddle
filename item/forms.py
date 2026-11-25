from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-2 px-3 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name' , 'category' , 'price' , 'description', 'image',]
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'Item name'}),
            
            'category' : forms.Select(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'Item category'}),
            
            'price' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'price'}),
            
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'description'
            }),
            
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES,
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name' , 'price' , 'description', 'image', 'is_sold']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'Item name'}),
            
            'price' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'price'}),
            
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES,
                'placeholder' : 'description'
            }),
            
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES,
            }),
        }
    