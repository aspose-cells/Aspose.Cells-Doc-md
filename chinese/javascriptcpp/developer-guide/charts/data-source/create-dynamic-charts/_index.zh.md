---
title: 使用 C++ 通过 JavaScript 创建动态图表
linktitle: 创建动态图表
description: 学习如何通过 C++ 使用 Aspose.Cells for JavaScript 创建动态图表。本指南将展示如何根据您的需求动态更新图表数据、系列和格式，从而在工作表中直观展示变化的数据。
keywords: Aspose.Cells for JavaScript 通过 C++、制图、动态图表、数据、系列、格式、工作表、更新。
type: docs
weight: 240
url: /zh/javascript-cpp/create-dynamic-charts/
---

{{% alert color="primary" %}}  
动态（或交互式）图表在更改数据范围时具有更改的能力。换句话说，当数据源更改时，动态图表可以自动反映更改。为了触发数据源的更改，可以使用Excel表的筛选选项，或者使用控件如下拉列表或下拉菜单。

 本文演示了使用 Aspose.Cells for JavaScript 通过C++ API创建动态图表的两种方法。  
{{% /alert %}}  

## **使用Excel表**  

{{% alert color="primary" %}}  
 Excel 表格在 Aspose.Cells 视角下称为 ListObjects，因此，为了更清晰，我们将使用“ListObject”这个术语，而不是“表”。请详细阅读如何[使用 Aspose.Cells for JavaScript 通过 C++ 创建和格式化表格](/cells/zh/javascript-cpp/create-and-format-table/)。  
{{% /alert %}}  

ListObjects提供了内置的功能，可以在人为操作下对数据进行排序和筛选。这些排序和筛选选项通过自动添加到[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject)标题行的下拉列表实现。由于这些功能（排序和筛选），[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject)似乎是用作动态图表数据源的理想候选，因为当排序或筛选变化时，图表中的数据表现也会随之改变，以反映[**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject)的当前状态。

为了让演示更简便易懂，我们将从零开始创建[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，并按照下面的步骤逐步进行。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。
1. 访问第 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 中第 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。
1. 向单元格插入一些数据。
1. 根据插入的数据创建 [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject)。
1. 根据 [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject) 的数据范围创建 [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart)。
1. 将结果保存到磁盘。  

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
        const { Workbook, SaveFormat, ChartType, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();
            // Access first worksheet from the collection
            const sheet = book.worksheets.get(0);
            // Access cells collection of the first worksheet
            const cells = sheet.cells;

            // Insert data column-wise
            cells.get("A1").putValue("Category");
            cells.get("A2").putValue("Fruit");
            cells.get("A3").putValue("Fruit");
            cells.get("A4").putValue("Fruit");
            cells.get("A5").putValue("Fruit");
            cells.get("A6").putValue("Vegetables");
            cells.get("A7").putValue("Vegetables");
            cells.get("A8").putValue("Vegetables");
            cells.get("A9").putValue("Vegetables");
            cells.get("A10").putValue("Beverages");
            cells.get("A11").putValue("Beverages");
            cells.get("A12").putValue("Beverages");

            cells.get("B1").putValue("Food");
            cells.get("B2").putValue("Apple");
            cells.get("B3").putValue("Banana");
            cells.get("B4").putValue("Apricot");
            cells.get("B5").putValue("Grapes");
            cells.get("B6").putValue("Carrot");
            cells.get("B7").putValue("Onion");
            cells.get("B8").putValue("Cabbage");
            cells.get("B9").putValue("Potato");
            cells.get("B10").putValue("Coke");
            cells.get("B11").putValue("Coladas");
            cells.get("B12").putValue("Fizz");

            cells.get("C1").putValue("Cost");
            cells.get("C2").putValue(2.2);
            cells.get("C3").putValue(3.1);
            cells.get("C4").putValue(4.1);
            cells.get("C5").putValue(5.1);
            cells.get("C6").putValue(4.4);
            cells.get("C7").putValue(5.4);
            cells.get("C8").putValue(6.5);
            cells.get("C9").putValue(5.3);
            cells.get("C10").putValue(3.2);
            cells.get("C11").putValue(3.6);
            cells.get("C12").putValue(5.2);

            cells.get("D1").putValue("Profit");
            cells.get("D2").putValue(0.1);
            cells.get("D3").putValue(0.4);
            cells.get("D4").putValue(0.5);
            cells.get("D5").putValue(0.6);
            cells.get("D6").putValue(0.7);
            cells.get("D7").putValue(1.3);
            cells.get("D8").putValue(0.8);
            cells.get("D9").putValue(1.3);
            cells.get("D10").putValue(2.2);
            cells.get("D11").putValue(2.4);
            cells.get("D12").putValue(3.3);

            // Create ListObject, Get the List objects collection in the first worksheet
            const listObjects = sheet.listObjects;

            // Add a List based on the data source range with headers on
            let index = listObjects.add(0, 0, 11, 3, true);

            sheet.autoFitColumns();

            // Create chart based on ListObject
            index = sheet.charts.add(ChartType.Column, 21, 1, 35, 18);
            const chart = sheet.charts.get(index);
            chart.chartDataRange = "A1:D12";
            chart.chartDataRangeHasHeaders = true;
            chart.nSeries.categoryData = "A2:B12";

            // Save spreadsheet
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **使用动态公式**  

如果您不希望使用 [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject) 作为动态图表的数据源，另一种选择是使用 Excel 函数（或公式）创建动态数据范围，并使用控件（如组合框）触发数据更改。在此场景中，我们将使用 VLOOKUP 函数根据组合框的选择提取相应的值。当选择更改时，VLOOKUP 函数将刷新单元格值。如果某个范围的单元格使用了 VLOOKUP 函数，则可以在用户交互时刷新整个范围，因此它可以作为动态图表的数据源。

为了使演示简单易懂，我们将从头开始创建工作簿，并按照下面的步骤一步步地前进。

1. 创建一个空的[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。
1. 访问第 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 中第 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。
1. 通过创建命名范围在单元格中插入一些数据。这些数据将作为动态图表的系列。
1. 根据在上一步中创建的命名范围创建 [**ComboBox**](https://reference.aspose.com/cells/javascript-cpp/combobox)。
1. 在作为VLOOKUP函数源的单元格中插入更多数据。
1. 在一组单元格中插入VLOOKUP函数（带有适当参数）。此范围将作为动态图表的数据源。
1. 根据前一步创建的范围创建 [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart)。
1. 将结果保存到磁盘。  

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
        const { Workbook, SaveFormat, ChartType, Color, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');
                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Creating a workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range in the worksheet
                const range = worksheet.cells.createRange("C21", "C24");

                // Name the range
                range.name = "MyRange";

                // Fill different cells with data in the range
                range.get(0, 0).putValue("North");
                range.get(1, 0).putValue("South");
                range.get(2, 0).putValue("East");
                range.get(3, 0).putValue("West");

                const comboBox = worksheet.shapes.addComboBox(15, 0, 2, 0, 17, 64);
                comboBox.inputRange = "=MyRange";
                comboBox.linkedCell = "=B16";
                comboBox.selectedIndex = 0;
                const cell = worksheet.cells.get("B16");
                const style = cell.style;
                style.font.color = Color.White;
                cell.style = style;

                worksheet.cells.get("C16").formula = "=INDEX(Sheet1!$C$21:$C$24,$B$16,1)";

                // Put some data for chart source
                // Data Headers
                worksheet.cells.get("D15").putValue("Jan");
                worksheet.cells.get("D20").putValue("Jan");

                worksheet.cells.get("E15").putValue("Feb");
                worksheet.cells.get("E20").putValue("Feb");

                worksheet.cells.get("F15").putValue("Mar");
                worksheet.cells.get("F20").putValue("Mar");

                worksheet.cells.get("G15").putValue("Apr");
                worksheet.cells.get("G20").putValue("Apr");

                worksheet.cells.get("H15").putValue("May");
                worksheet.cells.get("H20").putValue("May");

                worksheet.cells.get("I15").putValue("Jun");
                worksheet.cells.get("I20").putValue("Jun");

                // Data
                worksheet.cells.get("D21").putValue(304);
                worksheet.cells.get("D22").putValue(402);
                worksheet.cells.get("D23").putValue(321);
                worksheet.cells.get("D24").putValue(123);

                worksheet.cells.get("E21").putValue(300);
                worksheet.cells.get("E22").putValue(500);
                worksheet.cells.get("E23").putValue(219);
                worksheet.cells.get("E24").putValue(422);

                worksheet.cells.get("F21").putValue(222);
                worksheet.cells.get("F22").putValue(331);
                worksheet.cells.get("F23").putValue(112);
                worksheet.cells.get("F24").putValue(350);

                worksheet.cells.get("G21").putValue(100);
                worksheet.cells.get("G22").putValue(200);
                worksheet.cells.get("G23").putValue(300);
                worksheet.cells.get("G24").putValue(400);

                worksheet.cells.get("H21").putValue(200);
                worksheet.cells.get("H22").putValue(300);
                worksheet.cells.get("H23").putValue(400);
                worksheet.cells.get("H24").putValue(500);

                worksheet.cells.get("I21").putValue(400);
                worksheet.cells.get("I22").putValue(200);
                worksheet.cells.get("I23").putValue(200);
                worksheet.cells.get("I24").putValue(100);

                // Dynamically load data on selection of Dropdown value
                worksheet.cells.get("D16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)";
                worksheet.cells.get("E16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)";
                worksheet.cells.get("F16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)";
                worksheet.cells.get("G16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)";
                worksheet.cells.get("H16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)";
                worksheet.cells.get("I16").formula = "=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)";

                // Create Chart
                const index = worksheet.charts.add(ChartType.Column, 0, 3, 12, 9);
                const chart = worksheet.charts.get(index);
                chart.nseries.add("='Sheet1'!$D$16:$I$16", false);
                chart.nseries.get(0).name = "=C16";
                chart.nseries.categoryData = "=$D$15:$I$15";

                // Save result and provide download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
            });

        });
    </script>
</html>
```
