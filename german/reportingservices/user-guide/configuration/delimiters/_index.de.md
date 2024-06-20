---
title: Trennzeichen
type: docs
weight: 20
url: /de/reportingservices/delimiters/
---

Aspose.Cells for Reporting Services unterstützt ein festgelegtes Trennzeichen beim Rendern von TXT- oder CSV-Format. Zwei Einstellungen steuern das Feldtrennzeichen in Aspose.Cells for Reporting Services.

1. Der Feldtrennzeichen-Parameter in **rsreportserver.config** kann nur eine bestimmte Rendierungserweiterung steuern. 

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




1. Der Feldtrennzeichen-Parameter in **Aspose.Cells.ReportingServices.xml** kann alle TXT-Typ-Rendierungserweiterungen steuern. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

Der Feldtrennzeichen-Parameter in **rsreportserver.config** hat Vorrang vor dem Feldtrennzeichen-Parameter in **Aspose.Cells.ReportingServices.xml**. Wenn der Feldtrennzeichen-Parameter in **rsreportserver.config** null oder der Standardwert ist, wird der Feldtrennzeichen-Parameter in **Aspose.Cells.ReportingServices.xml** verwendet.
