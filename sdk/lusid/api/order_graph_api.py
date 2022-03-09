# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4077
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


class OrderGraphApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_order_graph_blocks(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.  # noqa: E501

        Lists all blocks of orders, subject to the filter, along with the IDs of orders, placements, allocations and  executions in the block, the total quantities of each, and a simple text field describing the overall state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_order_graph_blocks(async_req=True)
        >>> result = thread.get()

        :param as_at: See https://support.lusid.com/knowledgebase/article/KA-01832/
        :type as_at: datetime
        :param pagination_token: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type pagination_token: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName.
        :type sort_by: list[str]
        :param limit: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type limit: int
        :param filter: See https://support.lusid.com/knowledgebase/article/KA-01914/
        :type filter: str
        :param property_keys: Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/
        :type property_keys: list[str]
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
        :rtype: PagedResourceListOfOrderGraphBlock
        """
        kwargs['_return_http_data_only'] = True
        return self.list_order_graph_blocks_with_http_info(**kwargs)  # noqa: E501

    def list_order_graph_blocks_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.  # noqa: E501

        Lists all blocks of orders, subject to the filter, along with the IDs of orders, placements, allocations and  executions in the block, the total quantities of each, and a simple text field describing the overall state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_order_graph_blocks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param as_at: See https://support.lusid.com/knowledgebase/article/KA-01832/
        :type as_at: datetime
        :param pagination_token: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type pagination_token: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName.
        :type sort_by: list[str]
        :param limit: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type limit: int
        :param filter: See https://support.lusid.com/knowledgebase/article/KA-01914/
        :type filter: str
        :param property_keys: Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/
        :type property_keys: list[str]
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
        :rtype: tuple(PagedResourceListOfOrderGraphBlock, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'as_at',
            'pagination_token',
            'sort_by',
            'limit',
            'filter',
            'property_keys'
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
                    " to method list_order_graph_blocks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('pagination_token' in local_var_params and  # noqa: E501
                                                        len(local_var_params['pagination_token']) > 500):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `pagination_token` when calling `list_order_graph_blocks`, length must be less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('pagination_token' in local_var_params and  # noqa: E501
                                                        len(local_var_params['pagination_token']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `pagination_token` when calling `list_order_graph_blocks`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'pagination_token' in local_var_params and not re.search(r'^[a-zA-Z0-9\+\/]*={0,3}$', local_var_params['pagination_token']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `pagination_token` when calling `list_order_graph_blocks`, must conform to the pattern `/^[a-zA-Z0-9\+\/]*={0,3}$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_order_graph_blocks`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_order_graph_blocks`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) > 16384):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_order_graph_blocks`, length must be less than or equal to `16384`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_order_graph_blocks`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'filter' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_order_graph_blocks`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'pagination_token' in local_var_params and local_var_params['pagination_token'] is not None:  # noqa: E501
            query_params.append(('paginationToken', local_var_params['pagination_token']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'property_keys' in local_var_params and local_var_params['property_keys'] is not None:  # noqa: E501
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

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
            200: "PagedResourceListOfOrderGraphBlock",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/ordergraph/blocks', 'GET',
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

    def list_order_graph_placements(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.  # noqa: E501

        Lists all order placements, subject to the filter, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_order_graph_placements(async_req=True)
        >>> result = thread.get()

        :param as_at: See https://support.lusid.com/knowledgebase/article/KA-01832/
        :type as_at: datetime
        :param pagination_token: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type pagination_token: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName.
        :type sort_by: list[str]
        :param limit: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type limit: int
        :param filter: See https://support.lusid.com/knowledgebase/article/KA-01914/
        :type filter: str
        :param property_keys: Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/
        :type property_keys: list[str]
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
        :rtype: PagedResourceListOfOrderGraphPlacement
        """
        kwargs['_return_http_data_only'] = True
        return self.list_order_graph_placements_with_http_info(**kwargs)  # noqa: E501

    def list_order_graph_placements_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.  # noqa: E501

        Lists all order placements, subject to the filter, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_order_graph_placements_with_http_info(async_req=True)
        >>> result = thread.get()

        :param as_at: See https://support.lusid.com/knowledgebase/article/KA-01832/
        :type as_at: datetime
        :param pagination_token: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type pagination_token: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName.
        :type sort_by: list[str]
        :param limit: See https://support.lusid.com/knowledgebase/article/KA-01915/
        :type limit: int
        :param filter: See https://support.lusid.com/knowledgebase/article/KA-01914/
        :type filter: str
        :param property_keys: Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/
        :type property_keys: list[str]
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
        :rtype: tuple(PagedResourceListOfOrderGraphPlacement, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'as_at',
            'pagination_token',
            'sort_by',
            'limit',
            'filter',
            'property_keys'
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
                    " to method list_order_graph_placements" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('pagination_token' in local_var_params and  # noqa: E501
                                                        len(local_var_params['pagination_token']) > 500):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `pagination_token` when calling `list_order_graph_placements`, length must be less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('pagination_token' in local_var_params and  # noqa: E501
                                                        len(local_var_params['pagination_token']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `pagination_token` when calling `list_order_graph_placements`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'pagination_token' in local_var_params and not re.search(r'^[a-zA-Z0-9\+\/]*={0,3}$', local_var_params['pagination_token']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `pagination_token` when calling `list_order_graph_placements`, must conform to the pattern `/^[a-zA-Z0-9\+\/]*={0,3}$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_order_graph_placements`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_order_graph_placements`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) > 16384):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_order_graph_placements`, length must be less than or equal to `16384`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_order_graph_placements`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'filter' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_order_graph_placements`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'pagination_token' in local_var_params and local_var_params['pagination_token'] is not None:  # noqa: E501
            query_params.append(('paginationToken', local_var_params['pagination_token']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'property_keys' in local_var_params and local_var_params['property_keys'] is not None:  # noqa: E501
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

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
            200: "PagedResourceListOfOrderGraphPlacement",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/ordergraph/placements', 'GET',
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
