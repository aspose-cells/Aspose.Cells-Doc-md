---
title: 通过Node.js和C++管理分页符
linktitle: 管理分页
type: docs
weight: 30
url: /zh/nodejs-cpp/managing-page-breaks/
description: 本文提供示例代码，并说明如何以编程方式在Excel工作表中添加、清除或删除特定的分页符，使用Aspose.Cells for Node.js via C++。
keywords: 分页符Node.js via C++，Excel分页符Node.js via C++，清除分页符Node.js via C++，删除特定分页符Node.js via C++
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

分页符添加在单元格位置后，页面结束并在打印时分页符后的数据打印在下一页。简单地说，分页符根据您的设定将工作表分成多页。您还可以在运行时使用 Aspose.Cells 添加分页符。Aspose.Cells 允许开发人员添加两种分页符：

- 水平分页
- 垂直分页

在接下来的讨论中，我们将描述如何使用Aspose.Cells向工作表添加水平或垂直分页。

{{% /alert %}}

## **分页**

Aspose.Cells 提供了一个代表 Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供了用于管理工作表的广泛的属性和方法。

要添加分页符，使用 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类的 [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) 和 [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) 属性。

[**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) 和 [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) 属性是可能包含多个分页符的集合。每个集合都包含用于管理水平和垂直分页符的几种方法。

### **添加分页**

要在工作表中添加分页符，在指定的单元格插入水平和垂直分页符，调用 [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) 和 [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-) 方法。每个 **add** 方法都接受要添加分页符的单元格名称。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

在分页预览或打印预览模式下，您可以看到这些分页符的工作方式。

{{% /alert %}}

### **移除特定的分页符**

要删除特定分页符，请调用[**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-)和[**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-)方法。每个**removeAt**方法都接受即将删除的分页符的索引。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **重要提示**

当你在分页设置中设置**fitToPages**属性（即[**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--)和[**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)）时，分页设置会受到影响，因此，如果你打印工作表，分页设置将不予考虑，尽管它们仍然被设置。
