---
title: 设置共享公式（Node.js + C++）
linktitle: 设置共享公式
type: docs
weight: 10
url: /zh/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

如果你想在工作表中添加一个函数，进行一些计算，本文解释了如何使用 Aspose.Cells for Node.js via C++ 实现此任务。

{{% /alert %}}

## 使用 Aspose.Cells for Node.js via C++ 设置共享公式

假设您有一个填充有数据的工作表，格式如下所示的样本工作表。

|**带单列数据的输入文件**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

您希望在B2中添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文介绍了如何使用Aspose.Cells应用此公式。

Aspose.Cells允许您使用[**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--)属性指定一个公式。有两种选项可用于将公式添加到列中的其他单元格（B3、B4、B5等等）。

或者像你为第一个单元格所做的那样，为每个单元格设置公式，并相应更新单元格引用（A3*0.09, A4*0.09, A5*0.09 等）。这需要逐行更新单元格引用，也需要 Aspose.Cells 逐个解析每个公式，对于大型表格或复杂公式会比较耗时，也会多出一些代码，虽然循环可以略微减少这些代码。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行的单元格引用，使得税款可以正确计算。这种[**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) 方法比第一种方法更有效。

以下示例演示了如何使用它。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
