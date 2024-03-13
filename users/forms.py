from django.contrib.auth import get_user_model
# this looks for the AUTH_USER_MODEL config in settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm): # extends UserCreationForm

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm): # extends UserChangeForm

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)