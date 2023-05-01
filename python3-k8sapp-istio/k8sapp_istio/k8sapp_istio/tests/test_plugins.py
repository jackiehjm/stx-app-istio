#
# Copyright (c) 2022-2023 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

from k8sapp_istio.common import constants as app_constants

from sysinv.tests.db import base as dbbase


class K8SAppIstioAppMixin(object):
    app_name = app_constants.HELM_APP_ISTIO
    path_name = app_name + '.tgz'

    def setUp(self):
        super(K8SAppIstioAppMixin, self).setUp()


# Test Configuration:
# - Controller
# - IPv6
# - Ceph Storage
# - istio app
class K8SAppIstioControllerTestCase(K8SAppIstioAppMixin,
                                    dbbase.BaseIPv6Mixin,
                                    dbbase.BaseCephStorageBackendMixin,
                                    dbbase.ControllerHostTestCase):
    pass


# Test Configuration:
# - AIO
# - IPv4
# - Ceph Storage
# - istio app
class K8SAppIstioAIOTestCase(K8SAppIstioAppMixin,
                             dbbase.BaseCephStorageBackendMixin,
                             dbbase.AIOSimplexHostTestCase):
    pass
