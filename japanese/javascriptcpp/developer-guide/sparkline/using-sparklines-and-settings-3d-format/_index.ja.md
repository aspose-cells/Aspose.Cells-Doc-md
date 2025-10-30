---
title: JavaScriptを使用したスパークラインと3Dフォーマットの設定
linktitle: スパークラインと設定3Dフォーマットの使用
type: docs
weight: 40
url: /ja/javascript-cpp/using-sparklines-and-settings-3d-format/
description: スパークラインの使用と3Dフォーマットの適用方法をC++のAspose.Cells for Javaスクリプトで学習します。 
---

## **スパークラインの使用**
Microsoft Excel 2010では、これまで以上に情報をさまざまな方法で分析できます。新しいデータ分析および可視化ツールを使用して重要なデータトレンドを追跡および強調することができます。スパークラインは、表内に配置してデータとグラフを同時に表示できるミニチャートです。スパークラインを適切に使用すると、データ分析が迅速かつ的確になります。また、情報のシンプルな表示を提供し、多くの複雑なチャートでワークシートが過度に混雑するのを避けることもできます。

C++のAspose.Cells for Javaスクリプトは、スプレッドシート内のスパークラインを操作するAPIを提供します。
### **Microsoft Excelでのスパークライン**
Microsoft Excel 2010にスパークラインを挿入するには:

1. スパークラインが表示されるセルを選択します。視覚的にわかりやすくするため、データの横のセルを選択します。
1. リボンの**挿入**を選択し、**スパークライン**グループで**列**を選択します。
1. ワークシートに含まれるソースデータのセル範囲を選択または入力します。チャートが表示されます。

スパークラインは、例えばソフトボールリーグの勝敗記録などのトレンドを見るのに役立ちます。スパークラインは、リーグ内の各チームのシーズン全体を要約することさえできます。
### **C++のAspose.Cells for Javaスクリプトを使用したスパークライン**
開発者は、C++のAspose.Cells for Javaスクリプトが提供するAPIを使用して、テンプレートファイル内のスパークラインを作成、削除、読み取りできます。スパークラインを管理するクラスは[SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/)モジュールに含まれているため、これらの機能を使用する前にこのモジュールを読み込む必要があります。

指定されたデータ範囲にカスタムグラフィックスを追加することで、開発者は選択したセル領域に異なる種類の小さなチャートを追加する自由があります。

以下の例は、スパークライン機能を示しています。この例では次のことを示しています:

1. 簡単なテンプレートファイルを開きます。
1. ワークシートのスパークライン情報を読み取ります。
1.指定されたデータ範囲に新しいスパークラインをセル領域に追加します。
1. Excelファイルをディスクに保存します。


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
## **3Dフォーマットの設定**
状況に応じて結果だけを得るために3Dチャートスタイルが必要になる場合があります。C++のAspose.Cells for Javaスクリプトは、Microsoft Excel 2007の3Dフォーマットを適用するための関連APIを提供します。

Microsoft Excel 2007の3Dフォーマットを適用する方法を示す完全な例が以下に示されています。例のコードを実行すると、ワークシートに3D効果のある列グラフが追加されます。


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
