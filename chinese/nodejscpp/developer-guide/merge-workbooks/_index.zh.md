---
title: 通过Node.js和C++将多个工作簿合并为一个工作簿
linktitle: 工作簿合并器
type: docs
weight: 66
url: /zh/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: 学习如何使用Aspose.Cells for Node.js via C++将多个工作簿合并为一个工作簿。 
---

{{% alert color="primary" %}}

有时，你需要将包含图片、图表和数据等不同内容的多个工作簿合并成一个。Aspose.Cells for Node.js via C++支持此功能。本文展示如何创建控制台应用程序，只需几行简单的代码即可使用Aspose.Cells合并工作簿。

{{% /alert %}}

## **将具有图像和图表的工作簿合并**

示例代码结合了两个工作簿到一个工作簿，使用Aspose.Cells for Node.js via C++。代码加载源工作簿，使用[**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-)方法合并它们，并保存输出工作簿。

### **源工作簿**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **输出工作簿**

- [combined.xlsx](5473095.xlsx)

### **屏幕截图**

以下是源和输出工作簿的屏幕截图。

{{% alert color="primary" %}}

您可以使用任何源工作簿。这些图像仅用于说明目的。

{{% /alert %}}

**图表工作簿的第一个工作表 - 堆叠** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**图表工作簿的第二个工作表 - 折线** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**图片工作簿的第一个工作表 - 图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**组合工作簿中的三个工作表 - 堆叠、线条、图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **高级主题**
- [将多个工作表合并成一个工作表](/cells/zh/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [合并文件](/cells/zh/nodejs-cpp/merge-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
