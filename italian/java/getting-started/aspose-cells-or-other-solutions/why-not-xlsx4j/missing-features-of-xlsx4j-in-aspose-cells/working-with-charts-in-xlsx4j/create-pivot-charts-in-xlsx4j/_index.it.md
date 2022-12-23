---
title: Crea grafici pivot in xlsx4j
type: docs
weight: 30
url: /it/java/create-pivot-charts-in-xlsx4j/
---
## **Aspose.Cells - Crea grafici pivot**
Una tabella pivot è un riepilogo interattivo dei record. Ad esempio, potresti avere centinaia di voci di fattura in un elenco in un foglio di lavoro. Una tabella pivot può sommare le fatture per cliente, prodotto o data. Con Microsoft Excel è possibile riorganizzare rapidamente le informazioni nella tabella pivot trascinando i pulsanti in una nuova posizione.
Un grafico pivot è una rappresentazione grafica interattiva dei dati in una tabella pivot. I grafici pivot sono stati introdotti in Excel 2000. L'utilizzo di un grafico pivot rende ancora più semplice la comprensione dei dati poiché la tabella pivot crea automaticamente subtotali e totali.

Aspose.Cells supporta tabelle pivot e grafici pivot.

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
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/charts/createpivotcharts/AsposePivotChart.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Crea tabelle pivot e grafici pivot](/cells/it/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
