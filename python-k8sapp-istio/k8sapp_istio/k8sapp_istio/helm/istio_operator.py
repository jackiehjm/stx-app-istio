#
# Copyright (c) 2022 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

from sysinv.common import exception
from sysinv.helm import base

from k8sapp_istio.common import constants as app_constants


class IstioHelm(base.BaseHelm):
    """Class to encapsulate helm operations for the istio chart"""

    SUPPORTED_NAMESPACES = base.BaseHelm.SUPPORTED_NAMESPACES + \
        [app_constants.HELM_NS_ISTIO_SYSTEM]
    SUPPORTED_APP_NAMESPACES = {
        app_constants.HELM_APP_ISTIO:
            base.BaseHelm.SUPPORTED_NAMESPACES +
            [app_constants.HELM_NS_ISTIO_SYSTEM]
    }

    CHART = app_constants.HELM_CHART_ISTIO_OPERATOR

    SERVICE_NAME = app_constants.HELM_APP_ISTIO

    def get_namespaces(self):
        return self.SUPPORTED_NAMESPACES

    def get_overrides(self, namespace=None):
        overrides = {
            app_constants.HELM_NS_ISTIO_SYSTEM: {}
        }

        if namespace in self.SUPPORTED_NAMESPACES:
            return overrides[namespace]
        elif namespace:
            raise exception.InvalidHelmNamespace(chart=self.CHART,
                                                 namespace=namespace)
        else:
            return overrides
