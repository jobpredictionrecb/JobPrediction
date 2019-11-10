from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'text-uppercase form-control'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'text-uppercase form-control'
            }
        )
    )
    username = forms.CharField(
        label="Enter Username",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control '
            }
        )
    )
    password2 = forms.CharField(
        label="Enter Cofirm Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-control'
            }
        )

    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Enter Username",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )
