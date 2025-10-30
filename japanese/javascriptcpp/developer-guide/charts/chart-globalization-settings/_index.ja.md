---
title: JavaScript経由のC++でChartGlobalizationSettingsクラスを使用して、チャートコンポーネントの言語を設定する
linktitle: ChartGlobalizationSettingsクラスを使用して、チャートコンポーネントの異なる言語を設定する方法
description: C++経由のAspose.Cells for JavaScriptでChartGlobalizationSettingsクラスを使用し、チャート要素の多言語化について学びましょう。ガイドでは、チャートの要素、ラベル、凡例をローカライズする方法を説明します。
keywords: C++経由のAspose.Cells for JavaScriptによるチャート、チャートのグローバリゼーション、言語、ローカリゼーション、ChartGlobalizationSettings、要素、ラベル、凡例。
type: docs
weight: 2200
url: /ja/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **可能な使用シナリオ**  

Aspose.Cells APIは[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/)クラスを公開しており、これはユーザーがスプレッドシート内のチャートコンポーネントを異なる言語に設定し、小計のカスタムラベルも作成できるようにするためです。  

## **ChartGlobalizationSettingsクラスの紹介**  

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/)クラスは、現在8つのメソッドを提供しており、これらをカスタムクラスでオーバーライドして、軸タイトル名、軸単位名、チャートタイトル名などを異なる言語に翻訳できます。  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--)：軸タイトルの名前を取得します。  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-)：軸単位の名前を取得します。  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--)：チャートタイトルの名前を取得します。  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--)：凡例の減少の名前を取得します。  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--)：凡例の増加を示す名前を取得。  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--)：凡例の合計の名前を取得します。  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--)：チャートの「その他」ラベルの名前を取得します。  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--)：チャート内の系列の名前を取得します。  

### **カスタム言語の翻訳**  
以下、次のデータを元にウォーターフォールチャートを作成します。チャートコンポーネントの名前は、チャート内で英語で表示されます。チャートタイトル、凡例の増減名、合計名、および軸タイトルのトルコ語表示方法を示すためにトルコ語の例を使用します。  

![todo:image_alt_text](sample.png)  

## **サンプルコード**  
次のサンプルコードは、[サンプルExcelファイル](waterfall.xlsx)を読み込みます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Globalization Settings Example</title>
    </head>
    <body>
        <h1>Chart Globalization Settings Example (Turkey)</h1>
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

        // Define TurkeyChartGlobalizationSettings by converting getXxx methods to properties
        class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
            constructor() {
                super();
                this.chartTitleName = "Grafik Başlığı"; // Chart Title
                this.legendIncreaseName = "Artış"; // Increase
                this.legendDecreaseName = "Düşüş"; // Decrease
                this.legendTotalName = "Toplam"; // Total
                this.axisTitleName = "Eksen Başlığı"; // Axis Title
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: let errors propagate
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom chartGlobalizationSettings (Turkey)
            workbook.settings.globalizationSettings.chartSettings = new TurkeyChartGlobalizationSettings();

            // Access the first worksheet and its charts
            const worksheet = workbook.worksheets.get(0);
            const chartCollection = worksheet.charts;
            const chart = chartCollection.get(0);

            // Calculate the chart
            chart.calculate();

            // Get the chart title text
            const title = chart.title;
            const titleText = title ? title.text : "(No Title)";

            // Prepare output messages
            const messages = [];
            messages.push('<p style="color: green;">Operation completed successfully!</p>');
            messages.push(`<p>Workbook chart title: ${titleText}</p>`);

            // Get legend labels and output them
            const legendEntriesLabels = chart.legend.legendLabels;
            if (legendEntriesLabels && legendEntriesLabels.forEach) {
                const legendItems = [];
                legendEntriesLabels.forEach(label => {
                    legendItems.push(`<li>${label}</li>`);
                });
                if (legendItems.length) {
                    messages.push('<p>Workbook chart legend:</p>');
                    messages.push(`<ul>${legendItems.join('')}</ul>`);
                } else {
                    messages.push('<p>(No legend labels found)</p>');
                }
            } else {
                messages.push('<p>(No legend or legend labels available)</p>');
            }

            // Save modified workbook to allow download (optional)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = messages.join('');
        });
    </script>
</html>
```  

## サンプルコードによって生成された出力  

これは上記のサンプルコードのコンソール出力です。  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
