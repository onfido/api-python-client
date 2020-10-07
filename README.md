# :warning: Please use [onfido-python](https://github.com/onfido/onfido-python) instead :warning:

This library has been superseded by [onfido-python](https://github.com/onfido/onfido-python)

# onfido
The Onfido API is used to submit check requests.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.0
- Package version: 5.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

Install using pip:

```sh
pip install onfido
```

Then import the package:
```python
import onfido
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import sys
import onfido
import datetime
from pprint import pprint
from onfido.rest import ApiException

configuration = onfido.Configuration()
configuration.api_key['Authorization'] = 'token=' + 'YOUR API TOKEN'
configuration.api_key_prefix['Authorization'] = 'Token'

# Limit the at-rest region, if needed (optional, see https://documentation.onfido.com/#regions)
# configuration.host = configuration.get_host_from_settings(1, {'region': 'us'})

api_instance = onfido.DefaultApi(onfido.ApiClient(configuration))

# Setting applicant details

applicant_address = onfido.Address(
    building_number=100,
    street='Main Street',
    town='London',
    postcode='SW4 6EH',
    country='GBR'
)

applicant_details = onfido.Applicant(
    first_name='Jane',
    last_name='Doe',
    address=applicant_address
)

# Setting check details

check_data = onfido.Check()
check_data.report_names = ['identity_standard']

# Create an applicant and then a check with an Identity report

try:
    applicant_data = api_instance.create_applicant(applicant_details)
    applicant_id = applicant_data.id
    pprint('Applicant ID: '+applicant_id)
    check_data.applicant_id = applicant_id
    new_check = api_instance.create_check(check_data)
    pprint(new_check)
except ApiException as e:
    pprint(e.body)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.onfido.com/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**cancel_report**](docs/DefaultApi.md#cancel_report) | **POST** /reports/{report_id}/cancel | This endpoint is for cancelling individual paused reports.
*DefaultApi* | [**create_applicant**](docs/DefaultApi.md#create_applicant) | **POST** /applicants | Create Applicant
*DefaultApi* | [**create_check**](docs/DefaultApi.md#create_check) | **POST** /checks | Create a check
*DefaultApi* | [**create_webhook**](docs/DefaultApi.md#create_webhook) | **POST** /webhooks | Create a webhook
*DefaultApi* | [**delete_webhook**](docs/DefaultApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_id} | Delete a webhook
*DefaultApi* | [**destroy_applicant**](docs/DefaultApi.md#destroy_applicant) | **DELETE** /applicants/{applicant_id} | Delete Applicant
*DefaultApi* | [**download_document**](docs/DefaultApi.md#download_document) | **GET** /documents/{document_id}/download | Download a documents raw data
*DefaultApi* | [**download_live_photo**](docs/DefaultApi.md#download_live_photo) | **GET** /live_photos/{live_photo_id}/download | Download live photo
*DefaultApi* | [**download_live_video**](docs/DefaultApi.md#download_live_video) | **GET** /live_videos/{live_video_id}/download | Download live video
*DefaultApi* | [**edit_webhook**](docs/DefaultApi.md#edit_webhook) | **PUT** /webhooks/{webhook_id} | Edit a webhook
*DefaultApi* | [**find_addresses**](docs/DefaultApi.md#find_addresses) | **GET** /addresses/pick | Search for addresses by postcode
*DefaultApi* | [**find_applicant**](docs/DefaultApi.md#find_applicant) | **GET** /applicants/{applicant_id} | Retrieve Applicant
*DefaultApi* | [**find_check**](docs/DefaultApi.md#find_check) | **GET** /checks/{check_id} | Retrieve a Check
*DefaultApi* | [**find_document**](docs/DefaultApi.md#find_document) | **GET** /documents/{document_id} | A single document can be retrieved by calling this endpoint with the document’s unique identifier.
*DefaultApi* | [**find_live_photo**](docs/DefaultApi.md#find_live_photo) | **GET** /live_photos/{live_photo_id} | Retrieve live photo
*DefaultApi* | [**find_live_video**](docs/DefaultApi.md#find_live_video) | **GET** /live_videos/{live_video_id} | Retrieve live video
*DefaultApi* | [**find_report**](docs/DefaultApi.md#find_report) | **GET** /reports/{report_id} | A single report can be retrieved using this endpoint with the corresponding unique identifier.
*DefaultApi* | [**find_webhook**](docs/DefaultApi.md#find_webhook) | **GET** /webhooks/{webhook_id} | Retrieve a Webhook
*DefaultApi* | [**generate_sdk_token**](docs/DefaultApi.md#generate_sdk_token) | **POST** /sdk_token | Generate a SDK token
*DefaultApi* | [**list_applicants**](docs/DefaultApi.md#list_applicants) | **GET** /applicants | List Applicants
*DefaultApi* | [**list_checks**](docs/DefaultApi.md#list_checks) | **GET** /checks | Retrieve Checks
*DefaultApi* | [**list_documents**](docs/DefaultApi.md#list_documents) | **GET** /documents | List documents
*DefaultApi* | [**list_live_photos**](docs/DefaultApi.md#list_live_photos) | **GET** /live_photos | List live photos
*DefaultApi* | [**list_live_videos**](docs/DefaultApi.md#list_live_videos) | **GET** /live_videos | List live videos
*DefaultApi* | [**list_reports**](docs/DefaultApi.md#list_reports) | **GET** /reports | All the reports belonging to a particular check can be listed from this endpoint.
*DefaultApi* | [**list_webhooks**](docs/DefaultApi.md#list_webhooks) | **GET** /webhooks | List webhooks
*DefaultApi* | [**restore_applicant**](docs/DefaultApi.md#restore_applicant) | **POST** /applicants/{applicant_id}/restore | Restore Applicant
*DefaultApi* | [**resume_check**](docs/DefaultApi.md#resume_check) | **POST** /checks/{check_id}/resume | Resume a Check
*DefaultApi* | [**resume_report**](docs/DefaultApi.md#resume_report) | **POST** /reports/{report_id}/resume | This endpoint is for resuming individual paused reports.
*DefaultApi* | [**update_applicant**](docs/DefaultApi.md#update_applicant) | **PUT** /applicants/{applicant_id} | Update Applicant
*DefaultApi* | [**upload_document**](docs/DefaultApi.md#upload_document) | **POST** /documents | Upload a document
*DefaultApi* | [**upload_live_photo**](docs/DefaultApi.md#upload_live_photo) | **POST** /live_photos | Upload live photo


## Documentation For Models

 - [Address](docs/Address.md)
 - [AddressesList](docs/AddressesList.md)
 - [Applicant](docs/Applicant.md)
 - [ApplicantsList](docs/ApplicantsList.md)
 - [Check](docs/Check.md)
 - [ChecksList](docs/ChecksList.md)
 - [Document](docs/Document.md)
 - [DocumentsList](docs/DocumentsList.md)
 - [Error](docs/Error.md)
 - [ErrorProperties](docs/ErrorProperties.md)
 - [IdNumber](docs/IdNumber.md)
 - [LivePhoto](docs/LivePhoto.md)
 - [LivePhotosList](docs/LivePhotosList.md)
 - [LiveVideo](docs/LiveVideo.md)
 - [LiveVideosList](docs/LiveVideosList.md)
 - [Report](docs/Report.md)
 - [ReportDocument](docs/ReportDocument.md)
 - [ReportsList](docs/ReportsList.md)
 - [SdkToken](docs/SdkToken.md)
 - [Webhook](docs/Webhook.md)
 - [WebhooksList](docs/WebhooksList.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




