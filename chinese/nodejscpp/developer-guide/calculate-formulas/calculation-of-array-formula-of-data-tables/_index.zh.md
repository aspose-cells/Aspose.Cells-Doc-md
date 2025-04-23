---
title: 使用C++的Node.js计算数据表数组公式
linktitle: 数据表的数组公式计算
description: 如何使用Aspose.Cells库对Microsoft Excel中的数据表数组公式进行计算。加载或创建Excel文件，计算数组公式，然后保存修改后的文件。
keywords: Aspose.Cells，Excel，数据表，数组公式，计算，Node.js通过C++
type: docs
weight: 70
url: /zh/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

你可以在Microsoft Excel中通过数据 > 假设分析 > 数据表创建数据表……。Aspose.Cells现支持计算数据表的数组公式。请正常使用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)以计算任何类型的公式。

{{% /alert %}}

在以下示例代码中，我们使用了[source excel file](5115535.xlsx)。如果您将单元格B1的值更改为100，则填充为黄色的数据表的值将变为120，如下图所示。 示例代码生成了[output PDF](5115538.pdf)。

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

以下是用于从[source excel file](5115535.xlsx)生成[output PDF](5115538.pdf)的示例代码。 请阅读注释以获取更多信息。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
