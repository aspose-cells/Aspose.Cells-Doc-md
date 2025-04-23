---
title: 使用Node.js via C++在文档信息面板中添加可见的自定义属性
linktitle: 在文档信息面板中显示添加的自定义属性
type: docs
weight: 300
url: /zh/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: 学习如何使用Aspose.Cells for Node.js via C++向工作簿对象添加自定义属性。这些属性可以在文档信息面板中查看。
---

## **在文档信息面板中可见的自定义属性**

Aspose.Cells for Node.js via C++可用于在工作簿对象中添加自定义属性，这些属性在文档信息面板中可见。你可以在Microsoft Excel中通过File > Info > Properties > Show Document Panel菜单命令打开文档信息面板。

请使用 [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) 方法添加自定义属性，这些属性将在文档信息面板中显示。

以下示例代码添加了两个自定义属性，第一个没有设定类型，第二个设为日期时间类型。一旦打开由此代码生成的输出Excel文件，你会在文档信息面板中看到这两个属性。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **相关文章**

{{% alert color="primary" %}}

- [在Aspose.Cells中使用自定义XML部分](/cells/zh/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
