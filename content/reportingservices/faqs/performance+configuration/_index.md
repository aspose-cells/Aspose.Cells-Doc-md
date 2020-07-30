---
title : "Performance Configuration" 
description : "" 
weight : 8106 
toc : false
type: docs
url: /reportingservices/faqs/performance+configuration/
---

# Aspose.Cells for Reporting Services : Performance Configuration


Users can optimize performance to a certain extent. You can configure some attributes and parameters in the **Aspose.Cells.ReportingServices.xml** file as described below.

### Performance Section

This shows the Performance section as it is by default.

**XML**

{{< code lang="xml" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="True"/>
      <Merged value="True"/>
      <ConditionalFormatting value="True"/>
      </Report>
</Performance>
 
{{< /code >}}

### Performance Parameters

*   `LimitCellsNumberForMerged` – The default value of the parameter is 1000000. The parameter value is set by the client and is not effected by the performance parameter's switch. Please refer to the following configuration.
    
    **XML**
    
{{< code lang="xml" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">
 
{{< /code >}}
    
*   `IsAutoRowFit` – Can be either true or false:
    *   When the `Performance` parameter is set to ‘off’, the default value is false.
    *   When the `Performance` parameter is set to ‘on’, the default value is true.
    *   When the `Performance` parameter is set to ‘on’, a sub-element report can re-set the report’s `AutoRowFile` paramter.  
        Please refer to the following configuration.
        
        **XML**
        
{{< code lang="xml" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    	<Report name="Test">
      	<AutoRowFit value="False"/>
      	<SetStyle value="True"/>
      	<Merged value="True"/>
      	<ConditionalFormatting value="True"/>
      	</Report>
</Performance>
 
{{< /code >}}
        
*   `IsMerged` – Can be either true or false:
    *   When the `Performance` parameter is set to ‘off’, the default value is false.
    *   When the `Performance` parameter is set to ‘on’, the default value is true.
    *   When the `Performance` parameter is set to ‘on’, a sub-element report can re-set the report’s `AutoRowFile` paramter.  
        Please refer to the following configuration.
        
        **XML**
        
{{< code lang="xml" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="True"/>
      <Merged value="False"/>
      <ConditionalFormatting value="True"/>
      </Report>
</Performance>
 
{{< /code >}}
        
*   `IsSetStyle` – Can be either true or false:
    *   When the `Performance` parameter is set to ‘off’, the default value is false.
    *   When the `Performance` parameter is set to ‘on’, the default value is true.
    *   When the `Performance` parameter is set to ‘on’, a sub-element report can re-set the report’s `AutoRowFile` paramter.  
        Please refer to the following configuration.
        
        **XML**
        
{{< code lang="xml" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="False"/>
      <Merged value="True"/>
      <ConditionalFormatting value="True"/>
      </Report>
</Performance>
 
{{< /code >}}
        
*   IsConditionalFormatting – Can be either true or false:
    *   When the `Performance` parameter is set to ‘off’, the default value is false.
    *   When the `Performance` parameter is set to ‘on’, the default value is true.
    *   When the `Performance` parameter is set to ‘on’, sub-element report can re-set point report’s `AutoRowFile` paramter.
    *   When the `IsSetStyle` parameter is set to false, the value of the `Performance` parameter is invalid.  
        Please refer to the following configuration.
        
        **XML**
        
{{< code lang="xml" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="True"/>
      <Merged value="True"/>
      <ConditionalFormatting value="False"/>
      </Report>
</Performance>
 
{{< /code >}}
        

