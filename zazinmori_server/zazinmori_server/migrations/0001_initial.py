# Generated by Django 4.1.1 on 2022-09-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('concept_id', models.AutoField(db_column='concept_id', primary_key=True, serialize=False)),
                ('regi_code', models.IntegerField(db_column='regi_code')),
                ('date', models.CharField(db_column='date', max_length=200)),
                ('concept', models.CharField(db_column='concept', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Corp_finance',
            fields=[
                ('finance_id', models.AutoField(db_column='finance_id', primary_key=True, serialize=False)),
                ('regi_code', models.IntegerField(db_column='regi_code')),
                ('date', models.CharField(db_column='date', max_length=200)),
                ('stock', models.CharField(db_column='stock', max_length=45)),
                ('total_sales', models.FloatField(db_column='total_sales', max_length=100)),
                ('profit', models.FloatField(db_column='profit', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('regi_code', models.AutoField(db_column='regi_code', primary_key=True, serialize=False)),
                ('corp_nm', models.CharField(db_column='corp_nm', max_length=45)),
                ('category', models.CharField(db_column='email', max_length=45)),
                ('president', models.CharField(db_column='passwd', max_length=45)),
                ('stock', models.CharField(db_column='stock', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cvletter_items',
            fields=[
                ('cvletter_items_id', models.AutoField(db_column='cvletter_items_id', primary_key=True, serialize=False)),
                ('jobs_id', models.IntegerField(db_column='jobs_id')),
                ('question', models.TextField(db_column='question')),
                ('cvletter_itemscol', models.CharField(db_column='cvletter_itemscol', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Job_posting',
            fields=[
                ('jobposting_id', models.AutoField(db_column='jobposting_id', primary_key=True, serialize=False)),
                ('regi_code', models.IntegerField(db_column='regi_code')),
                ('period', models.CharField(db_column='period', max_length=45)),
                ('start_date', models.CharField(db_column='start_date', max_length=200)),
                ('end_date', models.CharField(db_column='end_date', max_length=200)),
                ('posting_detail', models.TextField(db_column='posting_detail')),
            ],
        ),
        migrations.CreateModel(
            name='Jobposting_job',
            fields=[
                ('jobs_id', models.AutoField(db_column='jobs_id', primary_key=True, serialize=False)),
                ('jobposting_id', models.IntegerField(db_column='jobposting_id')),
                ('job', models.CharField(db_column='job', max_length=45)),
                ('new_or_exp', models.CharField(db_column='new_or_exp', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='passcvletter',
            fields=[
                ('cvletter_id', models.AutoField(db_column='cvletter_id', primary_key=True, serialize=False)),
                ('regi_code', models.IntegerField(db_column='regi_code')),
                ('corp_nm', models.CharField(db_column='corp_nm', max_length=45)),
                ('job', models.CharField(db_column='job', max_length=45)),
                ('employment_date', models.CharField(db_column='employment_date', max_length=200)),
                ('new_or_exp', models.CharField(db_column='new_or_exp', max_length=45)),
                ('question', models.TextField(db_column='question')),
                ('question_type', models.CharField(db_column='question_type', max_length=45)),
                ('answer', models.TextField(db_column='answer')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(db_column='topic_id', primary_key=True, serialize=False)),
                ('regi_code', models.IntegerField(db_column='regi_code')),
                ('corp_nm', models.CharField(db_column='corp_nm', max_length=45)),
                ('date', models.CharField(db_column='date', max_length=200)),
                ('title', models.CharField(db_column='title', max_length=45)),
                ('context', models.TextField(db_column='context')),
                ('url', models.CharField(db_column='url', max_length=45)),
                ('keyword', models.CharField(db_column='keyword', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User_cvletter',
            fields=[
                ('user_cvletter_id', models.AutoField(db_column='user_cvletter_id', primary_key=True, serialize=False)),
                ('member_id', models.CharField(db_column='member_id', max_length=45)),
                ('written_name', models.CharField(db_column='written_name', max_length=200)),
                ('written_date', models.CharField(db_column='written_date', max_length=200)),
                ('update_date', models.CharField(db_column='update_date', max_length=200)),
                ('q1', models.TextField(db_column='q1')),
                ('a1', models.TextField(db_column='a1')),
                ('q2', models.TextField(db_column='q2')),
                ('a2', models.TextField(db_column='a2')),
                ('q3', models.TextField(db_column='q3')),
                ('a3', models.TextField(db_column='a3')),
                ('q4', models.TextField(db_column='q4')),
                ('a4', models.TextField(db_column='a4')),
                ('q5', models.TextField(db_column='q5')),
                ('a5', models.TextField(db_column='a5')),
                ('q6', models.TextField(db_column='q6')),
                ('a6', models.TextField(db_column='a6')),
                ('q7', models.TextField(db_column='q7')),
                ('a7', models.TextField(db_column='a7')),
                ('q8', models.TextField(db_column='q8')),
                ('a8', models.TextField(db_column='a8')),
            ],
        ),
        migrations.CreateModel(
            name='User_scraps',
            fields=[
                ('scrap_id', models.AutoField(db_column='scrap_id', primary_key=True, serialize=False)),
                ('member_id', models.IntegerField(db_column='member_id')),
                ('jobposting_id', models.CharField(db_column='jobposting_id', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users_info',
            fields=[
                ('member_id', models.AutoField(db_column='member_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=50)),
                ('email', models.CharField(db_column='email', max_length=50)),
                ('passwd', models.CharField(db_column='passwd', max_length=1000)),
                ('birth', models.CharField(db_column='birthday', max_length=200)),
                ('reg_date', models.CharField(db_column='reg_date', max_length=200)),
                ('update_date', models.CharField(db_column='update_date', max_length=200)),
            ],
        ),
    ]