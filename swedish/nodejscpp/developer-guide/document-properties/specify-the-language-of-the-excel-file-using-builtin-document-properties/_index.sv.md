---
title: Specificera språket för Excel filen med hjälp av inbyggda dokumentegenskaper med Node.js via C++
linktitle: Ange språket för Excel filen med hjälp av inbyggda dokumentegenskaper
type: docs
weight: 30
url: /sv/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Möjliga användningsscenario**

Du kan ändra språket för en Excel-fil genom att högerklicka på filen och välja Egenskaper > Detaljer och sedan redigera språket. Använd [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) egenskapen för att ändra det programmässigt med Aspose.Cells for Node.js via C++ API:er.

## **Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper**

Följande exempelkod skapar en arbetsbok och ändrar dess inbyggda dokumentegenskap som heter language. Se [utdata Excel-fil](64716891.xlsx) genererad av koden och skärmdumpen som visar det modifierade språkvärdet med [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) egenskapen.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
