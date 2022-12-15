---
title: Délimiteurs
type: docs
weight: 20
url: /fr/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services prend en charge un délimiteur spécifié lors du rendu au format TXT ou CSV. Deux paramètres contrôlent le délimiteur de champ dans Aspose.Cells for Reporting Services.

1.  Le paramètre de délimiteur de champ dans**rsreportserver.config** ne peut contrôler qu'une extension de rendu spécifiée.

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




1.  Le paramètre de délimiteur de champ dans**Aspose.Cells.ReportingServices.xml** peut contrôler toutes les extensions de rendu de type TXT.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 Le paramètre de délimiteur de champ dans**rsreportserver.config** est prioritaire sur le paramètre de délimiteur de champ dans**Aspose.Cells.ReportingServices.xml** Lorsque le paramètre de délimiteur de champ dans**rsreportserver.config** est nul ou la valeur par défaut, le paramètre de délimiteur de champ dans**Aspose.Cells.ReportingServices.xml** est utilisé.
