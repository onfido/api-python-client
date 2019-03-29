# onfido.DefaultApi

All URIs are relative to *https://api.onfido.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_report**](DefaultApi.md#cancel_report) | **POST** /checks/{check_id}/reports/{report_id}/cancel | This endpoint is for cancelling individual paused reports.
[**create_applicant**](DefaultApi.md#create_applicant) | **POST** /applicants | Create Applicant
[**create_check**](DefaultApi.md#create_check) | **POST** /applicants/{applicant_id}/checks | Create a check
[**create_webhook**](DefaultApi.md#create_webhook) | **POST** /webhooks | Create a webhook
[**destroy_applicant**](DefaultApi.md#destroy_applicant) | **DELETE** /applicants/{applicant_id} | Delete Applicant
[**download_document**](DefaultApi.md#download_document) | **GET** /applicants/{applicant_id}/documents/{document_id}/download | Download a documents raw data
[**download_live_photo**](DefaultApi.md#download_live_photo) | **GET** /live_photos/{live_photo_id}/download | Download live photo
[**download_live_video**](DefaultApi.md#download_live_video) | **GET** /live_videos/{live_video_id}/download | Download live video
[**find_addresses**](DefaultApi.md#find_addresses) | **GET** /addresses/pick | Search for addresses by postcode
[**find_applicant**](DefaultApi.md#find_applicant) | **GET** /applicants/{applicant_id} | Retrieve Applicant
[**find_check**](DefaultApi.md#find_check) | **GET** /applicants/{applicant_id}/checks/{check_id} | Retrieve a Check
[**find_document**](DefaultApi.md#find_document) | **GET** /applicants/{applicant_id}/documents/{document_id} | A single document can be retrieved by calling this endpoint with the document’s unique identifier.
[**find_live_photo**](DefaultApi.md#find_live_photo) | **GET** /live_photos/{live_photo_id} | Retrieve live photo
[**find_live_video**](DefaultApi.md#find_live_video) | **GET** /live_videos/{live_video_id} | Retrieve live video
[**find_report**](DefaultApi.md#find_report) | **GET** /checks/{check_id}/reports/{report_id} | A single report can be retrieved using this endpoint with the corresponding unique identifier.
[**find_report_type_group**](DefaultApi.md#find_report_type_group) | **GET** /report_type_groups/{report_type_group_id} | Retrieve single report type group object
[**find_webhook**](DefaultApi.md#find_webhook) | **GET** /webhooks/{webhook_id} | Retrieve a Webhook
[**generate_sdk_token**](DefaultApi.md#generate_sdk_token) | **POST** /sdk_token | Generate a SDK token
[**list_applicants**](DefaultApi.md#list_applicants) | **GET** /applicants | List Applicants
[**list_checks**](DefaultApi.md#list_checks) | **GET** /applicants/{applicant_id}/checks | Retrieve Checks
[**list_documents**](DefaultApi.md#list_documents) | **GET** /applicants/{applicant_id}/documents | List documents
[**list_live_photos**](DefaultApi.md#list_live_photos) | **GET** /live_photos | List live photos
[**list_live_videos**](DefaultApi.md#list_live_videos) | **GET** /live_videos | List live videos
[**list_report_type_groups**](DefaultApi.md#list_report_type_groups) | **GET** /report_type_groups | Retrieve all report type groups
[**list_reports**](DefaultApi.md#list_reports) | **GET** /checks/{check_id}/reports | All the reports belonging to a particular check can be listed from this endpoint.
[**list_webhooks**](DefaultApi.md#list_webhooks) | **GET** /webhooks | List webhooks
[**restore_applicant**](DefaultApi.md#restore_applicant) | **POST** /applicants/{applicant_id}/restore | Restore Applicant
[**resume_check**](DefaultApi.md#resume_check) | **POST** /checks/{check_id}/resume | Resume a Check
[**resume_report**](DefaultApi.md#resume_report) | **POST** /checks/{check_id}/reports/{report_id}/resume | This endpoint is for resuming individual paused reports.
[**update_applicant**](DefaultApi.md#update_applicant) | **PUT** /applicants/{applicant_id} | Update Applicant
[**upload_document**](DefaultApi.md#upload_document) | **POST** /applicants/{applicant_id}/documents | Upload a document
[**upload_live_photo**](DefaultApi.md#upload_live_photo) | **POST** /live_photos | Upload live photo


# **cancel_report**
> cancel_report(check_id, report_id)

This endpoint is for cancelling individual paused reports.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
check_id = 'check_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # This endpoint is for cancelling individual paused reports.
    api_instance.cancel_report(check_id, report_id)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_applicant**
> Applicant create_applicant(applicant)

Create Applicant

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant = onfido.Applicant() # Applicant | 

try:
    # Create Applicant
    api_response = api_instance.create_applicant(applicant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant** | [**Applicant**](Applicant.md)|  | 

### Return type

[**Applicant**](Applicant.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_check**
> Check create_check(applicant_id, check)

Create a check

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
check = onfido.Check() # Check | 

try:
    # Create a check
    api_response = api_instance.create_check(applicant_id, check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **check** | [**Check**](Check.md)|  | 

### Return type

[**Check**](Check.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook**
> Webhook create_webhook(webhook)

Create a webhook

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
webhook = onfido.Webhook() # Webhook | 

try:
    # Create a webhook
    api_response = api_instance.create_webhook(webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_applicant**
> destroy_applicant(applicant_id)

Delete Applicant

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 

try:
    # Delete Applicant
    api_instance.destroy_applicant(applicant_id)
except ApiException as e:
    print("Exception when calling DefaultApi->destroy_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> file download_document(applicant_id, document_id)

Download a documents raw data

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
document_id = 'document_id_example' # str | 

try:
    # Download a documents raw data
    api_response = api_instance.download_document(applicant_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

**file**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_live_photo**
> file download_live_photo(live_photo_id)

Download live photo

Live photos are downloaded using this endpoint.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
live_photo_id = 'live_photo_id_example' # str | The live photo’s unique identifier.

try:
    # Download live photo
    api_response = api_instance.download_live_photo(live_photo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->download_live_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_photo_id** | **str**| The live photo’s unique identifier. | 

### Return type

**file**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_live_video**
> file download_live_video(live_video_id)

Download live video

Live videos are downloaded using this endpoint.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
live_video_id = 'live_video_id_example' # str | The live video’s unique identifier.

try:
    # Download live video
    api_response = api_instance.download_live_video(live_video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->download_live_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_video_id** | **str**| The live video’s unique identifier. | 

### Return type

**file**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_addresses**
> GenericAddressesList find_addresses(postcode)

Search for addresses by postcode

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
postcode = 'postcode_example' # str | 

try:
    # Search for addresses by postcode
    api_response = api_instance.find_addresses(postcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postcode** | **str**|  | 

### Return type

[**GenericAddressesList**](GenericAddressesList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_applicant**
> Applicant find_applicant(applicant_id)

Retrieve Applicant

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 

try:
    # Retrieve Applicant
    api_response = api_instance.find_applicant(applicant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

[**Applicant**](Applicant.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_check**
> CheckWithReportIds find_check(applicant_id, check_id)

Retrieve a Check

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
check_id = 'check_id_example' # str | 

try:
    # Retrieve a Check
    api_response = api_instance.find_check(applicant_id, check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **check_id** | **str**|  | 

### Return type

[**CheckWithReportIds**](CheckWithReportIds.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_document**
> Document find_document(applicant_id, document_id)

A single document can be retrieved by calling this endpoint with the document’s unique identifier.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
document_id = 'document_id_example' # str | 

try:
    # A single document can be retrieved by calling this endpoint with the document’s unique identifier.
    api_response = api_instance.find_document(applicant_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_live_photo**
> LivePhoto find_live_photo(live_photo_id)

Retrieve live photo

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
live_photo_id = 'live_photo_id_example' # str | The live photo’s unique identifier.

try:
    # Retrieve live photo
    api_response = api_instance.find_live_photo(live_photo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_live_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_photo_id** | **str**| The live photo’s unique identifier. | 

### Return type

[**LivePhoto**](LivePhoto.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_live_video**
> LiveVideo find_live_video(live_video_id)

Retrieve live video

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
live_video_id = 'live_video_id_example' # str | The live video’s unique identifier.

try:
    # Retrieve live video
    api_response = api_instance.find_live_video(live_video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_live_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_video_id** | **str**| The live video’s unique identifier. | 

### Return type

[**LiveVideo**](LiveVideo.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_report**
> Report find_report(check_id, report_id)

A single report can be retrieved using this endpoint with the corresponding unique identifier.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
check_id = 'check_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # A single report can be retrieved using this endpoint with the corresponding unique identifier.
    api_response = api_instance.find_report(check_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

[**Report**](Report.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_report_type_group**
> ReportTypeGroup find_report_type_group(report_type_group_id)

Retrieve single report type group object

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
report_type_group_id = 'report_type_group_id_example' # str | 

try:
    # Retrieve single report type group object
    api_response = api_instance.find_report_type_group(report_type_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_report_type_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_type_group_id** | **str**|  | 

### Return type

[**ReportTypeGroup**](ReportTypeGroup.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_webhook**
> Webhook find_webhook(webhook_id)

Retrieve a Webhook

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | 

try:
    # Retrieve a Webhook
    api_response = api_instance.find_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sdk_token**
> SdkTokenResponse generate_sdk_token(sdk_token_request)

Generate a SDK token

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
sdk_token_request = onfido.SdkTokenRequest() # SdkTokenRequest | 

try:
    # Generate a SDK token
    api_response = api_instance.generate_sdk_token(sdk_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_sdk_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_token_request** | [**SdkTokenRequest**](SdkTokenRequest.md)|  | 

### Return type

[**SdkTokenResponse**](SdkTokenResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applicants**
> ApplicantsList list_applicants(page=page, per_page=per_page, include_deleted=include_deleted)

List Applicants

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
page = 1 # int | The page to return. The first page is `page=1` (optional) (default to 1)
per_page = 20 # int | The number of objects per page. (optional) (default to 20)
include_deleted = False # bool | Whether to also include applicants scheduled for deletion. (optional) (default to False)

try:
    # List Applicants
    api_response = api_instance.list_applicants(page=page, per_page=per_page, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_applicants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page to return. The first page is &#x60;page&#x3D;1&#x60; | [optional] [default to 1]
 **per_page** | **int**| The number of objects per page. | [optional] [default to 20]
 **include_deleted** | **bool**| Whether to also include applicants scheduled for deletion. | [optional] [default to False]

### Return type

[**ApplicantsList**](ApplicantsList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_checks**
> ChecksList list_checks(applicant_id, page=page, per_page=per_page)

Retrieve Checks

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
page = 1 # int | The page to return. The first page is `page=1`. (optional) (default to 1)
per_page = 20 # int | The number of objects per page. (optional) (default to 20)

try:
    # Retrieve Checks
    api_response = api_instance.list_checks(applicant_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **page** | **int**| The page to return. The first page is &#x60;page&#x3D;1&#x60;. | [optional] [default to 1]
 **per_page** | **int**| The number of objects per page. | [optional] [default to 20]

### Return type

[**ChecksList**](ChecksList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> DocumentsList list_documents(applicant_id)

List documents

All documents belonging to an applicant can be listed from this endpoint

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 

try:
    # List documents
    api_response = api_instance.list_documents(applicant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

[**DocumentsList**](DocumentsList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_live_photos**
> LivePhotosList list_live_photos(applicant_id)

List live photos

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | The id of the applicant the live photos belong to.

try:
    # List live photos
    api_response = api_instance.list_live_photos(applicant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_live_photos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**| The id of the applicant the live photos belong to. | 

### Return type

[**LivePhotosList**](LivePhotosList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_live_videos**
> LiveVideosList list_live_videos(applicant_id)

List live videos

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | The id of the applicant the live videos belong to.

try:
    # List live videos
    api_response = api_instance.list_live_videos(applicant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_live_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**| The id of the applicant the live videos belong to. | 

### Return type

[**LiveVideosList**](LiveVideosList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_report_type_groups**
> ReportTypeGroupsList list_report_type_groups()

Retrieve all report type groups

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))

try:
    # Retrieve all report type groups
    api_response = api_instance.list_report_type_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_report_type_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportTypeGroupsList**](ReportTypeGroupsList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reports**
> ReportsList list_reports(check_id)

All the reports belonging to a particular check can be listed from this endpoint.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
check_id = 'check_id_example' # str | 

try:
    # All the reports belonging to a particular check can be listed from this endpoint.
    api_response = api_instance.list_reports(check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 

### Return type

[**ReportsList**](ReportsList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhooksList list_webhooks()

List webhooks

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))

try:
    # List webhooks
    api_response = api_instance.list_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhooksList**](WebhooksList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_applicant**
> restore_applicant(applicant_id)

Restore Applicant

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 

try:
    # Restore Applicant
    api_instance.restore_applicant(applicant_id)
except ApiException as e:
    print("Exception when calling DefaultApi->restore_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_check**
> resume_check(check_id)

Resume a Check

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
check_id = 'check_id_example' # str | 

try:
    # Resume a Check
    api_instance.resume_check(check_id)
except ApiException as e:
    print("Exception when calling DefaultApi->resume_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_report**
> resume_report(check_id, report_id)

This endpoint is for resuming individual paused reports.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
check_id = 'check_id_example' # str | 
report_id = 'report_id_example' # str | 

try:
    # This endpoint is for resuming individual paused reports.
    api_instance.resume_report(check_id, report_id)
except ApiException as e:
    print("Exception when calling DefaultApi->resume_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_applicant**
> Applicant update_applicant(applicant_id, applicant)

Update Applicant

Allows updating of an applicant’s information before any checks are created. - Partial updates - Addresses and ID numbers present will replace existing ones - Same applicant validations to create applicant 

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
applicant = onfido.Applicant() # Applicant | 

try:
    # Update Applicant
    api_response = api_instance.update_applicant(applicant_id, applicant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **applicant** | [**Applicant**](Applicant.md)|  | 

### Return type

[**Applicant**](Applicant.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> Document upload_document(applicant_id, type, file, side=side, issuing_country=issuing_country)

Upload a document

Documents are uploaded using this endpoint. Along with the file upload the relevant document type must be specified. Documents must be uploaded as a multipart form. The valid file types are: jpg, png and pdf. The file size must be between 2KB and 3MB. 

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
type = 'type_example' # str | The type of document.
file = '/path/to/file' # file | The file to be uploaded.
side = 'side_example' # str | Either the `front` or `back` of the document. (optional)
issuing_country = 'issuing_country_example' # str | The issuing country of the document, a 3-letter ISO code. (optional)

try:
    # Upload a document
    api_response = api_instance.upload_document(applicant_id, type, file, side=side, issuing_country=issuing_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **type** | **str**| The type of document. | 
 **file** | **file**| The file to be uploaded. | 
 **side** | **str**| Either the &#x60;front&#x60; or &#x60;back&#x60; of the document. | [optional] 
 **issuing_country** | **str**| The issuing country of the document, a 3-letter ISO code. | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_live_photo**
> LivePhoto upload_live_photo(applicant_id, file, advanced_validation=advanced_validation)

Upload live photo

You can upload live photos to this endpoint. Like document upload, files must be uploaded as a multipart form. Valid file types are jpg, png and pdf. The file size must be between 32KB and 10MB. Live photos are validated at the point of upload to check that they contain exactly one face. This validation can be disabled by setting the advanced_validation argument to false. 

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint
configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))
applicant_id = 'applicant_id_example' # str | 
file = '/path/to/file' # file | The file to be uploaded.
advanced_validation = True # bool | Validates that the live photo contains exactly one face. (optional) (default to True)

try:
    # Upload live photo
    api_response = api_instance.upload_live_photo(applicant_id, file, advanced_validation=advanced_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_live_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **file** | **file**| The file to be uploaded. | 
 **advanced_validation** | **bool**| Validates that the live photo contains exactly one face. | [optional] [default to True]

### Return type

[**LivePhoto**](LivePhoto.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

