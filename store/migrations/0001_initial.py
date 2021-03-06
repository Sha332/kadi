# Generated by Django 3.2.2 on 2021-05-17 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('brands', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='post image')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('messages', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('customer_amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Cach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('delivery_instructions', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acount_number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=150)),
                ('delivery_instructions', models.CharField(max_length=150)),
                ('receipt', models.FileField(upload_to='post the receipt')),
            ],
        ),
        migrations.CreateModel(
            name='product_Antiques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='post image')),
            ],
        ),
        migrations.CreateModel(
            name='product_typewriters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='post image')),
            ],
        ),
        migrations.CreateModel(
            name='product_watches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='post image')),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Contact phone')),
                ('password', models.CharField(max_length=15, verbose_name='Password')),
            ],
        ),
    ]
