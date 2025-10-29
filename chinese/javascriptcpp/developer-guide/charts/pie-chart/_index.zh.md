---
title: 使用JavaScript通过C++创建带引线的饼图
description: 了解如何使用Aspose.Cells for JavaScript通过C++在Microsoft Excel中创建带引线的饼图。我们的指南将演示如何添加连接数据点与图例的引线，从而增强图表的整体清晰度。
keywords: 通过C++的Aspose.Cells for JavaScript，饼图，引线，Microsoft Excel，数据可视化，图表定制。
linktitle: 饼图
type: docs
weight: 45
url: /zh/javascript-cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

 本文介绍了如何从零开始使用Aspose.Cells for JavaScript通过C++ API创建带引线的饼图。在Excel中，默认开启“显示引线”选项，因此在Excel中创建饼图时引线会显示。然而，在使用Aspose.Cells API创建类似图表时，必须显式设置[**Series.hasLeaderLines**](https://reference.aspose.com/cells/javascript-cpp/series/#hasLeaderLines--)属性。

{{% /alert %}}

为了演示如何使用 Aspose.Cells for JavaScript 通过 C++ API 创建带有引线的饼图，我们首先会创建一个新的 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 并输入一些数据，作为系列数据源。数据就位后，我们将在图表集合中添加一个类型为 [**ChartType.Pie**](https://reference.aspose.com/cells/javascript-cpp/charttype) 的 [**Chart**](https://reference.aspose.com/cells/javascript-cpp/chart)，并设置其不同方面以获得理想的图表视图。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Pie Chart Example</title>
    </head>
    <body>
        <h1>Create Pie Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LabelPositionType, DataLabelsSeparatorType } = AsposeCells;

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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add two columns of data
            worksheet.cells.get("A1").putValue("Retail");
            worksheet.cells.get("A2").putValue("Services");
            worksheet.cells.get("A3").putValue("Info & Communication");
            worksheet.cells.get("A4").putValue("Transport Equip");
            worksheet.cells.get("A5").putValue("Construction");
            worksheet.cells.get("A6").putValue("Other Products");
            worksheet.cells.get("A7").putValue("Wholesale");
            worksheet.cells.get("A8").putValue("Land Transport");
            worksheet.cells.get("A9").putValue("Air Transport");
            worksheet.cells.get("A10").putValue("Electric Appliances");
            worksheet.cells.get("A11").putValue("Securities");
            worksheet.cells.get("A12").putValue("Textiles & Apparel");
            worksheet.cells.get("A13").putValue("Machinery");
            worksheet.cells.get("A14").putValue("Metal Products");
            worksheet.cells.get("A15").putValue("Cash");
            worksheet.cells.get("A16").putValue("Banks");

            worksheet.cells.get("B1").putValue(10.4);
            worksheet.cells.get("B2").putValue(5.2);
            worksheet.cells.get("B3").putValue(6.4);
            worksheet.cells.get("B4").putValue(10.4);
            worksheet.cells.get("B5").putValue(7.9);
            worksheet.cells.get("B6").putValue(4.1);
            worksheet.cells.get("B7").putValue(3.5);
            worksheet.cells.get("B8").putValue(5.7);
            worksheet.cells.get("B9").putValue(3);
            worksheet.cells.get("B10").putValue(14.7);
            worksheet.cells.get("B11").putValue(3.6);
            worksheet.cells.get("B12").putValue(2.8);
            worksheet.cells.get("B13").putValue(7.8);
            worksheet.cells.get("B14").putValue(2.4);
            worksheet.cells.get("B15").putValue(1.8);
            worksheet.cells.get("B16").putValue(10.1);

            // Create a pie chart and add it to the collection of charts
            const id = worksheet.charts.add(ChartType.Pie, 3, 3, 23, 13);

            // Access newly created Chart instance
            const chart = worksheet.charts.get(id);

            // Set series data range
            chart.nSeries.add("B1:B16", true);

            // Set category data range
            chart.nSeries.categoryData = "A1:A16";

            // Turn off legend
            chart.showLegend = false;

            // Access data labels
            const dataLabels = chart.nSeries.get(0).dataLabels;

            // Turn on category names
            dataLabels.showCategoryName = true;

            // Turn on percentage format
            dataLabels.showPercentage = true;

            // Set position
            dataLabels.position = LabelPositionType.OutsideEnd;

            // Set separator
            dataLabels.separatorType = DataLabelsSeparatorType.Comma;

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

到目前为止，我们已经创建了饼图并设置了其不同的方面。现在我们将为图表打开引导线。请注意，为了显示引导线，我们必须稍微移动数据标签的位置。

以下代码片段打开了引导线，刷新了图表，然后计算数据标签的位置，以相应地移动它们。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pie Chart Example</title>
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
        const { Workbook, SaveFormat, ChartType, LabelPositionType, DataLabelsSeparatorType } = AsposeCells;

        const initPromise = AsposeCells.onReady({
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

            await initPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            const cells = worksheet.cells;

            // Add two columns of data
            cells.get("A1").value = "Retail";
            cells.get("A2").value = "Services";
            cells.get("A3").value = "Info & Communication";
            cells.get("A4").value = "Transport Equip";
            cells.get("A5").value = "Construction";
            cells.get("A6").value = "Other Products";
            cells.get("A7").value = "Wholesale";
            cells.get("A8").value = "Land Transport";
            cells.get("A9").value = "Air Transport";
            cells.get("A10").value = "Electric Appliances";
            cells.get("A11").value = "Securities";
            cells.get("A12").value = "Textiles & Apparel";
            cells.get("A13").value = "Machinery";
            cells.get("A14").value = "Metal Products";
            cells.get("A15").value = "Cash";
            cells.get("A16").value = "Banks";

            cells.get("B1").value = 10.4;
            cells.get("B2").value = 5.2;
            cells.get("B3").value = 6.4;
            cells.get("B4").value = 10.4;
            cells.get("B5").value = 7.9;
            cells.get("B6").value = 4.1;
            cells.get("B7").value = 3.5;
            cells.get("B8").value = 5.7;
            cells.get("B9").value = 3;
            cells.get("B10").value = 14.7;
            cells.get("B11").value = 3.6;
            cells.get("B12").value = 2.8;
            cells.get("B13").value = 7.8;
            cells.get("B14").value = 2.4;
            cells.get("B15").value = 1.8;
            cells.get("B16").value = 10.1;

            // Create a pie chart and add it to the collection of charts
            const id = worksheet.charts.add(ChartType.Pie, 3, 3, 23, 13);

            // Access newly created Chart instance
            const chart = worksheet.charts.get(id);

            // Set series data range
            chart.nSeries.add("B1:B16", true);

            // Set category data range
            chart.nSeries.categoryData = "A1:A16";

            // Turn off legend
            chart.showLegend = false;

            // Access data labels
            const dataLabels = chart.nSeries.get(0).dataLabels;

            // Turn on category names
            dataLabels.showCategoryName = true;

            // Turn on percentage format
            dataLabels.showPercentage = true;

            // Set position
            dataLabels.position = LabelPositionType.OutsideEnd;

            // Set separator
            dataLabels.separatorType = DataLabelsSeparatorType.Comma;

            // Turn on leader lines
            chart.nSeries.get(0).hasLeaderLines = true;

            // Calculate chart
            chart.calculate();

            // You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
            const DELTA = 100;
            const series0 = chart.nSeries.get(0);
            for (let i = 0; i < series0.points.count; i++) {
                const pt = series0.points.get(i);
                let X = pt.dataLabels.x;
                // If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
                if (X > 2000)
                    pt.dataLabels.x = X + DELTA;
                else
                    pt.dataLabels.x = X - DELTA;
            }

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

最后，以下代码将图表保存为图像格式，将工作簿保存为XLSX格式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Pie Chart Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none; margin-right: 10px;">Download Excel File</a>
        <a id="downloadImageLink" style="display: none;">Download Chart Image</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // If a file is provided, load it. Otherwise create a new workbook in XLSX format.
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook(AsposeCells.FileFormatType.Xlsx);
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add two columns of data
            worksheet.cells.get("A1").putValue("Retail");
            worksheet.cells.get("A2").putValue("Services");
            worksheet.cells.get("A3").putValue("Info & Communication");
            worksheet.cells.get("A4").putValue("Transport Equip");
            worksheet.cells.get("A5").putValue("Construction");
            worksheet.cells.get("A6").putValue("Other Products");
            worksheet.cells.get("A7").putValue("Wholesale");
            worksheet.cells.get("A8").putValue("Land Transport");
            worksheet.cells.get("A9").putValue("Air Transport");
            worksheet.cells.get("A10").putValue("Electric Appliances");
            worksheet.cells.get("A11").putValue("Securities");
            worksheet.cells.get("A12").putValue("Textiles & Apparel");
            worksheet.cells.get("A13").putValue("Machinery");
            worksheet.cells.get("A14").putValue("Metal Products");
            worksheet.cells.get("A15").putValue("Cash");
            worksheet.cells.get("A16").putValue("Banks");

            worksheet.cells.get("B1").putValue(10.4);
            worksheet.cells.get("B2").putValue(5.2);
            worksheet.cells.get("B3").putValue(6.4);
            worksheet.cells.get("B4").putValue(10.4);
            worksheet.cells.get("B5").putValue(7.9);
            worksheet.cells.get("B6").putValue(4.1);
            worksheet.cells.get("B7").putValue(3.5);
            worksheet.cells.get("B8").putValue(5.7);
            worksheet.cells.get("B9").putValue(3);
            worksheet.cells.get("B10").putValue(14.7);
            worksheet.cells.get("B11").putValue(3.6);
            worksheet.cells.get("B12").putValue(2.8);
            worksheet.cells.get("B13").putValue(7.8);
            worksheet.cells.get("B14").putValue(2.4);
            worksheet.cells.get("B15").putValue(1.8);
            worksheet.cells.get("B16").putValue(10.1);

            // Create a pie chart and add it to the collection of charts
            const id = worksheet.charts.add(AsposeCells.ChartType.Pie, 3, 3, 23, 13);

            // Access newly created Chart instance
            const chart = worksheet.charts.get(id);

            // Set series data range
            chart.nSeries.add("B1:B16", true);

            // Set category data range
            chart.nSeries.categoryData = "A1:A16";

            // Turn off legend
            chart.showLegend = false;

            // Access data labels
            const dataLabels = chart.nSeries.get(0).dataLabels;

            // Turn on category names
            dataLabels.showCategoryName = true;

            // Turn on percentage format
            dataLabels.showPercentage = true;

            // Set position
            dataLabels.position = AsposeCells.LabelPositionType.OutsideEnd;

            // Set separator
            dataLabels.separatorType = AsposeCells.DataLabelsSeparatorType.Comma;

            // In order to save the chart image, create an instance of ImageOrPrintOptions
            const anOption = new AsposeCells.ImageOrPrintOptions();

            // Set image format
            anOption.imageType = AsposeCells.ImageType.Png;

            // Set resolution
            anOption.horizontalResolution = 200;
            anOption.verticalResolution = 200;

            // Render chart to image (returns image byte array in browser)
            const imageData = chart.toImage(anOption);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            const downloadImageLink = document.getElementById('downloadImageLink');
            downloadImageLink.href = URL.createObjectURL(imageBlob);
            downloadImageLink.download = 'output_out.png';
            downloadImageLink.style.display = 'inline-block';
            downloadImageLink.textContent = 'Download Chart Image';

            // Save the workbook to see chart inside the Excel
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart created and files are ready. Click the download links to get the results.</p>';
        });
    </script>
</html>
```

|**结果饼图**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **高级主题**
- [饼图中自定义切片或区块颜色](/cells/zh/javascript-cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [查找数据点是否在饼图的第二个饼图或柱状图的柱状图上](/cells/zh/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## 相关文章

- [创建图表](/cells/zh/javascript-cpp/creating-charts/)
- [自定义图表](/cells/zh/javascript-cpp/customizing-charts/)
- [图表中的数据格式化](/cells/zh/javascript-cpp/data-formatting-in-charts/)
- [设置图表外观](/cells/zh/javascript-cpp/setting-chart-appearance/)
