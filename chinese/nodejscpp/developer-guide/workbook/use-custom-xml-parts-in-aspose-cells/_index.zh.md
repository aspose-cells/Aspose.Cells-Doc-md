---
title: 在 Node.js 通过 C++ 使用自定义 XML 部件
linktitle: 在Aspose.Cells中使用自定义XML部件
type: docs
weight: 390
url: /zh/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: 学习如何在 Aspose.Cells for Node.js via C++ 中使用自定义 XML 部件。无缝集成外部 XML 数据到 Excel 文件。
--- 

## 在Aspose.Cells中使用自定义XML部件

自定义 XML 部件是由不同应用程序（如 SharePoint）存储在 Excel 文件中的 XML 数据。该数据被需要使用它的应用程序所使用。微软 Excel 不利用此数据，因此没有界面添加。可以通过将 **.xlsx** 扩展名更改为 **.zip** ，并用 **WinZip** 打开查看。也可以用任何第三方 Windows 压缩工具如 WinRAR 或 WinZip 打开 ZIP 文件。数据存放在 **customXml** 文件夹内。

你可以通过调用[**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/)方法，使用Aspose.Cells添加自定义XML部分。

以下示例代码使用 [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) 方法，添加了 **Book Catalog XML**，其名称为 **BookStore**。下图显示了这段代码的效果。可以看到，Book Catalog XML 被添加到名为 BookStore 的节点内。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## 使用 Node.js 通过 C++ 处理自定义 XML 部件的代码示例

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## 相关文章

- [在文档信息面板中可见的自定义属性](/cells/zh/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
