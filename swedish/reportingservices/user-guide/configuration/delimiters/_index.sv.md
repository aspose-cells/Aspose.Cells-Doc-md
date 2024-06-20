---
title: Avgränsare
type: docs
weight: 20
url: /sv/reportingservices/delimiters/
---

Aspose.Cells for Reporting Services stöder en specificerad avgränsare vid rendering i TXT- eller CSV-format. Två inställningar styr fältavgränsaren i Aspose.Cells for Reporting Services.

1. Fältavgränsarparametern i **rsreportserver.config** kan endast styra en specificerad renderingstillämpning. 

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




1. Fältavgränsarparametern i **Aspose.Cells.ReportingServices.xml** kan styra alla TXT-typens renderingstillämpningar. 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

Fältavgränsarparametern i **rsreportserver.config** har företräde framför fältavgränsarparametern i **Aspose.Cells.ReportingServices.xml**. När fältavgränsarparametern i **rsreportserver.config** är null eller standardvärdet används fältavgränsarparametern i **Aspose.Cells.ReportingServices.xml**.
