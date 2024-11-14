from django import forms
from .models import *

# Admin Form with password confirmation and proper validation
class AdminForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = Admin
        fields = ['username', 'password', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        
        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

# Category Form with proper field handling
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'created_by']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize ForeignKey fields (created_by) as dropdowns
        self.fields['created_by'].widget.attrs.update({'class': 'form-control'})
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

# Supplier Form with ForeignKey and field customization
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'created_by']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize ForeignKey fields (created_by) as dropdowns
        self.fields['created_by'].widget.attrs.update({'class': 'form-control'})
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

# Item Form with price handling and ForeignKey customizations
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'quantity', 'category', 'supplier', 'created_by']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize ForeignKey fields (category, supplier, created_by) as dropdowns
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['supplier'].widget.attrs.update({'class': 'form-control'})
        self.fields['created_by'].widget.attrs.update({'class': 'form-control'})
        
        # Customize price field with step and quantity with min value
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'step': '0.01'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'min': '0'})
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
