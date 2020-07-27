+++
title = "Delimiters" 
description = "" 
weight = 12082 
+++

Aspose.Cells for Reporting Services : Delimiters  

# Aspose.Cells for Reporting Services : Delimiters


Aspose.Cells for Reporting Services supports a specified delimiter when rendering TXT or CSV format. Two settings control the field delimiter in Aspose.Cells for Reporting Services.

1.  The field delimiter parameter in **rsreportserver.config** can only control a specified rendering extension.  
      
    
{{< code lang="cs" >}}
<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" >
<Configuration>
<DeviceInfo>
<FieldDelimiter>,</FieldDelimiter>
</DeviceInfo>
</Configuration>
</Extension>
Specified field delimiters configuration reference:
----blank delimiter
<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" >
<Configuration>
<DeviceInfo>
<FieldDelimiter>blank</FieldDelimiter>
</DeviceInfo>
</Configuration>
</Extension>

---- tab delimiter
<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" >
<Configuration>
<DeviceInfo>
<FieldDelimiter>tab</FieldDelimiter>
</DeviceInfo>
</Configuration>
</Extension>

{{< /code >}}
    
      
      
    
2.  The field delimiter parameter in **Aspose.Cells.ReportingServices.xml** can control all TXT type rendering extensions.  
      
    
{{< code lang="cs" >}}

<CSVRender Mode="Default">
    <encode value="Default"/>
    <Delimiters value=","/>
    <RenderTableList value ="False"/>
    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>
    <NoOutPutIsValid ALL="False"/>
  </CSVRender>

{{< /code >}}
    

The field delimiter parameter in **rsreportserver.config** takes priority over the field delimiter parameter in **Aspose.Cells.ReportingServices.xml**. When the field delimiter parameter in **rsreportserver.config** is null or the default value, the field delimiter parameter in **Aspose.Cells.ReportingServices.xml** is used.

