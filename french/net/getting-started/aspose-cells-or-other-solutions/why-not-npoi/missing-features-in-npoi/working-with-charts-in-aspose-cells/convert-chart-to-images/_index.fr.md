---
title: Convertir le graphique en images
type: docs
weight: 10
url: /fr/net/convert-chart-to-images/
---

## **Aspose.Cells - Convertir un graphique en images**
Les graphiques sont visuellement attrayants et facilitent la comparaison, la détection de motifs et de tendances dans les données.
La méthode toImage de la classe Chart convertit le graphique en un fichier image, qui peut être enregistré sur le disque ou dans un flux.

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
## **Télécharger le code en cours d'exécution**
Téléchargez le formulaire **Convertir le graphique en images** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Convertir le graphique en image](/cells/fr/net/converting-chart-to-image-in-svg-format/).

{{% /alert %}}
