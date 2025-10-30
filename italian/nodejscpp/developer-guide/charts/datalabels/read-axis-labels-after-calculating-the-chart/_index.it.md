---  
title: Leggi le etichette degli assi dopo aver calcolato il grafico con Node.js via C++  
linktitle: Leggere le etichette dell asse dopo il calcolo del grafico  
description: Impara come leggere le etichette degli assi in Aspose.Cells for Node.js via C++ dopo aver calcolato il grafico. La nostra guida mostrerà come accedere e recuperare le etichette degli assi, inclusa la loro formattazione e posizionamento.  
keywords: Aspose.Cells per Node.js, grafico, etichette degli assi, calcolo, lettura, accesso, recupero, formattazione, posizionamento, Node.js via C++  
type: docs  
weight: 90  
url: /it/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Possibili Scenari di Utilizzo**

Puoi leggere le etichette degli assi del tuo grafico dopo aver calcolato i valori usando il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--). Per questo scopo usa il metodo [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) che restituirà la lista delle etichette degli assi.

## **Leggere le etichette dell'asse dopo il calcolo del grafico**

Si prega di vedere il seguente codice di esempio che carica il file Excel di esempio e legge le etichette dell'asse delle categorie del grafico nel primo foglio di lavoro. Stampa quindi i valori delle etichette degli assi sulla console. Si prega di vedere l'output della console del codice di esempio riportato di seguito per un riferimento.

## **Codice di Esempio**

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

## **Output della console**

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
