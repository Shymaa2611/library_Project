# Generated by Django 4.1.7 on 2023-05-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_client_data_delete_blog_list_delete_doctor_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_data',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client_data',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]