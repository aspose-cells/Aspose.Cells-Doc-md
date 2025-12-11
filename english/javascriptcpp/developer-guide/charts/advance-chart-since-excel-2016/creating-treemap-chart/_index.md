---
title: How to create Treemap chart with JavaScript via C++
linktitle: How to create Treemap chart
description: Learn how to create a Treemap chart in Aspose.Cells for JavaScript via C++. Our guide will help you understand the various properties and formatting options available for Treemap charts, including colors, labels, and data representation.
keywords: Aspose.Cells for JavaScript via C++, Treemap chart, create, properties, formatting, colors, labels, data representation, circular chart, hierarchical charting.
type: docs
weight: 161
url: /javascript-cpp/creating-treemap-chart/
---

## **Possible Usage Scenarios**  
A Treemap chart provides a hierarchical view of your data and makes it easy to spot patterns, such as which items are a store's best sellers. The tree branches are represented by rectangles, and each sub‑branch is shown as a smaller rectangle. The Treemap chart displays categories by color and proximity, and it can easily show large amounts of data that would be difficult to represent with other chart types.  

![todo:image_alt_text](sample.png)  

## **Treemap chart**  
After running the code below, you will see the Treemap chart as shown below.  

![todo:image_alt_text](result.png)  

## **Sample Code**  
The following sample code loads the [sample Excel file](treemap.xlsx) and generates the [output Excel file](out.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Treemap Chart Example</title>
    </head>
    <body>
        <h1>Treemap Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, FillType } = AsposeCells;
        
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

            // Instantiate Workbook with uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);
            // Add a Treemap chart at row 5, column 6 with height 20 and width 12
            const treemapIdx = worksheet.charts.add(ChartType.Treemap, 5, 6, 20, 12);
            // Retrieve the Chart object
            const chart = worksheet.charts.get(treemapIdx);
            // Set the legend to be shown
            chart.showLegend = true;
            // Set the chart title text
            chart.title.text = "Treemap Chart";
            // Add series data range (D2:F13)
            chart.nSeries.add("D2:F13", true);
            // Set category data (A2:C13)
            chart.nSeries.setCategoryData("A2:C13");
            // Show the DataLabels with category names for the first series
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            // Fill the PlotArea with nothing
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Treemap chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```