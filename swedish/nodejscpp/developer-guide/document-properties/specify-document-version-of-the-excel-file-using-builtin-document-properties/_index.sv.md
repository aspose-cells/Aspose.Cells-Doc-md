---  
title: Specificera Excel filens dokumentversion med hjälp av inbyggda dokumentegenskaper med Node.js via C++  
linktitle: Ange dokumentversionen för Excel filen med hjälp av inbyggda dokumentegenskaper  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Lär dig hur man specificerar versionen av en Excel fil programmässigt med inbyggda dokumentegenskaper med Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Du kan ändra **Version number** på en Excel-fil genom att högerklicka på filen och välja Egenskaper > Detaljer och sedan redigera fältet **Version number**. Använd [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) egenskapen för att ändra det programmässigt med Aspose.Cells API:er.  

## **Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper**  

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskaper som inkluderar Titel, Författare och Versionnummer. Se [utdata Excel-fil](64716811.xlsx) genererad av koden och skärmdumpen som visar den modifierade Versionen med [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) egenskapen.  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

