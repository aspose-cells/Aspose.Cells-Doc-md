---
title: 如何使用 Aspose.Cells for JavaScript 通过 C++ 添加数据透视图表
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/javascript-cpp/how-to-add-pivot-chart/
description: 如何使用 Aspose.Cells for JavaScript 通过 C++ 添加数据透视图表
keywords: 通过 C++ 使用 JavaScript 操作数据透视图表
---
## 什么是数据透视图

透视图表是数据透视表的可视化表现形式。透视图表提供了汇总、分析、探索和展示汇总数据的方式。以下是透视图表的一些主要功能和特性：

1. 动态数据表示：数据透视图会自动更新以反映数据透视表的变化。如果在数据透视表中添加或删除字段，数据透视图也会相应更新。

1. 交互性强：数据透视图具有交互性，允许用户筛选、排序和深入分析数据。这使得探索数据的不同方面变得容易。

1. 灵活布局：用户可以通过拖放字段改变数据透视图的布局，为数据可视化提供灵活性。

1. 多种图表类型：可以根据数据的性质和需要获得的洞察，创建柱状图、折线图、饼图等多种类型的图表。

1. 汇总：数据透视图汇总大量数据，可以显示总计、平均值、计数或其他统计信息。

1. 筛选：提供筛选功能，仅显示符合特定条件的数据。

<br>
透视图表常用于商业智能和数据分析，帮助客户清晰、简洁地展示复杂数据，是做出数据驱动决策的强大工具。

## 如何使用 Aspose.Cells for JavaScript 通过 C++ 添加数据透视图表

### **添加数据透视表**

使用 Aspose.Cells for JavaScript 通过 C++ 创建数据透视表：

1. 使用单元格对象的`putValue`方法向工作表添加一些数据。您也可以使用已填充数据的模板文件。数据将作为数据透视表的数据源。
1. 通过调用`PivotTables`集合的`add`方法在工作表中添加数据透视表。
1. 通过传入索引从`PivotTables`集合访问新创建的PivotTable对象。使用封装在PivotTable对象中的任何数据透视表对象来管理表格。

下面是代码示例。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Download</h1>
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
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Name the sheet
            sheet.name = "Data";
            const cells = sheet.cells;

            // Setting the header values to the cells
            cells.get("A1").value = "Employee";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Product";
            cells.get("D1").value = "Continent";
            cells.get("E1").value = "Country";
            cells.get("F1").value = "Sale";

            const namesAndValues = [
                ["David", 1, "Maxilaku", "Asia", "China", 2000],
                ["David", 2, "Maxilaku", "Asia", "India", 500],
                ["David", 3, "Chai", "Asia", "Korea", 1200],
                ["David", 4, "Maxilaku", "Asia", "India", 1500],
                ["James", 1, "Chang", "Europe", "France", 500],
                ["James", 2, "Chang", "Europe", "France", 1500],
                ["James", 3, "Chang", "Europe", "Germany", 800],
                ["James", 4, "Chang", "Europe", "Italy", 900],
                ["James", 4, "Chang", "Europe", "France", 500],
                ["Miya", 1, "Geitost", "America", "U.S.", 1600],
                ["Miya", 2, "Chai", "America", "U.S.", 600],
                ["Miya", 3, "Geitost", "America", "Brazil", 2000],
                ["Miya", 2, "Geitost", "America", "U.S.", 500],
                ["Miya", 3, "Maxilaku", "America", "Canada", 900],
                ["Miya", 4, "Geitost", "America", "U.S.", 700],
                ["Miya", 5, "Geitost", "America", "U.S.", 1400],
                ["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
                ["Miya", 7, "Ikuru", "Europe", "France", 300],
                ["Miya", 8, "Ikuru", "Europe", "Italy", 500],
                ["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
                ["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
                ["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
                ["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
                ["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
                ["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
                ["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
                ["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
            ];

            namesAndValues.forEach((item, index) => {
                const rowIndex = index + 2;
                cells.get(`A${rowIndex}`).value = item[0];
                cells.get(`B${rowIndex}`).value = item[1];
                cells.get(`C${rowIndex}`).value = item[2];
                cells.get(`D${rowIndex}`).value = item[3];
                cells.get(`E${rowIndex}`).value = item[4];
                cells.get(`F${rowIndex}`).value = item[5];
            });

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet populated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **添加数据透视图**

使用 Aspose.Cells for JavaScript 通过 C++ 创建数据透视图表：

1. 添加图表。
1. 设置图表的`PivotSource`，指向工作表中的现有数据透视表。
1. 设置其他属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pivot Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new sheet of Chart type
            const sheetIndex = workbook.worksheets.add(AsposeCells.SheetType.Chart);
            const sheet3 = workbook.worksheets.get(sheetIndex);
            sheet3.name = "PivotChart";

            // Adding a column chart
            const index = sheet3.charts.add(AsposeCells.ChartType.Column, 0, 5, 28, 16);

            // Setting the pivot chart data source and hiding pivot field buttons
            const chart = sheet3.charts.get(index);
            chart.pivotSource = "PivotTable!PivotTable1";
            chart.hidePivotFieldButtons = false;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'pivotChart_test_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
