---
title: Skapa diagram i xlsx4j
type: docs
weight: 20
url: /sv/java/create-charts-in-xlsx4j/
---

## **Aspose.Cells - Skapa diagram**
Det är möjligt att lägga till olika diagram i kalkylblad med Aspose.Cells. Aspose.Cells tillhandahåller många flexibla diagramobjekt.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the first worksheet

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Adding some sample value to cells

Cells cells = sheet.getCells();

Cell cell = cells.get("A1");

cell.setValue(50);

cell = cells.get("A2");

cell. setValue (100);

cell = cells.get("A3");

cell.setValue(150);

cell = cells.get("B1");

cell.setValue(4);

cell = cells.get("B2");

cell.setValue(20);

cell = cells.get("B3");

cell.setValue(50);

ChartCollection charts = sheet.getCharts();

// Adding a chart to the worksheet

int chartIndex = charts.add(ChartType.PYRAMID,5,0,15,5);

Chart chart = charts.get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B3"

SeriesCollection serieses = chart.getNSeries();

serieses.add("A1:B3", true);

// Saving the Excel file

workbook.save(dataDir + "Chart_Aspose.xls");

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createcharts/AsposeCreateCharts.java)
{{< app/cells/assistant language="java" >}}
