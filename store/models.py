from django.db import models

class register(models.Model):
    name = models.CharField('Name',max_length=150)
    email = models.EmailField('Email')
    phone= models.CharField('Contact phone' , max_length=15)
    password = models.CharField('Password',max_length=15)


    def __str__(self):
        return self.name

class product_watches(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField(null=False)
    image = models.FileField(upload_to='post image', blank=False)

    def Fall_descrbation1 (self):
        return self.body[:100]

    def __str__(self):
        return self.name

class product_typewriters(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField(null=False)
    image = models.FileField(upload_to='post image', blank=False)

    def Fall_descrbation2 (self):
        return self.body[:100]

    def __str__(self):
        return self.name

class product_typewriters(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField(null=False)
    image = models.FileField(upload_to='post image', blank=False)

    def Fall_descrbation2 (self):
        return self.body[:100]

    def __str__(self):
        return self.name

class brands(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField(null=False)
    brands=models.CharField(max_length=150)
    image = models.FileField(upload_to='post image', blank=False)

    def Fall_descrbation3 (self):
        return self.body[:100]

    def __str__(self):
        return self.name

class product_Antiques(models.Model):
    name = models.CharField(max_length=250)
    price = models.PositiveIntegerField(null=False)
    image = models.FileField(upload_to='post image', blank=False)

    def Fall_descrbation4 (self):
        return self.body[:100]

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    messages = models.TextField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    name = models.CharField(max_length=150)
    customer_amount = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name

class Payment_Cach(models.Model):
    name = models.CharField(max_length=150)
    delivery_instructions = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Payment_transfer(models.Model):
    acount_number=models.PositiveIntegerField(null=False)
    name = models.CharField(max_length=150)
    delivery_instructions = models.CharField(max_length=150)
    receipt = models.FileField(upload_to='post the receipt', blank=False)

    def __str__(self):
            return self.name

