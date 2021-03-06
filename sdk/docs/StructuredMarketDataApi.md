# lusid.StructuredMarketDataApi

All URIs are relative to *http://local-unit-test-server.lusid.com:53528*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_structured_market_data**](StructuredMarketDataApi.md#delete_structured_market_data) | **POST** /api/structured/{scope}/$delete | [EXPERIMENTAL] DeleteStructuredMarketData: Delete one or more items of structured market data, assuming they are present.
[**get_structured_market_data**](StructuredMarketDataApi.md#get_structured_market_data) | **POST** /api/structured/{scope}/$get | [EXPERIMENTAL] GetStructuredMarketData: Get structured market data
[**upsert_structured_market_data**](StructuredMarketDataApi.md#upsert_structured_market_data) | **POST** /api/structured/{scope} | [EXPERIMENTAL] UpsertStructuredMarketData: Upsert a set of structured market data items. This creates or updates the data in Lusid.


# **delete_structured_market_data**
> AnnulStructuredDataResponse delete_structured_market_data(scope, request_body)

[EXPERIMENTAL] DeleteStructuredMarketData: Delete one or more items of structured market data, assuming they are present.

Delete one or more specified structured market data items from a single scope. Each item is identified by a unique id which includes  information about its type as well as the exact effective datetime (to the microsecond) at which it entered the system (became valid).                In the request each market data item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully deleted market data items, as well as those that failed.  For the failures a reason will be provided explaining why the it could not be deleted.                It is important to always check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:53528
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:53528"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:53528"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.StructuredMarketDataApi(api_client)
    scope = 'scope_example' # str | The scope of the structured market data to delete.
request_body = {"someCorrelationId1":{"provider":"DataScope","priceSource":"Some Bank Plc","lineage":"Swaps Desk Trader A","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketElementType":"FxVol","marketAsset":"USDJPY"}} # dict(str, StructuredMarketDataId) | The structured market data Ids to delete, each keyed by a unique correlation id.

    try:
        # [EXPERIMENTAL] DeleteStructuredMarketData: Delete one or more items of structured market data, assuming they are present.
        api_response = api_instance.delete_structured_market_data(scope, request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StructuredMarketDataApi->delete_structured_market_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the structured market data to delete. | 
 **request_body** | [**dict(str, StructuredMarketDataId)**](StructuredMarketDataId.md)| The structured market data Ids to delete, each keyed by a unique correlation id. | 

### Return type

[**AnnulStructuredDataResponse**](AnnulStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted StructuredMarketData along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structured_market_data**
> GetStructuredMarketDataResponse get_structured_market_data(scope, request_body, effective_at=effective_at, as_at=as_at, max_age=max_age)

[EXPERIMENTAL] GetStructuredMarketData: Get structured market data

Get one or more items of structured market data from a single scope.                Each item can be identified by its time invariant structured market data identifier.                For each id LUSID will return the most recent matched item with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified which defines how far back to look back for data from the specified effective datetime.  LUSID will return the most recent item within this window.                In the request each structured market data id must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each item in the response.                The response will return three collections. One, the successfully retrieved structured market data. Two, those that had a  valid identifier but could not be found. Three, those that failed because LUSID could not construct a valid identifier from the request.    For the ids that failed to resolve or could not be found a reason will be provided explaining why that is the case.                It is important to always check the failed and not found sets for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:53528
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:53528"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:53528"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.StructuredMarketDataApi(api_client)
    scope = 'scope_example' # str | The scope of the structured market data to retrieve.
request_body = {"someCorrelationId1":{"provider":"DataScope","priceSource":"Some Bank Plc","lineage":"Swaps Desk Trader A","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketElementType":"FxVol","marketAsset":"USDJPY"}} # dict(str, StructuredMarketDataId) | The time invariant set of structured data identifiers to retrieve the data for. These need to be               keyed by a unique correlation id allowing the retrieved item to be identified in the response.
effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the structured market data. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the structured market data. Defaults to return the latest version if not specified. (optional)
max_age = 'max_age_example' # str | The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a structured market data item must exist to be retrieved. (optional)

    try:
        # [EXPERIMENTAL] GetStructuredMarketData: Get structured market data
        api_response = api_instance.get_structured_market_data(scope, request_body, effective_at=effective_at, as_at=as_at, max_age=max_age)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StructuredMarketDataApi->get_structured_market_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the structured market data to retrieve. | 
 **request_body** | [**dict(str, StructuredMarketDataId)**](StructuredMarketDataId.md)| The time invariant set of structured data identifiers to retrieve the data for. These need to be               keyed by a unique correlation id allowing the retrieved item to be identified in the response. | 
 **effective_at** | **str**| The effective datetime at which to retrieve the structured market data. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the structured market data. Defaults to return the latest version if not specified. | [optional] 
 **max_age** | **str**| The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a structured market data item must exist to be retrieved. | [optional] 

### Return type

[**GetStructuredMarketDataResponse**](GetStructuredMarketDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved structured market data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_structured_market_data**
> UpsertStructuredDataResponse upsert_structured_market_data(scope, request_body)

[EXPERIMENTAL] UpsertStructuredMarketData: Upsert a set of structured market data items. This creates or updates the data in Lusid.

Update or insert one or more structured market data items in a single scope. An item will be updated if it already exists  and inserted if it does not.                In the request each structured market data item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each structured market data in the response.                The response will return both the collection of successfully updated or inserted structured market data, as well as those that failed.  For the failures a reason will be provided explaining why the item could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:53528
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:53528"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:53528"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.StructuredMarketDataApi(api_client)
    scope = 'scope_example' # str | The scope to use when updating or inserting the structured market data.
request_body = {"first-item":{"marketDataId":{"provider":"DataScope","priceSource":"Some Bank Plc","lineage":"Swaps Desk Trader A","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketElementType":"FxVolSurface","marketAsset":"USDJPY"},"marketData":{"documentFormat":"Xml","version":"1.0.0","name":"free text identifier of document 1","document":"<xml>data</xml>"}},"second-item":{"marketDataId":{"provider":"DataScope","priceSource":"AN.Other Bank Plc","lineage":"Swaps Desk Trader B","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","marketElementType":"IrVolCube","marketAsset":"RBS"},"marketData":{"documentFormat":"Json","version":"1.0.0","name":"free text identifier of document 1","document":"{ \"some\":\"valid json\"}"}}} # dict(str, UpsertStructuredMarketDataRequest) | The set of structured market data items to update or insert keyed by a unique correlation id.

    try:
        # [EXPERIMENTAL] UpsertStructuredMarketData: Upsert a set of structured market data items. This creates or updates the data in Lusid.
        api_response = api_instance.upsert_structured_market_data(scope, request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StructuredMarketDataApi->upsert_structured_market_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the structured market data. | 
 **request_body** | [**dict(str, UpsertStructuredMarketDataRequest)**](UpsertStructuredMarketDataRequest.md)| The set of structured market data items to update or insert keyed by a unique correlation id. | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted StructuredMarketData along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

