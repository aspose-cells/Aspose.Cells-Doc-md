---  
title: Användning av WorkbookMetadata med Node.js via C++  
linktitle: Arbetsboksmetadata   
type: docs  
weight: 320  
url: /sv/nodejs-cpp/using-workbookmetadata/  
description: Lär dig hur man redigerar arbetsboksmetadata med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells låter dig ladda en lättviktig version av en arbetsbok i minnet för att redigera dess metadata. Använd [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) klassen för att ladda arbetsboken.  
{{% /alert %}}  

Följande exempel använder [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) klassen för att redigera anpassade dokumentegenskaper i en arbetsbok. När du har öppnat arbetsboken med [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen kan du läsa dokumentegenskaperna. Här är ett exempel på kod med [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)-klassen.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
