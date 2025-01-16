from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    next = forms.URLField(label="Next", widget=forms.HiddenInput, initial="/")


class ProfileForm(forms.Form):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput,
        allow_empty_file=True,
        required=False,
    )
    bio = forms.CharField(
        label="Biography (Markdown is supported)", widget=forms.Textarea, required=False
    )
