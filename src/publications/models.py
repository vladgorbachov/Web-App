from django.db import models



class Publication(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    comments = models.CharField(max_length=248, blank=True)
    description = models.CharField(max_length=200, blank=True)
    contents = models.FileField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return f'nickname - {self.profile}'