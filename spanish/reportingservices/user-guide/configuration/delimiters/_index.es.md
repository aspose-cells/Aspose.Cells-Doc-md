---
title: Delimitadores
type: docs
weight: 20
url: /es/reportingservices/delimiters/
---

Aspose.Cells for Reporting Services admite un delimitador especificado al renderizar en formato TXT o CSV. Dos configuraciones controlan el delimitador de campo en Aspose.Cells for Reporting Services.

1. El parámetro del delimitador de campo en **rsreportserver.config** solo puede controlar una extensión de renderizado específica. 

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




1. El parámetro del delimitador de campo en **Aspose.Cells.ReportingServices.xml** puede controlar todas las extensiones de renderizado de tipo TXT. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

El parámetro del delimitador de campo en **rsreportserver.config** tiene prioridad sobre el parámetro del delimitador de campo en **Aspose.Cells.ReportingServices.xml**. Cuando el parámetro del delimitador de campo en **rsreportserver.config** es nulo o tiene el valor predeterminado, se utiliza el parámetro del delimitador de campo en **Aspose.Cells.ReportingServices.xml**.
