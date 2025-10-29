---
title: 通过C++的JavaScript获取图表所在的工作表
linktitle: 获取图表的工作表
description: 学习如何使用Aspose.Cells for Java脚本通过C++检索与Excel图表相关联的工作表，有效访问和操作图表的基础数据。
keywords: Aspose.Cells for Java脚本、Excel图表、工作表、数据操作、基础数据、操作、JavaScript通过C++
type: docs
weight: 1000
url: /zh/javascript-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您可能希望从图表的引用中访问工作表。Aspose.Cells提供了[**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)属性，该属性返回包含图表的工作表的引用。

{{% /alert %}}

 以下示例展示如何使用[**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)属性。代码首先打印工作表的名称，然后访问工作表上的第一个图表。接着再次使用[**Chart.worksheet**](https://reference.aspose.com/cells/javascript-cpp/chart/#worksheet--)属性打印工作表名称。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Print worksheet name
            const sheetName = worksheet.name;
            let outputHtml = `<p>Sheet Name: ${sheetName}</p>`;

            // Access the first chart inside this worksheet
            const charts = worksheet.charts;
            if (charts.count > 0) {
                const chart = charts.get(0);

                // Access the chart's sheet and display its name again
                const chartSheetName = chart.worksheet.name;
                outputHtml += `<p>Chart's Sheet Name: ${chartSheetName}</p>`;
            } else {
                outputHtml += `<p>No charts available in the worksheet.</p>`;
            }

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```

以下是示例代码产生的控制台输出。您可以看到，它两次打印了相同的工作表名称。

{{< highlight javascript >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
