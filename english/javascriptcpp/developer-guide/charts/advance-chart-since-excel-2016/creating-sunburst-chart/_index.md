---
title: How to create Sunburst chart with JavaScript via C++
linktitle: How to create Sunburst chart
description: Learn how to create a sunburst chart in Aspose.Cells for JavaScript via C++, a chart that presents data in a circle. Our guide will help you set up various properties and formatting of your chart, including data labels, legends, colors, and more.
keywords: Aspose.Cells for JavaScript via C++, sunburst chart, create, set properties, data labels, legend, format, color, circle, data rendering.
type: docs
weight: 162
url: /javascript-cpp/creating-sunburst-chart/
---

## **Possible Usage Scenarios**
Treemap charts are good for comparing proportions within the hierarchy; however, treemap charts aren't great at showing hierarchical levels between the largest categories and each data point. A sunburst chart is a much better visual for showing that. The sunburst chart is ideal for displaying hierarchical data. Each level of the hierarchy is represented by one ring or circle with the innermost circle as the top of the hierarchy. A sunburst chart without any hierarchical data (one level of categories) looks similar to a doughnut chart. However, a sunburst chart with multiple levels of categories shows how the outer rings relate to the inner rings. The sunburst chart is most effective at showing how one ring is broken into its contributing pieces, while another type of hierarchical chart, the treemap chart, is ideal for comparing relative sizes.

![todo:image_alt_text](sample.png)

## **Sunburst chart**
After running the code below, you will see the Sunburst chart as shown below.

![todo:image_alt_text](result.png)

## **Sample Code**
The following sample code loads the [sample Excel file](sunburst.xlsx) and generates the [output Excel file](out.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```