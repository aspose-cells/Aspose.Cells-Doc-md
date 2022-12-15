---
title: المحددات
type: docs
weight: 20
url: /ar/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services يدعم المحدد المحدد عند تحويل نسق TXT أو CSV. يتحكم إعدادان في محدد المجال في Aspose.Cells for Reporting Services.

1.  معلمة محدد الحقل في**rsreportserver.config** يمكن فقط التحكم في امتداد العرض المحدد.

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




1.  معلمة محدد الحقل في**Aspose.Cells.ReportingServices.xml** يمكنه التحكم في جميع امتدادات عرض نوع TXT.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 معلمة محدد الحقل في**rsreportserver.config** له الأولوية على معلمة محدد الحقل في**Aspose.Cells.ReportingServices.xml** عندما تكون معلمة محدد الحقل في**rsreportserver.config** هي القيمة الخالية أو القيمة الافتراضية ، فإن معلمة محدد الحقل في**Aspose.Cells.ReportingServices.xml** يستخدم.
