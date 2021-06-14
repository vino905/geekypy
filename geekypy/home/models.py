from django.db import models
from django.contrib.auth.models import User
# from .models import contact

# Create your models here.

# -------------------------------------- FOR PROJECT SECTION ------------------------------------------------
class Pythonproject(models.Model):
      Title = models.CharField(max_length=50)
      Text = models.TextField()
      file_upload = models.FileField(null=True )
    
     # class Meta:
      #    verbose_name_plural = 

      def __str__(self):
          return f'{self.Title}'


class Cproject(models.Model):
      Title = models.CharField(max_length=50)
      Text = models.TextField()
      file_upload = models.FileField(null=True )
    

      def __str__(self):
          return f'{self.Title}'       

class Webdevlopment(models.Model):
      Title = models.CharField(max_length=50)
      Text = models.TextField()
      file_upload = models.FileField(null=True )
   

      def __str__(self):
          return f'{self.Title}'        


class Guiproject(models.Model):
      Title = models.CharField(max_length=50)
      Text = models.TextField()
      file_upload = models.FileField(null=True )
   

      def __str__(self):
          return f'{self.Title}'                    
# ------------------------------------------------CS PAPER-------------------------------------------------
class Cs2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class Cs3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class Cs4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        

# ------------------------------------------------IT PAPER-------------------------------------------------
class It2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class It3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class It4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        

# ------------------------------------------------Civil PAPER-------------------------------------------------
class Cve2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class Cve3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class Cve4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'       

# ------------------------------------------------Chemical Eng.. PAPER-------------------------------------------------
class Che2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class Che3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class Che4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'   

# ------------------------------------------------ECE PAPER-------------------------------------------------
class Ece2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class Ece3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class Ece4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'     

# ------------------------------------------------EE PAPER-------------------------------------------------
class Ee2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class Ee3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class Ee4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'         
# ------------------------------------------------ME PAPER-------------------------------------------------
class Me2Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'        
class Me3Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'    

class Me4Paper(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)

                      
# ------------------------------------------- FIRST YEAR ENG.. PAPER -------------------------------------------
class Firstyear(models.Model):
      subject = models.CharField(max_length=50)
      fileupload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.subject}'          
# ------------------------------------------- E-BOOKS SECTION ---------------------------------------------------
class Ebooks(models.Model):
      title = models.CharField(max_length=50)
      author = models.CharField(max_length=50)
      bookimage = models.ImageField( upload_to="book/images", default="")
      book_upload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.title}'   
          
# ------------------------------------------- ethical hacking section ---------------------------------------------------
class Ethical(models.Model):
      title = models.CharField(max_length=50)
      author = models.CharField(max_length=50)
      book_upload = models.FileField(null=True)
     
      
      def __str__(self):
          return f'{self.title}'   
          
# ----------------------------------------------- codes section ----------------------------------------------------
class Ccodes(models.Model):
      title = models.CharField(max_length=200)
      code= models.TextField(max_length=2000)
      
      
     
      
      def __str__(self):
          return f'{self.title}'     
   