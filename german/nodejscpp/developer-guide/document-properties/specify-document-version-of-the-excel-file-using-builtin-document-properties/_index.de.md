---  
title: Dokumentversion der Excel Datei mit eingebauten Dokumenteigenschaften mit Node.js via C++ festlegen  
linktitle: Festlegen der Dokumentversion der Excel Datei unter Verwendung eingebauter Dokumenteigenschaften  
type: docs  
weight: 20  
url: /de/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Erfahren Sie, wie Sie die Dokumentversion einer Excel Datei programmatisch mit eingebauten Dokumenteigenschaften mit Node.js via C++ angeben.  
---  

## **Mögliche Verwendungsszenarien**  

Sie können die **Versionsnummer** einer Excel-Datei ändern, indem Sie mit der rechten Maustaste auf die Datei klicken, Eigenschaften > Details auswählen und dann das Feld **Versionsnummer** bearbeiten. Bitte verwenden Sie die [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--)-Eigenschaft, um sie programmatisch mit Aspose.Cells APIs zu ändern.  

## **Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften**  

Der folgende Beispielcode erstellt eine Arbeitsmappe und ändert deren eingebauten Dokumenteigenschaften, einschließlich Titel, Autoren und Versionsnummer. Bitte sehen Sie sich die [Ausgabedatei](64716811.xlsx) und den Screenshot an, der die geänderte Versionsnummer mit der [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--)-Eigenschaft zeigt.  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Beispielcode**  

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

