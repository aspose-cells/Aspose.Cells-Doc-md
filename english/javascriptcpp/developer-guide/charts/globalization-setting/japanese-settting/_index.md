---  
title: Convert Chart to Image for Japanese Region with JavaScript via C++  
description: Learn how to use Aspose.Cells for JavaScript via C++ to set the Japanese configuration for the chart. Our guide will demonstrate how to configure charts to support Japanese characters and formatting, including fonts, size, text direction, and more.  
keywords: Aspose.Cells for JavaScript via C++, Charts, Japanese configuration, font, font size, text direction, support.  
linktitle: Set Japanese Region  
type: docs  
weight: 10  
url: /javascript-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/javascript-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In this topic, we will show you how to set Japanese region for a chart.  
{{% /alert %}}  

## **Defines an Inheriting Class**  

In the first step, you need to define a class **ChartJapaneseSettings** that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/).  
Then, by rewriting the related functions, you can set the text of the chart elements in your own language.  
Code example:  
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

            // Example: show axis title name, chart title name, and a sample axis unit name
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

## **Configure Japanese Settings for Chart**  

In this step, you will use the class **ChartJapaneseSettings** you defined in the previous step.  
Code example:  

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

Then you can see the effect in the output image; the elements in the chart will be rendered according to your settings.  

## **Conclusion**  

In this example, if you do not set the Japanese region for a chart, the following chart elements may be rendered in the default language, such as English.  
After the above operation, you can get an output chart picture with Japanese region settings.  

| **Supported elements** | **Value in this example** | **Default value in the English environment** |
| :- | :- | :- |
| Axis Title Name | 軸タイトル | Axis Title |
| Axis Unit Name | 百,千... | Hundreds, Thousands... |
| Chart Title Name | グラフ タイトル | Chart Title |
| Legend Increase Name | ぞうか | Increase |
| Legend Decrease Name | 削減 | Decrease |
| Legend Total Name | すべての | Total |
| Other Name | その他 | Other |
| Series Name | シリーズ | Series |