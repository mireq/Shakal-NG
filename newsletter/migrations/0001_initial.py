# Generated by Django 4.2 on 2023-06-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='NewsletterSubscription',
			fields=[
				('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
			],
			options={
				'verbose_name': 'Newsletter subscription',
				'verbose_name_plural': 'Newsletter subscriptions',
			},
		),
	]
