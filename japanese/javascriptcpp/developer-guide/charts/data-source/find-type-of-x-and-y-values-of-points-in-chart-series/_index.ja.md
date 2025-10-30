---
title: JavaScriptを使用してC++経由でチャートシリーズのポイントのX値とY値のタイプを見つける方法
linktitle: チャートシリーズのポイントのXおよびY値のタイプを検索する
description: Aspose.Cells for JavaScript via C++を使用して、チャートシリーズのポイントのX値とY値のタイプを判定する方法を学びましょう。このガイドでは、データ値の種類や、それらにアクセスし操作する方法を解説します。
keywords: Aspose.Cells for JavaScript via C++、チャート作成、X値、Y値、データタイプ、アクセス、操作、チャートシリーズ。
type: docs
weight: 150
url: /ja/javascript-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **可能な使用シナリオ**  
時には、シリーズ内のチャートポイントのX値とY値のタイプを知りたいことがあります。Aspose.Cells for JavaScript via C++は、この目的に`ChartPoint.XValueType`と`ChartPoint.YValueType`プロパティを提供しています。ただし、これらのプロパティを効果的に使用する前に`Chart.calculate()`メソッドを呼び出す必要があることに注意してください。  

## **チャートシリーズのX値とY値のタイプを検索する**  
 以下のサンプルコードは、[サンプルExcelファイル](64716905.xlsx)を読み込み、最初のワークシート内の最初のチャートにアクセスします。次に、`Chart.calculate()`メソッドを呼び出し、最初のチャートポイントのX値とY値のタイプを調べ、コンソールに出力します。参考のために下記のコンソール出力を参照してください。  

## **サンプルコード**  
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

## **コンソール出力**  

{{< highlight java >}}  
 X Value Type: IsString  

Y Value Type: IsNumeric  
{{< /highlight >}}
