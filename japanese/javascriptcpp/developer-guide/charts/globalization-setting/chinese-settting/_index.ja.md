---
title: JavaScriptを使って中国地域用のチャートを画像に変換（C++経由）
description: Aspose.Cells for JavaScriptを使って、中国文字やフォーマット（フォント、サイズ、テキスト方向など）の設定方法を学びます。
keywords: Aspose.Cells for JavaScriptを使ったC++、チャート、中国語設定、フォント、フォントサイズ、テキスト方向、サポート。
linktitle: 中国地域を設定する
type: docs
weight: 9
url: /ja/javascript-cpp/convert-chart-to-image-for-chinese-region/
alias: [/javascript-cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}  
このトピックでは、チャートの中国地域を設定する方法を示します。  
{{% /alert %}}  

## **継承クラスを定義する**  

最初のステップでは、[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/)から継承する"ChartChineseSetttings"クラスを定義する必要があります。  
その後、関連する関数を書き換えることで、チャート要素のテキストを独自の言語で設定できます。  
コード例:  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Chart Globalization Settings (Chinese) Example</h1>
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

        class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
            get axisTitleName() {
                return "坐标轴标题";
            }

            axisUnitName(type) {
                switch (type) {
                    case AsposeCells.DisplayUnitType.None:
                        return '';
                    case AsposeCells.DisplayUnitType.Hundreds:
                        return '百';
                    case AsposeCells.DisplayUnitType.Thousands:
                        return '千';
                    case AsposeCells.DisplayUnitType.TenThousands:
                        return '万';
                    case AsposeCells.DisplayUnitType.HundredThousands:
                        return '十万';
                    case AsposeCells.DisplayUnitType.Millions:
                        return '百万';
                    case AsposeCells.DisplayUnitType.TenMillions:
                        return '千万';
                    case AsposeCells.DisplayUnitType.HundredMillions:
                        return '亿';
                    case AsposeCells.DisplayUnitType.Billions:
                        return '十亿';
                    case AsposeCells.DisplayUnitType.Trillions:
                        return '兆';
                    default:
                        return '';
                }
            }

            get chartTitleName() {
                return "图表标题";
            }

            get legendDecreaseName() {
                return "减少";
            }

            get legendIncreaseName() {
                return "增加";
            }

            get legendTotalName() {
                return "汇总";
            }

            get otherName() {
                return "其他";
            }

            get seriesName() {
                return "系列";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (optional). This example will demonstrate the ChartChineseSettings regardless.</p>';
            }

            const settings = new ChartChineseSettings();

            const lines = [];
            lines.push(`<p><strong>axisTitleName:</strong> ${settings.axisTitleName}</p>`);
            lines.push(`<p><strong>chartTitleName:</strong> ${settings.chartTitleName}</p>`);
            lines.push(`<p><strong>legendDecreaseName:</strong> ${settings.legendDecreaseName}</p>`);
            lines.push(`<p><strong>legendIncreaseName:</strong> ${settings.legendIncreaseName}</p>`);
            lines.push(`<p><strong>legendTotalName:</strong> ${settings.legendTotalName}</p>`);
            lines.push(`<p><strong>otherName:</strong> ${settings.otherName}</p>`);
            lines.push(`<p><strong>seriesName:</strong> ${settings.seriesName}</p>`);
            lines.push(`<p><strong>axisUnitName (Thousands):</strong> ${settings.axisUnitName(AsposeCells.DisplayUnitType.Thousands)}</p>`);
            lines.push(`<p><strong>axisUnitName (Millions):</strong> ${settings.axisUnitName(AsposeCells.DisplayUnitType.Millions)}</p>`);

            resultDiv.innerHTML = lines.join('');

            // If a file is provided, demonstrate opening it and (optionally) applying the settings.
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Apply the globalization settings to the workbook's chart globalization settings if available
                // (some environments may expose different integration points; this demonstrates usage)
                if (workbook.chartGlobalizationSettings !== undefined) {
                    workbook.chartGlobalizationSettings = settings;
                }

                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';
            }
        });
    </script>
</html>
```  

## **チャートの中国語設定を構成する**  

このステップでは、前のステップで定義した"ChartChineseSetttings"クラスを使用します。  
コード例:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartChineseSetttings } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Apply Chinese chart globalization settings
            workbook.settings.globalizationSettings = new ChartChineseSetttings();

            // Access the first worksheet and first chart
            const worksheet = workbook.worksheets.get(0);
            const chart0 = worksheet.charts.get(0);

            // Export chart to image (PNG)
            const imageData = chart0.toImage(SaveFormat.Png);

            // Create downloadable blob and link
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            resultDiv.innerHTML = '<p style="color: green;">Chart exported successfully! Click the download link to save the PNG.</p>';
        });
    </script>
</html>
```  

その後、出力イメージで効果を確認できます。チャートの要素は、設定に従ってレンダリングされます。  

## **結論**  

この例では、チャートに日本語の地域を設定しない場合、次のチャート要素はデフォルトの言語（英語など）でレンダリングされる場合があります。  
上記の操作を行った後、日本語の地域を設定した出力チャート画像を取得できます。  

|**サポートされる要素**|**この例の値**|**英語環境のデフォルト値**|  
| :- | :- | :- |  
| 軸タイトル名 | 坐標軸タイトル | 軸タイトル |  
|軸単位名|百,千...|Hundreds, Thousands...|  
| チャートタイトル名 | グラフタイトル | Chart Title |  
| 凡例の増加名 | 増加 | Increase |  
| 凡例の減少名 | 減少 | Decrease |  
| 凡例の合計名 | 汇总 | Total |  
| その他の名前 | その他 | Other |  
| 系列名 | 系列 | Series |
