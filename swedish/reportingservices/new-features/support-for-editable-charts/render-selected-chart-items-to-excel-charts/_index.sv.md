---
title: Gör valda diagramobjekt till Excel-diagram
type: docs
weight: 30
url: /sv/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

Så här återger du endast vissa diagram i en rapport till Excel-diagram:

1.  Öppna**Aspose.Cells.ReportingServices.xml** fil.
1.  Ändra konfigurationsparametrarna för**Aspose.Cells.ReportingServices.xml** fil.
1. Lägg till önskad rapportkonfigurationsinformation.
1. Lägg till informationen för de diagramobjekt du inte vill exportera som redigerbara diagram. Dessa objekt exporteras som statiska bilder.

Till exempel:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Ett diagram exporterat som en bild** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Ett diagram exporterat som ett redigerbart Excel-diagram** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
