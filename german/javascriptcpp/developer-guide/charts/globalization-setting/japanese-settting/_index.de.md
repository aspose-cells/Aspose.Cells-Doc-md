---
title: Diagramm in ein Bild für die japanische Region mit JavaScript via C++ konvertieren
description: Lernen Sie, wie man Aspose.Cells for JavaScript mittels C++ verwendet, um die japanische Konfiguration für das Diagramm einzustellen. Unser Leitfaden zeigt, wie man Diagramme konfiguriert, um japanische Zeichen und Formatierungen zu unterstützen, einschließlich Schriftarten, Größe, Textrichtung und mehr.  
keywords: Aspose.Cells for JavaScript via C++, Diagramme, Japanische Konfiguration, Schriftart, Schriftgröße, Textrichtung, Unterstützung.  
linktitle: Japanische Region festlegen  
type: docs  
weight: 10  
url: /de/javascript-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/javascript-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
In diesem Thema zeigen wir Ihnen, wie Sie die japanische Region für ein Diagramm festlegen können.  
{{% /alert %}}  

## **Definiert eine Vererbungsklasse**  

Der erste Schritt besteht darin, eine Klasse "ChartJapaneseSettings" zu definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) erbt.  
Dann können Sie durch Neudefinition der entsprechenden Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.  
Codebeispiel:  
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

## **Japanische Einstellung für Diagramm konfigurieren**  

In diesem Schritt verwenden Sie die Klasse "ChartJapaneseSettings", die Sie im vorherigen Schritt definiert haben.  
Codebeispiel:  

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

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.  

## **Fazit**  

In diesem Beispiel, wenn Sie für ein Diagramm keine japanische Region festlegen, können die folgenden Diagrammelemente in der Standardsprache gerendert werden, wie zum Beispiel Englisch.  
Nach obiger Operation können wir ein Ausgabediagrammbild mit japanischer Region erhalten.  

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|  
| :- | :- | :- |  
|Achsentitelname|軸タイトル|Achsentitel|  
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|  
|Diagramm-Titelname|グラフ タイトル|Diagrammtitel|  
|Legende Anstiegsname|ぞうか|Erhöhen|  
|Legende Abnahmename|削減|Abnehmen|  
|Legende Gesamtname|すべての|Gesamt|  
|Andere Bezeichnung|その他|Andere|  
|Serienname|シリーズ|Serie|
