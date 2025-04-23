---  
title: Verringern Sie die Berechnungszeit der Cell.Calculate Methode mit Node.js über C++  
linktitle: Verringerung der Berechnungszeit der Cell.Calculate Methode  
description: Dieser Artikel zeigt, wie die Aspose.Cells Bibliothek verwendet werden kann, um die Berechnungszeit für Zellberechnungsmethoden in Excel mithilfe von Node.js über C++ zu reduzieren.  
keywords: Aspose.Cells, Excel, Zellberechnungsmethoden, Optimierung, Leistung, Reduzierung der Berechnungszeit, Node.js über C++  
type: docs  
weight: 100  
url: /de/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/  
---  

## **Mögliche Verwendungsszenarien**

Normalerweise empfehlen wir Benutzern, die [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) Methode einmal aufzurufen und dann die berechneten Werte der einzelnen Zellen abzurufen. Manchmal möchten Benutzer jedoch nicht die gesamte Arbeitsmappe berechnen. Sie möchten nur eine einzelne Zelle berechnen. Aspose.Cells bietet die Eigenschaft [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--), die Sie auf **false** setzen können, um die Berechnungszeit einzelner Zellen erheblich zu verringern. Wenn die rekursive Eigenschaft auf **true** gesetzt ist, werden bei jedem Aufruf alle Abhängigen der Zellen neu berechnet. Bei gesetzter Eigenschaft auf **false** werden abhängige Zellen nur einmal berechnet und bei nachfolgenden Aufrufen nicht erneut.

## **Verringern Sie die Berechnungszeit der Methode Cell.calculate()**

Der folgende Beispielcode illustriert die Verwendung der [**CalculationOptions.getRecursive()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getRecursive--)-Eigenschaft. Führen Sie diesen Code mit der angegebenen [Beispieldatei Excel](5113710.xlsx) aus und überprüfen Sie die Konsolenausgabe. Sie werden feststellen, dass das Setzen der rekursiven Eigenschaft auf **false** die Berechnungszeit erheblich verkürzt. Lesen Sie auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.

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

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der angegebenen [Beispieldatei Excel](5113710.xlsx) auf unserem Rechner ausgeführt wird. Bitte beachten Sie, dass Ihre Ausgabe abweichen kann, aber die nach dem Setzen der rekursiven Eigenschaft auf **false** verstrichene Zeit immer kürzer ist als bei der Einstellung auf **true**.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}  

