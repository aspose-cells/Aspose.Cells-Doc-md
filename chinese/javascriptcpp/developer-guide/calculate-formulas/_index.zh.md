---
title: 通过C++用JavaScript计算公式
linktitle: 计算公式
description: 本文介绍如何使用Aspose.Cells库通过C++调用JavaScript在Microsoft Excel中计算公式。通过加载现有Excel文件或创建新Excel文件，我们可以使用Aspose.Cells提供的方法计算公式并获取结果。最后，将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells，Excel，公式，计算，直接计算公式，反复计算公式，通过C++添加JavaScript公式
type: docs
weight: 125
url: /zh/javascript-cpp/calculate-formulas/
---

## **添加公式及计算结果**

Aspose.Cells 有内嵌的公式计算引擎。它不仅可以重新计算导入设计模板中的公式，还支持计算在运行时添加的公式的结果。

Aspose.Cells支持大部分Microsoft Excel中的公式或函数（阅读[计算引擎支持的函数列表](/cells/zh/javascript-cpp/supported-formula-functions/)）。这些函数可通过API或设计器表格使用。Aspose.Cells支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。

使用 [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) 属性或 [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-) 方法将公式添加到单元格中。应用公式时，字符串前始终以等号（=）开始，就像在Microsoft Excel中创建公式一样，用逗号（,）分隔函数参数。

为了计算公式结果，可以调用 [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) 方法，该方法处理Excel文件中所有嵌入的公式；或者调用 [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-) 方法，处理工作表中的所有嵌入公式；或者调用 [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-) 方法，处理单个单元格的公式：

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **公式重复计算的重要信息**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的**公式**属性和**formula(...)**方法与[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)和[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)类的**calculate**方法不同。**公式**属性和**formula(...)**方法仅在添加公式到单元格时使用，运行时不计算结果。要获取公式的结果，请调用**calculate**方法。

{{% /alert %}}

## **直接计算公式**

Aspose.Cells内置了一个公式计算引擎。除了计算从设计文件导入的公式外，Aspose.Cells还可以直接计算公式的结果。

有时，您需要在不将其添加到工作表的情况下直接计算公式结果。已在工作表中的单元格值已经存在，您只需根据某个Microsoft Excel公式计算这些值的结果，无需在工作表中添加公式。

您可以使用 Aspose.Cells 的公式计算引擎API [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 来 [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) 这些公式的结果，而不必将它们添加到工作表中：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

以上代码生成以下输出：
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **如何重复计算公式**

当工作簿中有大量公式、用户需要反复计算而只修改少部分内容时，启用公式链计算可能对性能有帮助：[**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **重要知识**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建计算链也需要额外的时间，第一次计算公式（[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)）可能会比没有计算链的公式计算消耗更多的CPU处理时间和内存。如果用户不需要重复计算公式，默认行为（直接计算公式而不创建计算链）应该是更好的选择。

{{% /alert %}}

## **高级主题**
- [将单元格添加到Microsoft Excel公式监视窗口](/cells/zh/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [使用Aspose.Cells计算IFNA函数](/cells/zh/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [计算数据表的数组公式](/cells/zh/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [计算Excel 2016的MINIFS和MAXIFS函数](/cells/zh/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少 Cell.calculate 方法的计算时间](/cells/zh/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环引用](/cells/zh/javascript-cpp/detecting-circular-reference/)
- [在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用AbstractCalculationEngine返回一系列值](/cells/zh/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [设置工作簿的公式计算模式](/cells/zh/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [在 Aspose.Cells 中使用 FormulaText 函数](/cells/zh/javascript-cpp/using-formulatext-function-in-aspose-cells/)
