---  
title: Konvertera Excel till JSON med Node.js via C++  
linktitle: Konvertera Excel till JSON  
type: docs  
weight: 300  
url: /sv/nodejs-cpp/convert-excel-to-json/  
description: Lär dig hur du konverterar en Excel fil till JSON med Aspose.Cells for Node.js via C++.  
keywords: Exportera arbetsbok till JSON Node.js via C++, Konvertera Excel till JSON Node.js via C++  
---  

{{% alert color="primary" %}}  
Aspose.Cells stöder konvertering av en arbetsbok till JSON (JavaScript-objektnotation) fil.  
{{% /alert %}}  

## **Konvertera Excel-arbetsbok till JSON**  

Inga problem att undra hur man konverterar Excel-arbetsbok till JSON, eftersom Aspose.Cells for Node.js via C++-biblioteket tillhandahåller den bästa lösningen. Aspose.Cells API erbjuder stöd för att konvertera kalkylblad till JSON-format. För att exportera arbetsboken till JSON, skicka [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) som den andra parametern till [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-metoden. Du kan också använda [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/)-klassen för att specificera ytterligare inställningar för att exportera arket till JSON.  

Följande kodexempel visar hur man exporterar en Excel-arbetsbok till JSON. Se koden för att konvertera [källdatan](sample.xlsx) till JSON-filen som genereras av koden för referens.  

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

Följande kodexempel använder JsonSaveOptions-klassen för att specificera ytterligare inställningar och demonstrerar export av en Excel-arbetsbok till JSON. Se koden för att konvertera [källfilen](sample.xlsx) till JSON-filen som genereras av koden för referens.  

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


