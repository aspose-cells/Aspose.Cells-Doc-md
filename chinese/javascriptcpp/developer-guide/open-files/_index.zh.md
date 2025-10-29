---
title: 加载和管理Excel、OpenOffice、Json、Csv和Html文件
linktitle: 打开文件
type: docs
weight: 20
url: /zh/javascript-cpp/loading-saving-and-managing/
description: 使用Aspose.Cells，通过C++用JavaScript轻松创建、打开和管理Excel、CSV、TSV、ODS、HTML、Numbers、Json、XML、Pdf、Jpg、Tiff、图像、Mht和XPS文件。
---

{{% alert color="primary" %}}

使用Aspose.Cells，可以轻松创建、打开和管理Excel文件，例如检索数据或使用设计模板以加快开发流程。

{{% /alert %}}

## **创建新工作簿**
以下示例从零创建一个新工作簿。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **打开和保存文件**
使用Aspose.Cells，轻松打开、保存和管理Excel文件。

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## ** 高级主题**
- [打开文件的不同方式](/cells/zh/javascript-cpp/different-ways-to-open-files/)
- [在加载工作簿时过滤定义名称](/cells/zh/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [在加载工作簿或工作表时筛选对象](/cells/zh/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [从模板文件加载工作簿时筛选数据类型](/cells/zh/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [加载 Excel 文件时获取警告](/cells/zh/javascript-cpp/get-warnings-while-loading-excel-file/)
- [在不包含图表的源Excel文件中加载](/cells/zh/javascript-cpp/load-source-excel-file-without-charts/)
- [加载工作簿中特定的工作表](/cells/zh/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [加载带有指定打印纸张大小的工作簿](/cells/zh/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [打开不同版本的Microsoft Excel文件](/cells/zh/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [打开具有不同格式的文件](/cells/zh/javascript-cpp/opening-files-with-different-formats/)
- [在处理具有大数据集的大文件时优化内存使用](/cells/zh/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [使用 Aspose.Cells 读取由 Apple Inc. 开发的 Numbers 电子表格](/cells/zh/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载](/cells/zh/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [使用LightCells API](/cells/zh/javascript-cpp/using-lightcells-api/)
- [将CSV转换为JSON](/cells/zh/javascript-cpp/convert-csv-to-json/)
- [将Excel转换为JSON](/cells/zh/javascript-cpp/convert-excel-to-json/)
- [将JSON转换为CSV](/cells/zh/javascript-cpp/convert-json-to-csv/)
- [将JSON转换为Excel](/cells/zh/javascript-cpp/convert-json-to-excel/)
- [将Excel转换为Html](/cells/zh/javascript-cpp/convert-excel-to-html/)
