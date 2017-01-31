# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the report. | [optional] 
**created_at** | **datetime** | The date and time at which the report was first initiated. | [optional] 
**href** | **str** | The API endpoint to retrieve the report. | [optional] 
**name** | **str** | Report type string identifier. | [optional] 
**status** | **str** | The current state of the report in the checking process. | [optional] 
**result** | **str** | The result of the report. | [optional] 
**variant** | **str** | Report variant string identifier. Some reports e.g. criminal_history have sub-types, which are identified by this field. | [optional] 
**options** | **dict(str, str)** | Report options. Some reports e.g. criminal_history expose additional options. | [optional] 
**breakdowns** | **dict(str, str)** | The details of the report. This is specific to each type of report. | [optional] 
**properties** | **dict(str, str)** | The properties associated with the report, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


