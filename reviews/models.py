from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.CharField(max_length=20)
    grade = models.IntegerField(
        default=3,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        verbose_name="평점",
    )
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
