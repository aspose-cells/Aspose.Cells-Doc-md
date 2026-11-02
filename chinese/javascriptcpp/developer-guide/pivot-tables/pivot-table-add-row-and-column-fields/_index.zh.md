---
title: 在 Aspose.Cells for JavaScript via C++ 中向数据透视表添加行字段和列字段
linktitle: 在 Aspose.Cells for JavaScript via C++ 中向数据透视表添加行字段和列字段
description: 了解如何在 Aspose.Cells for JavaScript via C++ 中使用 PivotField.SetSubtotals 和 PivotFieldSubtotalType，向数据透视表添加行字段和列字段，并控制数据透视字段的小计。
keywords: Aspose.Cells, JavaScript via C++, 数据透视表, 行字段, 列字段, PivotField, setSubtotals, PivotFieldSubtotalType, 小计, JavaScript, Excel 数据透视表
type: docs
weight: 220
url: /zh/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **向行区域或列区域添加字段**
`pivotTable.addFieldToArea(fieldType, fieldName)` 方法将源数据中的基础字段移入数据透视表的四个区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。
- `Row` — 垂直放置在左侧的字段
- `Column` — 水平放置在顶部的字段
- `Data` — 对其值进行聚合的字段
- `Page` — 用作报表筛选器的字段
字段的嵌套顺序很重要。先将 `Category` 添加到行区域，再将 `Item` 添加到该区域，会生成外层分组为 `Category`、内层分组为 `Item` 的数据透视表。反转添加顺序会反转层级结构。

## **数据透视字段小计**
`pivotField.setSubtotals(subtotalType, shown)` 方法控制数据透视字段显示哪些小计行。每次调用都会独立切换一种小计类型。传入 `shown = true` 会显示小计，而 `shown = false` 会隐藏小计。由于每次调用仅影响一种类型，因此使用不同的 `subtotalType` 值多次调用该方法可构建自定义小计集合。
`PivotFieldSubtotalType` 枚举定义了可用的小计类型。
- `Automatic` — Aspose.Cells 选择默认选项（数值字段通常为 `Sum`）
- `None` — 不显示所有小计行
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
只有在行区域（或列区域）中存在两个或更多数据透视字段时，才会显示小计。只有一个字段时，分组层级之间没有可供小计计算的内容，因此此时调用 `setSubtotals` 不会产生可见效果。因此，本文中的每个示例都在行区域放置两个行字段（外层为 `Category`，内层为 `Item`），以便清楚显示每个 `Category` 组的小计边界。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**
如果完全不调用 `setSubtotals`，Aspose.Cells 会将 `Automatic` 选项应用于数值字段。以下示例通过在外层 `Category` 行字段上调用 `setSubtotals(PivotFieldSubtotalType.Automatic, true)`，明确确认此行为。

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **场景 2 — 不显示所有小计（None）**
调用 `setSubtotals(PivotFieldSubtotalType.None, true)` 会从数据透视表中移除所有小计行，仅保留字段行和底部的总计行。当您希望显示原始分组数据而不包含任何汇总行时，此设置非常有用。

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **场景 3 — 自定义小计集合（Sum + Average）**
您不必局限于单个小计类型。每次 `setSubtotals` 调用都会独立作用于一种类型，因此调用两次——一次使用 `Sum`，一次使用 `Average`——会为每个 `Category` 组生成由两行小计组成的自定义小计集合。

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
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const i = pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **回顾**
这三个场景仅有一项不同：`setSubtotals` 的调用方式。其他所有内容——数据集、字段及其所属区域——均完全相同，因此各布局可直接对比。
- **添加字段。** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` 将源列移入某个区域。在同一区域内，调用顺序即显示顺序，因此第一次调用会成为最外层分组。小计需要同一区域中有两个或更多字段：如果只有一个字段，分组层级之间就没有可供小计计算的内容。
- **场景 1 — 自动小计。** 不调用 `setSubtotals` 时，选择权交由 Excel，由 Excel 对数值字段应用其默认小计。使用 `PivotFieldSubtotalType.Automatic` 调用 `setSubtotals`，则会显式记录该选择，而不是使其保持隐式状态。
- **场景 2 — 无小计。** 使用 `PivotFieldSubtotalType.None` 调用 `setSubtotals` 会禁用默认小计。因此，数据透视表会保留字段行和总计行，但会移除 Excel 本应插入这些行之间的小计行。
- **场景 3 — 选定的小计集合。** 每次调用恰好切换一种小计类型，并且多次调用的效果会累积，而不会相互重置。因此，分别使用 `PivotFieldSubtotalType.Sum` 和 `PivotFieldSubtotalType.Average` 调用一次后，两种类型都会保持启用，数据透视表将呈现 `Sum` 小计、`Average` 小计和总计。

{{% alert color="primary" %}}
小计并非行区域特有。对从 `pivotTable.getColumnFields()` 获取的字段执行相同的 `setSubtotals` 调用，也会在列轴上产生与上述三种场景相同的布局，因为该设置属于数据透视字段，而不是字段所在的轴。
{{% /alert %}}

## **相关文章**
- [数据透视表中的页字段](/cells/zh/javascript-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for JavaScript via C++ 中刷新数据透视表](/cells/zh/javascript-cpp/refresh-pivot-table/)
- [对数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}