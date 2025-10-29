---
title: 使用 JavaScript 通过 C++ 查找图表系列中点的 X 和 Y 值类型
linktitle: 查找图表系列中点的X和Y值类型
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 确定图表系列点的 X 和 Y 值类型。本指南将解释数据值的类型以及如何在您的图表中访问和操作它们。
keywords: Aspose.Cells for JavaScript 通过 C++、制图、X 值、Y 值、数据类型、访问、操作、图表系列。
type: docs
weight: 150
url: /zh/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能的使用场景**  
 有时候，您可能想知道系列中图表点的 X 和 Y 值的类型。Aspose.Cells for JavaScript 通过 C++ 提供了 `ChartPoint.XValueType` 和 `ChartPoint.YValueType` 属性，可用于此目的。请注意，您在有效使用这些属性之前，需要调用 `Chart.calculate()` 方法。  

## **查找图表系列中点的X和Y值类型**  
以下示例代码加载了[示例Excel文件](64716905.xlsx)，访问了第一个工作表中的第一个图表，然后调用`Chart.calculate()`方法，并找出第一个图表点的X值和Y值类型，并在控制台输出。请参考下面的控制台输出。  

## **示例代码**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Find Type Of X and Y Values Of Points In Chart Series</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first chart.
            const chart = worksheet.charts.get(0);

            // Calculate chart data.
            chart.calculate();

            // Access first chart point in the first series.
            const point = chart.nSeries.get(0).points.get(0);

            // Get the types of X and Y values of chart point.
            const xValueType = point.xValueType;
            const yValueType = point.yValueType;

            // Display results
            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>X Value Type: ${xValueType}</p>
                <p>Y Value Type: ${yValueType}</p>
            `;
        });
    </script>
</html>
```  

## **控制台输出**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
