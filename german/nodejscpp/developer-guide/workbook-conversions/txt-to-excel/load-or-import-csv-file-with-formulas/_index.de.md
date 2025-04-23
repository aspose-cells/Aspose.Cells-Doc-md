---  
title: CSV Datei mit Formeln mit Node.js laden oder importieren  
linktitle: Laden oder Importieren von CSV Dateien mit Formeln  
type: docs  
weight: 350  
url: /de/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Lernen Sie, wie Sie CSV Dateien mit Formeln mit Aspose.Cells for Node.js via C++ laden und importieren.  
---  

{{% alert color="primary" %}}  

CSV-Dateien enthalten meist Textdaten und keine Formeln. Manchmal enthalten CSV-Dateien jedoch auch Formeln. Solche Dateien sollten mit der Eigenschaft [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) auf **true** gesetzt werden. Sobald diese Eigenschaft auf **true** gesetzt ist, behandelt Aspose.Cells Formeln nicht nur als einfachen Text, sondern verarbeitet sie wie gewohnt durch die Formel-Engine.

{{% /alert %}}  

Der folgende Code zeigt, wie Sie eine CSV-Datei mit Formeln laden sowie importieren können. Sie können jede CSV-Datei verwenden. Zur Veranschaulichung verwenden wir die [einfachen CSV](5115034.csv), die diese Daten enthält. Wie Sie sehen, enthält sie eine Formel.

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

Der Code lädt zuerst die CSV-Datei, importiert sie erneut bei Zelle D4. Schließlich speichert er das Arbeitsbuch im XLSX-Format. Die [Ausgabedatei XLSX](5115052.xlsx) sieht folgendermaßen aus. Wie du siehst, enthalten die Zellen C3 und F4 Formeln und deren Ergebnis ist 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


