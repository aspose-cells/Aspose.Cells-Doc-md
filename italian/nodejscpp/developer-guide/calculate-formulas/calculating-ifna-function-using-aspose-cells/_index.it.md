---
title: Calcolo della funzione IFNA usando Aspose.Cells for Node.js via C++
description: Come calcolare le funzioni IFNA usando la libreria Aspose.Cells per Node.js via C++. Carica un file Excel esistente o creane uno nuovo, e calcola la funzione IFNA per ottenere il risultato. Alla fine, salva il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, funzioni IFNA, calcoli Node.js via C++
type: docs
weight: 40
url: /it/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta il calcolo della funzione Excel IFNA. La funzione IFNA restituisce il valore specificato se la formula restituisce l'errore #N/A; altrimenti, restituisce il risultato della formula.

{{% /alert %}} 
## **Calcolo della funzione IFNA usando Aspose.Cells for Node.js via C++**
Il codice di esempio seguente illustra il calcolo della funzione IFNA usando Aspose.Cells for Node.js via C++.


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
## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
