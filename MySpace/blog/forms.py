from django.forms import Form, CharField, DateTimeField, ImageField, Textarea, PasswordInput
from django.forms import ModelForm
from blog.models import UserInfo
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class RegisterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = UserCreationForm()
        self.fields.update(self.user.fields)

    
    def save(self, commit=True):
        user = self.user.save()
        self.instance.user = user
        return super(RegisterForm, self).save(commit=commit)

    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'birth_date', 'email']


