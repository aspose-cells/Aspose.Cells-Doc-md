---
title: Obtenir le texte de l équation de la ligne de tendance du graphique avec Node.js via C++
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour récupérer le texte de l équation d une ligne de tendance dans un graphique créé dans Microsoft Excel. Notre guide montrera comment accéder et extraire l équation d une ligne de tendance pour une analyse ou un affichage ultérieur.
keywords: Aspose.Cells for Node.js via C++, Ligne de tendance du graphique, Texte de l équation, Microsoft Excel, Analyse de données, Affichage.
linktitle: Trendlines
type: docs
weight: 110
url: /fr/nodejs-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Vous pouvez récupérer le texte de l'équation de la ligne de tendance du graphique en utilisant Aspose.Cells for Node.js via C++. Aspose.Cells fournit la propriété [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) qui retourne le texte de l'équation de la ligne de tendance du graphique. Pour utiliser cette propriété, vous devrez d'abord appeler la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--).

{{% /alert %}}

La capture d'écran suivante montre le graphique avec une ligne de tendance et son texte d'équation en rouge. Nous allons récupérer ce texte en utilisant la propriété [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) dans l'exemple de code ci-dessous.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Code Node.js pour obtenir le texte de l'équation de la ligne de tendance du graphique

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Calculate the Chart first to get the Equation Text of Trendline
chart.calculate();

// Access the Trendline
const trendLine = chart.getNSeries().get(0).getTrendLines().get(0);

// Read the Equation Text of Trendline
console.log("Equation Text: " + trendLine.getDataLabels().getText());
```

## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight javascript >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
