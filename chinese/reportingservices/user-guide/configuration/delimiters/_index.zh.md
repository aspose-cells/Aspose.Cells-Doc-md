---
title: 分隔符
type: docs
weight: 20
url: /zh/reportingservices/delimiters/
---

当以 TXT 或 CSV 格式呈现时，Aspose.Cells for Reporting Services 支持指定分隔符。两个设置控制 Aspose.Cells for Reporting Services 中的字段分隔符。

1. **rsreportserver.config** 中的字段分隔符参数仅能控制特定呈现扩展。 

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




1. **Aspose.Cells.ReportingServices.xml** 中的字段分隔符参数能控制所有 TXT 类型呈现扩展。 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

**rsreportserver.config** 中的字段分隔符参数优先于 **Aspose.Cells.ReportingServices.xml** 中的字段分隔符参数。当 **rsreportserver.config** 中的字段分隔符参数为 null 或默认值时，将使用 **Aspose.Cells.ReportingServices.xml** 中的字段分隔符参数。
