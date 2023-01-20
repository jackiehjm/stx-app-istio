#
# Copyright (c) 2022 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

# Application Name
HELM_APP_ISTIO = 'istio'

# Namespace to deploy the application
HELM_NS_ISTIO_OPERATOR = 'istio-operator'
HELM_NS_ISTIO_SYSTEM = 'istio-system'

# Helm: Supported charts:
# These values match the names in the chart package's Chart.yaml
HELM_CHART_ISTIO_OPERATOR = 'istio-operator'
HELM_CHART_KIALI_SERVER = 'kiali-server'
