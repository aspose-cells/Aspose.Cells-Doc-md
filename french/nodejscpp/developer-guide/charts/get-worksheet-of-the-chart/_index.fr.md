---
title: Obtenez la feuille de calcul du graphique avec Node.js via C++
linktitle: Obtenir la feuille de calcul du graphique
description: Apprenez à récupérer la feuille de calcul associée à un graphique Excel en utilisant Aspose.Cells for Node.js via C++. Accédez et manipulez efficacement les données sous jacentes du graphique.
keywords: Aspose.Cells pour Node.js, graphiques Excel, feuilles de calcul, manipulation des données, données sous jacentes, opérations, Node.js via C++
type: docs
weight: 1000
url: /fr/nodejs-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous voulez accéder à une feuille de calcul à partir d'une référence à un graphique. Aspose.Cells fournit la propriété [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--) qui renvoie la référence de la feuille de calcul contenant le graphique.

{{% /alert %}}

L'exemple suivant montre comment utiliser la propriété [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--). Le code affiche d’abord le nom de la feuille, puis accède au premier graphique de la feuille. Ensuite, il affiche à nouveau le nom de la feuille en utilisant la propriété [**Chart.getWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getWorksheet--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet of the workbook
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet name
console.log("Sheet Name: " + worksheet.getName());

// Access the first chart inside this worksheet
const charts = worksheet.getCharts();
if (charts.getCount() > 0) {
const chart = charts.get(0);

// Access the chart's sheet and display its name again
console.log("Chart's Sheet Name: " + chart.getWorksheet().getName());
} else {
console.log("No charts available in the worksheet.");
}
```

Voici la sortie console que le code d'exemple produit. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
