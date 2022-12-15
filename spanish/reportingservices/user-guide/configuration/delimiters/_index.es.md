---
title: delimitadores
type: docs
weight: 20
url: /es/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services admite un delimitador específico al representar el formato TXT o CSV. Dos configuraciones controlan el delimitador de campo en Aspose.Cells for Reporting Services.

1.  El parámetro delimitador de campo en**rsreportserver.config** solo puede controlar una extensión de representación específica.

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




1.  El parámetro delimitador de campo en**Aspose.Cells.ReportingServices.xml** puede controlar todas las extensiones de representación de tipo TXT.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 El parámetro delimitador de campo en**rsreportserver.config** tiene prioridad sobre el parámetro delimitador de campo en**Aspose.Cells.ReportingServices.xml** Cuando el parámetro delimitador de campo en**rsreportserver.config** es nulo o el valor predeterminado, el parámetro delimitador de campo en**Aspose.Cells.ReportingServices.xml** se usa
