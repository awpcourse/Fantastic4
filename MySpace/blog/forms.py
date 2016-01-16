from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, CharField, TextInput,  DateTimeField, ImageField, Textarea, PasswordInput
from django.forms import ModelForm
from blog.models import UserInfo, User, UserPostComment, Likes
from django.contrib.auth.forms import UserCreationForm

class UserCreateFrom(UserCreationForm):
    
    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data["password1"])
        return user

class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class RegisterForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = UserCreateFrom()
        self.fields.update(self.user.fields)

    def is_valid(self):
        return super(RegisterForm, self).is_valid() and self.user.is_valid()

    
    def save(self, commit=True):
        self.user.data = {field: self.cleaned_data.pop(field) for field in self.user.fields}
        user = self.user.save()
        self.instance.user = user
        return super(RegisterForm, self).save(commit=commit)

    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'birth_date', 'email']

    
class UserPostCommentForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(UserPostCommentForm, self).__init__(*args, **kwargs)
        #self.comment = User
        #self.fields.update(self.comment.fields)
        self.fields['text'].widget.attrs['placeholder'] = 'Write a comment...'
        self.fields['text'].widget.attrs['label'] = ''
        self.fields['text'].widget.attrs['cols'] = 100
        self.fields['text'].widget.attrs['rows'] =  5
 
    class Meta:
        model = UserPostComment
        fields = ['text']

    
class UserPostCommentForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(UserPostCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Write a comment...'
        self.fields['text'].widget.attrs['label'] = ''
        self.fields['text'].widget.attrs['cols'] = 100
        self.fields['text'].widget.attrs['rows'] =  5
 
    class Meta:
        model = UserPostComment
        fields = ['text']


