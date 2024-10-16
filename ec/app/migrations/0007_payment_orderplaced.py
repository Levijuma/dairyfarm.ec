# Generated by Django 5.1.1 on 2024-10-09 22:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cart_product_alter_cart_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('ordered_data', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('001', 'Mombasa'), ('002', 'Kwale'), ('003', 'Kilifi'), ('004', 'Tana River'), ('005', 'Lamu'), ('006', 'Taita-Taveta'), ('007', 'Garissa'), ('008', 'Wajir'), ('009', 'Mandera'), ('010', 'Marsabit'), ('011', 'Isiolo'), ('012', 'Meru'), ('013', 'Tharaka-Nithi'), ('014', 'Embu'), ('015', 'Kitui'), ('016', 'Machakos'), ('017', 'Makueni'), ('018', 'Nyandarua'), ('019', 'Nyeri'), ('020', 'Kirinyaga'), ('021', 'Murang’a'), ('022', 'Kiambu'), ('023', 'Turkana'), ('024', 'West Pokot'), ('025', 'Samburu'), ('026', 'Trans-Nzoia'), ('027', 'Uasin Gishu'), ('028', 'Elgeyo-Marakwet'), ('029', 'Nandi'), ('030', 'Baringo'), ('031', 'Laikipia'), ('032', 'Nakuru'), ('033', 'Narok'), ('034', 'Kajiado'), ('035', 'Kericho'), ('036', 'Bomet'), ('037', 'Kakamega'), ('038', 'Vihiga'), ('039', 'Bungoma'), ('040', 'Busia'), ('041', 'Siaya'), ('042', 'Kisumu'), ('043', 'Homa Bay'), ('044', 'Migori'), ('045', 'Kisii'), ('046', 'Nyamira'), ('047', 'Nairobi')], default='pending', max_length=50)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payment')),
            ],
        ),
    ]
