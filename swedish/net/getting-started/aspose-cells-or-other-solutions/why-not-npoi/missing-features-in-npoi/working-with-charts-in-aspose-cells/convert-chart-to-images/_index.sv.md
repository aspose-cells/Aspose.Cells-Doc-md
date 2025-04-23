---
title: Konvertera diagram till bilder
type: docs
weight: 10
url: /sv/net/convert-chart-to-images/
---

## **Aspose.Cells - Konvertera diagram till bilder**
Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data.
Metoden toImage i Chart-klassen konverterar diagrammet till en bildfil, som kan sparas på hårddisken eller i en ström.

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
## **Ladda ned körbar kod**
Ladda ner **Konvertera diagram till bilder** från någon av nedanstående sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer detaljer, besök [Konvertera diagram till bild](/cells/sv/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
