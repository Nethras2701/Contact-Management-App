from django import forms
from .models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname','lastname','address','email','phoneno']
        labels = {
            'firstname' : 'First Name',
            'lastname' : 'Last Name' ,
            'address' : 'Address',
            'email' : 'Email Id',              
            'phoneno' : 'Phone Number'
        }
        widgets = {
            'firstname' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'enter first name '
            }),
            'lastname' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder' : 'enter last name'
            }),
            'address':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'enter address'
            }),
            'email' : forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'📧 ex: abc@email.com'    
            }),
            'phoneno':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': '📞 enter phone number'
            })

        }
    def clean_phoneno(self):
        phone = self.cleaned_data.get('phoneno')

        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits and length should be exactly 10")

        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits")

        return phone
