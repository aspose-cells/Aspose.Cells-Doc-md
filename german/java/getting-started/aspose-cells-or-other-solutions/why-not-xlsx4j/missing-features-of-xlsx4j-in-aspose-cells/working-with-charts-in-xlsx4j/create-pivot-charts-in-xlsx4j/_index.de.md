---
title: Erstellen Sie Pivot-Diagramme in xlsx4j
type: docs
weight: 30
url: /de/java/create-pivot-charts-in-xlsx4j/
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

// Saving the Excel file

workbook.save(dataDir + "Aspose_PivotChart_Out.xls");


{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Erstellen Sie Pivot-Tabellen und Pivot-Diagramme](/cells/de/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
