---
title: 使用 C++ 和 Node.js 将单元格链接到 XML 映射元素
linktitle: 将单元格链接到 XML 地图元素
type: docs
weight: 50
url: /zh/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **可能的使用场景**

你可以使用 Aspose.Cells for Node.js via C++ 将单元格链接至 XML 映射元素。请使用 [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) 方法实现此目的。

## **将单元格链接到 XML 地图元素**

以下示例代码加载了包含 XML 地图的 [源 Excel 文件](5115471.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在 [输出 Excel 文件](5115467.xlsx) 中。

如果您打开 [输出 Excel 文件](5115467.xlsx) 并单击“开发人员 > 源”按钮，您将看到单元格已链接到 XML 地图元素，并且它们也将被 Microsoft Excel 标记，如下图所示。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
