---
title: JavaScriptとC++を使用したティックラベルの方向変更方法
linktitle: 目盛りラベル方向の変更
description: C++を使用したAspose.Cells for JavaScriptでのティックラベルの方向調整方法を学習しましょう。軸上のティックラベルの向き（水平・垂直・角度付き）を調整する方法について理解を深めます。
keywords: C++を使用したAspose.Cells for JavaScriptによるティックラベル、方向、向き、軸、水平、垂直、角度付き
type: docs
weight: 170
url: /ja/javascript-cpp/change-tick-label-direction/
---

## **目盛りラベル方向の変更**

Aspose.Cellsは、[**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--)プロパティを使用してチャートのティックラベルの向きを変更する機能を提供します。[**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--)プロパティは[**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype)列挙値を受け入れます。[**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype)列挙には次のメンバーが含まれます：

－ 水平
－ 垂直
－ Rotate90
－ Rotate270
－ スタック

次の画像は、ソースファイルと出力ファイルを比較したものです。

### **ソースファイル画像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **出力ファイル画像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

次のコードスニペットは、Rotate90から水平への目盛りラベルの方向を変更します。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

ソースファイルと出力ファイルは、以下のリンクからダウンロードできます。

[ソースファイル](105480221.xlsx)

[出力ファイル](105480223.xlsx)
