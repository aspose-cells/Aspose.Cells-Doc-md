---  
title: Trova il tipo di valori X e Y dei punti nella serie del grafico con Node.js via C++  
linktitle: Trova il tipo di valori X e Y dei punti nella serie del grafico  
description: Impara come determinare il tipo di valori X e Y nei punti della serie del grafico usando Aspose.Cells for Node.js via C++. Questa guida spiega i tipi di valori di dati e come accedervi e lavorarci nei tuoi grafici.  
keywords: Aspose.Cells per Node.js, creazione grafici, valori X, valori Y, tipi di dati, accesso, lavorare, serie del grafico.  
type: docs  
weight: 150  
url: /it/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/  
---  

## **Possibili Scenari di Utilizzo**  
A volte vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells for Node.js via C++ fornisce le proprietà `ChartPoint.XValueType` e `ChartPoint.YValueType` che possono essere usate a questo scopo. Ricorda che devi chiamare il metodo `Chart.calculate()` prima di poter usare queste proprietà in modo efficace.  

## **Trova il tipo di valori X e Y dei punti nella serie del grafico**  
Il seguente esempio di codice carica il [file Excel di esempio](64716905.xlsx) e accede al primo grafico all'interno del primo foglio di lavoro. Poi chiama il metodo `Chart.calculate()` e determina il tipo di valori X e Y del primo punto del grafico, stampandoli in console. Consulta l'output della console mostrato di seguito come riferimento.  

## **Codice di Esempio**  
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

## **Output della console**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}  

