---
title: Trennzeichen
type: docs
weight: 20
url: /de/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services unterstützt ein bestimmtes Trennzeichen beim Rendern des Formats TXT oder CSV. Zwei Einstellungen steuern den Feldbegrenzer in Aspose.Cells for Reporting Services.

1.  Der Feldbegrenzerparameter in**rsreportserver.config** kann nur eine bestimmte Rendering-Erweiterung steuern.

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




1.  Der Feldbegrenzerparameter in**Aspose.Cells.ReportingServices.xml** kann alle Rendering-Erweiterungen vom Typ TXT steuern.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 Der Feldbegrenzerparameter in**rsreportserver.config** hat Vorrang vor dem Feldbegrenzerparameter in**Aspose.Cells.ReportingServices.xml** . Wenn der Feldbegrenzerparameter in**rsreportserver.config** null oder der Standardwert ist, der Feldbegrenzerparameter in**Aspose.Cells.ReportingServices.xml** wird genutzt.
