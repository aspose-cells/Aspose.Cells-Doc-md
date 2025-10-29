---  
title: Définir la source de données pour le graphique avec Node.js via C++  
description: Découvrez les différentes sources de données prises en charge par Aspose.Cells for Node.js via C++. Notre guide vous guidera à travers les différents types de sources de données disponibles et vous montrera comment vous connecter et récupérer des données pour remplir vos feuilles de calcul.  
keywords: Aspose.Cells for Node.js via C++, création de graphiques, formatage des données, étiquettes, couleurs, polices, apparence, convivialité.  
linktitle: Source de données  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/data-formatting-in-charts/  
---  

Dans nos sujets précédents, nous avons déjà fourni de nombreux exemples pour démontrer comment vous pouvez définir une source de données pour votre graphique, mais dans ce sujet, nous allons fournir plus de détails sur les types de données pouvant être définis pour un graphique.

## **Définition des données du graphique**

Il existe deux types de données à manipuler lors de l'utilisation de graphiques avec Aspose.Cells, comme suit :

- Données du graphique.
- Données de catégorie.

### **Données du graphique**

Les données du graphique sont les données que nous utilisons comme source pour construire nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en utilisant la méthode [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) de l'objet [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Données de catégorie**

Les données de catégorie sont utilisées pour l’étiquetage des données du graphique et peuvent être ajoutées à [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) en utilisant sa propriété [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--). Un exemple complet est donné ci-dessous pour démontrer l’utilisation des données de graphique et de catégorie. Après l’exécution du code ci-dessus, un graphique en colonnes sera ajouté à la feuille de calcul comme illustré ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Sujets avancés**  
- [Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage](/cells/fr/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Créer des graphiques dynamiques](/cells/fr/nodejs-cpp/create-dynamic-charts/)  
- [Méthode simple pour configurer un graphique en utilisant la méthode Chart.SetChartDataRange](/cells/fr/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
