---
title: 使用 C++ 操作带有 JavaScript 的图表中的形状
linktitle: 图表中的形状
description: 学习如何使用 Aspose.Cells for JavaScript 通过 C++ 添加控件并自定义 Microsoft Excel 中的图表。本指南演示如何操作图表元素、调整格式以及增强图表的整体外观和可用性。
keywords: 通过 C++ 使用 Aspose.Cells for JavaScript，图表控件，图表自定义，Microsoft Excel，图表元素，格式化。
type: docs
weight: 70
url: /zh/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
有时需要在图表中插入标签、文本框、图片等绘图对象。Aspose.Cells 可以在运行时向图表中添加控件。
{{% /alert %}}

## **向图表添加标签控件**

标签提供了向用户提供关于电子表格内容的信息的方法。Aspose.Cells 允许您甚至在图表中添加和操作标签。

[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/)类提供了一个名为[**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-)的方法，用于向图表添加标签控件。以下是该方法使用的参数列表：

- **top** – 以图表区域的1/4000单位为垂直偏移的标签。
- **left** – 以图表区域的1/4000单位为水平偏移的标签。
- **height** – 标签的高度，以图表区域的1/4000单位为单位。
- **width** – 标签的宽度，单位为图表区域的1/4000。

该方法返回[**Label**](https://reference.aspose.com/cells/javascript-cpp/label/)对象。[**Label**](https://reference.aspose.com/cells/javascript-cpp/label/)类代表图表中的标签，具有一些重要成员：

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--)（属性）– 指定标签的标题字符串。
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--)（属性）– 指定填充颜色属性。

以下示例演示如何向图表添加标签。示例使用了一个设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用此文件向图表插入标签。以下是添加标签到图表的原始代码。执行该代码时生成以下输出。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Label In Chart Example</title>
    </head>
    <body>
        <h1>Add Label In Chart Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new label to the chart.
            const label = chart.shapes.addLabelInChart(100, 100, 350, 900);

            // Set the caption of the label.
            label.text = "A Label In Chart";

            // Set the Placement Type, the way the Label is attached to the cells.
            label.placement = AsposeCells.PlacementType.FreeFloating;

            // Save the excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Label added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **将文本框控件添加到图表**

在报告中突出显示重要信息的一种方法是使用文本框。例如，输入文本以突出显示公司名称或指示销售额最高的地理区域。[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/)类提供了一个名为[**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-)的方法，用于向图表添加文本框控件。以下是该方法使用的参数列表：

- **top** – 文本框与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 文本框距离图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **height** – 文本框的高度，单位为图表区域的1/4000。
- **width** – 文本框的宽度，单位为图表区域的1/4000。

该方法返回一个 [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) 对象。[**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) 类表示图表中的文本框。

以下示例显示了如何向图表添加文本框。该示例使用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入文本框以显示图表标题。以下是添加文本框到图表的原始代码。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new textbox to the chart.
            const textbox0 = chart.shapes.addTextBoxInChart(100, 1100, 350, 2550);

            // Fill the text.
            textbox0.text = "Sales By Region";

            // Get the textbox text frame.
            // const textframe0 = textbox0.textFrame;

            // Set the textbox to adjust it according to its contents.
            // textframe0.autoSize = true;

            // Set the font color.
            textbox0.font.color = AsposeCells.Color.Maroon;

            // Set the font to bold.
            textbox0.font.isBold = true;

            // Set the font size.
            textbox0.font.size = 14;

            // Set font attribute to italic.
            textbox0.font.isItalic = true;

            // Get the fill format of the textbox.
            const fillformat = textbox0.fill;

            // Get the line format type of the textbox.
            const lineformat = textbox0.line;

            // Set the line weight.
            lineformat.weight = 2;

            // Set the dash style to solid.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **向图表添加图片**

Aspose.Cells 允许您将图像插入到图表中。例如，添加一张图片以强调或赋予图表或其内容更多的含义，或者插入一个品牌图片文件。

[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) 类提供了一个名为 [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) 的方法，用于向图表添加图片对象。以下是该方法使用的参数列表。

- **top** – 图片与图表区域左上角的垂直偏移量，单位为图表区域的1/4000。
- **left** – 图片与图表区域左上角的水平偏移量，单位为图表区域的1/4000。
- **stream** - 一个包含图像数据的流对象。
- **widthScale** - 图像宽度的比例值，以百分比表示。
- **heightScale** - 图像高度的比例值，以百分比表示。

该方法返回一个 [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) 对象。[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) 类表示图表中的图片对象。

以下示例显示了如何向图表添加图片。该示例利用之前的设计文件（**exp_piechart.xls**），其中包含一个图表。我们使用这个文件向图表中插入图片。以下是添加图片到图表的原始代码。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture to Chart</title>
    </head>
    <body>
        <h1>Add Picture to Chart Example</h1>
        <p>Select an Excel file and an image to add to the first chart in the first worksheet.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            if (!fileInput.files.length || !imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file and an image file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const imageFile = imageInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const imageBuffer = await imageFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first sheet.
            const sheet = workbook.worksheets.get(0);
            const chart = sheet.charts.get(0);

            // Add a new picture to the chart.
            const pic0 = chart.shapes.addPictureInChart(50, 50, new Uint8Array(imageBuffer), 40, 40);

            // Get the lineformat type of the picture.
            const lineformat = pic0.line;

            // Set the dash style.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Set the line weight.
            lineformat.weight = 4;

            // Save the modified Excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Picture added to chart successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **在图表中添加复选框**

Aspose.Cells 允许您通过使用 [**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/) 枚举向图表工作表中插入复选框。以下示例演示了向图表工作表添加复选框。

以下图像显示了输出文件中带有复选框的图表工作表。

![todo:image_alt_text](controls-in-charts_1.jpg)

以下代码片段生成的[输出文件](101089316.xlsx)已附上，供您参考。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Checkbox in Chart Sheet Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Insert Checkbox in Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            // This example creates a new workbook and inserts a chart sheet with a checkbox in the chart.
            // The file input is optional for this example (a new workbook is created regardless).

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a chart sheet to the workbook
            const index = workbook.worksheets.add(AsposeCells.SheetType.Chart);

            // Access the newly added chart sheet
            const sheet = workbook.worksheets.get(index);

            // Add a floating column chart to the chart sheet
            sheet.charts.addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);

            // Add nSeries to the chart (single series with values 1,2,3)
            sheet.charts.get(0).nSeries.add("{1,2,3}", false);

            // Add checkbox to the chart
            sheet.charts.get(0).shapes.addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);

            // Set text of the checkbox shape
            sheet.charts.get(0).shapes.get(0).text = "CheckBox 1";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertCheckboxInChartSheet_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart sheet with checkbox created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [向图表添加艺术字水印](/cells/zh/javascript-cpp/add-wordart-watermark-to-chart/)
