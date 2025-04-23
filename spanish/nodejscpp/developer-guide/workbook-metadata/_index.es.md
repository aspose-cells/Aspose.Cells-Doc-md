---  
title: Uso de WorkbookMetadata con Node.js a través de C++  
linktitle: Metadatos del libro de trabajo  
type: docs  
weight: 320  
url: /es/nodejs-cpp/using-workbookmetadata/  
description: Aprende cómo editar los metadatos del libro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells te permite cargar una versión ligera de un libro en memoria para editar su información de metadatos. Usa la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) para cargar el libro.  
{{% /alert %}}  

El siguiente código de ejemplo usa la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) para editar propiedades personalizadas de documentos de un libro. Una vez que abra el libro usando la clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), podrá leer las propiedades del documento. Aquí hay un código de ejemplo usando la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open Workbook metadata
const options = new AsposeCells.MetadataOptions(AsposeCells.MetadataType.Document_Properties);
const meta = new AsposeCells.WorkbookMetadata(path.join(dataDir, "Sample1.xlsx"), options);

// Set some properties
meta.getCustomDocumentProperties().add("test", "test");

// Save the metadata info
meta.save(path.join(dataDir, "Sample2.out.xlsx"));

// Open the workbook
const w = new AsposeCells.Workbook(path.join(dataDir, "Sample2.out.xlsx"));

// Read document property
console.log(w.getCustomDocumentProperties().get("test"));

console.log("Press any key to continue...");
```  

