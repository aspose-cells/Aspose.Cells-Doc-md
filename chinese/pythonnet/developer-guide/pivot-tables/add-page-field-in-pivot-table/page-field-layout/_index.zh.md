---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 学习如何使用 Aspose.Cells for Python via .NET 控制数据透视表中页面字段区域的布局，包括设置显示顺序、换行数以及数据透视表顶部页面字段的字段顺序。
keywords: Aspose.Cells, Python via .NET 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数, 移动页面字段
type: docs
weight: 191
url: /zh/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本文是 **向数据透视表中添加页面字段** 主题的延续。本文演示如何控制页面字段区域（即数据透视表顶部的筛选器控件条带）的布局，包括显示顺序、换行数和字段重排序。
{{% /alert %}}
## **简介**
在 Microsoft Excel 中，数据透视表暴露了一个专用的 **页面字段区域**，该区域位于表格的行/列/数据主体的上方。该区域被渲染为一组下拉筛选器控件（每个页面字段对应一个），终端用户通过点击这些控件可以按年份或区域等条件对数据透视表进行切片。Aspose.Cells for Python via .NET 通过 `pivot_table.page_fields` 集合对这一区域进行建模，并暴露三个属性用于控制该条带的可视化布局：
- `pivot_table.page_field_order`（一个 `PrintOrderType` 值）决定额外的页面字段是 *放置在现有字段旁边* 还是 *放置在现有字段下方*。
- `pivot_table.page_field_wrap_count` 设置每行或每列放置多少个页面字段后再换行。
- `pivot_table.page_fields.move(curr_index, dest_index)` 重排序页面字段而不改变排序模式。
本文通过三个代码示例演示每种操作，共用同一份数据集，以便您能够并排比较产生的布局差异。
## **源数据**
下面三个示例都将这八行销售数据加载到名为 `PivotData` 的工作表中。该数据包含两个页面字段候选项（`Year`、`Region`）、一个行字段候选项（`Fruit`）和一个度量值（`Amount`），便于检视页面字段条带。
在每个代码示例中，这八行数据均以相同的顺序填充，因此不同场景之间的源数据完全相同——只有页面字段的布局属性不同。
## **示例 1：先横后纵**
在第一种场景中，我们将两个页面字段（`Year`、`Region`）配置为在数据透视表顶部以 **单行水平并排** 的方式显示。我们将 `Fruit` 分配到行轴，将 `Year` 放置在页面的第一位、`Region` 放置在第二位（`add_field_to_area` 调用的顺序决定了起始索引），添加 `Amount`（Sum）作为数据字段，然后将 `page_field_order` 设置为 `PrintOrderType.OverThenDown`，并将 `page_field_wrap_count` 设为 `2`。在 `OverThenDown` 配合换行数为 2 时，两个页面字段将在数据透视表顶部单行水平并排显示，因此该条带占据一行宽度为二的区域。
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# 表头（第0行）
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# 第1行：Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# 第2行：Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# 第3行：Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# 第4行：Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# 第5行：Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# 第6行：Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# 第7行：Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# 第8行：Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# 添加 PivotTableReport 工作表
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# 创建数据源为 PivotData!A1:D9、放置在 PivotTableReport 的 A1 位置的数据透视表
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# 添加字段
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # 水果
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # 年份
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # 区域
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # 金额
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# 配置页面字段区域布局：先横向排列页面字段，每 2 个换行
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# 刷新并计算
pivot_table.calculate_data()

# 保存
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **示例 2：先纵后横**
在本示例中，我们将 `Fruit` 放在行轴上，`Year` 和 `Region` 放在页面轴上（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全相同。然后，我们将 `page_field_order` 设置为 `PrintOrderType.DownThenOver`，并将 `page_field_wrap_count` 设置为 `2`。在 `DownThenOver` 配合换行数为 2 时，两个页面字段将垂直堆叠——`Year` 在上，`Region` 紧接其下方——在数据透视表顶部形成单一列。因此，该条带占据两行宽度为一的区域，与示例 1 形成对比。
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **示例 3：移动页面字段**
在第三种场景中，我们保留相同的数据集和字段分配，设置一个中性布局（`OverThenDown`，换行数为 `2`），然后演示 `page_fields.move` 操作。`move(0, 1)` 调用将索引 0 处的页面字段（`Year`）移动到位置 1，而原本位于位置 1 的页面字段（`Region`）则移至位置 0。在此次调用之后，`Region` 成为第一个页面字段，`Year` 成为第二个。换行模式和顺序模式均未更改，因此该条带仍然以水平并排方式呈现——只是两个下拉框的顺序被交换了。
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **相关文章**
- [向数据透视表中添加页面字段](/cells/zh/python-net/add-page-field-in-pivot-table/) — 介绍如何向数据透视表中添加页面字段的父级页面。
- [数据透视表中的行字段和列字段](/cells/zh/python-net/row-and-column-fields/) — 涵盖将字段分配到行轴和列轴的方法，是对本文页面轴工作的补充。
- [管理数据透视表中的值字段](/cells/zh/python-net/manage-value-fields/) — 介绍如何配置数据（值）区域，包括本文使用的 `Sum` 聚合方式。
- [刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/) — 解释 `refresh_data` 和 `calculate_data`，这是在重排序页面字段之后必需执行的操作。
- [向数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/) — 介绍在页面字段条带布局完成之后，如何为渲染后的数据透视表进行格式设置。
{{< app/cells/assistant language="python-net" >}}