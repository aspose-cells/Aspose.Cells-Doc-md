---  
title: Redimensionner la forme de l étiquette de données du graphique pour l adapter au texte avec Node.js via C++  
linktitle: Redimensionner la forme de l étiquette de données du graphique pour s adapter au texte  
description: Apprenez comment redimensionner la forme de l étiquette de données dans un graphique pour qu elle s adapte au texte dans Aspose.Cells for Node.js via C++. Notre guide vous montrera comment ajuster la taille et la forme du conteneur de l étiquette pour s assurer que le texte s affiche correctement sans tronquature ni chevauchement.  
keywords: Aspose.Cells for Node.js via C++, programmation de graphiques, étiquettes de données, redimensionnement de forme, ajustement du texte, truncature, chevauchement.  
type: docs  
weight: 220  
url: /fr/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
L'application Excel propose l'option **Redimensionner la forme pour s'adapter au texte** pour les étiquettes de données du graphique afin d'augmenter la taille de la forme afin que le texte s'y insère.  
{{% /alert %}}  

## **Comment redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte dans Microsoft Excel**  

Cette option peut être accessible via l'interface Excel en sélectionnant n'importe quelle étiquette de données sur le graphique. Faites un clic droit et choisissez le menu **Format DataLabels**. Dans l'onglet **Taille & Propriétés**, développez **Alignement** pour révéler les propriétés associées, y compris l'option **Redimensionner la forme pour corriger le texte**.  

## **Comment redimensionner la forme de l'étiquette de données du graphique pour qu'elle s'adapte au texte en utilisant Aspose.Cells for Node.js via C++**  

Pour imiter la fonction d'Excel de redimensionnement des formes d'étiquettes de données pour les adapter au texte, les APIs Aspose.Cells ont exposé la propriété Booléenne [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--). Le code ci-dessous montre un scénario d'utilisation simple de la propriété [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

