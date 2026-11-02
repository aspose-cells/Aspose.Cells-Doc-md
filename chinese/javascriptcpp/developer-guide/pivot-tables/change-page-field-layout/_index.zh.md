---
title: 修改数据透视表中的页字段布局
linktitle: 修改数据透视表中的页字段布局
description: 了解如何使用 Aspose.Cells for JavaScript via C++ 控制数据透视表中的页字段区域布局，包括设置数据透视表顶部页字段的显示顺序、换行数和字段顺序。
keywords: Aspose.Cells for JavaScript via C++, 电子表格, 数据透视表, 页字段, 页字段顺序, 页字段换行数, 移动页字段
type: docs
weight: 191
url: /zh/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
本文是**在数据透视表中添加页字段**主题的延续。本文演示如何控制页字段区域的布局，即数据透视表顶部的筛选控件栏，包括显示顺序、换行数和字段重新排序。
{{% /alert %}}

## **简介**
Microsoft Excel 中的数据透视表提供专用的**页字段区域**，该区域位于数据透视表的行区域、列区域和值区域上方。此区域呈现为一栏下拉筛选控件（每个页字段对应一个），最终用户可借此按年份或地区等条件筛选数据透视表。Aspose.Cells 通过 `pivotTable.pageFields` 集合表示该区域，并提供三个用于控制筛选控件栏视觉布局的属性：
- `pivotTable.pageFieldOrder`（一个 `Aspose.Cells.PrintOrderType` 值）决定其余页字段是放在现有字段的*旁边*还是*下方*。
- `pivotTable.pageFieldWrapCount` 设置每行或每列在换行前可容纳的页字段数量。
- `pivotTable.pageFields.move(currIndex, destIndex)` 在不更改顺序模式的情况下重新排列页字段。
本文通过三个代码示例演示如何使用同一数据集执行上述各项操作，以便并排比较所得布局。

## **源数据**
| Fruit | Year | Region | Amount |
|--------|------|--------|--------|
| Apple | 2022 | North | 150 |
| Apple | 2023 | North | 180 |
| Banana | 2022 | South | 120 |
| Banana | 2023 | South | 140 |
| Cherry | 2022 | East | 200 |
| Cherry | 2023 | East | 220 |
| Grape | 2022 | West | 90 |
| Grape | 2023 | West | 110 |
每个代码示例都使用全部八行数据，且顺序完全相同，因此各场景中的源数据始终相同，只有页字段布局属性有所不同。

## **示例 1：先横向后纵向**
在第一个场景中，我们将两个页字段（`Year`、`Region`）配置为在数据透视表顶部**并排显示在同一行**。我们将 `Fruit` 分配到行轴，在页字段轴上先放置 `Year`，再放置 `Region`（`addFieldToArea` 调用的顺序决定初始索引），将 `Amount`（`Sum`）添加为值字段，然后将 `pivotTable.pageFieldOrder` 设置为 `PrintOrderType.OverThenDown`，并设置 `pivotTable.pageFieldWrapCount = 2`。使用 `OverThenDown` 且换行数为 2 时，两个页字段会在数据透视表顶部横向并排显示，因此筛选控件栏仅占一行，宽度为两个字段。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // 标题（第 0 行）
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // 第 1 行：Apple、2022、North、150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // 第 2 行：Apple、2023、North、180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // 第 3 行：Banana、2022、South、120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // 第 4 行：Banana、2023、South、140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // 第 5 行：Cherry、2022、East、200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // 第 6 行：Cherry、2023、East、220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // 第 7 行：Grape、2022、West、90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // 第 8 行：Grape、2023、West、110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // 添加 PivotTableReport 工作表
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // 创建数据源为 PivotData!A1:D9 的数据透视表，并将其放置在 PivotTableReport 的 A1 单元格
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // 添加字段
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // 水果
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // 年份
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // 地区
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // 金额
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // 配置页面字段区域布局：页面字段优先按行排列，每 2 个换行
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // 刷新并计算
            pivotTable.calculateData();
            // 保存
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **示例 2：先纵向后横向**
在本示例中，我们将 `Fruit` 放在行轴上，将 `Year` 和 `Region` 放在页字段轴上（`Year` 排在第一位），并将 `Amount`（`Sum`）设置为值字段，这与示例 1 完全相同。然后将 `pivotTable.pageFieldOrder` 设置为 `PrintOrderType.DownThenOver`，并将 `pivotTable.pageFieldWrapCount` 设置为 `2`。使用 `DownThenOver` 且换行数为 2 时，两个页字段将纵向排列，即 `Year` 位于顶部，`Region` 紧随其下，从而在数据透视表顶部形成一列。因此，与示例 1 不同，筛选控件栏占据两行，每行仅容纳一个字段。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
            }
            const data = [
                ["Apple", 2022, "North", 150],
                ["Apple", 2023, "North", 180],
                ["Banana", 2022, "South", 120],
                ["Banana", 2023, "South", 140],
                ["Cherry", 2022, "East", 200],
                ["Cherry", 2023, "East", 220],
                ["Grape", 2022, "West", 90],
                ["Grape", 2023, "West", 110]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **示例 3：移动页字段**
在第三个场景中，我们保持该数据集和字段分配方式不变，采用中性布局（`OverThenDown`，换行数为 `2`），然后演示 `pivotTable.pageFields.move` 操作。`move(0, 1)` 调用将索引 0 处的页字段（`Year`）移至位置 1，同时将原位置 1 处的页字段（`Region`）移至位置 0。调用完成后，`Region` 成为第一个页字段，`Year` 成为第二个页字段。换行数和顺序模式保持不变，因此筛选控件栏仍以横向并排方式呈现，仅交换了两个下拉框的顺序。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **相关文章**
- [在数据透视表中添加页字段](/cells/zh/javascript-cpp/add-page-field-in-pivot-table/) — 介绍如何将页字段添加到数据透视表的上级主题页面。
- [管理数据透视表中的值字段](/cells/zh/javascript-cpp/manage-value-fields/) — 说明如何配置数据（值）区域，包括本文使用的 `Sum` 汇总方式。
- [对数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/) — 演示如何在页字段筛选控件栏完成布局后，对呈现的数据透视表应用格式。

{{< app/cells/assistant language="javascript-cpp" >}}