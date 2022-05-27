from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500, blank=False)
    description = models.CharField(max_length=500, blank=False)
    published = models.BooleanField(default=False)
    post_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title
