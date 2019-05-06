from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class Article(models.Model):
    title = models.CharField("blog_title",max_length = 100)
    category = models.CharField("category",max_length = 50, blank = True)
    pub_date = models.DateTimeField("pub_date",auto_now_add = True,editable=True)
    content = UEditorField("Title",height = 300, width = 1000, default = 'Time to write!',blank = True,imagePath='uploads/blog/images',
                           toolbars = "besttome",filePath = "uploads/blog/files")

    def __unicode__(self):
        return self.title

    class Meta: 
        ordering = ['-pub_date']
        verbose_name = "Article"
        verbose_name_plural = "Aritcle"
    