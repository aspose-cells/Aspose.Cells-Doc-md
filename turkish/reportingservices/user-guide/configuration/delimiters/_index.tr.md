---
title: Sınırlayıcılar
type: docs
weight: 20
url: /tr/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services, TXT veya CSV biçimini işlerken belirli bir sınırlayıcıyı destekler. Aspose.Cells for Reporting Services'de alan sınırlayıcıyı iki ayar kontrol eder.

1.  Alan sınırlayıcı parametresi**rsreportserver.config** yalnızca belirli bir işleme uzantısını kontrol edebilir.

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




1.  Alan sınırlayıcı parametresi**Aspose.Cells.ReportingServices.xml** tüm TXT tipi oluşturma uzantılarını kontrol edebilir.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 Alan sınırlayıcı parametresi**rsreportserver.config** alan sınırlayıcı parametresine göre önceliklidir**Aspose.Cells.ReportingServices.xml** Alan sınırlayıcı parametresi**rsreportserver.config** boş veya varsayılan değer, alan sınırlayıcı parametresi**Aspose.Cells.ReportingServices.xml** kullanıldı.
