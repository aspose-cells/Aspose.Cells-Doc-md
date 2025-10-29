---
title: 如何用 JavaScript 设置点为总数，使用 C++
linktitle: 设置点为总数的方法。
description: 学习如何用 Aspose.Cells for JavaScript 通过 C++ 在瀑布图中设置点为总数。
keywords: 瀑布图、点、设置为总数、JavaScript 通过 C++
type: docs
weight: 72
url: /zh/javascript-cpp/how-to-set-point-as-total/
---

## Excel图表中的"设为总和"是什么意思

在某些 Excel 图表中，例如瀑布图，一些点数据是前面点的总和，你可能需要“设置点为总计”。我们将展示示例代码和下面的说明。

## 瀑布图需要 "设置点为总计" 

![todo:image_alt_text](set-as-total1.png)

此图片显示了 Excel 中的瀑布图。可以看到有四个以“Total”开头的数据点，用于统计之前所有数据点。在此图片中，设置可能不完全正确。当我们选择“Total 2024”这一点时，可以看到“设置为总数”选项在 Excel 中未被勾选。下面附有需要修改的[示例 Excel 文件](SampleSheet.xlsx)，我们将利用 Aspose.Cells for JavaScript 通过 C++ 正确设置。

## 使用 Aspose.Cells for JavaScript 通过 C++ "设置点为总数" 

我们使用以下代码来正确设置文件：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

你可以得到以下正确的[输出文件](output.xlsx)

如下图所示，四个"总和"数据点已正确设置，你可以看到与之前图表的区别。

![todo:image_alt_text](set-as-total2.png)
