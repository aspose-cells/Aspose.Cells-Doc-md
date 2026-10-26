---
title: 插入数据透视表
linktitle: 插入数据透视表
description: 使用 Aspose.Cells for Node.js via Java 创建 Excel 电子表格文件中的数据透视表并设置其格式。
keywords: 创建数据透视表, 插入数据透视表, 设置数据透视表格式, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /zh/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报告：无需任何公式，即可将大量逐行排列的原始数据压缩为紧凑矩阵。您可以决定哪些列作为行标签、哪些列作为列标签，以及哪些列作为值进行聚合——分组和计算均由数据透视表完成：
- **汇总** — 按产品、地区或季度统计销售总额，无需冗长的公式链。
- **比较** — 将类别置于行、将期间置于列，可将扁平列表转换为交叉报表，从而一眼看清趋势。
- **下钻** — 双击任一汇总值，即可查看其对应的源数据行。
- **刷新** — 源数据发生变化时，只需刷新一次即可重新计算整个报告。
常见应用场景包括销售仪表板、费用明细分析和库存分析——适用于“这些数字如何按类别和时间细分？”之类的问题。Aspose.Cells for Node.js via Java 可通过编程方式构建相同的数据透视表，因此应用程序生成的工作簿能够包含现成的报告，而不仅是原始数据。

### **数据透视表对象模型**
Aspose.Cells 提供了一组用于创建和控制数据透视表的类。其基本组成部分如下：
- `PivotField` 表示 `PivotTable` 中的一个字段。
- `PivotFieldCollection` 表示 `PivotTable` 中所有 `PivotField` 对象的集合。
- `PivotTable` 表示工作表上的一个数据透视表。
- `PivotTableCollection` 表示工作表上所有 `PivotTable` 对象的集合。

### **使用 Aspose.Cells 创建简单数据透视表**
创建数据透视表的过程如下：将源数据写入工作表单元格、在目标位置添加数据透视表，以及将数据透视字段放入行区域、列区域和数据区域。
1. 使用单元格的 `putValue` 方法将数据添加到工作表。该数据将用作数据透视表的数据源。
2. 调用 `PivotTables` 集合的 `add` 方法，将数据透视表添加到工作表：`add(sourceData, row, column)`。`sourceData` 是源区域（例如 "A1:C8"）；`row` 和 `column` 分别是数据透视表左上角目标单元格的行索引和列索引（均从 0 开始；单元格 E3 对应第 2 行、第 4 列）。该方法直接返回新的 `PivotTable` 对象。
3. 使用 `PivotTable` 对象的 `addFieldToArea` 方法放置数据透视字段：将字段名称放入行区域（`PivotFieldType.ROW`）、列区域（`PivotFieldType.COLUMN`）或数据区域（`PivotFieldType.DATA`）。
4. 保存工作簿——数据透视表将写入已保存的文件。
执行示例代码后，工作表中将添加一个数据透视表。

```javascript
const AsposeCells = require("aspose.cells");

// 创建一个新的工作簿并获取第一个工作表
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// 写入源数据：按运动项目和季度统计的销售额
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// 在目标单元格 E3 处添加数据透视表，数据源为 A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// 设置透视字段：将 Sport 放置到行区域，将 Quarter 放置到列区域，将 Sales 放置到数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// 保存工作簿
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
将单元格区域指定为数据源时，该区域必须从左上角延伸到右下角。例如，"A1:C3" 有效，而 "C3:A1" 无效。
{{% /alert %}}

## 相关文章
- [使用 Aspose.Cells for Node.js via Java 向数据透视表添加筛选字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [使用 Aspose.Cells for Node.js via Java 为数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/nodejs-java/change-page-field-layout/)
- [按标签或值筛选数据透视表](/cells/zh/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [使用 Aspose.Cells for Node.js via Java 管理数据透视表值字段](/cells/zh/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}