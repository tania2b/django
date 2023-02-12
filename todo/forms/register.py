from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name", min_length=5, max_length=100,
                               widget=forms.TextInput(attrs={'class': 'input',  'placeholder': 'Username'}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'input',  'placeholder': 'Email'}))
    password = forms.CharField(label="password", min_length=5, max_length=100, widget=forms.PasswordInput(attrs={'class': 'input',  'placeholder': 'Password'}))
    """
    PROFILE_IMAGE_CHOICES = [
        ('static/images/image1.jpg', 'Image 1'),
        ('static/images/image2.jpg', 'Image 2'),
        ('static/images/image3.jpg', 'Image 3'),
        ('static/images/image4.jpg', 'Image 4'),
        ('static/images/image5.jpg', 'Image 5'),
    ]
    profile_picture = forms.ChoiceField(label="Profile Image", choices=PROFILE_IMAGE_CHOICES)
    """
