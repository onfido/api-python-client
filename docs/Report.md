# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the report. Read-only. | [optional] 
**created_at** | **datetime** | The date and time at which the report was first initiated. Read-only. | [optional] 
**href** | **str** | The API endpoint to retrieve the report. Read-only. | [optional] 
**status** | **str** | The current state of the report in the checking process. Read-only. | [optional] 
**result** | **str** | The result of the report. Read-only. | [optional] 
**sub_result** | **str** | The sub_result of the report. It gives a more detailed result for document reports only, and will be null otherwise. Read-only. | [optional] 
**breakdown** | **dict(str, object)** | The details of the report. This is specific to each type of report. Read-only. | [optional] 
**properties** | **dict(str, object)** | The properties associated with the report, if any. Read-only. | [optional] 
**name** | **str** | The name of the report type. | 
**variant** | **str** | The name of the report type variant, if required. | [optional] 
**options** | [**list[ReportOption]**](ReportOption.md) | List of Report Option objects. | [optional] 
**documents** | [**list[ReportDocument]**](ReportDocument.md) | Array of objects with document ids that were used in the Onfido engine. [ONLY USED IN A DOCUMENT CHECK] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


