# Generated by Django 2.2.4 on 2019-08-23 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appproduto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ManyToManyField(to='appproduto.Produto'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
