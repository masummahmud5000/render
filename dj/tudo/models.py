from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, name, username, password=None):
        user = self.model(name=name, username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, username, password=None):
        user = self.create_user(
            name=name,
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
    
class Server(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    username = models.CharField(db_index=True, unique=True, max_length=100)
    joinDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['username'],
            name = 'user_btree_idx'
            ),]
        
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username
        