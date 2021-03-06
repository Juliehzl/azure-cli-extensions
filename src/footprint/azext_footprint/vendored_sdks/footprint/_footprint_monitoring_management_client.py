# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import FootprintMonitoringManagementClientConfiguration
from .operations import OperationOperations
from .operations import ProfileOperations
from .operations import MeasurementEndpointOperations
from .operations import MeasurementEndpointConditionOperations
from .operations import ExperimentOperations
from . import models


class FootprintMonitoringManagementClient(object):
    """Microsoft Footprint active monitoring system REST API version 2020-02-01-preview.

    :ivar operation: OperationOperations operations
    :vartype operation: footprint_monitoring_management_client.operations.OperationOperations
    :ivar profile: ProfileOperations operations
    :vartype profile: footprint_monitoring_management_client.operations.ProfileOperations
    :ivar measurement_endpoint: MeasurementEndpointOperations operations
    :vartype measurement_endpoint: footprint_monitoring_management_client.operations.MeasurementEndpointOperations
    :ivar measurement_endpoint_condition: MeasurementEndpointConditionOperations operations
    :vartype measurement_endpoint_condition: footprint_monitoring_management_client.operations.MeasurementEndpointConditionOperations
    :ivar experiment: ExperimentOperations operations
    :vartype experiment: footprint_monitoring_management_client.operations.ExperimentOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = FootprintMonitoringManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.profile = ProfileOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.measurement_endpoint = MeasurementEndpointOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.measurement_endpoint_condition = MeasurementEndpointConditionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.experiment = ExperimentOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> FootprintMonitoringManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
