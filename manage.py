#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""
import os
import sys
from backend.configloader import Config


if __name__ == '__main__':
    Config.validate()
    wsgi_file = f'backend.settings.{Config.get("mode")}'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', wsgi_file)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
