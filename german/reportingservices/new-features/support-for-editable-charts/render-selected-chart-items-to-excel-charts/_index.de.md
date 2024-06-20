---
title: Ausgewählte Diagrammelemente als Excel Diagramme rendern
type: docs
weight: 30
url: /de/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

Um nur einige Diagramme in einem Bericht als Excel-Diagramme zu rendern:

1. Öffnen Sie die Datei **Aspose.Cells.ReportingServices.xml**.
1. Ändern Sie die Konfigurationsparameter der Datei **Aspose.Cells.ReportingServices.xml**.
1. Fügen Sie die gewünschten Berichtskonfigurationsinformationen hinzu.
1. Fügen Sie die Informationen für die Diagrammelemente hinzu, die nicht als bearbeitbare Diagramme exportiert werden sollen. Diese Elemente werden als statische Bilder exportiert.

Zum Beispiel:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Ein als Bild exportiertes Diagramm** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Ein als bearbeitbares Excel-Diagramm exportiertes Diagramm** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
