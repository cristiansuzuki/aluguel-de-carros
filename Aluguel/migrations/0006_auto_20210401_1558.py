# Generated by Django 3.1.7 on 2021-04-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0005_auto_20210329_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='valor',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]