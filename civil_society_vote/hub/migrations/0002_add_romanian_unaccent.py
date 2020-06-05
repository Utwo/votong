from django.contrib.postgres.operations import TrigramExtension, UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0001_initial"),
    ]

    operations = [
        TrigramExtension(),
        UnaccentExtension(),
        migrations.RunSQL(
            """
            CREATE TEXT SEARCH CONFIGURATION romanian_unaccent( COPY = romanian );
            ALTER TEXT SEARCH CONFIGURATION romanian_unaccent
            ALTER MAPPING FOR hword, hword_part, word
            WITH unaccent, romanian_stem;
            """
        ),
    ]
