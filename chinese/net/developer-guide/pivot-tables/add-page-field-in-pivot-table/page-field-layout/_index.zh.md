---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 学习如何使用 Aspose.Cells for .NET 控制数据透视表中页面字段区域的布局，包括设置数据透视表顶部页面字段的显示顺序、换行数量和字段顺序。
keywords: Aspose.Cells, .NET 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数量, 移动页面字段
type: docs
weight: 191
url: /zh/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

本文是 **在数据透视表中添加页面字段** 主题的延续。本文演示如何控制页面字段区域的布局——即数据透视表顶部的一排筛选器控件，包括显示顺序、换行数量和字段重排序。

{{% /alert %}}

## **介绍**

Microsoft Excel 中的数据透视表提供了一个专用的**页面字段区域**，位于数据透视表的行/列/数据主体之上。该区域以一排下拉筛选控件的形式呈现（每个页面字段对应一个控件），终端用户通过单击这些控件来按年份或区域等条件对数据透视表进行切片。Aspose.Cells 通过 `PivotTable.PageFields` 集合对该区域进行建模，并公开三个属性来控制该条带的可视化布局：

- `PivotTable.PageFieldOrder`（一个 `Aspose.Cells.PrintOrderType` 值）决定附加的页面字段是放置在现有字段*旁边*还是放置在现有字段*下方*。
- `PivotTable.PageFieldWrapCount` 设置在换行之前每行或每列放置的页面字段数量。
- `PivotTable.PageFields.Move(currIndex, destIndex)` 用于在不更改排序模式的情况下重新排序页面字段。

本文将逐步介绍三个代码示例，每个示例演示上述操作在共享数据集上的应用，便于您并排比较生成的布局。

## **源数据**

下面的所有三个示例均将这八行销售数据加载到名为 `PivotData` 的工作表中。数据包含两个页面字段候选（`Year`、`Region`）、一个行字段候选（`Fruit`）和一个度量（`Amount`），这使得检查页面字段条带具有实际意义。

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

在每个代码示例中均按相同顺序填充全部八行，因此各场景之间的源数据始终相同——只有页面字段布局属性会有所不同。

## **示例 1：先行后列**

在第一个场景中，我们将两个页面字段（`Year`、`Region`）配置为在数据透视表顶部**以单行并排**方式显示。我们将 `Fruit` 分配到行轴，按顺序将 `Year` 放在页面轴的第一位、将 `Region` 放在第二位（`AddFieldToArea` 调用的顺序决定起始索引），将 `Amount`（Sum）添加为数据字段，然后将 `PageFieldOrder` 设置为 `PrintOrderType.OverThenDown`，并将 `PageFieldWrapCount` 设为 `2`。使用 `OverThenDown` 且换行数量为 2 时，两个页面字段会在数据透视表顶部以单行横向并排方式布局，因此该条带占用一行（宽度为 2）的空间。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// 表头（第 0 行）
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// 第 1 行：Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// 第 2 行：Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// 第 3 行：Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// 第 4 行：Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// 第 5 行：Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// 第 6 行：Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// 第 7 行：Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// 第 8 行：Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// 添加 PivotTableReport 工作表
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// 创建数据源为 PivotData!A1:D9 的透视表，放置在 PivotTableReport 的 A1 单元格
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// 添加字段
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // 水果
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // 年份
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // 区域
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // 金额
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// 配置页面字段区域布局：先横向排列页面字段，每 2 个换行
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// 刷新并计算
pivotTable.CalculateData();

// 保存
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **示例 2：先列后行**

在本示例中，我们将 `Fruit` 放在行轴上，将 `Year` 和 `Region` 放在页面轴上（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全相同。然后将 `PageFieldOrder` 设置为 `PrintOrderType.DownThenOver`，并将 `PageFieldWrapCount` 设为 `2`。使用 `DownThenOver` 且换行数量为 2 时，两个页面字段会垂直堆叠——`Year` 在顶部，`Region` 正下方——在数据透视表顶部形成单列。因此该条带占用两行（宽度为 1）的空间，与示例 1 形成对比。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **示例 3：移动页面字段**

在第三个场景中，我们保留相同的数据集和字段分配，并设置一个中性布局（`OverThenDown`，换行数量为 `2`），然后演示 `PageFields.Move` 操作。`Move(0, 1)` 调用会将索引 0 处的页面字段（`Year`）移动到位置 1，原本位于位置 1 的页面字段（`Region`）则移至位置 0。在此次调用之后，`Region` 成为第一个页面字段，`Year` 成为第二个页面字段。换行数量和排序模式保持不变，因此该条带仍然以横向并排方式呈现——只是两个下拉框的顺序被互换了。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **相关文章**

- [在数据透视表中添加页面字段](/cells/zh/net/add-page-field-in-pivot-table/) — 介绍如何将页面字段添加到数据透视表的父页面。
- [数据透视表中的行和列字段](/cells/zh/net/pivot-table-add-row-and-column-fields/) — 介绍如何将字段分配到行轴和列轴，是对本文页面轴工作的补充。
- [管理数据透视表中的值字段](/cells/zh/net/manage-value-fields/) — 介绍如何配置数据（值）区域，包括本文中使用的 `Sum` 聚合。
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/) — 解释 `RefreshData` 和 `CalculateData`，这是在重新排序页面字段后所必需的。
- [将样式应用于数据透视表](/cells/zh/net/apply-style-to-pivot-table/) — 展示在布局完页面字段条带后如何对已呈现的数据透视表进行格式化。

{{< app/cells/assistant language="csharp" >}}