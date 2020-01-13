# Applicant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the applicant. Read-only. | [optional] 
**created_at** | **datetime** | The date and time when this applicant was created. Read-only. | [optional] 
**delete_at** | **datetime** | The date and time when this applicant is scheduled to be deleted. Read-only. | [optional] 
**href** | **str** | The uri of this resource. Read-only. | [optional] 
**sandbox** | **bool** | Read-only. | [optional] 
**first_name** | **str** | The applicant’s first name | [optional] 
**last_name** | **str** | The applicant’s surname | [optional] 
**email** | **str** | The applicant’s email address. Required if doing a US check, or a UK check for which &#x60;applicant_provides_data&#x60; is &#x60;true&#x60;. | [optional] 
**dob** | **date** | The applicant’s date of birth | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**id_numbers** | [**list[IdNumber]**](IdNumber.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


