# Generated by Django 2.2.12 on 2020-05-06 17:45

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RegisterNGORequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="updated"),
                ),
                ("name", models.CharField(max_length=254, verbose_name="Name")),
                (
                    "description",
                    models.TextField(
                        help_text="Organization's short description - max 500 chars.",
                        max_length=500,
                        verbose_name="Description",
                    ),
                ),
                (
                    "past_actions",
                    models.TextField(
                        help_text="Description of past actions, with empahsis on COVID-19 related actions.",
                        max_length=500,
                        verbose_name="Past actions",
                    ),
                ),
                (
                    "resource_types",
                    models.TextField(
                        help_text="The types of resources you anticipate you will need.",
                        max_length=500,
                        verbose_name="Resource tags",
                    ),
                ),
                (
                    "contact_name",
                    models.CharField(
                        max_length=254, verbose_name="Contact person's name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(default="", max_length=254, verbose_name="Email"),
                ),
                (
                    "contact_phone",
                    models.CharField(
                        max_length=15, verbose_name="Contact person's phone"
                    ),
                ),
                ("address", models.CharField(max_length=400, verbose_name="Address")),
                ("city", models.CharField(max_length=100, verbose_name="City")),
                (
                    "county",
                    models.CharField(
                        choices=[
                            ("ALBA", "ALBA"),
                            ("ARGES", "ARGES"),
                            ("ARAD", "ARAD"),
                            ("BACAU", "BACAU"),
                            ("BIHOR", "BIHOR"),
                            ("BISTRITA-NASAUD", "BISTRITA-NASAUD"),
                            ("BRAILA", "BRAILA"),
                            ("BRASOV", "BRASOV"),
                            ("BOTOSANI", "BOTOSANI"),
                            ("BUCURESTI", "BUCURESTI"),
                            ("BUZAU", "BUZAU"),
                            ("CLUJ", "CLUJ"),
                            ("CALARASI", "CALARASI"),
                            ("CARAS-SEVERIN", "CARAS-SEVERIN"),
                            ("CONSTANTA", "CONSTANTA"),
                            ("COVASNA", "COVASNA"),
                            ("DAMBOVITA", "DAMBOVITA"),
                            ("DOLJ", "DOLJ"),
                            ("GORJ", "GORJ"),
                            ("GALATI", "GALATI"),
                            ("GIURGIU", "GIURGIU"),
                            ("HUNEDOARA", "HUNEDOARA"),
                            ("HARGHITA", "HARGHITA"),
                            ("IALOMITA", "IALOMITA"),
                            ("IASI", "IASI"),
                            ("ILFOV", "ILFOV"),
                            ("MEHEDINTI", "MEHEDINTI"),
                            ("MARAMURES", "MARAMURES"),
                            ("MURES", "MURES"),
                            ("NEAMT", "NEAMT"),
                            ("OLT", "OLT"),
                            ("PRAHOVA", "PRAHOVA"),
                            ("SIBIU", "SIBIU"),
                            ("SALAJ", "SALAJ"),
                            ("SATU-MARE", "SATU-MARE"),
                            ("SECTOR 1", "SECTOR 1"),
                            ("SECTOR 2", "SECTOR 2"),
                            ("SECTOR 3", "SECTOR 3"),
                            ("SECTOR 4", "SECTOR 4"),
                            ("SECTOR 5", "SECTOR 5"),
                            ("SECTOR 6", "SECTOR 6"),
                            ("SUCEAVA", "SUCEAVA"),
                            ("TULCEA", "TULCEA"),
                            ("TIMIS", "TIMIS"),
                            ("TELEORMAN", "TELEORMAN"),
                            ("VALCEA", "VALCEA"),
                            ("VRANCEA", "VRANCEA"),
                            ("VASLUI", "VASLUI"),
                        ],
                        max_length=50,
                        verbose_name="County",
                    ),
                ),
                (
                    "social_link",
                    models.CharField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="Link to website or Facebook",
                    ),
                ),
                ("active", models.BooleanField(default=False, verbose_name="Active")),
                (
                    "resolved_on",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Resolved on"
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        help_text="Image should be 500x500px",
                        max_length=300,
                        upload_to="",
                        verbose_name="logo",
                    ),
                ),
                (
                    "last_balance_sheet",
                    models.FileField(
                        max_length=300,
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to="",
                        verbose_name="First page of last balance sheet",
                    ),
                ),
                (
                    "statute",
                    models.FileField(
                        max_length=300,
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to="",
                        verbose_name="NGO Statute",
                    ),
                ),
                (
                    "registered_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Registered on"
                    ),
                ),
                ("closed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Vote history",
                "verbose_name_plural": "Votes history",
            },
        ),
        migrations.CreateModel(
            name="NGO",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="updated"),
                ),
                ("name", models.CharField(max_length=254, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "contact_name",
                    models.CharField(
                        max_length=254, verbose_name="Contact person's name"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=30, verbose_name="Phone")),
                ("address", models.CharField(max_length=400, verbose_name="Address")),
                (
                    "cif",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="CIF"
                    ),
                ),
                (
                    "cui",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="CUI"
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        choices=[
                            ("ALBA", "ALBA"),
                            ("ARGES", "ARGES"),
                            ("ARAD", "ARAD"),
                            ("BACAU", "BACAU"),
                            ("BIHOR", "BIHOR"),
                            ("BISTRITA-NASAUD", "BISTRITA-NASAUD"),
                            ("BRAILA", "BRAILA"),
                            ("BRASOV", "BRASOV"),
                            ("BOTOSANI", "BOTOSANI"),
                            ("BUCURESTI", "BUCURESTI"),
                            ("BUZAU", "BUZAU"),
                            ("CLUJ", "CLUJ"),
                            ("CALARASI", "CALARASI"),
                            ("CARAS-SEVERIN", "CARAS-SEVERIN"),
                            ("CONSTANTA", "CONSTANTA"),
                            ("COVASNA", "COVASNA"),
                            ("DAMBOVITA", "DAMBOVITA"),
                            ("DOLJ", "DOLJ"),
                            ("GORJ", "GORJ"),
                            ("GALATI", "GALATI"),
                            ("GIURGIU", "GIURGIU"),
                            ("HUNEDOARA", "HUNEDOARA"),
                            ("HARGHITA", "HARGHITA"),
                            ("IALOMITA", "IALOMITA"),
                            ("IASI", "IASI"),
                            ("ILFOV", "ILFOV"),
                            ("MEHEDINTI", "MEHEDINTI"),
                            ("MARAMURES", "MARAMURES"),
                            ("MURES", "MURES"),
                            ("NEAMT", "NEAMT"),
                            ("OLT", "OLT"),
                            ("PRAHOVA", "PRAHOVA"),
                            ("SIBIU", "SIBIU"),
                            ("SALAJ", "SALAJ"),
                            ("SATU-MARE", "SATU-MARE"),
                            ("SECTOR 1", "SECTOR 1"),
                            ("SECTOR 2", "SECTOR 2"),
                            ("SECTOR 3", "SECTOR 3"),
                            ("SECTOR 4", "SECTOR 4"),
                            ("SECTOR 5", "SECTOR 5"),
                            ("SECTOR 6", "SECTOR 6"),
                            ("SUCEAVA", "SUCEAVA"),
                            ("TULCEA", "TULCEA"),
                            ("TIMIS", "TIMIS"),
                            ("TELEORMAN", "TELEORMAN"),
                            ("VALCEA", "VALCEA"),
                            ("VRANCEA", "VRANCEA"),
                            ("VASLUI", "VASLUI"),
                        ],
                        max_length=50,
                        verbose_name="County",
                    ),
                ),
                ("city", models.CharField(max_length=100, verbose_name="City")),
                (
                    "logo",
                    models.ImageField(
                        max_length=300,
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to="",
                        verbose_name="Logo",
                    ),
                ),
                (
                    "last_balance_sheet",
                    models.FileField(
                        blank=True,
                        max_length=300,
                        null=True,
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to="",
                        verbose_name="First page of last balance sheet",
                    ),
                ),
                (
                    "statute",
                    models.FileField(
                        blank=True,
                        max_length=300,
                        null=True,
                        storage=django.core.files.storage.FileSystemStorage(),
                        upload_to="",
                        verbose_name="NGO Statute",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="ngos", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "My organization",
                "verbose_name_plural": "My organizations",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="PendingRegisterNGORequest",
            fields=[],
            options={
                "verbose_name": "Pending NGO",
                "verbose_name_plural": "Pending NGOs",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("hub.registerngorequest",),
        ),
        migrations.CreateModel(
            name="RegisterNGORequestVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="updated"),
                ),
                ("entity", models.CharField(max_length=30)),
                (
                    "vote",
                    models.CharField(
                        choices=[
                            ("YES", "YES"),
                            ("NO", "NO"),
                            ("ABSTENTION", "ABSTENTION"),
                        ],
                        default="ABSTENTION",
                        max_length=10,
                        verbose_name="Vote",
                    ),
                ),
                (
                    "motivation",
                    models.TextField(
                        blank=True,
                        help_text="Motivate your decision",
                        max_length=500,
                        null=True,
                        verbose_name="Motivation",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Date")),
                (
                    "ngo_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="hub.RegisterNGORequest",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "My vote",
                "verbose_name_plural": "My votes",
                "unique_together": {("ngo_request", "entity")},
            },
        ),
    ]
