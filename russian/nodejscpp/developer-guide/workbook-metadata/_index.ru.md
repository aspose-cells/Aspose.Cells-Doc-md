---  
title: Использование WorkbookMetadata с Node.js через C++  
linktitle: Метаданные книги  
type: docs  
weight: 320  
url: /ru/nodejs-cpp/using-workbookmetadata/  
description: Узнайте, как редактировать метаданные книги, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells позволяет загружать легкую версию книги в память для редактирования метаданных. Пожалуйста, используйте класс [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) для загрузки книги.  
{{% /alert %}}  

Следующий пример кода использует класс [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) для редактирования пользовательских свойств документа книги. После открытия книги с помощью класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), вы сможете читать свойства документа. Вот пример использования класса [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata).  

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
