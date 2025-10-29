---
title: 如何使用 C++ 管理带有 PivotOptions 的 PivotGraph（数据透视图）
linktitle: 数据透视表选项
type: docs
weight: 10
url: /zh/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: 如何用 C++ 通过 JavaScript 管理带有 PivotOptions 的 PivotChart
keywords: 通过 C++ 使用 JavaScript 操作数据透视图表
---

## 什么是数据透视图

Excel中的数据透视图是从数据透视表中创建的数据的图形表示。它允许用户通过以图表形式汇总和显示信息来动态可视化和分析数据。数据透视图是交互式的，可以轻松修改以显示数据的不同视角，因此是Excel中数据分析和演示的强大工具。

## 如何使用数据透视表选项管理数据透视图

通过使用 C++ 结合 Aspose.Cells for JavaScript，您可以使用 [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) 来管理数据透视图。

样本文件和代码：
[样本文件](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

通过上面的示例代码，您可以查看以下效果的结果文件，如下图所示：

**![输出](Output.png)**
