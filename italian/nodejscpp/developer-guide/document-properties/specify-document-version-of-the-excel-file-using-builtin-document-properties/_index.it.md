---  
title: Specificare la versione del documento del file Excel usando Proprietà Documento Incorporate con Node.js via C++  
linktitle: Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato  
type: docs  
weight: 20  
url: /it/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Impara come specificare la versione del documento di un file Excel programmaticamente utilizzando le proprietà documento incorporate con Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Puoi cambiare il **Numero di versione** di un file Excel facendo clic destro sul file e selezionando Proprietà > Dettagli e modificando il campo **Numero di versione**. Usa la proprietà [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) per cambiarlo programmaticamente usando le API Aspose.Cells.  

## **Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato**  

Il codice di esempio seguente crea un workbook e ne modifica le proprietà documento incorporate, inclusi Titolo, Autori e Numero di versione. Si prega di vedere il [file Excel di output](64716811.xlsx) generato dal codice e lo screenshot che mostra il numero di versione modificato tramite la proprietà [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Codice di Esempio**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
