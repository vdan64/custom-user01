from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from .models import CustomUser

class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)

class CustomUserChangeform(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields