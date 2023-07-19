import json
import os

import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

User = get_user_model()


def migrate_users():
    print("Migrating users...")

    with open("./temp_data/profile_data.json") as file:
        data = json.load(file)

    user_objects = []

    for entry in data:
        pk = entry["pk"]
        password = entry["fields"]["password"]
        last_login = entry["fields"]["last_login"]
        is_superuser = entry["fields"]["is_superuser"]
        username = entry["fields"]["username"]
        first_name = entry["fields"]["first_name"]
        last_name = entry["fields"]["last_name"]
        email = entry["fields"]["email"]
        is_staff = entry["fields"]["is_staff"]
        is_active = entry["fields"]["is_active"]
        date_joined = entry["fields"]["date_joined"]
        gender = entry["fields"]["gender"]
        nick_name = entry["fields"]["nick_name"]
        bio = entry["fields"]["bio"]
        staff_notes = entry["fields"]["staff_notes"]
        is_volunteer = entry["fields"]["is_volunteer"]
        is_premium = entry["fields"]["is_premium"]
        is_moderator = entry["fields"]["is_moderator"]
        is_lifetime_vip = entry["fields"]["is_lifetime_vip"]
        is_max_studying = entry["fields"]["is_max_studying"]

        user_objects.append(
            User(
                pk=pk,
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                bio=bio,
                date_joined=date_joined,
                last_login=last_login,
                is_superuser=is_superuser,
                is_staff=is_staff,
                is_active=is_active,
                nick_name=nick_name,
                staff_notes=staff_notes,
                is_volunteer=is_volunteer,
                is_premium=is_premium,
                is_moderator=is_moderator,
                is_lifetime_vip=is_lifetime_vip,
                is_max_studying=is_max_studying,
            )
        )

    User.objects.bulk_create(user_objects)


def main():
    migrate_users()


main()
