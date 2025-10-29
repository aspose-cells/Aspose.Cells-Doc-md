---  
title: Trouvez si les points de données se trouvent dans le second diagramme ou la seconde barre sur un graphique en secteur de secteurs ou en barres de secteurs avec Node.js via C++  
linktitle: Trouver si les points de données sont dans le deuxième secteur ou barre d un diagramme de secteur ou barre de diagramme.  
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour déterminer si les points de données se trouvent dans le second diagramme ou la seconde barre sur un graphique en secteur de secteurs ou en barres de secteurs. Ce guide montrera comment identifier et accéder au secteur ou à la barre secondaire sur un graphique composite, vous permettant d’analyser et de manipuler efficacement les données.  
keywords: Aspose.Cells for Node.js via C++, Graphique en secteurs avec secteurs secondaires, Barre secondaire, Analyse de données, Manipulation de données.  
type: docs  
weight: 180  
url: /fr/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Scénarios d'utilisation possibles**  
Vous pouvez déterminer si les points de données d'une série se trouvent dans le second secteur sur un graphique *Secteur de secteurs* ou dans la barre d’un graphique *Barre de secteurs* en utilisant Aspose.Cells for Node.js via C++. Veuillez utiliser la propriété [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) pour le déterminer.  

Veuillez télécharger le [fichier Excel d’exemple](5115193.xlsx) utilisé dans le code d’exemple suivant et voir sa sortie console. Si vous ouvrez le [fichier Excel d’exemple](5115193.xlsx), vous constaterez que tous les points de données inférieurs à 10 se trouvent dans la barre du graphique *Barre de secteurs*, comme le montre également la sortie de la console.  
## **Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles**  
Le code d’exemple suivant montre comment déterminer si les points de données se trouvent dans le second secteur ou la seconde barre sur un graphique *Secteur de secteurs* ou *Barre de secteurs*.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load source excel file containing Bar of Pie chart
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieBars.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart which is Bar of Pie chart and calculate it
const chart = worksheet.getCharts().get(0);
chart.calculate();

// Access the chart series
const series = chart.getNSeries().get(0);

/* 
* Print the data points of the chart series and 
* check its IsInSecondaryPlot property to determine 
* if data point is inside the bar or pie 
*/
for (let i = 0; i < series.getPoints().getCount(); i++) {
// Access chart point
const chartPoint = series.getPoints().get(i);

// Skip null values
if (chartPoint.get_YValue() === null) continue;

/* 
* Print the chart point value and see if it is inside bar or pie.
* If the IsInSecondaryPlot is true, then the data point is inside bar 
* otherwise it is inside the pie. 
*/
console.log("Value: " + chartPoint.get_YValue());
console.log("IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot());
console.log();
}
```  
## **Sortie console**  
Veuillez voir la sortie de la console suivante générée après l’exécution du code d’exemple ci-dessus avec le [fichier Excel d’exemple](5115193.xlsx). Si [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) est **faux**, le point de données se trouve dans le secteur ou, s’il est **vrai**, alors le point de données se trouve dans la barre.  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
