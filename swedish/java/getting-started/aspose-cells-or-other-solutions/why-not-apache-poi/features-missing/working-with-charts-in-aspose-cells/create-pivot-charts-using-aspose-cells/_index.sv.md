---
title: Skapa pivotdiagram med hjälp av Aspose.Cells
type: docs
weight: 40
url: /sv/java/create-pivot-charts-using-aspose-cells/
---

## **Aspose.Cells - Skapa Pivot-diagram**
En pivottabell är en interaktiv sammanfattning av poster. Till exempel kan du ha hundratals faktura-poster i en lista i ett kalkylblad. En pivottabell kan summera fakturorna efter kund, produkt eller datum. Med Microsoft Excel är det möjligt att snabbt omorganisera informationen i pivottabellen genom att dra knappar till en ny position.
Ett pivotdiagram är en interaktiv grafisk representation av data i en pivottabell. Pivotdiagram introducerades i Excel 2000. Att använda ett pivotdiagram gör det ännu enklare att förstå data eftersom pivottabellen skapar delsummer och totaler automatiskt.

Aspose.Cells stöder pivottabeller och pivotdiagram.

**Java**

{{< highlight java >}}

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
## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

För mer information, besök [Skapa Pivottabeller och Pivotdiagram](/cells/sv/java/skapa-pivottabeller-och-pivotdiagram/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
