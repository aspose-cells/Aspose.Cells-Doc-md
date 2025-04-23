---
title: Berechnung der IFNA Funktion mit Aspose.Cells for Node.js via C++
description: So berechnen Sie die IFNA Funktion mit der Aspose.Cells Bibliothek für Node.js via C++. Laden Sie eine bestehende Excel Datei oder erstellen Sie eine neue, berechnen Sie die IFNA Funktion, um das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, IFNA Funktionen, Berechnungen Node.js via C++
type: docs
weight: 40
url: /de/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Berechnung der Excel-IFNA-Funktion. Die IFNA-Funktion gibt den angegebenen Wert zurück, wenn die Formel den Fehlerwert #N/A ergibt; andernfalls gibt sie das Ergebnis der Formel zurück.

{{% /alert %}} 
## **Berechnung der IFNA-Funktion mit Aspose.Cells for Node.js via C++**
Das folgende Beispiel zeigt die Berechnung der IFNA-Funktion mit Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
