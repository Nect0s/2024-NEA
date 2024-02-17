from django.apps import AppConfig


class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'

#"members" is the only app held on the server, this contains all web pages and functionality
    