from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('clicks', models.IntegerField()),
                ('impressions', models.IntegerField(blank=True, null=True)),
                ('campaign', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='ad_statistics.Campaign')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_statistics.Source')),
            ],
        ),
        migrations.AddConstraint(
            model_name='statistic',
            constraint=models.UniqueConstraint(
                fields=('date', 'campaign', 'source'), name='unique_daily_campaign_sources'),
        ),
    ]
