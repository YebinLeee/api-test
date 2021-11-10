from django.db import models
from taggit.managers import TaggableManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        
class Post(BaseModel):
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=64, blank = False)
    content = models.TextField()
    image = models.ImageField(blank=True, null = True)
    # likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    tags = TaggableManager()

    def __str__(self):
        return '%s - %s' %(self.id, self. title)

    # def total_likes(self):
    #     return self.likes.count()