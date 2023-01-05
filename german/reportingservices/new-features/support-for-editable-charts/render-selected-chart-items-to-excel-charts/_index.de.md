---
title: Ausgewählte Diagrammelemente in Excel-Diagramme rendern
type: docs
weight: 30
url: /de/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

So rendern Sie nur einige Diagramme in einem Bericht in Excel-Diagramme:

1. Öffne das**Aspose.Cells.ReportingServices.xml** Datei.
1.  Ändern Sie die Konfigurationsparameter der**Aspose.Cells.ReportingServices.xml** Datei.
1. Fügen Sie die gewünschten Informationen zur Berichtskonfiguration hinzu.
1. Fügen Sie die Informationen für die Diagrammelemente hinzu, die Sie nicht als bearbeitbare Diagramme exportieren möchten. Diese Elemente werden als statische Bilder exportiert.

Zum Beispiel:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Ein als Bild exportiertes Diagramm** 

![todo: Bild_alt_Text](render-selected-chart-items-to-excel-charts_1.png)

**Ein Diagramm, das als bearbeitbares Excel-Diagramm exportiert wurde** 

![todo: Bild_alt_Text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
