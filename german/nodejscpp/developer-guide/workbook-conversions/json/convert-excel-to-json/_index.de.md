---  
title: Konvertieren von Excel in JSON mit Node.js via C++  
linktitle: Konvertieren Sie Excel in JSON  
type: docs  
weight: 300  
url: /de/nodejs-cpp/convert-excel-to-json/  
description: Lernen Sie, wie Sie eine Excel Datei mithilfe von Aspose.Cells for Node.js via C++ in JSON konvertieren.  
keywords: Exportieren eines Arbeitsbuchs nach JSON mit Node.js via C++, Konvertieren von Excel nach JSON mit Node.js via C++  
---  

{{% alert color="primary" %}}  
Aspose.Cells unterstützt die Konvertierung eines Arbeitsbuchs in eine JSON (JavaScript-Objekt-Notation)-Datei.  
{{% /alert %}}  

## **Excel-Arbeitsmappe in JSON konvertieren**  

Sie müssen sich keine Sorgen machen, wie man ein Excel-Arbeitsbuch in JSON konvertiert, denn die Aspose.Cells for Node.js via C++-Bibliothek bietet die beste Lösung. Die Aspose.Cells-API unterstützt die Konvertierung von Tabellenblättern in das JSON-Format. Um das Arbeitsbuch in JSON zu exportieren, übergeben Sie [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) als zweiten Parameter der [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode. Sie können auch die [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts in JSON festzulegen.  

Das folgende Codebeispiel demonstriert das Exportieren eines Excel-Arbeitsbuchs nach JSON. Bitte beachten Sie den Code zur Konvertierung der [Quelldatei](sample.xlsx) in die durch den Code generierte JSON-Datei.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

Das folgende Codebeispiel verwendet die JsonSaveOptions-Klasse, um zusätzliche Einstellungen festzulegen, und zeigt das Exportieren eines Excel-Arbeitsbuchs nach JSON. Bitte beachten Sie den Code zur Konvertierung der [Quelldatei](sample.xlsx) in die durch den Code generierte JSON-Datei.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
