# Webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the webhook. Read-only. | [optional] 
**token** | **str** | Webhook secret token used to sign the webhook&#39;s payload. Read-only. | [optional] 
**href** | **str** | The API endpoint to retrieve the webhook. Read-only. | [optional] 
**url** | **str** | The url that will listen to notifications (must be https). | 
**enabled** | **bool** | Determine if the webhook is active. | [optional] 
**environments** | **list[str]** | The environments from which the webhook will receive events. Allowed values are “sandbox” and “live”. If the environments parameter is omitted the webhook will receive events from both environments.  | [optional] 
**events** | **list[str]** | The events that will be published to the webhook. The supported events are: &#x60;report.completed&#x60;, &#x60;report.withdrawn&#x60;, &#x60;check.completed&#x60;, &#x60;check.started&#x60;, &#x60;check.form_opened&#x60;, &#x60;check.form_completed&#x60;. If the events parameter is omitted all the events will be subscribed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


