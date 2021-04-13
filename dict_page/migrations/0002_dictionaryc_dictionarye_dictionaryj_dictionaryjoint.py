# Generated by Django 3.0.7 on 2020-08-04 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dict_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictionaryC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=50, null=True)),
                ('definition', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DictionaryE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=50, null=True)),
                ('definition', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DictionaryJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=50, null=True)),
                ('definition', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DictionaryJoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dict_page.DictionaryC')),
                ('english', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dict_page.DictionaryE')),
                ('japansese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dict_page.DictionaryJ')),
            ],
        ),
    ]