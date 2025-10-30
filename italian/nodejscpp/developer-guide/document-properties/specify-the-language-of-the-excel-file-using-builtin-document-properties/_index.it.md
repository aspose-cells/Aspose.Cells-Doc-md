---
title: Specificare la lingua del file Excel usando Proprietà Documento Incorporate con Node.js via C++
linktitle: Specificare la lingua del file Excel utilizzando le proprietà del documento integrato
type: docs
weight: 30
url: /it/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Possibili Scenari di Utilizzo**

Puoi cambiare la lingua di un file Excel facendo clic destro sul file e selezionando Proprietà > Dettagli e modificando il campo Lingua. Usa la proprietà [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) per cambiarlo programmaticamente usando le API Aspose.Cells for Node.js via C++.

## **Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate**

Il codice di esempio seguente crea un workbook e ne modifica la proprietà documento incorporata chiamata lingua. Si prega di vedere il [file Excel di output](64716891.xlsx) generato dal codice e lo screenshot che mostra il campo Lingua modificato tramite la proprietà [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Codice di Esempio**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
