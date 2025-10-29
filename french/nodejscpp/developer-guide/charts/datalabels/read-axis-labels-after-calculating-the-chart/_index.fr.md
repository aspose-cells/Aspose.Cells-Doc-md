---  
title: Lecture des étiquettes d axe après le calcul du graphique avec Node.js via C++  
linktitle: Lire les étiquettes d axe après avoir calculé le graphique  
description: Apprenez comment lire les étiquettes d axe dans Aspose.Cells for Node.js via C++ après avoir calculé le graphique. Notre guide vous montrera comment accéder et récupérer les étiquettes d axe, y compris leur mise en forme et leur positionnement.  
keywords: Aspose.Cells pour Node.js, graphique, étiquettes d axe, calcul, lecture, accès, récupération, mise en forme, positionnement, Node.js via C++  
type: docs  
weight: 90  
url: /fr/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Scénarios d'utilisation possibles**

Vous pouvez lire les étiquettes d'axe de votre graphique après avoir calculé ses valeurs en utilisant la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--). Veuillez utiliser la méthode [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) à cette fin, qui renverra la liste des étiquettes d'axe.

## **Lire les étiquettes des axes après le calcul du graphique**

Veuillez consulter le code d'exemple suivant qui charge le fichier Excel d'exemple et lit les étiquettes d'axe de catégorie du graphique dans la première feuille de calcul. Il imprime ensuite les valeurs des étiquettes d'axe sur la console. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour une référence.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **Sortie console**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
