# Generated by Django 2.2.12 on 2020-05-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0002_add_romanian_unaccent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="county",
            field=models.CharField(
                choices=[
                    ("Alba", "Alba"),
                    ("Arad", "Arad"),
                    ("Arges", "Arges"),
                    ("Bacau", "Bacau"),
                    ("Bihor", "Bihor"),
                    ("Bistrita-Nasaud", "Bistrita-Nasaud"),
                    ("Botosani", "Botosani"),
                    ("Braila", "Braila"),
                    ("Brasov", "Brasov"),
                    ("Bucuresti", "Bucuresti"),
                    ("Buzau", "Buzau"),
                    ("Caras-Severin", "Caras-Severin"),
                    ("Calarasi", "Calarasi"),
                    ("Cluj", "Cluj"),
                    ("Constanta", "Constanta"),
                    ("Covasna", "Covasna"),
                    ("Dambovita", "Dambovita"),
                    ("Dolj", "Dolj"),
                    ("Galati", "Galati"),
                    ("Giurgiu", "Giurgiu"),
                    ("Gorj", "Gorj"),
                    ("Harghita", "Harghita"),
                    ("Hunedoara", "Hunedoara"),
                    ("Ialomita", "Ialomita"),
                    ("Iasi", "Iasi"),
                    ("Ilfov", "Ilfov"),
                    ("Maramures", "Maramures"),
                    ("Mehedinti", "Mehedinti"),
                    ("Mures", "Mures"),
                    ("Neamt", "Neamt"),
                    ("Olt", "Olt"),
                    ("Prahova", "Prahova"),
                    ("Satu Mare", "Satu Mare"),
                    ("Salaj", "Salaj"),
                    ("Sibiu", "Sibiu"),
                    ("Suceava", "Suceava"),
                    ("Teleorman", "Teleorman"),
                    ("Timis", "Timis"),
                    ("Tulcea", "Tulcea"),
                    ("Vaslui", "Vaslui"),
                    ("Valcea", "Valcea"),
                    ("Vrancea", "Vrancea"),
                ],
                max_length=50,
                verbose_name="County",
            ),
        ),
    ]