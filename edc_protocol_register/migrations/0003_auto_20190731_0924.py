# Generated by Django 2.2 on 2019-07-31 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_protocol_register', '0002_auto_20190731_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='protocolrequest',
            options={'ordering': ['-request_date'], 'permissions': [('can_approve_request', 'user can approve request'), ('can_reject_request', 'user can reject request')]},
        ),
        migrations.AlterModelOptions(
            name='protocolresponse',
            options={},
        ),
    ]
