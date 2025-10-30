---  
title: Especificar la Versión del Documento del Archivo Excel usando Propiedades de Documento Incorporadas con Node.js a través de C++  
linktitle: Especificar la versión de documento del archivo de Excel usando las propiedades de documento integradas  
type: docs  
weight: 20  
url: /es/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Aprende cómo especificar la versión del documento de un archivo Excel programáticamente usando propiedades de documento incorporadas con Node.js a través de C++.  
---  

## **Escenarios de uso posibles**  

Puedes cambiar el **Número de versión** de un archivo Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y luego editando el campo **Número de versión**. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) para cambiarlo programáticamente usando las API de Aspose.Cells.  

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**  

El siguiente código de ejemplo crea un libro y cambia sus propiedades de documento incorporadas que incluyen Título, Autores y Número de versión. Por favor, mira el [archivo Excel de salida](64716811.xlsx) generado por el código y la captura de pantalla que muestra el Número de versión modificado por la propiedad [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Código de muestra**  

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
