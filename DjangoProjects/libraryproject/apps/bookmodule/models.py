from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
    
class Publisher(models.Model):
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=300)
    
class Author(models.Model):
  name = models.CharField(max_length=200)
  DOB = models.DateField(null=True)
    
class NBook(models.Model):
  title = models.CharField(max_length= 100)
  price = models.FloatField(default=0.0)
  quantity = models.IntegerField(default=1)
  pubdate = models.DateTimeField()
  rating = models.SmallIntegerField(default = 1)
        
  publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
  authors = models.ManyToManyField(Author)
        
@property
def availability_percentage(self):
    total_quantity = NBook.objects.aggregate(total=models.Sum('quantity'))['total']
    if total_quantity and total_quantity > 0:
        return (self.quantity / total_quantity) * 100
    return 0