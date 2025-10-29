---  
title: Déterminer quel axe existe dans le graphique avec Node.js via C++  
linktitle: Déterminez quel axe existe dans le graphique  
description: Apprenez comment déterminer quel axe existe dans un graphique créé avec Aspose.Cells for Node.js via C++. Notre guide vous aidera à identifier et accéder aux différents axes du graphique, y compris les axes catégorie, valeur et secondaires.  
keywords: Aspose.Cells pour Node.js, graphique, axe, existence, catégorie, valeur, secondaire.  
type: docs  
weight: 140  
url: /fr/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
 Parfois, l'utilisateur doit savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeur secondaire existe dans le graphique ou non. Certains graphiques comme Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc., n'ont pas d'axe.  

Aspose.Cells fournit [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) méthode pour déterminer si le graphique a un axe particulier ou non.  
{{% /alert %}}  

Le code d'exemple suivant montre comment utiliser [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) pour déterminer si le graphique d'exemple possède un axe de catégorie et de valeur principal et secondaire.  

## Code Node.js pour déterminer quel axe existe dans le graphique  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## Sortie console générée par le code d'exemple  

La sortie console du code est affichée ci-dessous, elle montre true pour l'axe de catégorie principal et de valeur, et false pour l'axe secondaire de catégorie et de valeur.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
