from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-enfold-teal-500 focus:border-enfold-teal-500'
        })
    )
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-enfold-teal-500 focus:border-enfold-teal-500'
        }),
        help_text='Your password must contain at least 8 characters.'
    )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-enfold-teal-500 focus:border-enfold-teal-500'
        }),
        help_text='Enter the same password as before, for verification.'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        
        # Additional username validation
        if not re.match(r'^[\w.@+-]+$', username):
            raise ValidationError("Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")
        
        # Case-insensitive username check
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("A user with that username already exists.")
        
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Password validation
        if password1 and password2:
            if password1 != password2:
                raise ValidationError({
                    "password2": "Passwords do not match."
                })
            
            # Additional password strength checks
            if len(password1) < 8:
                raise ValidationError({
                    "password1": "Password must be at least 8 characters long."
                })
            
            # Optional: Add more password complexity checks
            if not re.search(r'[A-Z]', password1):
                raise ValidationError({
                    "password1": "Password must contain at least one uppercase letter."
                })
            
            if not re.search(r'[0-9]', password1):
                raise ValidationError({
                    "password1": "Password must contain at least one number."
                })

        return cleaned_data