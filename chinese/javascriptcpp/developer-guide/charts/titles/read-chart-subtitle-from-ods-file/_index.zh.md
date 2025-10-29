---
title: 使用JavaScript通过C++从ODS文件读取图表副标题
linktitle: 从ODS文件中读取图表副标题
description: 学习如何通过C++使用Aspose.Cells for JavaScript从OpenDocument Spreadsheet（ODS）文件中读取图表副标题。我们的指南将演示如何提取和访问图表的副标题以便进行进一步分析或显示。
keywords: 用C++通过Aspose.Cells for JavaScript读取图表副标题、OpenDocument Spreadsheet、ODS文件、图表提取、数据分析。
type: docs
weight: 160
url: /zh/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **从ODS文件中读取图表副标题**

Aspose.Cells提供使用[**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--)属性读取ODS文件中图表副标题的能力。以下示例代码加载[示例ODS文件](89620481.ods)，并使用[**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--)属性读取图表副标题，然后在控制台窗口中打印。请参考以下代码的控制台输出。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
