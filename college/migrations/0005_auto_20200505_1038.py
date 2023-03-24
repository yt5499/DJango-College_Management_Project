

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_auto_20200504_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student_id',
        ),
        migrations.AddField(
            model_name='attendance',
            name='roll',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='roll',
            field=models.CharField(max_length=10),
        ),
    ]
