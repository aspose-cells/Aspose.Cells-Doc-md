---
title: Rendera utvalda diagramobjekt till Excel diagram
type: docs
weight: 30
url: /sv/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

För att rendera endast vissa diagram i en rapport till Excel-diagram:

1. Öppna filen **Aspose.Cells.ReportingServices.xml**.
1. Ändra konfigurationsparametrarna i filen **Aspose.Cells.ReportingServices.xml**.
1. Lägg till önskad rapportkonfigurationsinformation.
1. Lägg till information för diagramobjekten du inte vill exportera som redigerbara diagram. Dessa objekt exporteras som statiska bilder.

Exempelvis:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Ett diagram exporterat som en bild** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**En diagram som exporteras som en redigerbar Excel-diagram** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
