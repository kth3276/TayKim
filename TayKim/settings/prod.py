from .common import *

# 실 서비스 들어가게 되면 도메인 입력
# ALLOWED_HOSTS = ['www.example.kr']

DEBUG = False

STATICFILES_STORAGE = 'TayKim.storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'TayKim.storages.MediaStorage'

# AZURE_ACCOUNT_NAME = os.environ['AZURE_ACCOUNT_NAME']
AZURE_ACCOUNT_NAME = 'taykim'
# AZURE_ACCOUNT_KEY = os.environ['AZURE_ACCOUNT_KEY']
AZURE_ACCOUNT_KEY = '9AFrRC/m/9W08G7kHNknQTsd1AEBDSoxHgGkGh3cezB64S5CHLgK+e6kGGZyW7PZOZe1pB0iRvmM0uAqkv5GyA=='
AZURE_SSL = True