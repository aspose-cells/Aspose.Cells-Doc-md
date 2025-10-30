---
title: Sprache der Excel Datei mit eingebauten Dokumenteigenschaften mit Node.js via C++ festlegen
linktitle: Festlegen der Sprache der Excel Datei unter Verwendung eingebauter Dokumenteigenschaften
type: docs
weight: 30
url: /de/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Mögliche Verwendungsszenarien**

Sie können die Sprache einer Excel-Datei ändern, indem Sie mit der rechten Maustaste auf die Datei klicken, Eigenschaften > Details auswählen und dann das Feld Sprache bearbeiten. Bitte verwenden Sie die [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--)-Eigenschaft, um sie programmatisch mit Aspose.Cells for Node.js via C++ APIs zu ändern.

## **Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften**

Der folgende Beispielcode erstellt eine Arbeitsmappe und ändert die eingebaute Dokumenteigenschaft namens Sprache. Bitte sehen Sie sich die [Ausgabedatei](64716891.xlsx) und den Screenshot an, der das geänderte Sprachfeld mit der [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--)-Eigenschaft zeigt.

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Beispielcode**

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
