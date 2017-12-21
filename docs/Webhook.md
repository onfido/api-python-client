# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the webhook. | [optional] 
**url** | **str** | The url of the webhook | [optional] 
**token** | **str** | Webhook secret token used to sign the webhook&#39;s payload | [optional] 
**enabled** | **bool** | Determine if the webhook is active. | [optional] 
**href** | **str** | The API endpoint to retrieve the webhook. | [optional] 
**environments** | **list[str]** | The environments from which the webhook will receive events. | [optional] 
**events** | **list[str]** | The events that will be published to the webhook. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


