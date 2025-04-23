---
title: 使用 C++ 和 Node.js 查找 XML 映射的根元素名
linktitle: 查找 XML 地图的根元素名称
type: docs
weight: 30
url: /zh/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 查找 Excel 中 XML 映射的根元素名。
---

## **可能的使用场景**

你可以使用 Aspose.Cells for Node.js via C++ 和 [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--) 属性找到 XML 映射的根元素名。下图显示了 Microsoft Excel 中 XML 映射的根元素名。

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **示例代码**

以下示例代码加载[示例 Excel 文件](55541789.xlsx)，访问第一个 XML 映射并打印其 [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--) 属性。请查看下面提供的控制台输出。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **控制台输出**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
