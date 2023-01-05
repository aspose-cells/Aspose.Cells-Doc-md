---
title: Delimitatori
type: docs
weight: 20
url: /it/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services supporta un delimitatore specificato durante il rendering del formato TXT o CSV. Due impostazioni controllano il delimitatore di campo in Aspose.Cells for Reporting Services.

1.  Il parametro del delimitatore di campo in**rsreportserver.config** può controllare solo un'estensione per il rendering specificata.

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




1.  Il parametro del delimitatore di campo in**Aspose.Cells.ReportingServices.xml** può controllare tutte le estensioni per il rendering del tipo TXT.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 Il parametro del delimitatore di campo in**rsreportserver.config** ha la priorità sul parametro delimitatore di campo in**Aspose.Cells.ReportingServices.xml** . Quando il parametro delimitatore di campo in**rsreportserver.config** è nullo o il valore predefinito, il parametro del delimitatore di campo in**Aspose.Cells.ReportingServices.xml** viene usato.
