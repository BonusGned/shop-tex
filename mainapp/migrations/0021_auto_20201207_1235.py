# Generated by Django 3.1.3 on 2020-12-07 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20201130_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_key', models.CharField(max_length=100, verbose_name='Ключ характеристка')),
                ('feature_name', models.CharField(max_length=255, verbose_name='Наименование харктеристики')),
                ('postfix_for_value', models.CharField(blank=True, help_text='НАпример для характеристики "Часы работы" кзначению можно добавить пстфикс "часов", и как результат - значение "10 часов"', max_length=20, null=True, verbose_name='Постфикс для значения')),
                ('use_in_filter', models.BooleanField(default=False, verbose_name='Использовать для фильтрации товаров в шаблоне')),
                ('filter_type', models.CharField(choices=[('radio', 'Радиокнопка'), ('checkbox', 'Чекбокс')], default='checkbox', max_length=20, verbose_name='Тип фильтра')),
                ('filter_measure', models.CharField(help_text='ЕДиница измерения для конкретного фильтра. Например "Частота процессора (Ghz)."Единицей измерения будет информации в скобках.', max_length=50, verbose_name='Единица измерения для фильтра')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='ProductFeatureValidators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_value', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Значение характеристики')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
                ('feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.productfeatures', verbose_name='Характеристика')),
            ],
        ),
        migrations.AddField(
            model_name='productfeatures',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория'),
        ),
    ]
