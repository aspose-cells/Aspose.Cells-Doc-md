---  
title: Using WorkbookMetadata with Node.js via C++  
linktitle: Workbook Metadata  
type: docs  
weight: 320  
url: /nodejs-cpp/using-workbookmetadata/  
description: Learn how to edit workbook metadata using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells allows you to load a light-weight version of a workbook into memory to edit its metadata information. Please use the [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) class to load the workbook.  
{{% /alert %}}  

The following sample code uses the [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) class to edit custom document properties of a workbook. Once you open the workbook using the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class, you will be able to read the document properties. Here is a sample code using the [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) class.  

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
process.stdin.once("data", () => {
    process.exit();
});
```  
  