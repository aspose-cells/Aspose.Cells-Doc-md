---
title: 使用 JavaScript 通过 C++ 管理 Excel 文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/javascript-cpp/using-formulas-or-functions-to-process-data/
description: 学习如何通过 C++ 版的 Script 管理 Excel 文件的公式。Aspose.Cells 可以轻松获取、设置和计算 Excel 公式。
keywords: 如何用 C++ 的 JavaScript 计算公式，JavaScript 通过 C++ 使用的函数和公式，管理内置函数，如何用 JavaScript 通过 C++ 使用插件函数，数组公式的使用方法，如何在 JavaScript 通过 C++ 中使用 R1C1 公式。
---

## **介绍**

Microsoft Excel的一个引人注目的功能是其使用公式和函数处理数据的能力。Microsoft Excel提供了一组内置函数和公式，帮助用户快速执行复杂计算。Aspose.Cells还提供了大量内置函数和公式，帮助开发者轻松计算值。Aspose.Cells还支持插件函数。此外，Aspose.Cells支持数组和R1C1公式。

## **如何使用公式和函数**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供了一个[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)集合。Cells集合中的每个项都代表了[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的对象。

可以使用[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类提供的属性和方法将公式应用到单元格中，下面将更详细地讨论。

- 使用内置函数。
- 使用插件函数。
- 使用数组公式。
- 创建R1C1公式。

## **如何使用内置函数**

内置函数或公式作为现成的功能提供，减少开发者的努力和时间。请参阅 [Aspose.Cells 支持的内置函数列表](/cells/zh/javascript-cpp/supported-formula-functions/)。函数以字母顺序列出。未来将支持更多函数。

Aspose.Cells 支持大部分微软 Excel 提供的公式或函数。开发者可以通过 API 或 [设计师电子表格](/cells/zh/javascript-cpp/what-is-a-designer-spreadsheet/) 使用这些公式。Aspose.Cells 支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。

使用[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--)属性向单元格添加公式。**复杂的公式**，例如

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

Aspose.Cells也支持定义的函数。在将公式应用于单元格时，始终要以等号（=）开头，就像在Microsoft Excel中创建公式时一样，并使用逗号（，）来分隔函数参数。

在下面的示例中，复杂的公式应用于工作表的第一个单元格的[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合。该公式使用Aspose.Cells提供的内置**IF**函数。

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
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **如何使用Add-in函数**

我们可以定义一些用户自定义的公式，作为 Excel 插件包含在内。在设置 cell.formula 时，内置函数可以正常工作，但需要使用插件函数设置自定义函数或公式。

Aspose.Cells 提供注册插件函数的功能，使用 [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-)。之后，将 cell.formula 设置为任何插件中的函数，输出的 Excel 文件将包含该插件函数的计算值。

可以下载以下XLAM文件以注册以下示例代码中的加载项函数。类似地，可以下载输出文件"test_udf.xlsx"以检查输出。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **如何使用数组公式**

数组公式是以数组作为参数的函数所组成的公式。在显示数组公式时，会用大括号({})括起来。

某些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将数组输入到与数组参数具有相同行数和列数的单元格范围中。

可以通过调用[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-)方法将数组公式应用于单元格。[**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-)方法接受以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，要填充数组公式结果的列数。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **如何使用R1C1公式**

使用[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的[**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--)属性向单元格添加**R1C1**引用样式的公式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [前导和从属](/cells/zh/javascript-cpp/precedents-and-dependents/)
- [设置公式中的外部链接](/cells/zh/javascript-cpp/set-external-links-in-formulas/)
- [在输入新数据时自动传播表或列表对象中的公式](/cells/zh/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [为命名范围设置公式](/cells/zh/javascript-cpp/setting-formula-for-named-range/)
- [设置公式-非英语用户注意事项](/cells/zh/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/javascript-cpp/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [支持的Excel函数](/cells/zh/javascript-cpp/supported-formula-functions/)
