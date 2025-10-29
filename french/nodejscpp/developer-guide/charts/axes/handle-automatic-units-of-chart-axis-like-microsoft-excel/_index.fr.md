---  
title: Gérer les unités automatiques de l axe du graphique comme Microsoft Excel avec Node.js via C++  
linktitle: Gérer les Unités Automatiques de l Axe du Graphique comme Microsoft Excel  
description: Apprenez à gérer les unités automatiques sur les axes du graphique dans Aspose.Cells for Node.js via C++. Notre guide vous montrera comment configurer et personnaliser les unités automatiques sur un axe de graphique, y compris l affichage de la notation scientifique et le réglage de l’échelle.  
keywords: Aspose.Cells for Node.js via C++, axes du graphique, unités automatiques, Microsoft Excel, configuration, personnalisation, notation scientifique, mise à l’échelle.  
type: docs  
weight: 120  
url: /fr/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Scénarios d'utilisation possibles**  
Les premières versions de Aspose.Cells for Node.js via C++ n’étaient pas en mesure de gérer correctement les unités automatiques de l'axe du graphique lors de l rendu de l'image ou du PDF. Maintenant, Aspose.Cells for Node.js via C++ supporte la gestion des unités automatiques de l’axe du graphique. Aucun changement de code n’est nécessaire. Il suffit de convertir votre graphique en une image ou un PDF et l’axe du graphique sera rendu comme dans Microsoft Excel.  

## **Gérer les unités automatiques de l'axe du graphique comme dans Microsoft Excel**  
Le code d’exemple suivant charge le [fichier Excel d’exemple](61767755.xlsx) et génère le [graphique PDF de sortie](61767752.pdf). La capture d'écran montre les unités automatiques de l’axe du graphique encadrées en rouge et compare également le graphique du fichier Excel d’origine avec le graphique PDF de sortie. Les deux sont exactement identiques.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Code d'exemple**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
