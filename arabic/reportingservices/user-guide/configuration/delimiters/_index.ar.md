---
title: فواصل
type: docs
weight: 20
url: /ar/reportingservices/delimiters/
---

يدعم Aspose.Cells for Reporting Services فاصلاً محددًا عند تقديم شكل TXT أو CSV. تتحكم إعداداتان في فاصل الحقل في Aspose.Cells for Reporting Services.

1. لا يمكن لمعلمة فاصل الحقل في **rsreportserver.config** التحكم في توسيع التقرير المحدد فقط. 

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




1. يمكن لمعلمة فاصل الحقل في **Aspose.Cells.ReportingServices.xml** التحكم في جميع توسيعات تقرير نوع TXT. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

تأخذ معلمة فاصل الحقل في **rsreportserver.config** الأولوية على معلمة فاصل الحقل في **Aspose.Cells.ReportingServices.xml**. عندما تكون معلمة فاصل الحقل في **rsreportserver.config** فارغة أو تحتوي على القيمة الافتراضية، يتم استخدام معلمة فاصل الحقل في **Aspose.Cells.ReportingServices.xml**.
