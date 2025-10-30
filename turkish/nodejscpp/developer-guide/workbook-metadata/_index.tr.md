---  
title: Node.js ile C++ kullanarak WorkbookMetadata kullanma  
linktitle: Çalışma Kitabı Meta Verisi  
type: docs  
weight: 320  
url: /tr/nodejs-cpp/using-workbookmetadata/  
description: Aspose.Cells for Node.js via C++ kullanılarak çalışma kitabı meta verisini düzenlemeyi öğrenin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, metaveri bilgilerini düzenlemek için hafif bir çalışma kitabı sürümünü belleğe yüklemenize olanak tanır. Lütfen çalışma kitabını yüklemek için [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) sınıfını kullanın.  
{{% /alert %}}  

Aşağıdaki örnek kod, bir çalışma kitabının özel belge özelliklerini düzenlemek için [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) sınıfını kullanır. Çalışma kitabını [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı kullanarak açtıktan sonra belge özelliklerini okuyabilirsiniz. İşte [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) sınıfını kullanarak örnek kod.  

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
