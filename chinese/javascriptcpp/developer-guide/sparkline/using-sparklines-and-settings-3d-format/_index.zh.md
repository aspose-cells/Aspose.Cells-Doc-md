---
title: 使用 Sparklines 和三维格式设置 通过 C++ 的 JavaScript
linktitle: 使用Sparklines和设置3D格式
type: docs
weight: 40
url: /zh/javascript-cpp/using-sparklines-and-settings-3d-format/
description: 学习在 Excel 文件中如何使用 Sparklines 以及应用三维格式 设置，使用 Aspose.Cells for JavaScript 和 C++。 
---

## **使用迷你图**
Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。 Sparklines是迷你图，可以放置在单元格内，以便您可以在同一张表格中查看数据和图表。当Sparklines被正确使用时，数据分析更快捷、更简洁。它们还提供信息的简单视图，避免了拥挤的工作表和繁忙的图表。

Aspose.Cells for JavaScript 通过 C++ 提供了一套操作电子表格中的 Sparklines 的 API。
### **Microsoft Excel 中的迷你图**
如何在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了方便查看，选择数据旁边的单元格。
1. 在功能区上单击**插入**，然后在**迷你图**组中选择**柱**。
1. 选择或输入包含源数据的工作表中的单元格范围。图表将出现。

迷你图可帮助您查看趋势，例如垒球联赛的胜负记录。迷你图甚至可以总结联赛中每支队伍整个赛季的情况。
### **使用 Aspose.Cells for JavaScript 和 C++ 的 Sparklines**
开发者可以使用 Aspose.Cells for JavaScript 和 C++ 提供的 API 来创建、删除或读取模板文件中的 Sparklines。管理 Sparklines 的类包含在 [SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/) 模块中，使用这些功能前需引入该模块。

通过为给定的数据范围添加自定义图形，开发人员可以自由地向选定的单元区域添加不同类型的迷你图。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围向单元区域添加新的迷你图。
1. 将 Excel 文件保存到磁盘。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sparkline Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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

            // Instantiate a Workbook by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Read the Sparklines from the worksheet (if any)
            const sparklinesCount = sheet.sparklineGroups.count;
            let logHtml = '';
            for (let i = 0; i < sparklinesCount; i++) {
                const group = sheet.sparklineGroups.get(i);
                logHtml += `sparkline group: type:${group.type}, sparkline items count:${group.sparklines.count}<br/>`;
                const sparklineCount = group.sparklines.count;
                for (let j = 0; j < sparklineCount; j++) {
                    const sparkline = group.sparklines.get(j);
                    logHtml += `sparkline: row:${sparkline.row}, col:${sparkline.column}, dataRange:${sparkline.dataRange}<br/>`;
                }
            }

            // Add Sparklines
            // Define the CellArea D2:D10 (rows and columns are zero-based: D is column 4 -> index 4)
            const ca = CellArea.createCellArea(1, 4, 7, 4);
            // Add new Sparklines for a data range to a cell area
            const idx = sheet.sparklineGroups.add(SparklineType.Column, "Sheet1!B2:D8", false, ca);
            const newGroup = sheet.sparklineGroups.get(idx);
            // Create CellsColor and set color
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            newGroup.seriesColor = clr;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><div>' + logHtml + '</div>';
        });
    </script>
</html>
```
## **设置 3D 格式**
您可能需要 3D 图表样式以获得最佳效果。 Aspose.Cells for JavaScript 和 C++ 提供相关 API 以应用 Microsoft Excel 2007 3D 格式。

下面给出了一个完整的示例，演示如何创建图表并应用 Microsoft Excel 2007 的 3D 格式。执行示例代码后，工作表中将添加一个带有 3D 效果的柱状图。


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>3D Chart Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, BevelPresetType, PresetMaterialType, LightRigType } = AsposeCells;

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
            // Creating a new workbook
            const book = new Workbook();

            // Add a Data Worksheet
            const dataSheet = book.worksheets.add("DataSheet");

            // Add Chart Worksheet
            const sheet = book.worksheets.add("MyChart");

            // Put some values into the cells in the data worksheet
            dataSheet.cells.get("B1").value = 1;
            dataSheet.cells.get("B2").value = 2;
            dataSheet.cells.get("B3").value = 3;
            dataSheet.cells.get("A1").value = "A";
            dataSheet.cells.get("A2").value = "B";
            dataSheet.cells.get("A3").value = "C";

            // Define the Chart Collection
            const charts = sheet.charts;
            // Add a Column chart to the Chart Worksheet
            const chartSheetIdx = charts.add(ChartType.Column, 5, 0, 25, 15);

            // Get the newly added Chart
            const chart = book.worksheets.get(2).charts.get(0);

            // Set the background/foreground color for PlotArea/ChartArea
            chart.plotArea.area.backgroundColor = Color.White;
            chart.chartArea.area.backgroundColor = Color.White;
            chart.plotArea.area.foregroundColor = Color.White;
            chart.chartArea.area.foregroundColor = Color.White;

            // Hide the Legend
            chart.showLegend = false;

            // Add Data Series for the Chart
            chart.nSeries.add("DataSheet!B1:B3", true);
            // Specify the Category Data
            chart.nSeries.categoryData = "DataSheet!A1:A3";

            // Get the Data Series
            const ser = chart.nSeries.get(0);

            // Apply the 3-D formatting
            const spPr = ser.shapeProperties;
            const fmt3d = spPr.format3D;

            // Specify Bevel with its height/width
            const bevel = fmt3d.topBevel;
            bevel.type = BevelPresetType.Circle;
            bevel.height = 2;
            bevel.width = 5;

            // Specify Surface material type
            fmt3d.surfaceMaterialType = PresetMaterialType.WarmMatte;

            // Specify surface lighting type
            fmt3d.surfaceLightingType = LightRigType.ThreePoint;

            // Specify lighting angle
            fmt3d.lightingAngle = 20;

            // Specify Series background/foreground and line color
            ser.area.backgroundColor = Color.Maroon;
            ser.area.foregroundColor = Color.Maroon;
            ser.border.color = Color.Maroon;

            // Saving the modified Excel file and providing download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = '3d_format.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
