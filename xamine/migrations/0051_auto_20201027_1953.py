# Generated by Django 3.1.2 on 2020-10-27 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0050_auto_20201026_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='amountPaid',
            new_name='amount_Ins_Paid',
        ),
        migrations.AddField(
            model_name='balance',
            name='amount_Pat_Paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]