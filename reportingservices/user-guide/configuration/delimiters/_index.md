---
title: Delimiters
type: docs
weight: 20
url: /reportingservices/delimiters/
---

Aspose.Cells for Reporting Services supports a specified delimiter when rendering TXT or CSV format. Two settings control the field delimiter in Aspose.Cells for Reporting Services.

1. The field delimiter parameter in **rsreportserver.config** can only control a specified rendering extension. 

{{< highlight java >}}

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


{{< /highlight >}}




1. The field delimiter parameter in **Aspose.Cells.ReportingServices.xml** can control all TXT type rendering extensions. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

The field delimiter parameter in **rsreportserver.config** takes priority over the field delimiter parameter in **Aspose.Cells.ReportingServices.xml**. When the field delimiter parameter in **rsreportserver.config** is null or the default value, the field delimiter parameter in **Aspose.Cells.ReportingServices.xml** is used.
