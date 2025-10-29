---  
title: 使用 Node.js 和 C++ 管理工作簿元数据  
linktitle: 工作簿元数据  
type: docs  
weight: 320  
url: /zh/nodejs-cpp/using-workbookmetadata/  
description: 学习如何使用Aspose.Cells for Node.js via C++编辑工作簿元数据。  
---  

{{% alert color="primary" %}}  
Aspose.Cells 允许你加载工作簿的轻量级版本以编辑其元数据信息。请使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) 类加载工作簿。  
{{% /alert %}}  

以下示例代码使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) 类编辑工作簿的自定义文档属性。打开工作簿后，便可读取文档属性。以下为使用 [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) 类的示例代码。  

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
