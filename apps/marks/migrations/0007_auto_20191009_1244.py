# Generated by Django 2.1.11 on 2019-10-09 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marks', '0006_auto_20190506_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkRuleSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('valid_from_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(help_text='Regelsett skrevet i markdown', verbose_name='Regler')),
                ('version', models.CharField(max_length=128, unique=True, verbose_name='Versjon')),
            ],
            options={
                'verbose_name': 'Prikkegelsett',
                'verbose_name_plural': 'Prikkeregelsett',
                'ordering': ('-valid_from_date',),
            },
        ),
        migrations.CreateModel(
            name='RuleAcceptance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_date', models.DateTimeField(auto_now_add=True)),
                ('rule_set', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_accepts', to='marks.MarkRuleSet', verbose_name='Brukere som har akseptert')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_mark_rule_sets', to=settings.AUTH_USER_MODEL, verbose_name='Godkjente prikkeregelsett')),
            ],
            options={
                'verbose_name': 'Regelgodkjenning',
                'verbose_name_plural': 'Regelgodkjennelser',
                'ordering': ('rule_set', 'accepted_date'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='ruleacceptance',
            unique_together={('user', 'rule_set')},
        ),
    ]