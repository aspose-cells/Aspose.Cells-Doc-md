---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 学习如何使用 Aspose.Cells for Python via Java 控制数据透视表中页面字段区域的布局，包括设置数据透视表顶部页面字段的显示顺序、换行数量和字段顺序。
keywords: Aspose.Cells for Python via Java, Python Java 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数量, 移动页面字段
type: docs
weight: 191
url: /zh/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本文是 **Add Page Field in Pivot Table** 主题的延续。文章演示如何控制页面字段区域的布局——即数据透视表顶部的筛选控件条，包括显示顺序、换行数量和字段重排序。
{{% /alert %}}
## **简介**
Microsoft Excel 中的数据透视表在表格的行/列/数据主体之上设置了一个专用的**页面字段区域**。该区域呈现为一行下拉筛选控件条（每个页面字段对应一个），用户可以点击它来按年份或区域等条件对数据进行切片。Aspose.Cells for Python via Java 通过 `pivot_table.page_fields` 集合建模该区域，并提供三个属性来控制该控件条的视觉布局：
- `pivot_table.page_field_order`（一个 `Aspose.Cells.PrintOrderType` 枚举值）决定其他页面字段是放置在现有字段的*旁边*还是*下方*。
- `pivot_table.page_field_wrap_count` 设置每行或每列放置多少个页面字段后再换行。
- `pivot_table.page_fields.move(curr_index, dest_index)` 在不改变顺序模式的前提下重排页面字段。
本文通过三个代码示例演示在共享数据集上分别执行这些操作，方便您并排比较生成的布局效果。
## **源数据**
下方所有三个示例均将这八行销售数据加载到一个名为 `PivotData` 的工作表中。数据包含两个页面字段候选（`Year`、`Region`）、一个行字段候选（`Fruit`）和一个度量字段（`Amount`），便于检查页面字段条的布局效果。
每个代码示例中均按相同顺序填充所有八个数据行，因此各场景之间的源数据始终一致——只有页面字段布局属性有所不同。
## **示例 1：先行后列 (Over Then Down)**
在第一个场景中，我们将两个页面字段（`Year`、`Region`）配置为在数据透视表顶部**以单行并排显示**。我们将 `Fruit` 分配到行轴，将 `Year` 放在页面轴的第一位、`Region` 放在第二位（`add_field_to_area` 调用的顺序决定起始索引），将 `Amount`（Sum）作为数据字段，然后将 `page_field_order` 设置为 `PrintOrderType.OVER_THEN_DOWN`，并将 `page_field_wrap_count` 设为 `2`。在 `OVER_THEN_DOWN` 与换行数量为 2 的组合下，两个页面字段在数据透视表顶部以单行水平并排呈现，因此该控件条占据一行两列的宽度。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# 表头（第 0 行）
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# 第 1 行：Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# 第 2 行：Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# 第 3 行：Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# 第 4 行：Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# 第 5 行：Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# 第 6 行：Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# 第 7 行：Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# 第 8 行：Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# 添加 PivotTableReport 工作表
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# 创建数据源为 PivotData!A1:D9 的数据透视表，放置在 PivotTableReport 的 A1 位置
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# 添加字段
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # 水果
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # 年份
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # 地区
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # 金额
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# 配置页面字段区域布局：先横向放置页面字段，每 2 个换行
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# 刷新并计算
pivotTable.calculateData()

# 保存
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **示例 2：先列后行 (Down Then Over)**
在本示例中，我们将 `Fruit` 放在行轴，将 `Year` 和 `Region` 放在页面轴（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全相同。然后将 `page_field_order` 设置为 `PrintOrderType.DOWN_THEN_OVER`，并将 `page_field_wrap_count` 设为 `2`。在 `DOWN_THEN_OVER` 与换行数量为 2 的组合下，两个页面字段垂直堆叠——`Year` 在上方，`Region` 正下方——在数据透视表顶部形成单列。因此该控件条占据两行一列的高度，与示例 1 相反。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **示例 3：移动页面字段**
在第三个场景中，我们沿用该数据集与字段分配，设置一个中性布局（`OVER_THEN_DOWN`，换行数量为 `2`），然后演示 `page_fields.move` 操作。`move(0, 1)` 调用将索引 0 处的页面字段（`Year`）移动到位置 1，原本位于位置 1 的页面字段（`Region`）则移至位置 0。调用后，`Region` 成为第一个页面字段，`Year` 成为第二个。换行与顺序模式保持不变，因此该控件条仍然水平并排呈现——只是两个下拉框的顺序互换了。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **相关文章**
- [Add Page Field in Pivot Table](/cells/zh/python-java/add-page-field-in-pivot-table/) — 介绍如何向数据透视表添加页面字段的父级主题。
- [Row and Column Fields in Pivot Table](/cells/zh/python-java/row-and-column-fields/) — 介绍如何将字段分配到行轴和列轴，补充本文所示的页面轴操作。
- [Manage Value Fields in Pivot Table](/cells/zh/python-java/manage-value-fields/) — 介绍如何配置数据（值）区域，包括本文使用的 `SUM` 聚合方式。
- [Refresh Pivot Table](/cells/zh/python-java/refresh-pivot-table/) — 介绍 `refresh_data` 与 `calculate_data`，在重排页面字段后需要调用它们。
- [Apply Style to Pivot Table](/cells/zh/python-java/apply-style-to-pivot-table/) — 介绍在页面字段条布局确定后，如何为渲染后的数据透视表设置格式。
{{< app/cells/assistant language="python" >}}