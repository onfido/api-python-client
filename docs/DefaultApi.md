# onfido.DefaultApi

All URIs are relative to *https://api.onfido.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_report**](DefaultApi.md#cancel_report) | **POST** /checks/{check_id}/reports/{report_id}/cancel | This endpoint is for cancelling individual paused reports.
[**create_applicant**](DefaultApi.md#create_applicant) | **POST** /applicants | Create Applicant
[**create_check**](DefaultApi.md#create_check) | **POST** /applicants/{applicant_id}/checks | Create a check
[**destroy_applicant**](DefaultApi.md#destroy_applicant) | **DELETE** /applicants/{applicant_id} | Delete Applicant
[**download_document**](DefaultApi.md#download_document) | **GET** /applicants/{applicant_id}/documents/{document_id}/download | Download a documents raw data
[**find_applicant**](DefaultApi.md#find_applicant) | **GET** /applicants/{applicant_id} | Retrieve Applicant
[**find_check**](DefaultApi.md#find_check) | **GET** /applicants/{applicant_id}/checks/{check_id} | Retrieve a Check
[**find_document**](DefaultApi.md#find_document) | **GET** /applicants/{applicant_id}/documents/{document_id} | A single document can be retrieved by calling this endpoint with the document’s unique identifier.
[**find_report**](DefaultApi.md#find_report) | **GET** /checks/{check_id}/reports/{report_id} | A single report can be retrieved using this endpoint with the corresponding unique identifier.
[**find_report_type_group**](DefaultApi.md#find_report_type_group) | **GET** /report_type_groups/{report_type_group_id} | Retrieve single report type group object
[**list_applicants**](DefaultApi.md#list_applicants) | **GET** /applicants | List Applicants
[**list_checks**](DefaultApi.md#list_checks) | **GET** /applicants/{applicant_id}/checks | Retrieve Checks
[**list_documents**](DefaultApi.md#list_documents) | **GET** /applicants/{applicant_id}/documents | List documents
[**list_report_type_groups**](DefaultApi.md#list_report_type_groups) | **GET** /report_type_groups | Retrieve all report type groups
[**list_reports**](DefaultApi.md#list_reports) | **GET** /checks/{check_id}/reports | All the reports belonging to a particular check can be listed from this endpoint.
[**resume_check**](DefaultApi.md#resume_check) | **POST** /checks/{check_id}/resume | Resume a Check
[**resume_report**](DefaultApi.md#resume_report) | **POST** /checks/{check_id}/reports/{report_id}/resume | This endpoint is for resuming individual paused reports.
[**update_applicant**](DefaultApi.md#update_applicant) | **PUT** /applicants/{applicant_id} | Update Applicant
[**upload_document**](DefaultApi.md#upload_document) | **POST** /applicants/{applicant_id}/documents | Upload a document


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

