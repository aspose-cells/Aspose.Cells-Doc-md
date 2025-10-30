---  
title: Verwendung von WorkbookMetadata mit Node.js über C++  
linktitle: Metadaten der Arbeitsmappe  
type: docs  
weight: 320  
url: /de/nodejs-cpp/using-workbookmetadata/  
description: Lernen, wie man Arbeitsmappen Metadaten mit Aspose.Cells for Node.js via C++ bearbeitet.  
---  

{{% alert color="primary" %}}  
Aspose.Cells ermöglicht das Laden einer leichten Version eines Arbeitsbuchs ins Speicher für die Bearbeitung seiner Metadaten. Bitte verwenden Sie die [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)-Klasse, um das Arbeitsbuch zu laden.  
{{% /alert %}}  

Der folgende Beispielcode verwendet die [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)-Klasse, um benutzerdefinierte Dokumenteigenschaften eines Arbeitsbuchs zu bearbeiten. Nachdem Sie das Arbeitsbuch mit der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse geöffnet haben, können Sie die Dokumenteigenschaften lesen. Hier ist ein Beispielcode mit der [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata)-Klasse.  

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
