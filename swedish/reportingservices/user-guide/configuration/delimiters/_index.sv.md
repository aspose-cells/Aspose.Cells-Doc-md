---
title: Avgränsare
type: docs
weight: 20
url: /sv/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services stöder en specificerad avgränsare vid rendering av TXT- eller CSV-format. Två inställningar styr fältavgränsaren i Aspose.Cells for Reporting Services.

1.  Fältavgränsningsparametern i**rsreportserver.config** kan bara styra en specificerad renderingstillägg.

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




1.  Fältavgränsningsparametern i**Aspose.Cells.ReportingServices.xml** kan styra alla renderingstillägg av TXT-typ.

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

 Fältavgränsningsparametern i**rsreportserver.config** har prioritet över fältavgränsningsparametern i**Aspose.Cells.ReportingServices.xml** När parametern för fältavgränsare in**rsreportserver.config** är null eller standardvärdet, parametern fältavgränsare i**Aspose.Cells.ReportingServices.xml** är använd.
