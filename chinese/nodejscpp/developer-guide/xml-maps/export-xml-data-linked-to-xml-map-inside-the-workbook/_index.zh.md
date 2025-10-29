---
title: 利用 C++ 和 Node.js 导出与 XML 映射关联的 XML 数据到 Excel 工作簿中
linktitle: 导出工作簿中与 XML 地图关联的 XML 数据
type: docs
weight: 20
url: /zh/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 导出工作簿中与 XML 映射关联的 XML 数据。 
---

## **导出链接到工作簿中的 XML 映射的 XML 数据**

请使用[**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-)方法导出工作簿内与XML映射相关联的XML数据。以下示例代码逐个导出所有XML映射的XML数据。请查看此代码中使用的【示例Excel文件】(5115497.xlsx) 和【第一个XML映射导出的XML数据】(5472487.xml)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
