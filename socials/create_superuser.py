import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from django.contrib.auth import get_user_model
from base.models import Profile

User = get_user_model()
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser {username}...")
    user = User.objects.create_superuser(username=username, email=email, password=password)
    Profile.objects.get_or_create(user=user, username=username)
else:
    print(f"Superuser {username} already exists.")
    user = User.objects.get(username=username)
    Profile.objects.get_or_create(user=user, username=username)
