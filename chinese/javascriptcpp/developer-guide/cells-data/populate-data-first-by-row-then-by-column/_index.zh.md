---
title: 首先按行然后按列填充数据
type: docs
weight: 1000
url: /zh/javascript-cpp/populate-data-first-by-row-then-by-column/
description: 了解如何通过Aspose.Cells for Java脚本在C++ API中先按行后按列填充数据。
keywords: 先按行后按列填充数据JavaScript via C++，先插入数据后按行按列JavaScript via C++，添加数据先按行后按列JavaScript via C++，高性能数据插入JavaScript via C++，高性能数据添加JavaScript via C++
---

{{% alert color="primary" %}}  

通过首先按行然后按列填充电子表格来提高整体性能。  

{{% /alert %}}  

将数据放入顺序A1，B1，A2，B2比A1，A2，B1，B2更快。如果工作表中有许多单元格，并且按行填充数据，这个提示可以使程序运行速度更快。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
