# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3687
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


class SearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def instruments_search(self, instrument_search_property, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] InstrumentsSearch: Instruments search  # noqa: E501

        Search across all instruments that have been mastered in LUSID. Optionally augment the results with instruments from an external symbology service,  currently OpenFIGI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.instruments_search(instrument_search_property, async_req=True)
        >>> result = thread.get()

        :param instrument_search_property: A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. (required)
        :type instrument_search_property: list[InstrumentSearchProperty]
        :param mastered_effective_at: The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified.
        :type mastered_effective_at: str
        :param mastered_only: If set to true, only search over instruments that have been mastered within LUSID. Defaults to false.
        :type mastered_only: bool
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
        :rtype: list[InstrumentMatch]
        """
        kwargs['_return_http_data_only'] = True
        return self.instruments_search_with_http_info(instrument_search_property, **kwargs)  # noqa: E501

    def instruments_search_with_http_info(self, instrument_search_property, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] InstrumentsSearch: Instruments search  # noqa: E501

        Search across all instruments that have been mastered in LUSID. Optionally augment the results with instruments from an external symbology service,  currently OpenFIGI.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.instruments_search_with_http_info(instrument_search_property, async_req=True)
        >>> result = thread.get()

        :param instrument_search_property: A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. (required)
        :type instrument_search_property: list[InstrumentSearchProperty]
        :param mastered_effective_at: The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified.
        :type mastered_effective_at: str
        :param mastered_only: If set to true, only search over instruments that have been mastered within LUSID. Defaults to false.
        :type mastered_only: bool
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
        :rtype: tuple(list[InstrumentMatch], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'instrument_search_property',
            'mastered_effective_at',
            'mastered_only'
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
                    " to method instruments_search" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_search_property' is set
        if self.api_client.client_side_validation and ('instrument_search_property' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrument_search_property'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_search_property` when calling `instruments_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'mastered_effective_at' in local_var_params and local_var_params['mastered_effective_at'] is not None:  # noqa: E501
            query_params.append(('masteredEffectiveAt', local_var_params['mastered_effective_at']))  # noqa: E501
        if 'mastered_only' in local_var_params and local_var_params['mastered_only'] is not None:  # noqa: E501
            query_params.append(('masteredOnly', local_var_params['mastered_only']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'instrument_search_property' in local_var_params:
            body_params = local_var_params['instrument_search_property']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3687'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            200: "list[InstrumentMatch]",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/search/instruments', 'POST',
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

    def search_portfolio_groups(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups  # noqa: E501

        Search through all portfolio groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_portfolio_groups(async_req=True)
        >>> result = thread.get()

        :param search: A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type search: str
        :param filter: Expression to filter the result set.   For example, to filter on the Scope, use \"id.scope eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type filter: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.
        :type page: str
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
        :rtype: PagedResourceListOfPortfolioGroupSearchResult
        """
        kwargs['_return_http_data_only'] = True
        return self.search_portfolio_groups_with_http_info(**kwargs)  # noqa: E501

    def search_portfolio_groups_with_http_info(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] SearchPortfolioGroups: Search Portfolio Groups  # noqa: E501

        Search through all portfolio groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_portfolio_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param search: A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type search: str
        :param filter: Expression to filter the result set.   For example, to filter on the Scope, use \"id.scope eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type filter: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.
        :type page: str
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
        :rtype: tuple(PagedResourceListOfPortfolioGroupSearchResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'search',
            'filter',
            'sort_by',
            'limit',
            'page'
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
                    " to method search_portfolio_groups" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            200: "PagedResourceListOfPortfolioGroupSearchResult",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/search/portfoliogroups', 'GET',
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

    def search_portfolios(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] SearchPortfolios: Search Portfolios  # noqa: E501

        Search through all portfolios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_portfolios(async_req=True)
        >>> result = thread.get()

        :param search: A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type search: str
        :param filter: Expression to filter the result set.   For example, to filter on the portfolio Type, use \"type eq 'Transaction'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type filter: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.
        :type page: str
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
        :rtype: PagedResourceListOfPortfolioSearchResult
        """
        kwargs['_return_http_data_only'] = True
        return self.search_portfolios_with_http_info(**kwargs)  # noqa: E501

    def search_portfolios_with_http_info(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] SearchPortfolios: Search Portfolios  # noqa: E501

        Search through all portfolios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_portfolios_with_http_info(async_req=True)
        >>> result = thread.get()

        :param search: A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type search: str
        :param filter: Expression to filter the result set.   For example, to filter on the portfolio Type, use \"type eq 'Transaction'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type filter: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.
        :type page: str
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
        :rtype: tuple(PagedResourceListOfPortfolioSearchResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'search',
            'filter',
            'sort_by',
            'limit',
            'page'
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
                    " to method search_portfolios" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            200: "PagedResourceListOfPortfolioSearchResult",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/search/portfolios', 'GET',
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

    def search_properties(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] SearchProperties: Search Property Definitions  # noqa: E501

        Search through all Property Definitions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_properties(async_req=True)
        >>> result = thread.get()

        :param search: A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type search: str
        :param filter: Expression to filter the result set.   For example, to filter on the Value Type, use \"valueType eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type filter: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.
        :type page: str
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
        :rtype: PagedResourceListOfPropertyDefinitionSearchResult
        """
        kwargs['_return_http_data_only'] = True
        return self.search_properties_with_http_info(**kwargs)  # noqa: E501

    def search_properties_with_http_info(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] SearchProperties: Search Property Definitions  # noqa: E501

        Search through all Property Definitions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_properties_with_http_info(async_req=True)
        >>> result = thread.get()

        :param search: A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type search: str
        :param filter: Expression to filter the result set.   For example, to filter on the Value Type, use \"valueType eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid.
        :type filter: str
        :param sort_by: Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied.
        :type page: str
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
        :rtype: tuple(PagedResourceListOfPropertyDefinitionSearchResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'search',
            'filter',
            'sort_by',
            'limit',
            'page'
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
                    " to method search_properties" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            200: "PagedResourceListOfPropertyDefinitionSearchResult",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/search/propertydefinitions', 'GET',
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
