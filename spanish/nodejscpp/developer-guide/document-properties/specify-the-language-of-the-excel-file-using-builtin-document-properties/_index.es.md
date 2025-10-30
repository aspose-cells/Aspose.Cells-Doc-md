---
title: Especificar el Idioma del Archivo Excel usando Propiedades de Documento Incorporadas con Node.js a través de C++
linktitle: Especificar el idioma del archivo de Excel usando las propiedades de documento integradas
type: docs
weight: 30
url: /es/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Escenarios de uso posibles**

Puedes cambiar el idioma de un archivo Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y luego editando el campo Idioma. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) para cambiarlo programáticamente usando las API Aspose.Cells for Node.js via C++.

## **Especificar el idioma del archivo de Excel mediante propiedades de documento integradas**

El siguiente código de ejemplo crea un libro y cambia su propiedad de documento incorporada llamada idioma. Por favor, mira el [archivo Excel de salida](64716891.xlsx) generado por el código y la captura de pantalla que muestra el campo de idioma modificado por la propiedad [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

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
