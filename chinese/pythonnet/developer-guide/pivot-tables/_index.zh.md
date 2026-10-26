---
title: 插入数据透视表
linktitle: 插入数据透视表
description: 使用 Aspose.Cells for Python via .NET 创建数据透视表并设置其格式。
keywords: 创建数据透视表, 插入数据透视表, 设置数据透视表格式.
type: docs
weight: 160
url: /zh/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报表：无需任何公式，即可将大量逐行排列的原始数据压缩为紧凑的矩阵。您可以决定哪些列用作行标签、哪些列用作列标签，以及哪些列作为值进行聚合——分组和计算均由数据透视表完成：
- **汇总** — 按产品、地区或季度统计销售总额，取代冗长的公式链。
- **比较** — 将类别置于行、期间置于列，可将扁平列表转换为交叉报表，从而一目了然地查看趋势。
- **下钻** — 双击任意汇总值，查看该值所对应的源数据行。
- **刷新** — 源数据发生变化时，只需刷新一次即可重新计算整个报表。
典型应用场景包括销售仪表板、费用细分分析和库存分析——任何类似于“如何按类别和时间细分这些数字？”之类的问题。Aspose.Cells for Python via .NET 可以以编程方式创建同类数据透视表，使应用程序生成的工作簿能够直接包含现成的报表，而不仅仅是原始数据。

### **数据透视表对象模型**
Aspose.Cells for Python via .NET 在 [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) 命名空间中提供了一组专门用于创建和控制数据透视表的类。这些类用于创建和配置 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) 对象，这些对象是构成数据透视表的基本单元。具体包括：
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) 表示 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) 中的字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) 表示 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 中所有 [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 表示工作表中的数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) 表示工作表中所有 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 对象的集合。

### **使用 Aspose.Cells 创建简单数据透视表**
创建数据透视表包括三个步骤：将源数据写入工作表单元格、在目标位置添加数据透视表，以及将数据透视字段放入行区域、列区域和数据区域。
1. 使用 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 对象的 [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) 方法将数据添加到工作表。该数据将用作数据透视表的数据源。
2. 调用 [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) 集合的 [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) 方法，将数据透视表添加到工作表：`add(source_data, row, column)`。`source_data` 是源区域（例如，“A1:C8”）；`row` 和 `column` 是数据透视表左上角目标单元格的坐标，均从 0 开始计数（单元格 E3 表示行索引 2、列索引 4）。该方法直接返回新的 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 对象。
3. 使用 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 对象的 `add_field_to_area` 方法将数据透视字段添加到相应区域：字段名称进入行区域（`PivotFieldType.ROW`）、列区域（`PivotFieldType.COLUMN`）或数据区域（`PivotFieldType.DATA`）。
4. 保存工作簿——保存后，数据透视表即会写入文件。
执行示例代码后，工作表中将添加一个数据透视表。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# 创建一个新工作簿并获取第一个工作表
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# 写入源数据：按运动和季度统计的销售额
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# 在目标单元格 E3 添加数据透视表，源数据为 A1:C8
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# 分配透视字段：将 Sport 放入行区域，将 Quarter 放入列区域，将 Sales 放入数据区域
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# 保存工作簿
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
将单元格区域指定为数据源时，该区域必须从左上角延伸到右下角。例如，“A1:C3”有效，但“C3:A1”无效。
{{% /alert %}}

## 相关文章
- [在 Aspose.Cells for Python via .NET 中为数据透视表添加筛选字段](/cells/zh/python-net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Python via .NET 中为数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/python-net/change-page-field-layout/)
- [按标签或值筛选数据透视表](/cells/zh/python-net/filter-by-label-or-value-of-pivot-table/)
- [在 Aspose.Cells for Python via .NET 中管理数据透视表值字段](/cells/zh/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}