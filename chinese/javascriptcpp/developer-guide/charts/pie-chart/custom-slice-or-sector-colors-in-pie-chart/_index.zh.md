---
title: 用 JavaScript 通过 C++ 在饼图中自定义切片或扇区颜色
linktitle: 在饼图中自定义切片或扇区的颜色
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 自定义饼图中的切片和扇区颜色。我们的指南将演示如何为每个切片、扇区或区域分配独特的颜色，以增强视觉吸引力和数据表现。
keywords: 使用 Aspose.Cells for JavaScript 通过 C++ 创建饼图，支持自定义切片颜色和扇区颜色，提升视觉效果和数据表达。
type: docs
weight: 60
url: /zh/javascript-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文解释了如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用Microsoft Excel的默认模板。要使用其他颜色，需要重新定义图表中的颜色。

{{% /alert %}}

要为饼图的单独切片或扇区设置自定义颜色：

1. 访问[**Series**](https://reference.aspose.com/cells/javascript-cpp/series)对象的[**ChartPoint**](https://reference.aspose.com/cells/javascript-cpp/chartpoint)。
1. 使用[**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--)属性分配你选择的颜色。

本文还解释了如何：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/area/#foregroundColor--) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pie Chart Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in a pie chart
            worksheet.cells.get("C3").value = "India";
            worksheet.cells.get("C4").value = "China";
            worksheet.cells.get("C5").value = "United States";
            worksheet.cells.get("C6").value = "Russia";
            worksheet.cells.get("C7").value = "United Kingdom";
            worksheet.cells.get("C8").value = "Others";

            // Put the sample values used in a pie chart
            worksheet.cells.get("D2").value = "% of world population";
            worksheet.cells.get("D3").value = 25;
            worksheet.cells.get("D4").value = 30;
            worksheet.cells.get("D5").value = 10;
            worksheet.cells.get("D6").value = 13;
            worksheet.cells.get("D7").value = 9;
            worksheet.cells.get("D8").value = 13;

            // Create a pie chart with desired length and width
            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

            // Access the pie chart
            const pie = worksheet.charts.get(pieIdx);

            // Set the pie chart series
            pie.nSeries.add("D3:D8", true);

            // Set the category data
            pie.nSeries.categoryData = "=Sheet1!$C$3:$C$8";

            // Set the chart title that is linked to cell D2
            pie.title.linkedSource = "D2";

            // Set the legend position at the bottom.
            pie.legend.position = AsposeCells.LegendPositionType.Bottom;

            // Set the chart title's font name and color
            pie.title.font.name = "Calibri";
            pie.title.font.size = 18;

            // Access the chart series
            const srs = pie.nSeries.get(0);

            // Color the individual points with custom colors
            srs.points.get(0).area.foregroundColor = new AsposeCells.Color(0, 246, 22, 219);
            srs.points.get(1).area.foregroundColor = new AsposeCells.Color(0, 51, 34, 84);
            srs.points.get(2).area.foregroundColor = new AsposeCells.Color(0, 46, 74, 44);
            srs.points.get(3).area.foregroundColor = new AsposeCells.Color(0, 19, 99, 44);
            srs.points.get(4).area.foregroundColor = new AsposeCells.Color(0, 208, 223, 7);
            srs.points.get(5).area.foregroundColor = new AsposeCells.Color(0, 222, 69, 8);

            // Autofit all columns
            worksheet.autoFitColumns();

            // Saving the modified Excel file and offering download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
