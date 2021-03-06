# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################
import logging
import pkg_resources

from pkgutil import extend_path


__path__ = extend_path(__path__, __name__)  # noqa
__version__ = pkg_resources.require("django-mapstore-adapter")[0].version

logger = logging.getLogger(__name__)


def fixup_map(map_id):
    """ ------------------------------------- Maps Fix """
    from geonode.maps.models import Map
    from django.contrib.auth import get_user_model
    from mapstore2_adapter.api.models import MapStoreResource
    for _m in Map.objects.filter(id=map_id):
        try:
            _u = get_user_model().objects.get(username=_m.owner.username)
            _mm, _created = MapStoreResource.objects.get_or_create(id=_m.id, user_id=_u.id)
            if _created:
                _mm.save()
        except Exception as e:
            logger.exception(e)


class DjangoMapstore2AdapterBaseException(Exception):
    """Base class for exceptions in this module."""
    pass


default_app_config = "mapstore2_adapter.apps.AppConfig"
