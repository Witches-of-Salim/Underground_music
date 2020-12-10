# Generated by Django 3.0.11 on 2020-12-10 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.AlterModelOptions(
            name='albums',
            options={'verbose_name': 'альбом', 'verbose_name_plural': 'альбомы'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'исполнитель', 'verbose_name_plural': 'исполнители'},
        ),
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': 'трек', 'verbose_name_plural': 'треки'},
        ),
        migrations.AddField(
            model_name='albums',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musics.Author', verbose_name='исполнитель'),
        ),
        migrations.AddField(
            model_name='music',
            name='position',
            field=models.CharField(default=1, max_length=3, verbose_name='position_in_album'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='data',
            field=models.DateTimeField(verbose_name='дата издания'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='picture',
            field=models.ImageField(upload_to='media/', verbose_name='обложка'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(upload_to='media/', verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musics.Albums', verbose_name='альбом'),
        ),
        migrations.AlterField(
            model_name='music',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musics.Author', verbose_name='исполнитель'),
        ),
        migrations.AlterField(
            model_name='music',
            name='music',
            field=models.FileField(upload_to='media/', verbose_name='песня'),
        ),
        migrations.AlterField(
            model_name='music',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musics.Category', verbose_name='категория'),
        ),
    ]