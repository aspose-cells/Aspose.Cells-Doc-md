---
title: Convert Chart to Image for Chinese Region with JavaScript via C++
description: Learn how to use Aspose.Cells for JavaScript via C++ to configure charts for Chinese characters and formats, including fonts, sizes, text directions, and more.
keywords: Aspose.Cells for JavaScript via C++, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: Set Chinese Region
type: docs
weight: 9
url: /javascript-cpp/convert-chart-to-image-for-chinese-region/
alias: [/javascript-cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}  
In this topic, we will show you how to set Chinese Region for a chart.  
{{% /alert %}}  

## **Defines an inheritance class**  

First step, you need to define a class "ChartChineseSetttings" that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/).  
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

## **Config Chinese Setting For Chart**  

In this step, you will use the class "ChartChineseSetttings" you defined in the previous step.  
Code example:  

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

Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.  

## **Conclusion**  

In this example, if you do not set Chinese Region for a chart, the following chart elements may be rendered in the default language, such as English.  
After the above operation, we can get an output chart picture with Chinese Region.  

|**Supported elements**|**Value in this example**|**default value in the English environment**|  
| :- | :- | :- |  
|Axis Title Name|坐标轴标题|Axis Title|  
|Axis Unit Name|百,千...|Hundreds, Thousands...|  
|Chart Title Name|图表标题|Chart Title|  
|Legend Increase Name|增加|Increase|  
|Legend Decrease Name|减少|Decrease|  
|Legend Total Name|汇总|Total|  
|Other Name|其他|Other|  
|Series Name|系列|Series|