---
title: 读取和写入 DBF 文件
linktitle: 读取和写入 DBF 文件
description: Aspose.Cells 是一个基于 C++ 的 JavaScript 库，用于处理电子表格文件，支持读取和写入 dBASE III 和 IV (DBF) 文件。本文介绍如何使用 Aspose.Cells 从 DBF 文件导入数据并将数据导出到 DBF 文件，包括文件格式详细信息、支持的特性和分步示例。
keywords: Aspose.Cells, 基于 C++ 的 JavaScript 库, DBF, dBASE, 读取 DBF, 写入 DBF, 导入 DBF, 导出 DBF, 文件格式, .dbf
type: docs
weight: 200
url: /zh/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 全面支持读取和写入 DBF (dBASE) 文件。您可以将现有的 dBASE III 和 dBASE IV 文件加载到 Workbook 对象中，使用功能丰富的 Aspose.Cells API 操作数据，并将工作簿保存回 DBF 格式，以供旧版数据库应用程序使用。
{{% /alert %}}

## **简介**
DBF（数据库文件）是一种旧版数据库文件格式，最早由 dBASE 于 20 世纪 80 年代初推出。尽管这种格式已有较长历史，但 DBF 文件至今仍广泛应用于许多行业，用于存储结构化数据，尤其是在会计、GIS 和其他专业应用中。借助 Aspose.Cells，您可以将这些旧版文件无缝集成到现代电子表格工作流中。
该库同时支持读取和写入 DBF 文件，让您能够：
- 将现有 DBF 文件中的数据导入 Aspose.Cells Workbook 对象，以便进一步处理或转换为其他格式。
- 从头创建新的 DBF 文件，或通过转换其他电子表格格式中的数据来创建新的 DBF 文件。
- 在数据传入或传出 DBF 格式时保留字段定义、数据类型和记录结构。
DBF 文件还可以直接在 Microsoft Excel 和其他电子表格应用程序中打开，因此可作为旧版系统与现代电子表格工具之间的便捷桥梁。

## **支持的 DBF 版本和功能**
Aspose.Cells 支持以下 DBF 格式版本：
- **dBASE III** — 最初推出且支持最广泛的 DBF 格式变体。
- **dBASE IV** — 支持更多数据类型和更大字段长度的扩展版本。

### 支持的功能
该库全面支持以下操作：
- 将 DBF 数据读取到 Workbook 对象中，并保留所有记录和字段定义。
- 将工作簿数据写回 DBF 格式，以供兼容 dBASE 的应用程序使用。
- 处理 DBF 文件中常用的数据类型，包括字符、数值、日期和逻辑字段。
- 在读写操作中保留字段定义，例如字段名称、类型和长度。

### 限制和注意事项
处理 DBF 文件时，请注意以下限制：
- 每个文件的最大字段数为 **128**。
- 最大记录大小为 **4000 字节**。
- 字段名限制为 **10 个字符**，必须为大写且不能包含空格。
- DBF 文件中的日期值以 `YYYYMMDD` 格式存储。
- 字符编码可能因源应用程序而异（通常为 Windows-1252 或 OEM 代码页）。

## **读取 DBF 文件**
Aspose.Cells 可轻松将数据从 DBF 文件加载到 Workbook 对象中。该库使用 `LoadOptions` 类指定源格式，确保在加载过程中正确解释数据。

### 使用 Aspose.Cells 读取 DBF 文件
要读取 DBF 文件，需要创建 `LoadOptions` 实例，将其 `loadFormat` 属性设置为 `LoadFormat.Dbf`，然后将其与文件路径一并传递给 `Workbook` 构造函数。加载完成后，可通过 `Worksheets` 集合访问数据，在其中遍历单元格、提取值或按需操作数据。
以下示例演示如何将现有 DBF 文件加载到 Aspose.Cells 中，访问第一个工作表并读取单元格值。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
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
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
您可以在“打开”对话框中选择文件，直接在 Microsoft Excel 中打开 DBF 文件。Excel 会将 DBF 文件视为电子表格，并以表格布局显示其中的记录。这有助于快速验证使用 Aspose.Cells 读取或写入后的数据。
{{% /alert %}}

## **写入 DBF 文件**
使用 Aspose.Cells 将数据写入 DBF 文件的过程与保存其他电子表格格式类似。首先创建或加载 Workbook，使用数据填充工作表，然后调用 `save` 方法并指定 `SaveFormat.Dbf` 作为目标格式。

### 使用 Aspose.Cells 写入 DBF 文件
创建 DBF 文件时，请执行以下步骤：
1. 创建新的 `Workbook` 实例。
2. 从 `Worksheets` 集合中访问第一个工作表。
3. 使用数据填充工作表，包括第一行中的标题以及后续行中的记录。
4. 调用 `Workbook.save` 方法，将文件路径和 `SaveFormat.Dbf` 作为参数传入。
以下示例演示如何从头创建新的 DBF 文件。该示例使用包含不同数据类型（字符串、数字和日期）的数据填充工作表，以说明导出到 DBF 格式时如何处理字段类型。

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
            const cells = worksheet.cells;
            // 列标题
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // 数据行 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // 数据行 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // 数据行 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // 数据行 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // 数据行 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // 设置列宽以提高可读性
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
将数据写入 DBF 文件时，请确保数据符合该格式的限制。字段名长度不应超过 10 个字符，并且不应包含空格。总大小超过 4000 字节的记录将无法正确保存。日期应为可表示为 YYYYMMDD 格式的有效日期值。
{{% /alert %}}

## **数据类型和格式注意事项**
在 Aspose.Cells 与 DBF 格式之间传输数据时，了解两个系统之间的数据类型映射关系有助于确保数据完整性。

### 单元格类型与 DBF 字段类型的映射
保存时，Aspose.Cells 单元格值会自动转换为相应的 DBF 字段类型：
- **字符串**映射到字符 (C) 字段。
- **数值**（整数和小数）映射到数值 (N) 字段。
- **日期值**映射到采用 `YYYYMMDD` 格式的日期 (D) 字段。
- **布尔值**映射到逻辑 (L) 字段。

### 编码
DBF 文件可能使用不同的字符编码，具体取决于创建它们的应用程序。在大多数情况下，Aspose.Cells 会自动处理编码，但如果遇到字符显示问题，可能需要验证源文件的编码。

### 字段名规则
DBF 字段名必须遵守以下规则：
- 长度最多为 10 个字符。
- 必须以字母开头。
- 不能包含空格或特殊字符。
- 无论输入时使用何种大小写，均存储为大写形式。

### 验证输出
写入 DBF 文件后，可以在 Microsoft Excel 或任何兼容 dBASE 的应用程序中打开该文件，以验证结果。数据应以表格布局显示，其中字段名称作为列标题，各条记录则根据您提供的数据填充。

## **在 DBF 与其他格式之间转换**
使用 Aspose.Cells 读取和写入 DBF 文件最实用的应用场景之一，是在 DBF 格式与现代电子表格格式（如 XLSX、XLS 或 CSV）之间转换数据。由于 Aspose.Cells 支持多种格式，您可以轻松加载 DBF 文件并将其重新保存为任何其他受支持的格式，反之亦然。

{{< app/cells/assistant language="javascript-cpp" >}}