---
title: Erstellen Sie Pivot-Diagramme mit Aspose.Cells
type: docs
weight: 40
url: /de/java/create-pivot-charts-using-aspose-cells/
---
## **Aspose.Cells – Pivot-Diagramme erstellen**
Eine Pivot-Tabelle ist eine interaktive Zusammenfassung von Datensätzen. Beispielsweise können Sie Hunderte von Rechnungseinträgen in einer Liste in einem Arbeitsblatt haben. Eine Pivot-Tabelle kann die Rechnungen nach Kunde, Produkt oder Datum summieren. Mit Microsoft Excel ist es möglich, die Informationen in der Pivot-Tabelle schnell neu anzuordnen, indem Sie Schaltflächen an eine neue Position ziehen.
Ein Pivot-Diagramm ist eine interaktive grafische Darstellung der Daten in einer Pivot-Tabelle. Pivot-Diagramme wurden in Excel 2000 eingeführt. Die Verwendung eines Pivot-Diagramms macht es noch einfacher, die Daten zu verstehen, da die Pivot-Tabelle Zwischensummen und Summen automatisch erstellt.

Aspose.Cells unterstützt Pivot-Tabellen und Pivot-Diagramme.

**Java**

{{< highlight "java" >}}

 // Instantiating an Workbook object

Workbook workbook = new Workbook(dataDir + "AsposePivotTable.xls");

// Adding a new sheet

int sheetIndex = workbook.getWorksheets().add(SheetType.CHART);

Worksheet sheet3 = workbook.getWorksheets().get(sheetIndex);

// Naming the sheet

sheet3.setName("PivotChart");

// Adding a column chart

int chartIndex = sheet3.getCharts().add(ChartType.COLUMN, 0, 5, 28, 16);

Chart chart = sheet3.getCharts().get(chartIndex);

// Setting the pivot chart data source

chart.setPivotSource("PivotTable!PivotTable1");

chart.setHidePivotFieldButtons(false);

{{< /highlight >}}
## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Erstellen Sie Pivot-Tabellen und Pivot-Diagramme](/cells/de/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
