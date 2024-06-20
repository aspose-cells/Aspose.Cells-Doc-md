---
title: Diagramm in Bilder konvertieren
type: docs
weight: 10
url: /de/net/convert-chart-to-images/
---

## **Aspose.Cells - Diagramm in Bilder umwandeln**
Diagramme sind optisch ansprechend und erleichtern es Benutzern, Vergleiche, Muster und Trends in Daten zu erkennen.
Die Chart-Klasse toImage-Methode konvertiert das Diagramm in eine Bilddatei, die auf der Festplatte oder im Stream gespeichert werden kann.

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
## **Laufenden Code herunterladen**
Laden Sie **Diagramm in Bilder konvertieren** von einer der unten aufgeführten sozialen Code-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Konvertieren von Diagramm in Bild](/cells/de/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
