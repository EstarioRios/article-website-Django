from django.db import models
from AuthenticationSystem.models import CustomUser


class Blog(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    contect = models.FileField(null=False, blank=False)
    tags = models.TextField(
        null=True, blank=True, default="none"
    )  # tags will be like : "none - lovely - fun"
    likes = models.IntegerField(default=0, blank=False, null=False)
    dislikes = models.IntegerField(default=0, blank=False, null=False)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE(),
        null=False,
        blank=False,
        related_name="blogs",
    )


class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    like = models.IntegerField(default=0, blank=False, null=False)
    dislike = models.IntegerField(default=0, blank=False, null=False)
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE(),
        blank=False,
        null=False,
        related_name="comments",
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE(),
        null=False,
        blank=False,
    )
