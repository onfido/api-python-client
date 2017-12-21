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
[**find_addresses**](DefaultApi.md#find_addresses) | **GET** /addresses/pick | Search for addresses by postcode
[**find_applicant**](DefaultApi.md#find_applicant) | **GET** /applicants/{applicant_id} | Retrieve Applicant
[**find_check**](DefaultApi.md#find_check) | **GET** /applicants/{applicant_id}/checks/{check_id} | Retrieve a Check
[**find_document**](DefaultApi.md#find_document) | **GET** /applicants/{applicant_id}/documents/{document_id} | A single document can be retrieved by calling this endpoint with the document’s unique identifier.
[**find_live_photo**](DefaultApi.md#find_live_photo) | **GET** /live_photos/{live_photo_id} | Retrieve live photo
[**find_report**](DefaultApi.md#find_report) | **GET** /checks/{check_id}/reports/{report_id} | A single report can be retrieved using this endpoint with the corresponding unique identifier.
[**find_report_type_group**](DefaultApi.md#find_report_type_group) | **GET** /report_type_groups/{report_type_group_id} | Retrieve single report type group object
[**find_webhook**](DefaultApi.md#find_webhook) | **GET** /webhooks/{webhook_id} | Retrieve a Webhook
[**list_applicants**](DefaultApi.md#list_applicants) | **GET** /applicants | List Applicants
[**list_checks**](DefaultApi.md#list_checks) | **GET** /applicants/{applicant_id}/checks | Retrieve Checks
[**list_documents**](DefaultApi.md#list_documents) | **GET** /applicants/{applicant_id}/documents | List documents
[**list_live_photos**](DefaultApi.md#list_live_photos) | **GET** /live_photos | List live photos
[**list_report_type_groups**](DefaultApi.md#list_report_type_groups) | **GET** /report_type_groups | Retrieve all report type groups
[**list_reports**](DefaultApi.md#list_reports) | **GET** /checks/{check_id}/reports | All the reports belonging to a particular check can be listed from this endpoint.
[**list_webhooks**](DefaultApi.md#list_webhooks) | **GET** /webhooks | List webhooks
[**resume_check**](DefaultApi.md#resume_check) | **POST** /checks/{check_id}/resume | Resume a Check
[**resume_report**](DefaultApi.md#resume_report) | **POST** /checks/{check_id}/reports/{report_id}/resume | This endpoint is for resuming individual paused reports.
[**update_applicant**](DefaultApi.md#update_applicant) | **PUT** /applicants/{applicant_id} | Update Applicant
[**upload_document**](DefaultApi.md#upload_document) | **POST** /applicants/{applicant_id}/documents | Upload a document
[**upload_live_photo**](DefaultApi.md#upload_live_photo) | **POST** /live_photos | Upload live photo


# **cancel_report**
> cancel_report(check_id, report_id)

This endpoint is for cancelling individual paused reports.

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
check_id = 'check_id_example' # str | 
report_id = 'report_id_example' # str | 

try: 
    # This endpoint is for cancelling individual paused reports.
    api_instance.cancel_report(check_id, report_id)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

void (empty response body)

# **create_applicant**
> Applicant create_applicant(data=data)

Create Applicant

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
data = onfido.Applicant() # Applicant |  (optional)

try: 
    # Create Applicant
    api_response = api_instance.create_applicant(data=data)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Applicant**](Applicant.md)|  | [optional] 

### Return type

[**Applicant**](Applicant.md)

# **create_check**
> Check create_check(applicant_id, data=data)

Create a check

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 
data = onfido.CheckCreationRequest() # CheckCreationRequest |  (optional)

try: 
    # Create a check
    api_response = api_instance.create_check(applicant_id, data=data)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **data** | [**CheckCreationRequest**](CheckCreationRequest.md)|  | [optional] 

### Return type

[**Check**](Check.md)

# **create_webhook**
> Webhook create_webhook(data=data)

Create a webhook

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
data = onfido.Webhook() # Webhook |  (optional)

try: 
    # Create a webhook
    api_response = api_instance.create_webhook(data=data)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Webhook**](Webhook.md)|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

# **destroy_applicant**
> destroy_applicant(applicant_id)

Delete Applicant

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 

try: 
    # Delete Applicant
    api_instance.destroy_applicant(applicant_id)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

void (empty response body)

# **download_document**
> file download_document(applicant_id, document_id)

Download a documents raw data

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 
document_id = 'document_id_example' # str | 

try: 
    # Download a documents raw data
    api_response = api_instance.download_document(applicant_id, document_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

[**file**](file.md)

# **download_live_photo**
> file download_live_photo(live_photo_id)

Download live photo

Live photos are downloaded using this endpoint.

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
live_photo_id = 'live_photo_id_example' # str | The live photo’s unique identifier.

try: 
    # Download live photo
    api_response = api_instance.download_live_photo(live_photo_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_photo_id** | **str**| The live photo’s unique identifier. | 

### Return type

[**file**](file.md)

# **find_addresses**
> GenericAddressesList find_addresses(postcode)

Search for addresses by postcode

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
postcode = 'postcode_example' # str | 

try: 
    # Search for addresses by postcode
    api_response = api_instance.find_addresses(postcode)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postcode** | **str**|  | 

### Return type

[**GenericAddressesList**](GenericAddressesList.md)

# **find_applicant**
> Applicant find_applicant(applicant_id)

Retrieve Applicant

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 

try: 
    # Retrieve Applicant
    api_response = api_instance.find_applicant(applicant_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

[**Applicant**](Applicant.md)

# **find_check**
> Check find_check(applicant_id, check_id)

Retrieve a Check

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 
check_id = 'check_id_example' # str | 

try: 
    # Retrieve a Check
    api_response = api_instance.find_check(applicant_id, check_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **check_id** | **str**|  | 

### Return type

[**Check**](Check.md)

# **find_document**
> Document find_document(applicant_id, document_id)

A single document can be retrieved by calling this endpoint with the document’s unique identifier.

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 
document_id = 'document_id_example' # str | 

try: 
    # A single document can be retrieved by calling this endpoint with the document’s unique identifier.
    api_response = api_instance.find_document(applicant_id, document_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

[**Document**](Document.md)

# **find_live_photo**
> LivePhoto find_live_photo(live_photo_id)

Retrieve live photo

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
live_photo_id = 'live_photo_id_example' # str | The live photo’s unique identifier.

try: 
    # Retrieve live photo
    api_response = api_instance.find_live_photo(live_photo_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_photo_id** | **str**| The live photo’s unique identifier. | 

### Return type

[**LivePhoto**](LivePhoto.md)

# **find_report**
> Report find_report(check_id, report_id)

A single report can be retrieved using this endpoint with the corresponding unique identifier.

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
check_id = 'check_id_example' # str | 
report_id = 'report_id_example' # str | 

try: 
    # A single report can be retrieved using this endpoint with the corresponding unique identifier.
    api_response = api_instance.find_report(check_id, report_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

[**Report**](Report.md)

# **find_report_type_group**
> ReportTypeGroup find_report_type_group(report_type_group_id)

Retrieve single report type group object

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
report_type_group_id = 'report_type_group_id_example' # str | 

try: 
    # Retrieve single report type group object
    api_response = api_instance.find_report_type_group(report_type_group_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_type_group_id** | **str**|  | 

### Return type

[**ReportTypeGroup**](ReportTypeGroup.md)

# **find_webhook**
> Webhook find_webhook(webhook_id)

Retrieve a Webhook

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
webhook_id = 'webhook_id_example' # str | 

try: 
    # Retrieve a Webhook
    api_response = api_instance.find_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**Webhook**](Webhook.md)

# **list_applicants**
> ApplicantsList list_applicants()

List Applicants

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()

try: 
    # List Applicants
    api_response = api_instance.list_applicants()
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicantsList**](ApplicantsList.md)

# **list_checks**
> ChecksList list_checks(applicant_id)

Retrieve Checks

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 

try: 
    # Retrieve Checks
    api_response = api_instance.list_checks(applicant_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

[**ChecksList**](ChecksList.md)

# **list_documents**
> DocumentsList list_documents(applicant_id)

List documents

All documents belonging to an applicant can be listed from this endpoint

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 

try: 
    # List documents
    api_response = api_instance.list_documents(applicant_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 

### Return type

[**DocumentsList**](DocumentsList.md)

# **list_live_photos**
> LivePhotosList list_live_photos(applicant_id)

List live photos

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | The id of the applicant the live photos belongs to.

try: 
    # List live photos
    api_response = api_instance.list_live_photos(applicant_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**| The id of the applicant the live photos belongs to. | 

### Return type

[**LivePhotosList**](LivePhotosList.md)

# **list_report_type_groups**
> ReportTypeGroupsList list_report_type_groups()

Retrieve all report type groups

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()

try: 
    # Retrieve all report type groups
    api_response = api_instance.list_report_type_groups()
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportTypeGroupsList**](ReportTypeGroupsList.md)

# **list_reports**
> ReportsList list_reports(check_id)

All the reports belonging to a particular check can be listed from this endpoint.

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
check_id = 'check_id_example' # str | 

try: 
    # All the reports belonging to a particular check can be listed from this endpoint.
    api_response = api_instance.list_reports(check_id)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 

### Return type

[**ReportsList**](ReportsList.md)

# **list_webhooks**
> WebhooksList list_webhooks()

List webhooks

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()

try: 
    # List webhooks
    api_response = api_instance.list_webhooks()
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WebhooksList**](WebhooksList.md)

# **resume_check**
> resume_check(check_id)

Resume a Check

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
check_id = 'check_id_example' # str | 

try: 
    # Resume a Check
    api_instance.resume_check(check_id)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 

### Return type

void (empty response body)

# **resume_report**
> resume_report(check_id, report_id)

This endpoint is for resuming individual paused reports.

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
check_id = 'check_id_example' # str | 
report_id = 'report_id_example' # str | 

try: 
    # This endpoint is for resuming individual paused reports.
    api_instance.resume_report(check_id, report_id)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | **str**|  | 
 **report_id** | **str**|  | 

### Return type

void (empty response body)

# **update_applicant**
> Applicant update_applicant(applicant_id, data=data)

Update Applicant

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 
data = onfido.Applicant() # Applicant |  (optional)

try: 
    # Update Applicant
    api_response = api_instance.update_applicant(applicant_id, data=data)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **data** | [**Applicant**](Applicant.md)|  | [optional] 

### Return type

[**Applicant**](Applicant.md)

# **upload_document**
> Document upload_document(applicant_id, type, side=side, file=file)

Upload a document

Documents are uploaded using this endpoint. Along with the file upload the relevant document type must be specified. Documents must be uploaded as a multipart form. The valid file types are: jpg, png and pdf. The file size must be between 2KB and 3MB. 

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | 
type = 'type_example' # str | 
side = 'side_example' # str |  (optional)
file = '/path/to/file.txt' # file |  (optional)

try: 
    # Upload a document
    api_response = api_instance.upload_document(applicant_id, type, side=side, file=file)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**|  | 
 **type** | **str**|  | 
 **side** | **str**|  | [optional] 
 **file** | **file**|  | [optional] 

### Return type

[**Document**](Document.md)

# **upload_live_photo**
> LivePhoto upload_live_photo(applicant_id, file, advanced_validation=advanced_validation)

Upload live photo

You can upload live photos to this endpoint. Like document upload, files must be uploaded as a multipart form. Valid file types are jpg, png and pdf. The file size must be between 32KB and 10MB. Live photos are validated at the point of upload to check that they contain exactly one face. This validation can be disabled by setting the advanced_validation argument to false. 

### Example 
```python
from __future__ import print_statement
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = onfido.DefaultApi()
applicant_id = 'applicant_id_example' # str | The applicant_id to associate the live photo to.
file = '/path/to/file.txt' # file | The file to be uploaded.
advanced_validation = true # bool | Validates that the live photo contains exactly one face. (optional)

try: 
    # Upload live photo
    api_response = api_instance.upload_live_photo(applicant_id, file, advanced_validation=advanced_validation)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicant_id** | **str**| The applicant_id to associate the live photo to. | 
 **file** | **file**| The file to be uploaded. | 
 **advanced_validation** | **bool**| Validates that the live photo contains exactly one face. | [optional] 

### Return type

[**LivePhoto**](LivePhoto.md)

