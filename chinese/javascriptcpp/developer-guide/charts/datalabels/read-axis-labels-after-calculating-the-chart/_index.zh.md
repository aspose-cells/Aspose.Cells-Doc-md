---
title: 在用 C++ 通过 JavaScript 计算图表后读取坐标轴标签
linktitle: 在计算图表后读取轴标签
description: 学习如何在绘制图表后通过 C++ 读取 Aspose.Cells for JavaScript 中的坐标轴标签。我们的指南将展示如何访问和获取坐标轴标签，包括它们的格式和位置。
keywords: Aspose.Cells for JavaScript，图表，坐标轴标签，计算，读取，访问，检索，格式，定位，JavaScript 与 C++
type: docs
weight: 90
url: /zh/javascript-cpp/read-axis-labels-after-calculating-the-chart/
---

## **可能的使用场景**

你可以使用 [**Chart.calculate()**](https://reference.aspose.com/cells/javascript-cpp/chart/#calculate--) 方法在计算图表值后读取你的图表的坐标轴标签。请使用 [**Axis.axisTexts**](https://reference.aspose.com/cells/javascript-cpp/axis/#axisTexts--) 属性实现此目的，它将返回坐标轴标签的列表。

## **计算图表后读取轴标签**

请参阅以下示例代码，加载[sample Excel file]（ReadAxisLabels.xlsx）并读取第一个工作表中图表的类别轴标签。然后在控制台上打印轴标签的值。请参阅下面的示例代码的控制台输出进行参考。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Read Axis Labels</title>
    </head>
    <body>
        <h1>Read Chart Category Axis Labels</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the chart
            const chart = worksheet.charts.get(0);

            // Calculate the chart
            chart.calculate();

            // Read axis labels of category axis
            const lstLabels = chart.categoryAxis.axisTexts;

            // Display axis labels
            let html = '<h2>Category Axis Labels:</h2>';
            html += '<hr/>';
            if (!lstLabels || !lstLabels.length) {
                html += '<p>No axis labels found.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < lstLabels.length; i++) {
                    console.log(lstLabels[i]);
                    html += `<li>${lstLabels[i]}</li>`;
                }
                html += '</ul>';
            }
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}
