---
title: 分隔符
type: docs
weight: 20
url: /zh/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services 渲染TXT或CSV格式时支持指定分隔符。两个设置控制 Aspose.Cells for Reporting Services 中的字段分隔符。

1. 中的字段分隔符参数**rsreportserver.config**只能控制指定的渲染扩展。

{{< highlight "java" >}}

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




1. 中的字段分隔符参数**Aspose.Cells.ReportingServices.xml**可以控制所有TXT类型的渲染扩展。

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

中的字段分隔符参数**rsreportserver.config**优先于字段分隔符参数**Aspose.Cells.ReportingServices.xml**.当字段分隔符参数在**rsreportserver.config**为空或默认值，字段分隔符参数**Aspose.Cells.ReportingServices.xml**用来。
