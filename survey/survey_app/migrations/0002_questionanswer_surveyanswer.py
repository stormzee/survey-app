# Generated by Django 3.1.2 on 2020-12-06 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_app.survey')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survey_app.choice')),
                ('survey_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_app.surveyanswer')),
            ],
        ),
    ]
