---
title: C++を通じてExcelチャートの軸を管理する
description: C++を通じてAspose.Cells for JavaScriptでチャートの軸を設定する方法を学びます。私たちのガイドは、一次軸と二次軸の調整、範囲設定、プロパティの変更方法を示し、チャートを向上させます。
keywords: C++経由のAspose.Cells for JavaScriptによるスクリプト、チャート軸、設定、主要軸、副軸、範囲、プロパティ。
linktitle: 軸
type: docs
weight: 50
url: /ja/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

Excelチャートには、3種類の軸があります。  
1. 水平（カテゴリ）軸：X軸  
1. 垂直（値）軸：Y軸  
1. 深度（シリーズ）軸：Z軸  

{{% /alert %}}  

## **軸オプション**  
C++経由のAspose.Cells for JavaScriptは、ランタイム中にチャートの軸を管理することも可能です。 [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/) オブジェクトを使用して、Excelと同様に軸のすべてのオプションを変更できます。  

|![todo:image_alt_text](chart_axes.png)|  

## **X軸とY軸を管理する**  
Excelのチャートでは、水平方向と垂直方向の軸が最も一般的に使用される軸です。  

次のコードスニペットは、X軸とY軸のオプション設定方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **高度なトピック**  
- [目盛りラベル方向の変更](/cells/ja/javascript-cpp/change-tick-label-direction/)  
- [チャートに存在する軸を特定する](/cells/ja/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Microsoft Excelのようにチャートの軸の自動単位を処理する](/cells/ja/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [チャートを計算した後に軸ラベルを読み取る](/cells/ja/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Excelチャートでカテゴリ軸を設定する方法](/cells/ja/javascript-cpp/how-to-set-category-axis/)
