from django.db import models

# Create your models here.
class Page(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    last_update=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/paged/detail/%i/" % self.id
        # return "Title: %s  Content: %s "%(self.title, self.content)

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('pages.views.Detail', args=[str(self.id)])
