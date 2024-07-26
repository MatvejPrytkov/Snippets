from django.db import models
from django.contrib.auth.models import User


LANGS = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
    ('html', 'HTML')
)
private = (
    ('+', 'Private'),
    ('-', 'Public')
)


class Snippet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_snippets', null=True)
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    priv = models.CharField(max_length=30, choices=private,   null=True)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,  null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributed_snippets', null=True)
    #title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)

