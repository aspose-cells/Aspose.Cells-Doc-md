---
title: 插入数据透视表
linktitle: 插入数据透视表
description: 使用 Aspose.Cells for Node.js via C++ 创建并设置数据透视表的格式。
keywords: 创建数据透视表, 插入数据透视表, 格式化数据透视表.
type: docs
weight: 160
url: /zh/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报表：它无需使用任何公式，即可将大量逐行排列的原始数据压缩为紧凑的矩阵。您可以决定哪些列用作行标签、哪些列用作列标签，以及哪些列聚合为值——数据透视表负责分组和计算：
- **汇总**——按产品、区域或季度汇总销售总额，无需使用冗长的公式链。
- **比较**——将类别置于行中、时间段置于列中，可将平面列表转换为交叉报表，使趋势一目了然。
- **下钻**——双击任意汇总值，即可查看其对应的源数据行。
- **刷新**——源数据发生变化后，只需刷新一次即可重新计算整个报表。
常见应用场景包括销售仪表板、费用细分和库存分析——可回答任何类似“这些数字如何按类别和时间细分？”的问题。借助 Aspose.Cells for Node.js via C++，您可以以编程方式构建同类数据透视表，使应用程序生成的工作簿能够包含现成的报表，而不只是原始数据。

### **数据透视表对象模型**
Aspose.Cells for Node.js via C++ 提供了一组用于创建和管理数据透视表的专用类。这些类用于创建和设置 [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 对象，而 PivotTable 对象是数据透视表的基本构建单元。相关对象包括：
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) 表示 [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 中的一个字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) 表示 [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 中所有 [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 表示工作表上的一个数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) 表示工作表上所有 [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 对象的集合。

### **使用 Aspose.Cells 创建简单数据透视表**
创建数据透视表的过程包括三个主要步骤：将源数据写入工作表单元格、在目标位置添加数据透视表，以及将数据透视字段放入行、列和数据区域，最后保存工作簿。
1. 使用 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 对象的 [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) 方法将数据添加到工作表。该数据将用作数据透视表的数据源。
2. 通过调用 [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) 集合的 [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) 方法，将数据透视表添加到工作表：`add(sourceData, row, column)`。`sourceData` 是源区域（例如"A1:C8"）；`row` 和 `column` 是数据透视表左上角目标单元格的从 0 开始的坐标（单元格 E3 对应行索引 2、列索引 4）。该方法直接返回新的 [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 对象。
3. 使用 [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 对象的 `addFieldToArea` 方法放置数据透视字段：将字段名称添加到行区域（`PivotFieldType.Row`）、列区域（`PivotFieldType.Column`）或数据区域（`PivotFieldType.Data`）。
4. 保存工作簿，即可将数据透视表写入文件。
执行示例代码后，工作表中将添加数据透视表。

```javascript
const AsposeCells = require("aspose.cells.node");

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

// 指定数据透视字段：将 Sport 放置在行区域，将 Quarter 放置在列区域，将 Sales 放置在数据区域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// 保存工作簿
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
将单元格区域指定为数据源时，该区域必须从左上角延伸至右下角。例如，"A1:C3"有效，而"C3:A1"无效。
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}