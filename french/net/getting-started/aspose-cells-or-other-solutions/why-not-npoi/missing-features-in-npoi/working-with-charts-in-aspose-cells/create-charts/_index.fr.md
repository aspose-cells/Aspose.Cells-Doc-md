---
title: Créer des graphiques
type: docs
weight: 20
url: /fr/net/create-charts/
---
## **Aspose.Cells - Créer des graphiques**
Il est possible d'ajouter une variété de graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells fournit de nombreux objets graphiques flexibles.

**C#**

{{< highlight "cs" >}}

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

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B3"

SeriesCollection serieses = chart.NSeries;

serieses.Add("A1:B3", true);

// Saving the Excel file

workbook.Save("Chart_Aspose.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Créer des graphiques** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Create.Charts.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Comment créer un graphique](/cells/fr/net/create-charts/).

{{% /alert %}}
