import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'AMG.settings'

try:
    import django
    django.setup()
    print("Django setup successful!")
except Exception as e:
    import traceback
    with open('error_log.txt', 'w') as f:
        traceback.print_exc(file=f)
    print("Full error written to error_log.txt")
