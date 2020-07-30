---
title : "Performance" 
description : "" 
weight : 12083 
toc : false
type: docs
url: /reportingservices/userguide/configuration/performance/
---

# Aspose.Cells for Reporting Services : Performance


To improve performance, set the `Performance` parameter to **ON**.

{{< code lang="cs" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">
    <Report name="">
    <AutoRowFit value="True"/>
    <SetStyle value="True"/>
    <Merged value="True"/>
      <ConditionalFormatting value="True"/>
      </Report>
   </Performance>
{{< /code >}}

The various performance parameters are as follows:

*   **`LimitCellsNumberForMerged`**: the maximum number of cells that can be merged. The default value 1,000,000. The parameter value is set by the user and is not affected by the performance parameter switch.  
      
    
{{< code lang="cs" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">
{{< /code >}}
    
      
      
    
*   **`IsAutoRowFit`**: When the value of `Performance` is **off**, the value of `IsAutoRowFit` is **false** by default. When the value of performance parameter is **on**, the value is **true** by default. When the value of `Performance` is **on**, a sub-element report can reset point report to the `AutoRowFit` value.  
      
    
{{< code lang="cs" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="Test">
      <AutoRowFit value="False"/>
      <SetStyle value="True"/>
      <Merged value="True"/>
      <ConditionalFormatting value="True"/>
      </Report>
   </Performance>
{{< /code >}}
    
      
      
    
*   **`IsMerged`**: When the value of `Performance` is **off**, `IsMerged` default value is **false**. When the value of `Performance` is **on**, the default value is **true**. When the value `Performance` parameter is **on**, a sub-element report can reset the point report to the `AutoRowFit` value.  
      
    
{{< code lang="cs" >}}
<Performance value="ON" IsAutoRowFit ="True" IsMerged="True" IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="True"/>
      <Merged value="False"/>
      <ConditionalFormatting value="True"/>
      </Report>
   </Performance>
{{< /code >}}
    
      
      
    
*   **`IsSetStyle`**: When the value of `Performance` is **off**, the default value is **false**. When `Performance` is **on**, the default value is **true**. Also, when `Performance` is **on**, a sub-element report can reset the point report to the `AutoRowFit` value.  
      
    
{{< code lang="cs" >}}
  <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="False"/>
      <Merged value="True"/>
      <ConditionalFormatting value="True"/>
      </Report>
   </Performance>
{{< /code >}}
    
      
      
    
*   **`IsConditionalFormatting`**: When `Performance` is **off**, the default value is **false**. When `Performance` is **on**, the default value is **true**. Also, when `Performance` is **on**, a sub-element report can reset the point report to the `AutoRowFit` value. When the `IsSetStyle` parameter value is set to **false**, the value of `Performance` is invalid.  
      
    
{{< code lang="cs" >}}
  <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">
    <Report name="">
      <AutoRowFit value="True"/>
      <SetStyle value="True"/>
      <Merged value="True"/>
      <ConditionalFormatting value="False"/>
      </Report>
   </Performance>
{{< /code >}}
    

