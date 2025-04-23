---  
title: Comment définir un point comme total avec Node.js via C++  
linktitle: Comment définir un point comme total  
description: Apprenez à définir des points comme totaux dans les graphiques en cascade en utilisant Aspose.Cells for Node.js via C++.  
keywords: Graphique en cascade, Point, Définir comme total, Node.js via C++  
type: docs  
weight: 72  
url: /fr/nodejs-cpp/how-to-set-point-as-total/  
---  

## Qu'est-ce que "Définir le point comme total" dans un graphique Excel

Dans certains graphiques Excel, par exemple un graphique en cascade, certaines données de points sont la somme des points précédents, et vous pouvez avoir besoin de "définir le point comme total". Nous montrerons le code d'exemple et l'illustration ci-dessous.

## Un graphique en cascade nécessite de "Définir le point comme total" 

![todo:image_alt_text](set-as-total1.png)

Cette image montre un graphique en cascade dans Excel. Nous pouvons voir qu'il y a quatre points de données commençant par "Total", qui sont utilisés pour compter tous les points précédents. Dans cette image, les paramètres ne sont pas tout à fait corrects. Lorsque nous sélectionnons un point "Total 2024", nous pouvons voir que l’option "Définir comme total" n’est pas cochée dans Excel. Ci-dessous, un [fichier Excel exemple](SampleSheet.xlsx) à modifier, et nous utiliserons Aspose.Cells for Node.js via C++ pour le configurer correctement.

## Utiliser Aspose.Cells for Node.js via C++ pour "Définir le point comme total" 

Nous utilisons le code suivant pour configurer le fichier correctement :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Vous pouvez obtenir le [fichier de sortie correct](output.xlsx) suivant

Comme le montre la figure ci-dessous, les quatre points de données "Total" sont correctement configurés, et vous pouvez voir la différence avec le graphique précédent.

![todo:image_alt_text](set-as-total2.png)  
