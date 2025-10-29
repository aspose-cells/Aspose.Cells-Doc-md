---  
title: Conversion de graphique en PDF avec Node.js via C++  
linktitle: Graphique en PDF  
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour convertir un graphique en un document PDF. Notre guide montrera comment exporter un graphique depuis Microsoft Excel et le sauvegarder en tant que PDF pour une distribution et une archivage ultérieurs.  
keywords: Aspose.Cells for Node.js via C++, Graphique en PDF, Microsoft Excel, Conversion en PDF, Exportation, Distribution, Archivage.  
type: docs  
weight: 47  
url: /fr/nodejs-cpp/chart-to-pdf/  
---  

## **Rendu du graphique en PDF**

Afin de rendre le graphique en format PDF, les API Aspose.Cells ont exposé la méthode [**Chart.toPdf(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toPdf-string-) avec la capacité de stocker le PDF résultant sur le chemin du disque ou en Stream.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to PDF
chart.toPdf(path.join(dataDir, "chartPDF_out.pdf"));
```

## **Créer un PDF de graphique avec la taille de page souhaitée**  
Vous pouvez créer un PDF de graphique avec la taille de page souhaitée en utilisant Aspose.Cells et préciser comment vous souhaitez aligner le graphique à l'intérieur de la page, par exemple en haut, en bas, au centre, à gauche, à droite, etc. De plus, le graphique de sortie peut être créé en stream ou sur le disque. Veuillez voir le code d'exemple ci-dessous qui charge le fichier Excel [exemple](64716906.xlsx), accède au premier graphique dans la feuille de calcul, puis le convertit en [PDF de sortie](64716907.pdf) avec la taille de page souhaitée. La capture d'écran suivante montre que la taille de la page dans le PDF de sortie est de 7x7 comme spécifié dans le code et que le graphique est centré horizontalement et verticalement.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)  
## **Code d'exemple**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing the chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateChartPDFWithDesiredPageSize.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet.
const chart = worksheet.getCharts().get(0);

// Create chart pdf with desired page size.
chart.toPdf(path.join(outputDir, "outputCreateChartPDFWithDesiredPageSize.pdf"), 7, 7, AsposeCells.PageLayoutAlignmentType.Center, AsposeCells.PageLayoutAlignmentType.Center);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
