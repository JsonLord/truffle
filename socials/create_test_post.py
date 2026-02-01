import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from django.contrib.auth import get_user_model
from base.models import Profile, Post
from django.core.files.base import ContentFile

User = get_user_model()
admin = User.objects.get(username='admin')
profile = Profile.objects.get(user=admin)

# Create a test post
if not Post.objects.filter(title='Test Post with Media').exists():
    post = Post.objects.create(
        title='Test Post with Media',
        author=profile,
        caption='This is a test post with simulated media.',
        location='Test Location'
    )
    # Adding a dummy image
    post.image.save('test.jpg', ContentFile(b'dummy image content'), save=True)
    print("Test post created.")
else:
    print("Test post already exists.")
