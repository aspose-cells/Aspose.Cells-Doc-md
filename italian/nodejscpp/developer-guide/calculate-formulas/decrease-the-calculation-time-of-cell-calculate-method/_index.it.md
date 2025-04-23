---  
title: Riduci il tempo di calcolo del metodo Cell.Calculate con Node.js via C++  
linktitle: Ridurre il tempo di calcolo del metodo Cell.Calculate  
description: Questo articolo introduce come usare la libreria Aspose.Cells per ridurre i tempi di calcolo dei metodi di calcolo delle celle in Excel usando Node.js via C++.  
keywords: Aspose.Cells, Excel, metodi di calcolo delle celle, ottimizzazione, prestazioni, riduzione del tempo di calcolo, Node.js via C++  
type: docs  
weight: 100  
url: /it/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Possibili Scenari di Utilizzo**

Normalmente, consigliamo agli utenti di chiamare il metodo [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) una volta e poi ottenere i valori calcolati delle singole celle. Ma a volte, gli utenti non vogliono calcolare l'intero workbook. Volevano solo calcolare una singola cella. Aspose.Cells fornisce la proprietà [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--), che può essere impostata su **false** per diminuire significativamente il tempo di calcolo delle singole celle. Quando la proprietà ricorsiva è impostata su **true**, tutti i dipendenti delle celle vengono ricalcolati ad ogni chiamata. Tuttavia, quando la proprietà ricorsiva è **false**, le celle dipendenti vengono calcolate solo una volta e non vengono ricalcolate nelle chiamate successive.

## **Riduci il tempo di calcolo del metodo Cell.calculate()**

Il codice di esempio seguente illustra l'uso della proprietà [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--). Eseguire questo codice con il [file Excel di esempio](5113710.xlsx) fornito e verificare l'output della console. Noterete che impostare la proprietà ricorsiva su **false** riduce significativamente il tempo di calcolo. Leggere anche i commenti per una migliore comprensione di questa proprietà.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Test calculation time after setting recursive true
workbook.calculateFormula(); // Call calculateFormula method to initiate calculation

// Test calculation time after setting recursive false
workbook.calculateFormula(false); // Specify ignoreError as false
```  
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

function testCalcTimeRecursive(rec) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Set the calculation option, set recursive true or false as per parameter
const opts = new AsposeCells.CalculationOptions();
opts.setRecursive(rec);

// Start stop watch            
const start = process.hrtime();

// Calculate cell A1 one million times
for (let i = 0; i < 1000000; i++) {
ws.getCells().get("A1").calculate(opts);
}

// Stop the watch
const end = process.hrtime(start);

// Calculate elapsed time in seconds
const estimatedTime = end[0] + end[1] / 1e9;

// Print the elapsed time in seconds
console.log(`Recursive ${rec}: ${estimatedTime} seconds`);
}

// Call the function for testing
testCalcTimeRecursive(true);
testCalcTimeRecursive(false);
```

## **Output della console**

Questo è l'output della console del codice di esempio sopra quando eseguito con il [file Excel di esempio](5113710.xlsx) sulla nostra macchina. Si noti che il vostro output potrebbe differire, ma il tempo trascorso dopo aver impostato la proprietà ricorsiva su **false** sarà sempre inferiore rispetto a impostarla su **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

