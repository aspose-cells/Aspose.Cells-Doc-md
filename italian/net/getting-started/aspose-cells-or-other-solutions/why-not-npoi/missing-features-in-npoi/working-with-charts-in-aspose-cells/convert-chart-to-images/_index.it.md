---
title: Converti grafico in immagini
type: docs
weight: 10
url: /it/net/convert-chart-to-images/
---

## **Aspose.Cells - Converti grafico in immagini**
I grafici sono visualmente accattivanti e rendono facile per gli utenti vedere confronti, modelli e tendenze nei dati.
Il metodo toImage della classe Chart converte il grafico in un file immagine, che può essere salvato su disco o in uno stream.

**C#**

{{< highlight cs >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the first worksheet

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet sheet = worksheets[0];

// Adding some sample value to cells

Cells cells = sheet.Cells;

Cell cell = cells["A1"];

cell.Value = 50;

cell = cells["A2"];

cell.Value = 100;

cell = cells["A3"];

cell.Value = 150;

cell = cells["B1"];

cell.Value = 4;

cell = cells["B2"];

cell.Value = 20;

cell = cells["B3"];

cell.Value = 50;

ChartCollection charts = sheet.Charts;

// Adding a chart to the worksheet

int chartIndex = charts.Add(ChartType.Pyramid, 5, 0, 15, 5);

Chart chart = charts[chartIndex];

//Save the chart image file.

chart.ToImage("AsposeChartImage.png", ImageFormat.Png);

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Converti grafico in immagini** da uno dei siti di codice sociale qui sotto:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per maggiori dettagli, visita [Converting Chart to Image](/cells/it/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
