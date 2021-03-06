# Generated by Django 3.1.2 on 2020-10-16 00:19



from django.db import migrations, models

import django.db.models.deletion





class Migration(migrations.Migration):



    dependencies = [

        ('xamine', '0045_auto_20201014_2035'),

    ]



    operations = [

        migrations.CreateModel(

            name='Material',

            fields=[

                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=128)),

            ],

        ),

        migrations.CreateModel(

            name='MaterialOrder',

            fields=[

                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('quantity', models.IntegerField()),

                ('price', models.IntegerField(blank=True, null=True)),

                ('billed', models.IntegerField(default=0)),

                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='xamine.material')),

                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mat_order', to='xamine.order')),

            ],

        ),

    ]
