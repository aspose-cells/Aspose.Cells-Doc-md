---
title: JavaScriptをC++経由で使用して、円のグラフの第2の円または棒のポイントが含まれているかどうかを確認する方法  
linktitle: パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける  
description: C++を使ったAspose.Cells for JavaScriptを使用して、円のグラフの第2の円または棒にデータポイントが含まれているかどうかを確認する方法を学びます。このガイドでは、複合グラフの二次円または棒にアクセスし、分析とデータ操作を効果的に行う方法を示します。  
keywords: C++を使用したAspose.Cells for JavaScript, 円のグラフ, 棒の円グラフ, 第二の円, 第二の棒, データ分析, データ操作。  
type: docs  
weight: 180  
url: /ja/javascript-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/  
---  

## **可能な使用シナリオ**  
 seriesのデータポイントが**円グラフの第2の円**または**棒の棒グラフ**内にあるかどうかをAspose.Cells for JavaScriptを使って確認できます。[ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) プロパティを利用してください。  

以下のサンプルコードと[サンプルExcelファイル](5115193.xlsx)をダウンロードし、そのコンソール出力を確認してください。Excelファイルを開くと、すべての値が10未満のデータポイントが*Bar of Pie*チャートの棒内にあることがわかります。  
## **パイオブパイチャートまたはバーオブパイチャートでデータポイントが第2パイまたは棒にあるかどうかを見つける**  
次のサンプルコードは、*Pie of Pie*または*Bar of Pie*チャートの第二の円または棒内にデータポイントがあるかどうかを確認する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Bar of Pie Chart Data Points Example</h1>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., PieBars.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first chart which is Bar of Pie chart and calculate it
            const chart = worksheet.charts.get(0);
            chart.calculate();

            // Access the chart series
            const series = chart.nSeries.get(0);

            // Iterate and collect output
            let outputLines = [];
            for (let i = 0; i < series.points.count; i++) {
                // Access chart point
                const chartPoint = series.points.get(i);

                // Skip null values
                if (chartPoint.yValue === null) continue;

                // Print the chart point value and see if it is inside bar or pie.
                // If the IsInSecondaryPlot is true, then the data point is inside bar 
                // otherwise it is inside the pie. 
                const valueLine = "Value: " + chartPoint.yValue;
                const inSecondaryLine = "IsInSecondaryPlot: " + chartPoint.isInSecondaryPlot();
                console.log(valueLine);
                console.log(inSecondaryLine);
                console.log();

                outputLines.push(valueLine);
                outputLines.push(inSecondaryLine);
                outputLines.push("");
            }

            if (outputLines.length === 0) {
                resultDiv.innerHTML = '<p style="color: orange;">No data points found or all values are null.</p>';
            } else {
                resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
            }
        });
    </script>
</html>
```  
## **コンソール出力**  
上記のサンプルコードと[サンプルExcelファイル](5115193.xlsx)の実行後に生成されるコンソール出力を参照してください。 [ChartPoint.isInSecondaryPlot()](https://reference.aspose.com/cells/javascript-cpp/chartpoint/#isInSecondaryPlot--) が**false**の場合、そのデータポイントは円の内側にあり、**true**の場合は棒の内側にあります。  

{{< highlight javascript >}}  
 Value: 15  
IsInSecondaryPlot: false  

Value: 9  
IsInSecondaryPlot: true  

Value: 2  
IsInSecondaryPlot: true  

Value: 40  
IsInSecondaryPlot: false  

Value: 5  
IsInSecondaryPlot: true  

Value: 4  
IsInSecondaryPlot: true  

Value: 25  
IsInSecondaryPlot: false  
{{< /highlight >}}
