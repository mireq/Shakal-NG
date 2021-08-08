# Generated by Django 3.2.4 on 2021-06-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		('blackhole', '0002_auto_20170603_1644'),
	]

	operations = [
		migrations.AlterModelOptions(
			name='term',
			options={'verbose_name': 'blackhole kategória', 'verbose_name_plural': 'blackhole kategórie'},
		),
		migrations.AlterField(
			model_name='term',
			name='level',
			field=models.PositiveIntegerField(editable=False),
		),
		migrations.AlterField(
			model_name='term',
			name='lft',
			field=models.PositiveIntegerField(editable=False),
		),
		migrations.AlterField(
			model_name='term',
			name='rght',
			field=models.PositiveIntegerField(editable=False),
		),
		migrations.AlterIndexTogether(
			name='term',
			index_together={('tree_id', 'lft')},
		),
	]