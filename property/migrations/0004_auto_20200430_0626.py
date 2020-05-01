# Generated by Django 2.2.4 on 2020-04-30 03:26

from django.db import migrations


def check_out_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year < 2016:
            flat.new_building = False
        else:
            flat.new_building = True


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(check_out_new_building),
    ]
