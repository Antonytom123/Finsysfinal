# Generated by Django 3.2.23 on 2024-03-01 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0002_fin_recurring_invoice_comments_fin_recurring_invoice_history_fin_recurring_invoice_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
        migrations.CreateModel(
            name='Fin_Attendances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.employee')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Attendance_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2024, 3, 1))),
                ('action', models.CharField(max_length=100)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_attendances')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_attendance_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date(2024, 3, 1))),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_attendances')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
    ]
