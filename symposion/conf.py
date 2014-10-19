# settings is needed for internal view
from django.conf import settings

from appconf import AppConf


class SymposionAppConf(AppConf):
    VOTE_THRESHOLD = 3
