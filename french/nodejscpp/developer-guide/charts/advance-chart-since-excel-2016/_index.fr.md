---  
title: Lire et manipuler les graphiques Excel 2016 avec Node.js via C++  
linktitle: Lire et Manipuler les Graphiques Excel 2016  
description: Apprenez comment lire et manipuler les graphiques Excel 2016 en utilisant Aspose.Cells for Node.js via C++. Ce guide vous montrera comment accéder et modifier diverses propriétés du graphique.  
keywords: Aspose.Cells pour Node.js, graphiques Excel 2016, lecture, manipulation, étiquettes de données, couleurs des séries, disposition, graphique hiérarchique, graphique circulaire.  
type: docs  
weight: 48  
url: /fr/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Scénarios d'utilisation possibles**  
Aspose.Cells prend désormais en charge la lecture et la manipulation des graphiques Microsoft Excel 2016 qui ne sont pas présents dans Microsoft Excel 2013 ou les versions antérieures.  
## **Lire et manipuler les graphiques Excel 2016**  
Le code d'exemple suivant charge le fichier Excel source (22774101.xlsx) contenant des graphiques Excel 2016 dans la première feuille. Il lit tous les graphiques un par un et modifie leur titre en fonction de leur type de graphique. La capture d'écran suivante montre le fichier Excel source avant l'exécution du code. Comme vous pouvez le voir, le titre du graphique est identique pour tous.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

La capture d'écran suivante montre le [fichier Excel de sortie](22774104.xlsx) après l'exécution du code. Comme vous pouvez le voir, le titre du graphique est modifié en fonction de son type de graphique.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Code d'exemple**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **Sortie console**  
Voici la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel source](22774101.xlsx) fourni.

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Sujets avancés**  
- [Création de Graphique en Cascade](/cells/fr/nodejs-cpp/creating-waterfall-chart/)  
- [Création de Graphique TreeMap](/cells/fr/nodejs-cpp/creating-treemap-chart/)  
- [Création de Graphique Sunburst](/cells/fr/nodejs-cpp/creating-sunburst-chart/)  

