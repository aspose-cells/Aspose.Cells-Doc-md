---
title: 转置区域
linktitle: 转置区域
description: 本文介绍了如何使用 Aspose.Cells for JavaScript via C++ 在 Excel 文件中将数据从行转置或旋转为列，或反之，并提供三种不同的方法。
keywords: Aspose.Cells, JavaScript via C++, 电子表格, 转置区域, 旋转数据, 转置函数, 动态数组公式, 数组公式, Excel TRANSPOSE, 行到列
type: docs
weight: 80
url: /zh/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ 支持以三种不同方式对数据进行转置（旋转），即行变为列、列变为行。第一种方法使用就地的 `range.transpose()` 方法，适用于所有 Excel 版本；第二种方法使用 `cell.setDynamicArrayFormula()` 编写现代动态数组公式 `=TRANSPOSE(...)`，在 Excel 365 或 Excel 2021 中会自动溢出；第三种方法使用 `cell.setArrayFormula()` 编写经典的 Ctrl+Shift+Enter (CSE) 数组公式，兼容旧版 Excel。本文将逐步介绍每种方法并提供完整代码示例。
{{% /alert %}}

## **介绍**
转置区域指的是将其旋转，使原本的行变为列，原本的列变为行，等同于沿主对角线对数据进行镜像。在 Microsoft Excel 中，工作表函数 `TRANSPOSE` 实现此操作，相关概念参考文档位于 [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function)。该概念可以以编程方式应用于单元格区域，在许多业务和报表场景中非常有用。
- 重新定位季度或年度销售报告，使季度通常横向排列、地区纵向排列，或反之。
- 在仪表板或图表中交换坐标轴方向，使时间序列纵向排列而非横向。
- 重塑从外部系统导入的数据，使其符合下游分析或报表模板所需的布局。
为了使文章后续内容具体化，所有示例均使用下面的区域 **A1:D5** 的小型地区‑季度销售表。表格的 **A1** 为空，**B1:D1** 为地区标题，**A2:A5** 为季度标题。
| 地区            | 欧洲    | 亚洲      | 北美 |
|-------------------|-----------|-----------|---------------|
| 第1季度             | 21704714  | 8774099   | 12094215      |
| 第2季度             | 17987034  | 12214447  | 10873099      |
| 第3季度             | 19485029  | 14356879  | 15689543      |
| 第4季度             | 22567894  | 15763492  | 17456723      |
本文随后展示使用 Aspose.Cells for JavaScript via C++ 转置此数据的三种不同方法，每种方法适用于不同的 Excel 版本和使用场景。

## **方法 1 — 原地转置区域 (Range.transpose)**
当您希望在不使用 `TRANSPOSE` 工作表函数的情况下转置数据时，请使用此方法。它适用于 **所有 Excel 版本**，且不依赖动态数组，是最安全的跨版本兼容选项。当您只需要最终的转置结果且不需要在工作簿中保留原始的 `TRANSPOSE` 公式时，此方法是理想选择。

### **使用的 API**
`Range.transpose()` 是 `Aspose.Cells.Range` 类的实例方法。调用它会就地翻转区域，交换其行和列，使原本的行变为列，原本的列变为行。该方法直接修改底层单元格，不会写入公式。

### **步骤**
1. 使用 `LoadOptions` 将格式设为 `.xlsx`，通过调用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 打开源工作簿。
2. 使用 `workbook.getWorksheets().get(0)` 获取工作簿的第一个工作表。
3. 通过 `worksheet.getCells()` 访问工作表的单元格集合。
4. 调用 `cells.createRange("A1:D5")` 创建覆盖 **A1:D5** 的源区域。
5. 调用 `source.transpose()` 对区域就地进行旋转，交换行列。
6. 使用 `workbook.save(outputFile)` 保存工作簿。
转置后，此锚点区域包含旋转后的数据。首行显示 (空, **Europe**, **Asia**, **North America**)，首列显示 (空, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**)。原始的每一列销售数据在转置后都成为一行。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **方法 2 — 使用动态数组公式转置（Excel 365 / 2021）**
当您希望在输出工作簿中保留 `=TRANSPOSE(A1:D5)` 公式为实时公式，以便源数据更改时结果自动更新，并且目标 Excel 文件将在支持动态数组和溢出运算符的 **Excel 365 / Excel 2021 及更高版本** 中打开时，请使用此方法。

### **使用的 API**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` 是 `Aspose.Cells.Cell` 类的方法，用于将单元格的公式设为 **动态数组公式**。Excel 会对公式求值一次，并自动将结果溢出到相邻单元格。第三个参数设为 `true` 时，指示 Aspose.Cells 在写入时也计算结果值。

### **步骤**
1. 使用 `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` 加载源工作簿。
2. 获取第一个工作表并访问其单元格集合。
3. 通过调用 `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` 将动态数组公式放置在源区域下方的 **A6** 单元格。
4. `new FormulaParseOptions()` 参数采用默认设置，第三个参数 `true` 告诉 Aspose.Cells 将公式视为动态数组并进行求值，以便将溢出的数值写入工作簿。
5. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 包含公式 `=TRANSPOSE(A1:D5)`，Excel 会自动将结果溢出到 **A6:E9** 区域，该区域为 4 行 5 列的块，与转置后的数据相同。

{{% alert color="primary" %}}
此方法仅在 **Excel 365 / 2021 及更高版本** 上有效。旧版 Excel 不会正确溢出动态数组公式。
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **方法 3 — 使用经典数组公式转置（CSE）**
当您希望在工作簿中保留 `TRANSPOSE` 公式，但目标 Excel 文件可能在 **旧版 Excel（2021 之前，包括 2019、2016、2013 等）** 中打开且不支持动态数组溢出时，请使用此方法。经典的 CSE（Ctrl+Shift+Enter）数组公式是兼容所有 Excel 版本的传统替代方案。

### **使用的 API**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` 是 `Aspose.Cells.Cell` 类的方法，用于向锚点单元格分配 **经典数组（CSE）公式** 并声明结果数组的维度。Aspose.Cells 会写入多单元格数组公式标记，使 Excel 将该公式作为单一数组表达式进行求值，填充声明的范围。

### **步骤**
1. 按照前述方法加载源工作簿。
2. 获取第一个工作表并访问其单元格集合。
3. 调用 `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`。第二个参数 `4` 表示目标数组的行数，第三个参数 `5` 表示列数。
4. 使用 `workbook.save(outputFile)` 保存工作簿。
单元格 **A6** 是数组公式的锚点，计算后的数组从 A6 开始跨越 4 行 5 列，与 A1:D5 源区域的转置尺寸相匹配。Excel 在结果范围内写入单一的数组公式标记，使旧版 Excel 能够正确求值。

{{% alert color="primary" %}}
CSE 数组公式是 Excel 评估 `TRANSPOSE` 表达式的经典方式，此方法在所有 Excel 版本中均通用兼容。
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // 加载源工作簿，使用 xlsx LoadOptions
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // 访问第一张工作表及其 Cells 集合
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // 在单元格 A6 上设置经典的 CSE 数组公式。
                // 公式 =TRANSPOSE(A1:D5) 将 5 行 x 4 列的源范围旋转
                // 成为 4 行 x 5 列的数组。第二个参数（4）是行数
                // 第三个参数（5）是结果数组的列数。
                // Aspose.Cells 写入 CSE 数组公式标记，使 Excel 将其评估为
                // 单个多单元格数组公式，兼容不支持动态数组溢出的旧 Excel 版本
                // （2019、2016、2013 等）。
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // 保存工作簿，以持久化数组公式标记
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **比较 — 何时使用每种方法**
| 方法 | API / 方法 | Excel 版本 | 是否保留源公式 | 输出范围 |
|----------|--------------|---------------|--------------------------|--------------|
| 方法 1 — 原地转置 | `range.transpose()` | 所有 Excel 版本 | 否（仅值） | 初始锚点区域，5×4 |
| 方法 2 — 动态数组公式 | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | 是（动态溢出） | 从锚点溢出 |
| 方法 3 — 经典数组公式（CSE） | `cell.setArrayFormula()` | 所有 Excel 版本 | 是（多单元格数组公式） | 显式尺寸，4×5 |
当需要快速、跨版本的转换且仅需将转置后的数值写入文件时，请使用 **方法 1**。当确定使用现代 Excel 并希望公式保持为实时并在源数据更改时自动更新时，请使用 **方法 2**。当需要在所有 Excel 版本（包括不支持动态数组的旧版）中保留公式并实现最广泛兼容性时，请使用 **方法 3**。

{{< app/cells/assistant language="javascript-cpp" >}}