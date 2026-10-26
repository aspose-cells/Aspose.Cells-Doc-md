---
title: 插入数据透视表
linktitle: 插入数据透视表
description: 创建 Excel 电子表格文件中的数据透视表并设置其格式。
keywords: 创建数据透视表, 插入数据透视表, 设置数据透视表格式.
type: docs
weight: 160
url: /zh/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报表：无需使用任何公式，即可将大量逐行呈现的原始数据精简为紧凑的矩阵。您可以决定哪些列用作行标签、哪些列用作列标签，以及哪些列作为值进行聚合——数据透视表负责分组和计算：
- **汇总** — 按产品、地区或季度汇总销售总额，无需冗长的公式链。
- **比较** — 将类别置于行、将期间置于列，可将平面列表转换为交叉报表，一眼即可看出趋势。
- **钻取** — 双击任意汇总值，即可查看其对应的源行。
- **刷新** — 源数据发生变化时，只需刷新一次即可重新计算整个报表。
常见场景包括销售仪表板、费用明细分析和库存分析——对于“这些数字如何按类别和时间细分？”之类的问题，均可借助数据透视表来解决。Aspose.Cells for .NET 可通过编程创建同类数据透视表，因此应用程序生成的工作簿可以包含预先构建的报表，而不再仅包含原始数据。

### **数据透视表对象模型**
Aspose.Cells 在 [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) 命名空间中提供了一组专门用于创建和管理数据透视表的类。这些类用于创建和设置 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象，这些对象是构建数据透视表的基本组成部分。具体包括：
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) 表示 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 中的字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) 表示 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 中所有 [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 表示工作表上的数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) 表示工作表上所有 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象的集合。

### **使用 Aspose.Cells 创建简单数据透视表**
创建数据透视表的过程包括：将源数据写入工作表单元格、在目标位置添加数据透视表，以及将数据透视字段放入行区域、列区域和数据区域。
1. 使用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 对象的 [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法将数据添加到工作表。该数据将用作数据透视表的数据源。
2. 调用 [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) 集合的 [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) 方法，将数据透视表添加到工作表：`Add(sourceData, row, column)`。`sourceData` 是源区域（例如，“A1:C8”）；`row` 和 `column` 分别是数据透视表左上角目标单元格的行索引和列索引（从 0 开始；例如，单元格 E3 表示行索引 2、列索引 4）。该方法直接返回新创建的 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象。
3. 使用 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象的 `AddFieldToArea` 方法将数据透视字段添加到相应区域：字段名称可添加到行区域（`PivotFieldType.Row`）、列区域（`PivotFieldType.Column`）或数据区域（`PivotFieldType.Data`）。
4. 保存工作簿——数据透视表将写入保存的文件。
执行示例代码后，工作表中将添加一个数据透视表。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建一个新的工作簿并获取第一个工作表
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// 写入源数据：按运动项目划分的各季度销售额
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// 在目标单元格 E3 处添加数据透视表，数据源为 A1:C8
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// 分配透视字段：将“Sport”添加到行区域，将“Quarter”添加到列区域，将“Sales”添加到数据区域
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// 保存工作簿
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
将单元格区域指定为数据源时，该区域必须从左上角延伸到右下角。例如，“A1:C3”有效，而“C3:A1”无效。
{{% /alert %}}

## 相关文章
- [在 Aspose.Cells for .NET 中向数据透视表添加筛选字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .NET 中为数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/net/change-page-field-layout/)
- [按标签或值筛选数据透视表](/cells/zh/net/filter-by-label-or-value-of-pivot-table/)
- [在 Aspose.Cells for .NET 中管理数据透视表值字段](/cells/zh/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}