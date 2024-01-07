from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))

    class Meta:
        model = get_user_model()
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'username': 'Логин',
        }

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Логин'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Аккаунт с этим Email уже зарегистрирован')
        return email


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'organisation', 'description', 'photo']
        labels = {
            'organisation': 'Организация',
            'description': 'Ваше описание',
        }

        widgets = {
            'organisation' : forms.TextInput(attrs={'placeholder': 'Ваше место работы'}),
            'first_name' : forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'description': forms.Textarea(attrs={'placeholder': 'Описание'}),
            'photo': forms.FileInput(),
        }
