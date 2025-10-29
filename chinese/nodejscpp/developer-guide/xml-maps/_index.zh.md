---
title: 通过Node.js和C++向Excel工作簿导入XML
linktitle: XML 映射
type: docs
weight: 210
url: /zh/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: 使用Aspose.Cells for Node.js via C++导入XML文件中的数据到Excel。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您使用 [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-) 方法导入工作簿内的XML映射。可以按照以下步骤在Microsoft Excel中导入XML映射：

- 选择** 开发人员** 选项卡
- 单击 **在 XML 部分导入** 并按照所需步骤操作。

您需要提供您的 XML 数据以完成导入。这里是一个[样本 XML 数据](5115037.txt)，您可以用于测试。

{{% /alert %}}

## **使用 Microsoft Excel 导入 XML 地图**

下面的截图显示如何使用 Microsoft Excel 导入 XML 地图。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **使用Aspose.Cells for Node.js via C++导入XML映射。**

以下示例代码展示了如何使用 [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-)。它可生成 [输出的 Excel 文件](5115036.xlsx)，如此截图所示。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## ** 高级主题**
- [ 使用 XmlMapCollection.add() 方法在工作簿内添加XML映射](/cells/zh/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [导出链接到工作簿中的 XML 映射的 XML 数据](/cells/zh/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [查找 XML 映射的根元素名称](/cells/zh/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [将单元格链接到 XML 地图元素](/cells/zh/nodejs-cpp/link-cells-to-xml-map-elements/)

{{< app/cells/assistant language="nodejs-cpp" >}}
