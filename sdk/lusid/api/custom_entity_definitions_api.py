# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3580
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CustomEntityDefinitionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_entity_definition(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateCustomEntityDefinition: Create a new CustomEntityDefinition  # noqa: E501

        Create a custom entity definition that does not already exist. Will return a Bad Request if the CustomEntityDefinition already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_custom_entity_definition(async_req=True)
        >>> result = thread.get()

        :param custom_entity_definition_request: The CustomEntityDefinitionRequest
        :type custom_entity_definition_request: CustomEntityDefinitionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CustomEntityDefinition
        """
        kwargs['_return_http_data_only'] = True
        return self.create_custom_entity_definition_with_http_info(**kwargs)  # noqa: E501

    def create_custom_entity_definition_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateCustomEntityDefinition: Create a new CustomEntityDefinition  # noqa: E501

        Create a custom entity definition that does not already exist. Will return a Bad Request if the CustomEntityDefinition already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_custom_entity_definition_with_http_info(async_req=True)
        >>> result = thread.get()

        :param custom_entity_definition_request: The CustomEntityDefinitionRequest
        :type custom_entity_definition_request: CustomEntityDefinitionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CustomEntityDefinition, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'custom_entity_definition_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_entity_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'custom_entity_definition_request' in local_var_params:
            body_params = local_var_params['custom_entity_definition_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3580'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            200: "CustomEntityDefinition",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentities/entitytypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_definition(self, entity_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetDefinition: Get CustomEntityDefinition  # noqa: E501

        Retrieve a CustomEntityDefinition by a specific EntityType at a point in AsAt time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_definition(entity_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of entity for which to retrieve the CustomEntityDefinition. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest). (required)
        :type entity_type: str
        :param as_at: The AsAt at which to retrieve the CustomEntityDefinition.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CustomEntityDefinition
        """
        kwargs['_return_http_data_only'] = True
        return self.get_definition_with_http_info(entity_type, **kwargs)  # noqa: E501

    def get_definition_with_http_info(self, entity_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetDefinition: Get CustomEntityDefinition  # noqa: E501

        Retrieve a CustomEntityDefinition by a specific EntityType at a point in AsAt time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_definition_with_http_info(entity_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of entity for which to retrieve the CustomEntityDefinition. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest). (required)
        :type entity_type: str
        :param as_at: The AsAt at which to retrieve the CustomEntityDefinition.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CustomEntityDefinition, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'entity_type',
            'as_at'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_type' is set
        if self.api_client.client_side_validation and ('entity_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_type` when calling `get_definition`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `get_definition`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `get_definition`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_type' in local_var_params:
            path_params['entityType'] = local_var_params['entity_type']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            200: "CustomEntityDefinition",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentities/entitytypes/{entityType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
