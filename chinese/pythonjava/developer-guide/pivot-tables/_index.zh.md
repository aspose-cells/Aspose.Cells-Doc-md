---
title: 数据透视表
linktitle: 数据透视表
description: 使用 Aspose.Cells for Python via Java 创建数据透视表并设置其格式。
keywords: 创建数据透视表, 插入数据透视表, 设置数据透视表格式。
type: docs
weight: 160
url: /zh/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报告：无需任何公式，它便可将大量逐行排列的原始数据汇总为紧凑的矩阵。您可以决定哪些列用作行标签、哪些列用作列标签，以及哪些列用作值进行聚合——分组和计算均由数据透视表完成：
- **汇总** — 按产品、地区或季度汇总销售总额，无需使用冗长的公式链。
- **比较** — 将类别置于行中、时期置于列中，可将扁平列表转换为交叉分析报告，从而直观呈现趋势。
- **下钻** — 双击任意汇总值，即可查看其对应的源数据行。
- **刷新** — 源数据发生变化时，只需刷新一次即可重新计算整个报告。
常见场景包括销售仪表板、费用构成分析和库存分析——无论要回答“这些数字按类别和时间如何分解？”之类的问题。Aspose.Cells for Python via Java 支持以编程方式创建同类数据透视表，使您的应用程序生成的工作簿能够直接包含现成报告，而不只是原始数据。

### **数据透视表对象模型**
Aspose.Cells 提供一组用于创建和管理数据透视表的类。其基本组成部分如下：
- `PivotField` 表示 `PivotTable` 中的一个字段。
- `PivotFieldCollection` 表示 `PivotTable` 中所有 `PivotField` 对象的集合。
- `PivotTable` 表示工作表上的一个 `PivotTable`。
- `PivotTableCollection` 表示工作表上所有 `PivotTable` 对象的集合。

### **使用 Aspose.Cells 创建简单的数据透视表**
创建数据透视表的基本过程可分为三个步骤：将源数据写入工作表单元格，在目标位置添加数据透视表，然后将数据透视字段放入行区域、列区域和数据区域。
1. 使用单元格的 `putValue` 方法将数据添加到工作表中。该数据将作为数据透视表的数据源。
2. 通过调用 `PivotTables` 集合的 `add` 方法，将数据透视表添加到工作表：`add(sourceData, row, column)`。`sourceData` 表示源区域（例如，“A1:C8”）；`row` 和 `column` 表示数据透视表左上角目标单元格的基于 0 的坐标（单元格 E3 对应行索引 2、列索引 4）。该方法直接返回新的 `PivotTable` 对象。
3. 使用 `PivotTable` 对象的 `addFieldToArea` 方法放置数据透视字段：将字段名称放入行区域（`PivotFieldType.ROW`）、列区域（`PivotFieldType.COLUMN`）或数据区域（`PivotFieldType.DATA`）。
4. 保存工作簿——数据透视表将写入保存的文件。
执行示例代码后，工作表中将添加一个数据透视表。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# 创建一个新的工作簿并获取第一个工作表
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# 写入源数据：按运动和季度统计的销售额
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# 在目标单元格 E3 处添加数据透视表，数据源为 A1:C8
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# 分配数据透视字段：将 Sport 放入行区域，将 Quarter 放入列区域，将 Sales 放入数据区域
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# 保存工作簿
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
将单元格区域用作数据源时，该区域必须从左上角延伸到右下角。例如，“A1:C3”是有效的，而“C3:A1”无效。
{{% /alert %}}

## 相关文章
- [在 Aspose.Cells for Python via Java 中将筛选字段添加到数据透视表](/cells/zh/python-java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Python via Java 中为数据透视表应用样式](/cells/zh/python-java/apply-style-to-pivot-table/)
- [修改数据透视表中的页字段布局](/cells/zh/python-java/change-page-field-layout/)
- [按标签或值筛选数据透视表](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)
- [在 Aspose.Cells for Python via Java 中管理数据透视表值字段](/cells/zh/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}