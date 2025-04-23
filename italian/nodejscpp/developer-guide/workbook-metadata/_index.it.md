---  
title: Utilizzo di WorkbookMetadata con Node.js tramite C++  
linktitle: Metadati del foglio di lavoro  
type: docs  
weight: 320  
url: /it/nodejs-cpp/using-workbookmetadata/  
description: Scopri come modificare i metadati del workbook usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells permette di caricare una versione leggera di una cartella di lavoro in memoria per modificare le sue informazioni metadata. Si prega di usare la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) per caricare la cartella di lavoro.  
{{% /alert %}}  

Il seguente esempio di codice usa la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) per modificare le proprietà personalizzate di un documento. Una volta aperta la cartella di lavoro usando la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), sarai in grado di leggere le proprietà del documento. Ecco un esempio di codice usando la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata).  

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

