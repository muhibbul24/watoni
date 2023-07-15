from django import forms
from django.utils.safestring import mark_safe

# model user aut
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(), required=True
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(), required=True
    )

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]


class VisibleMultipleHiddenInput(forms.widgets.HiddenInput):
    def render(self, name, value, attrs=None, renderer=None):
        if not attrs:
            attrs = {}
        attrs['type'] = 'hidden'  # Change the input type to 'hidden'
        return mark_safe(super().render(name, value, attrs, renderer))

class ImageUploadForm(forms.Form):
    # css class for bootstrap 4
    image = forms.ImageField(
        label='Select a file',
        help_text='max. 42 megabytes',
        widget=VisibleMultipleHiddenInput(
            attrs={
                'multiple': True,
                'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100 cursor-pointer',
                'id': 'image-field',
                'accept': 'image/*',
                'onchange': 'previewImage()',
                'type': 'file'
            },
        ),
        allow_empty_file=False,
        required=True,
        error_messages={'required': 'Please select an image file.'},
        disabled=False
    )
    uploader = forms.CharField(
        max_length=100,
        label='Uploader',
        help_text='Who upload this image?',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input your name',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'uploader'
                }
            ),
        required=True,
        error_messages={'required': 'Please input your name.'},
        empty_value='Anonymous'
    )