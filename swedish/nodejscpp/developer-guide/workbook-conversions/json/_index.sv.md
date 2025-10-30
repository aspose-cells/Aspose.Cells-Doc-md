---  
title: Json med Node.js via C++  
linktitle: Json  
type: docs  
weight: 300  
url: /sv/nodejs-cpp/convert-workbook-to-json/  
description: Lär dig hur du konverterar Excel arbetsbok till JSON med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells stöder konvertering av en arbetsbok till JSON (JavaScript Object Notation) fil.  
{{% /alert %}}  

## **Konvertera Excel-arbetsbok till JSON**  

Aspose.Cells API erbjuder stöd för att konvertera kalkylblad till JSON-format. För att exportera arbetsboken till JSON, ange [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) som andra parameter i [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metoden. Du kan också använda [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) klassen för att specificera ytterligare inställningar för export av arbetsblad till JSON.  

Följande kodexempel demonstrerar export av det aktiva arbetsbladet till JSON med hjälp av [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json) enumeration-medlem. Se koden för att konvertera [källfilen](book1.xlsx) till den [utdata JSON-filen](book1.Json) genererad av koden för referens.  

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

## **Fortsatta ämnen**  
- [Konvertera CSV till JSON](/cells/sv/nodejs-cpp/convert-csv-to-json/)  
- [Konvertera-Excel-till-JSON](/cells/sv/nodejs-cpp/convert-excel-to-json/)  
- [Konvertera JSON till CSV](/cells/sv/nodejs-cpp/convert-json-to-csv/)  
- [Konvertera-JSON-till-Excel](/cells/sv/nodejs-cpp/convert-json-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
