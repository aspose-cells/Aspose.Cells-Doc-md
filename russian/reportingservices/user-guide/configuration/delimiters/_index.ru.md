---
title: Разделители
type: docs
weight: 20
url: /ru/reportingservices/delimiters/
---

Aspose.Cells for Reporting Services поддерживает указанный разделитель при отображении формата TXT или CSV. Два параметра управляют разделителем полей в Aspose.Cells for Reporting Services.

1. Параметр разделителя полей в **rsreportserver.config** может управлять только определенным расширением отображения. 

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




1. Параметр разделителя полей в **Aspose.Cells.ReportingServices.xml** может управлять всеми расширениями отображения типа TXT. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

Параметр разделителя полей в **rsreportserver.config** имеет приоритет над параметром разделителя полей в **Aspose.Cells.ReportingServices.xml**. Когда параметр разделителя полей в **rsreportserver.config** равен null или значению по умолчанию, используется параметр разделителя полей в **Aspose.Cells.ReportingServices.xml**.
