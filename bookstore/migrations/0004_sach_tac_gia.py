# Generated by Django 4.2.7 on 2023-12-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_alter_bc_congno_no_cuoi_alter_bc_congno_no_dau_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sach',
            name='tac_gia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
