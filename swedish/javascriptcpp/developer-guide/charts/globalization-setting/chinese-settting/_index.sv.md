---
title: Konvertera diagram till bild för kinesiska regioner med JavaScript via C++
description: Lär dig hur du använder Aspose.Cells for JavaScript via C++ för att konfigurera diagram för kinesiska tecken och format, inklusive typsnitt, storlekar, textriktningar och mer.
keywords: Aspose.Cells for JavaScript via C++, diagram, kinesisk konfiguration, typsnitt, teckenstorlek, textriktning, stöd.
linktitle: Ställ in kinesisk region
type: docs
weight: 9
url: /sv/javascript-cpp/convert-chart-to-image-for-chinese-region/
alias: [/javascript-cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}  
I det här ämnet kommer vi att visa dig hur du ställer in kinesisk region för ett diagram.  
{{% /alert %}}  

## **Definierar en arvs klass**  

 Första steget, du måste definiera en klass "ChartChineseSetttings" som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/).  
Sedan, genom att omdefiniera relaterade funktioner, kan du ange texten i diagramelementen på ditt eget sprak.  
Kodexempel:  
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

## **Konfigurera kinesiska inställningar för diagram**  

I det här steget kommer du att använda klassen "ChartChineseSetttings" du har definierat i det föregående steget.  
Kodexempel:  

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

Sedan kan du se effekten i utdata bilden, elementen i diagrammet kommer att renderas enligt dina inställningar.  

## **Slutsats**  

I det här exemplet, om du inte ställer in kinesisk region för ett diagram, kan följande diagramelement renderas på det vanliga språket, såsom engelska.  
Efter ovanstående åtgärd kan vi få en utmatningsdiagrambild med kinesisk region.  

|**Stödda element**|**Värde i detta exempel**|**Standardvärde i den engelska miljön**|  
| :- | :- | :- |  
|Axel Titel Namn|坐标轴标题|Axis Title|  
|axelenhetsnamn|百,千...|Hundratals, Tusentals...|  
|Diagram Titel Namn|图表标题|Chart Title|  
|Legend Öka Namn|增加|Increase|  
|Legend Minska Namn|减少|Decrease|  
|Legend Total Namn|汇总|Total|  
|Annat Namn|其他|Other|  
|Serienamn|系列|Series|
