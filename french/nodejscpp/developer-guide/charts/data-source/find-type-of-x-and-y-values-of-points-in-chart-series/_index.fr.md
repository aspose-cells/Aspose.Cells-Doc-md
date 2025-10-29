---  
title: Trouver le type de valeurs X et Y des points dans une série de graphiques avec Node.js via C++  
linktitle: Trouver le type de valeurs X et Y des points dans la série de graphique  
description: Apprenez comment déterminer le type de valeurs X et Y dans une série de points de graphique en utilisant Aspose.Cells for Node.js via C++. Ce guide explique les types de valeurs de données et comment y accéder et travailler avec elles dans vos graphiques.  
keywords: Aspose.Cells pour Node.js, création de graphiques, valeurs X, valeurs Y, types de données, accès, travail avec, série de graphiques.  
type: docs  
weight: 150  
url: /fr/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Scénarios d'utilisation possibles**  
Parfois, vous souhaitez connaître le type de valeurs X et Y des points dans une série. Aspose.Cells for Node.js via C++ fournit les propriétés `ChartPoint.XValueType` et `ChartPoint.YValueType` qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode `Chart.calculate()` avant de pouvoir utiliser ces propriétés efficacement.  

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**  
Le code exemple suivant charge le [fichier Excel d'exemple](64716905.xlsx) et accède au premier graphique dans la première feuille. Il appelle ensuite la méthode `Chart.calculate()` et détermine le type de valeurs X et Y du premier point du graphique, puis affiche ces informations dans la console. Voir la sortie de console ci-dessous pour référence.  

## **Code d'exemple**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Load sample Excel file containing chart.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first chart.
const chart = worksheet.getCharts().get(0);

// Calculate chart data.
chart.calculate();

// Access first chart point in the first series.
const point = chart.getNSeries().get(0).getPoints().get(0);

// Print the types of X and Y values of chart point.
console.log("X Value Type: " + point.getXValueType());
console.log("Y Value Type: " + point.getYValueType());
```  

## **Sortie console**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
