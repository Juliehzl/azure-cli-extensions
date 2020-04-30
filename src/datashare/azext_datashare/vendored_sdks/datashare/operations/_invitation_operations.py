# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class InvitationOperations(object):
    """InvitationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_share_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        invitation_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Invitation"
        """Get an invitation in a share.

        Get Invitation in a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param invitation_name: The name of the invitation.
        :type invitation_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Invitation or the result of cls(response)
        :rtype: ~data_share_management_client.models.Invitation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Invitation"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'invitationName': self._serialize.url("invitation_name", invitation_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DataShareError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Invitation', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations/{invitationName}'}

    def create(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        invitation_name,  # type: str
        target_active_directory_id=None,  # type: Optional[str]
        target_email=None,  # type: Optional[str]
        target_object_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Invitation"
        """Create an invitation.

        Sends a new invitation to a recipient to access a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share to send the invitation for.
        :type share_name: str
        :param invitation_name: The name of the invitation.
        :type invitation_name: str
        :param target_active_directory_id: The target Azure AD Id. Can't be combined with email.
        :type target_active_directory_id: str
        :param target_email: The email the invitation is directed to.
        :type target_email: str
        :param target_object_id: The target user or application Id that invitation is being sent to.
         Must be specified along TargetActiveDirectoryId. This enables sending
         invitations to specific users or applications in an AD tenant.
        :type target_object_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Invitation or the result of cls(response)
        :rtype: ~data_share_management_client.models.Invitation or ~data_share_management_client.models.Invitation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Invitation"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _invitation = models.Invitation(target_active_directory_id=target_active_directory_id, target_email=target_email, target_object_id=target_object_id)
        api_version = "2019-11-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'invitationName': self._serialize.url("invitation_name", invitation_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_invitation, 'Invitation')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DataShareError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Invitation', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Invitation', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations/{invitationName}'}

    def delete(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        invitation_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete an invitation in a share.

        Delete Invitation in a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param invitation_name: The name of the invitation.
        :type invitation_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'invitationName': self._serialize.url("invitation_name", invitation_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DataShareError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations/{invitationName}'}

    def list_by_share(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        skip_token=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.InvitationList"
        """List invitations in a share.

        List all Invitations in a share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param skip_token: The continuation token.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: InvitationList or the result of cls(response)
        :rtype: ~data_share_management_client.models.InvitationList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.InvitationList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_share.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str'),
                    'shareName': self._serialize.url("share_name", share_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skip_token is not None:
                query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('InvitationList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DataShareError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_share.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations'}
