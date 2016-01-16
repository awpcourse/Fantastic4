from django.forms import Form, CharField, DateTimeField, ImageField, Textarea, PasswordInput

class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)
