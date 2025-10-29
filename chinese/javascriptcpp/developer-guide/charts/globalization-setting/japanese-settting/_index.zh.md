---
title: 使用C++通过JavaScript将图表转为日本地区图片
description: 了解如何使用Aspose.Cells for JavaScript通过C++设置图表的日语配置。我们的指南将演示如何配置支持日语字符和格式，包括字体、大小、文本方向等。  
keywords: Aspose.Cells for JavaScript通过C++、图表、日语配置、字体、字体大小、文本方向、支持。  
linktitle: 设置日本地区  
type: docs  
weight: 10  
url: /zh/javascript-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/javascript-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
在本主题中，我们将向您展示如何为图表设置日本地区。  
{{% /alert %}}  

## **定义继承类**  

第一步，您需要定义一个继承自 [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) 的 "ChartJapaneseSettings" 类。  
然后，通过重写相关函数，您可以将图表元素的文本设置为您自己的语言。  
代码示例:  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Chart Globalization - Japanese Example</h1>
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

        // Converted class from JavaScript to browser-compatible JavaScript
        class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
            constructor() {
                super();
                // Parameterless getters converted to properties
                this.axisTitleName = "軸タイトル";
                this.chartTitleName = "グラフ タイトル";
                this.legendDecreaseName = "削減";
                this.legendIncreaseName = "ぞうか";
                this.legendTotalName = "すべての";
                this.otherName = "その他";
                this.seriesName = "シリーズ";
            }

            // Getter with parameter converted to a method with lowercase first letter (no 'get' prefix)
            axisUnitName(type) {
                switch (type) {
                    case AsposeCells.DisplayUnitType.None:
                        return '';
                    case AsposeCells.DisplayUnitType.Hundreds:
                        return "百";
                    case AsposeCells.DisplayUnitType.Thousands:
                        return "千";
                    case AsposeCells.DisplayUnitType.TenThousands:
                        return "万";
                    case AsposeCells.DisplayUnitType.HundredThousands:
                        return "10万";
                    case AsposeCells.DisplayUnitType.Millions:
                        return "百万";
                    case AsposeCells.DisplayUnitType.TenMillions:
                        return "千万";
                    case AsposeCells.DisplayUnitType.HundredMillions:
                        return "億";
                    case AsposeCells.DisplayUnitType.Billions:
                        return "10億";
                    case AsposeCells.DisplayUnitType.Trillions:
                        return "兆";
                    default:
                        return '';
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (optional for this demo).</p>';
                return;
            }

            // No try-catch per instructions; let errors propagate
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Example usage: instantiate the ChartJapaneseSettings and demonstrate properties/methods
            const settings = new ChartJapaneseSettings();

            // Example: show axis title name and chart title name and a sample axis unit name
            const axisTitle = settings.axisTitleName;
            const chartTitle = settings.chartTitleName;
            const sampleUnit = settings.axisUnitName(AsposeCells.DisplayUnitType.Thousands);

            document.getElementById('result').innerHTML = `
                <p><strong>axisTitleName:</strong> ${axisTitle}</p>
                <p><strong>chartTitleName:</strong> ${chartTitle}</p>
                <p><strong>axisUnitName(DisplayUnitType.Thousands):</strong> ${sampleUnit}</p>
                <p style="color: green;">ChartJapaneseSettings instantiated successfully.</p>
            `;

            // Additionally, demonstrate opening the provided file as a Workbook (no modifications)
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare a simple save to allow downloading the opened file back (unchanged)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```  

## **为图表配置日本设置**  

在此步骤中，您将使用上一节中定义的 "ChartJapaneseSettings" 类。  
代码示例:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart to Image</title>
    </head>
    <body>
        <h1>Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils, ChartJapaneseSettings } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Apply Japanese chart settings
            workbook.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();

            // Access the first chart in the first worksheet
            const chart0 = workbook.worksheets.get(0).charts.get(0);

            // Convert chart to image (PNG)
            const imageData = chart0.toImage(SaveFormat.Png);
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```

然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。  

## **结论**  

在此示例中，如果不为图表设置日本地区，则以下图表元素可能以默认语言（如英文）呈现。  
在上述操作后，我们可以获得一个具有日本区域的输出图表图片。  

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|  
| :- | :- | :- |  
|轴标题名称|軸タイトル|Axis Title|  
|轴单位名称|百,千...|Hundreds, Thousands...|  
|图表标题名称|グラフ タイトル|Chart Title|  
|图例增加名称|ぞうか|Increase|  
|图例减少名称|削減|Decrease|  
|图例总数名称|すべての|Total|  
|其它名称|その他|Other|  
|系列名称|シリーズ|Series|
