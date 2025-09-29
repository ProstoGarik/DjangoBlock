from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        label='Заголовок',
        max_length=127,
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea,
        max_length=512,
    )

class UserForm(forms.Form):
    username = forms.CharField(
        max_length=127,
    )
    password = forms.CharField(
        max_length=127,
        widget=forms.PasswordInput,
    )
