---
title: 在 Aspose.Cells for JavaScript via C++ 中将样式应用于数据透视表
linktitle: 在 Aspose.Cells for JavaScript via C++ 中将样式应用于数据透视表
description: 了解如何在 Aspose.Cells for JavaScript via C++ 中将内置和自定义样式应用于数据透视表，涵盖旧版 XLS 自动格式、现代 Excel 2007+ 命名样式、自定义数据透视表样式以及 FormatAll 快捷方式。
keywords: Aspose.Cells for JavaScript via C++ 数据透视表样式, PivotTableStyleType, AutoFormatType, FormatAll, 自定义样式, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /zh/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持应用旧版数据透视表自动格式（适用于 `.xls` 文件）以及现代命名或自定义数据透视表样式（适用于 `.xlsx`、`.xlsm` 和 `.xlsb` 文件）。应调用的 API 取决于工作簿保存时的文件格式，而不是加载时的文件格式。
{{% /alert %}}

## **简介**
Aspose.Cells 为数据透视表提供两套并行的样式 API。选择哪一套取决于工作簿保存时的文件格式，而不是读取时的文件格式。以 `.xls` 文件加载的工作簿可以重新保存为 `.xlsx`，此时应使用现代样式 API，而不是旧版 API。
- `pivotTable.pivotTableStyleType` 用于选择一种内置命名样式（浅色和深色主题，包括 Excel 2017 中新增的样式）。这些预设为只读。
- `pivotTable.pivotTableStyleName` 用于选择通过 `workbook.worksheets.tableStyles.addPivotTableStyle(...)` 自行定义的自定义样式。如果希望修改预设无法提供的颜色、边框或字体，则必须使用自定义样式。
此外，`pivotTable.formatAll(style)` 是一个快捷方法，可将单个 `style` 对象应用于数据透视表中的每个单元格，并覆盖上述任一样式名称 API 所设置的样式。无论采用何种基础主题，当需要为整个数据透视表呈现统一外观时，此方法非常实用。

## **应用旧版 XLS 预设自动格式**
`pivotTable.autoFormatType` 接受 `Aspose.Cells.Pivot.PivotTableAutoFormatType` 枚举中的值。可用值包括 `Report1` 至 `Report10`、`Classic` 以及 `Table1` 至 `Table10`。
以下示例加载一个新工作簿，填充 Fruit/Year/Amount 示例数据，添加数据透视表，应用 `PivotTableAutoFormatType.Report5`，并将结果保存为 `.xls`。

{{% alert color="primary" %}}
**为何没有列字段？** 报表系列自动格式（`Report1` 至 `Report10`、`Table1` 至 `Table10`）是在经典 Excel 中针对仅包含行字段和值的**单维数据透视表**设计的，因此没有为列字段标题提供内置样式。如果数据透视表需要列字段，请改用[方案 2](#apply-a-modern-named-preset-pivot-table-style)中的现代 `PivotTableStyleType` 预设，这些预设专为现代 Excel 使用的二维布局而设计。
{{% /alert %}}

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
            // 场景 1：应用旧版 XLS 预设自动格式
            // 使用的 API：PivotTable.AutoFormatType
            // 目标文件格式：.xls（旧版）
            // 如需完整示例和数据文件，请访问 https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // 创建新工作簿
            const workbook = new Workbook();
            // 获取第一个工作表
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // 使用标题行（Fruit、Year、Amount）填充源数据
            // 并添加 9 行数据，涵盖 2020 年和 2021 年的 grape、blueberry、kiwi、cherry
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // 在目标单元格 E3 处添加数据透视表，使用源范围 A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // 分配字段：Fruit -> 行，Amount -> 数据
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 应用旧版 XLS 预设自动格式“Report5”
            // 注意：此属性仅在保存为 .xls 时有效
            // 保存为 .xlsx/.xlsm/.xlsb 时，Excel 会忽略 AutoFormatType
            // 并使用 PivotTableStyleType / PivotTableStyleName 指定的样式
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // 以旧版 .xls 格式保存工作簿
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **应用现代命名预设数据透视表样式**
`pivotTable.pivotTableStyleType` 用于选择 Excel 2007 为数据透视表引入的一种内置命名样式。`PivotTableStyleType` 枚举提供三个主题系列：从 `PivotTableStyleLight1` 到 `PivotTableStyleLight28` 的浅色系列、从 `PivotTableStyleMedium1` 到 `PivotTableStyleMedium28` 的中等系列，以及从 `PivotTableStyleDark1` 到 `PivotTableStyleDark28` 的深色系列。该枚举还定义了 `None` 和 `Custom`。每个系列中编号较高的成员均为 Excel 2017 新增的样式。
这些预设为只读。一旦需要更改预设无法提供的颜色、边框或字体，就必须改为定义自定义数据透视表样式，如[方案 3](#define-and-apply-a-custom-pivot-table-style)所示。

{{% alert color="primary" %}}
**为何使用现代预设而不使用报表系列自动格式？** `PivotTableAutoFormatType` 的 `Report1` 至 `Report10` 和 `Table1` 至 `Table10` 值早于数据透视表列字段出现，因此不包含列字段标题样式，Excel 会以无样式方式呈现这些标题。`PivotTableStyleType` 预设专为现代 Excel 使用的二维布局而设计，并会同时为行字段和列字段标题应用样式。
{{% /alert %}}

本方案复用方案 1 的 Fruit/Year/Amount 数据集，通过 `PivotFieldType.Column` 将 `Year` 添加到列区域，同时将 `Fruit` 用作行字段；随后通过 `pivotTable.pivotTableStyleType` 应用深色主题预设 `PivotTableStyleDark1`，并将结果保存为 `.xlsx`。这是 `PivotTableStyleType` 适用的文件格式。

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // 场景 2：使用 PivotTableStyleType 应用现代 Excel 2007+ 命名的预设样式。
            // 目标文件格式：.xlsx。PivotTableStyleType 枚举位于 Aspose.Cells 命名空间中
            // （而非 Aspose.Cells.Pivot），因此无需额外添加 using 指令。
            // GitHub 参考：https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // 标题行：水果 / 年份 / 金额
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 行水果 / 年份 / 金额数据
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // 在 E3 处添加数据透视图，源数据范围为 A1:C10
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // 分配数据透视字段：水果 -> 行区域，年份 -> 列区域，金额 -> 数据区域
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 应用现代 Excel 2007+ 命名的预设数据透视图样式。
            // 对于 .xlsx / .xlsm / .xlsb 文件，PivotTableStyleType 是正确的 API；Excel 会忽略这些格式中的 AutoFormatType。
            // PivotTableStyleDark1 属于深色主题系列（PivotTableStyleDark1..PivotTableStyleDark28），同一枚举还提供
            // 较新的 Excel 2017 浅色/深色主题（PivotTableStyleLight1..Light28 / Dark1..Dark28）。
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // 另存为现代 .xlsx 格式——PivotTableStyleType 仅在此格式中有意义。
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **定义并应用自定义数据透视表样式**
内置预设无法修改。每当需要覆盖颜色、边框或字体时，都必须定义自定义数据透视表样式。该工作流包含三个步骤：
1. 通过 `workbook.worksheets.tableStyles.addPivotTableStyle(name)` 向工作簿的 `tableStyles` 集合中添加自定义样式。该方法返回新建样式的索引。
2. 通过 `tableStyle.tableStyleElements.add(tableStyleElementType)` 添加元素（如 `WholeTable` 或 `GrandTotalRow`）来配置样式，然后通过 `tableStyleElement.setElementStyle(style)` 为每个元素分配 `style`。
3. 将 `pivotTable.pivotTableStyleName` 设置为该样式的名称，以将自定义样式应用于数据透视表。此处不要使用 `pivotTable.pivotTableStyleType`，因为该属性用于选择内置预设。

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` 和 `pivotTable.pivotTableStyleType` 不可互换。对于内置预设，请使用 `pivotTable.pivotTableStyleType`；对于通过 `addPivotTableStyle` 定义的自定义样式，请使用 `pivotTable.pivotTableStyleName`。同时设置两者不会产生问题，但最终只会呈现与预期来源相符的样式。
可用的 `TableStyleElementType` 值包括 `WholeTable`、`FirstRow`、`LastRow`、`FirstColumn`、`LastColumn`、`GrandTotalRow`、`GrandTotalColumn`、`PageFieldLabels` 和 `PageFieldValues`。
以下示例定义一个自定义数据透视表样式，为 `WholeTable` 设置细黑色边框，为 `GrandTotalRow` 设置粗体红色字体，然后通过 `pivotTable.pivotTableStyleName` 应用该样式，并将其保存为 `.xlsx`。
{{% /alert %}}

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
            const cells = worksheet.cells;
            // Populate source data: header row + 9 data rows (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Add pivot table sourced from A1:C10, anchored at E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Step 1: register a new custom pivot table style and capture its index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Step 2: add a WholeTable element and apply thin black borders on all four sides
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Step 3: add a GrandTotalRow element and apply bold red font
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **使用 formatAll 将一种样式应用于所有数据透视表单元格**
`pivotTable.formatAll(style)` 是一个快捷方法，可将单个 `style` 对象应用于数据透视表中的每个单元格，包括数据区域、行标题、列标题和总计单元格。先前通过 `pivotTable.pivotTableStyleType` 或 `pivotTable.pivotTableStyleName` 设置的所有样式都会被覆盖。

{{% alert color="primary" %}}
`formatAll` 会覆盖 `pivotTable.pivotTableStyleType` 和 `pivotTable.pivotTableStyleName`。仅当整个数据透视表都需要统一且不依赖主题的外观时，才应使用此方法。
以下示例创建一个具有黄色纯色填充、粗体深蓝色字体和四周细黑色边框的 `style`，然后通过 `formatAll` 应用该样式，并将其保存为 `.xlsx`。
{{% /alert %}}

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
            // 场景 4：使用 FormatAll 将单个样式应用到数据透视表的所有单元格
            // 使用的 API：PivotTable.FormatAll(Style)
            // 目标格式：.xlsx
            // GitHub 参考：参阅 Aspose.Cells-for-.NET 仓库——数据透视表样式示例
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // 填充源数据：标题行（第 1 行）+ 9 个数据行（第 2-10 行）
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // 添加数据透视表：源范围 A1:C10，目标单元格 E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // 分配数据透视字段：Fruit -> 行区域，Year -> 列区域，Amount -> 数据区域
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // 创建一个将强制应用到数据透视表每个单元格的 Style
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // 应用 FormatAll：将此单个样式强制应用到数据透视表的每个单元格，
            // 覆盖之前设置的任何 PivotTableStyleType / PivotTableStyleName
            pivotTable.formatAll(style);
            // 将工作簿保存为现代 .xlsx 格式
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **应使用哪种样式 API？**
样式 API 的选择取决于保存时使用的文件格式。请参考下表快速选择。
| 目标文件格式 | 应使用的 API | 备注 |
|---|---|---|
| `.xls`（旧版） | `pivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` 中的值（例如 `Report1`–`Report10`、`Classic`、`Table1`–`Table10`）。保存为现代格式时会被忽略。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代格式，内置样式） | `pivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` 中的值（浅色/深色主题，包括 Excel 2017 新增的样式）。 |
| `.xlsx` / `.xlsm` / `.xlsb`（现代格式，自定义样式） | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | 当内置预设无法满足需求时使用。通过 `tableStyleElement.setElementStyle(...)` 配置样式。 |
| 任意格式（统一覆盖） | `pivotTable.formatAll(style)` | 可覆盖整个数据透视表中所有其他样式设置的快捷方法。 |
如果不确定如何选择，请保存为 `.xlsx`，并对内置主题使用 `pivotTable.pivotTableStyleType`，对自定义主题使用 `pivotTable.pivotTableStyleName`。

{{< app/cells/assistant language="javascript-cpp" >}}