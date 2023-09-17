from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField(unique=True)
    password = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)
    login_date = models.DateTimeField(null=True, blank=True)
    withdrawal = models.DateTimeField(null=True, blank=True)
    
class NameSuggestion(models.Model):
    suggestion_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion_name = models.TextField()
    suggestion_date = models.DateTimeField()
    
class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_file_name = models.TextField()
    image_upload_date = models.DateTimeField()
    image_url = models.TextField()
    suggestion = models.ForeignKey(NameSuggestion, on_delete=models.CASCADE)
    
class PrivacySetting(models.Model):
    privacy_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    setting_update_date = models.DateTimeField()