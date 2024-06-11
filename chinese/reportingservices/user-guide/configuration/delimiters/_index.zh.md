---
title: 分隔符
type: docs
weight: 20
url: /zh/reportingservices/delimiters/
---

在生成 TXT 或 CSV 格式时，Aspose.Cells for Reporting Services 支持指定的分隔符。两个设置控制 Aspose.Cells for Reporting Services 中的字段分隔符。

1. **rsreportserver.config** 中的字段分隔符参数只能控制指定的渲染扩展。 

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




1. **Aspose.Cells.ReportingServices.xml** 中的字段分隔符参数可以控制所有 TXT 类型的渲染扩展。 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

**rsreportserver.config** 中的字段分隔符参数优先于 **Aspose.Cells.ReportingServices.xml** 中的字段分隔符参数。当 **rsreportserver.config** 中的字段分隔符参数为空或默认值时，将使用 **Aspose.Cells.ReportingServices.xml** 中的字段分隔符参数。
