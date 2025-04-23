---  
title: JSON mit Node.js via C++  
linktitle: Json  
type: docs  
weight: 300  
url: /de/nodejs-cpp/convert-workbook-to-json/  
description: Erfahren Sie, wie Sie Excel Arbeitsmappen mithilfe von Aspose.Cells for Node.js via C++ in JSON konvertieren.  
---  

{{% alert color="primary" %}}  
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine Json-Datei (JavaScript Object Notation).  
{{% /alert %}}  

## **Excel-Arbeitsmappe in JSON konvertieren**  

Das Aspose.Cells API unterstützt die Konvertierung von Tabellen in das JSON-Format. Um die Arbeitsmappe als JSON zu exportieren, übergeben Sie [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode. Sie können auch die [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach JSON zu spezifizieren.  

Das folgende Code-Beispiel zeigt den Export des aktiven Arbeitsblatts nach JSON unter Verwendung des [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json)-Aufzählungsmitglieds. Bitte beachten Sie den Code, um die [Quelldatei](book1.xlsx) in die durch den Code generierte [Ausgabedatei Json](book1.Json) umzuwandeln.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Erweiterte Themen**  
- [Konvertieren von CSV in JSON](/cells/de/nodejs-cpp/convert-csv-to-json/)  
- [In-Excel-in-JSON-konvertieren](/cells/de/nodejs-cpp/convert-excel-to-json/)  
- [JSON in CSV konvertieren](/cells/de/nodejs-cpp/convert-json-to-csv/)  
- [JSON-in-Excel-konvertieren](/cells/de/nodejs-cpp/convert-json-to-excel/)  

