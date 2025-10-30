---
title: JavaScriptを使用してC++でチャートに存在する軸を判定する
linktitle: チャートにどの軸が存在するかを判断する
description: C++を使用してAspose.Cells for JavaScriptで作成されたチャートにどの軸が存在するかを判別する方法を学びましょう。ガイドは、カテゴリ軸、値軸、セカンダリ軸を含む、チャート内の異なる軸を識別してアクセスするのに役立ちます。
keywords: Aspose.Cells for JavaScriptを使用したC++、チャート、軸、存在、カテゴリ、値、セカンダリ。それ
type: docs
weight: 140
url: /ja/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
時には、ユーザーは特定の軸がチャートに存在するかどうかを知る必要があります。例として、二次値軸がチャート内に存在するかどうかを知りたい場合などです。円グラフ、爆発円グラフ、パイパイ、パイバー、3Dパイ、3D爆発パイ、ドーナツ、爆発ドーナツなどの一部のグラフには軸がありません。  

Aspose.Cellsは、特定の軸がチャートに存在するかどうかを判断するための[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-)メソッドを提供します。  
{{% /alert %}}  

次のサンプルコードは、[**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-)を使用してサンプルチャートにプライマリおよびセカンダリのカテゴリ軸と値軸が存在するかどうかを判断する例です。  

## JavaScriptコードによるチャート内に存在する軸の判定方法

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## サンプルコードによって生成されたコンソール出力

コードのコンソール出力は以下の通りで、プライマリのカテゴリ軸と値軸にはtrue、セカンダリのカテゴリ軸と値軸にはfalseが表示されます。  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}
