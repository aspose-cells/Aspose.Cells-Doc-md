---  
title: Trova se i punti dati sono nel secondo grafico a torta o barra di un grafico Pie of Pie o Bar of Pie con Node.js tramite C++  
linktitle: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.  
description: Impara come usare Aspose.Cells for Node.js via C++ per trovare se i punti dati sono nel secondo grafico a torta o barra di un grafico Pie of Pie o Bar of Pie. Questa guida dimostrerà come identificare e accedere alla torta o barra secondaria su un grafico composito, consentendoti di analizzare e manipolare i dati efficacemente.  
keywords: Aspose.Cells for Node.js via C++, Grafico Pie of Pie, Bar of Pie, Torta Secondaria, Barra Secondaria, Analisi Dati, Manipolazione Dati.  
type: docs  
weight: 180  
url: /it/nodejs-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **Possibili Scenari di Utilizzo**  
Puoi verificare se i punti dati di una serie sono nel secondo settore di *Pie of Pie* o nel bar di *Bar of Pie* utilizzando Aspose.Cells for Node.js via C++. Si prega di usare la proprietà [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) per determinarlo.  

Scarica il [file Excel di esempio](5115193.xlsx) usato nel codice di esempio seguente e verifica l'output sulla console. Se apri il [file Excel di esempio](5115193.xlsx), troverai che tutti i punti dati inferiori a 10 sono all’interno della barra di *Bar of Pie* come mostrato anche dall’output della console.  
## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**  
Il codice di esempio seguente mostra come trovare se i punti dati sono nel secondo settore o barra di un grafico *Pie of Pie* o *Bar of Pie*.  

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
## **Output della console**  
Vedi l'output sulla console generato dopo l'esecuzione del codice di esempio sopra con il [file Excel di esempio](5115193.xlsx). Se [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/nodejs-cpp/chartpoint/#isInSecondaryPlot--) è **false**, il punto dati si trova all’interno del Torta o, se è **true**, il punto dati si trova all’interno della Barra.  

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
