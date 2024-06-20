---
title: Sınır İşaretleyicileri
type: docs
weight: 20
url: /tr/reportingservices/delimiters/
---

Aspose.Cells for Reporting Services, TXT veya CSV biçiminde render edilirken belirli bir sınırlayıcıyı destekler. Aspose.Cells for Reporting Services'te iki ayar Aspose.Cells for Reporting Services alanında sınırlayıcıyı denetler.

1. **rsreportserver.config**'deki alan sınırlayıcı parametresi yalnızca belirli bir render uzantısını denetleyebilir. 

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




1. **Aspose.Cells.ReportingServices.xml** içindeki alan sınırlayıcı parametresi tüm TXT tipi render uzantılarını denetleyebilir. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

**rsreportserver.config** içindeki alan sınırlayıcı parametresi, **Aspose.Cells.ReportingServices.xml** içindeki alan sınırlayıcı parametresinden önceliklidir. **rsreportserver.config** içindeki alan sınırlayıcı parametresi null veya varsayılan değerse, **Aspose.Cells.ReportingServices.xml** içindeki alan sınırlayıcı parametresi kullanılır.
