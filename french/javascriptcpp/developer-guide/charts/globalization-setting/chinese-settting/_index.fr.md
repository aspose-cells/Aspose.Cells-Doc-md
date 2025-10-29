---
title: Convertir un graphique en image pour la région chinoise avec JavaScript via C++
description: Apprenez comment utiliser Aspose.Cells for JavaScript via C++ pour configurer des graphiques pour les caractères et formats chinois, y compris les polices, tailles, directions du texte et plus encore.
keywords: Aspose.Cells for JavaScript via C++, Graphiques, Configuration chinoise, Polices, Taille de police, Direction du texte, Support.
linktitle: Définir la région chinoise
type: docs
weight: 9
url: /fr/javascript-cpp/convert-chart-to-image-for-chinese-region/
alias: [/javascript-cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}  
Dans ce sujet, nous vous montrerons comment définir la région chinoise pour un graphique.  
{{% /alert %}}  

## **Définit une classe d'héritage**  

Première étape, vous devez définir une classe "ChartChineseSetttings" qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/).  
Ensuite, en réécrivant les fonctions liées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.  
Exemple de code :  
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

## **Configurer les paramètres chinois pour le graphique**  

À cette étape, vous utiliserez la classe "ChartChineseSetttings" que vous avez définie lors de l'étape précédente.  
Exemple de code :  

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

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus selon vos paramètres.  

## **Conclusion**  

Dans cet exemple, si vous ne définissez pas la région chinoise pour un graphique, les éléments du graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.  
Après l'opération ci-dessus, nous pouvons obtenir une image de graphique de sortie avec une région chinoise.  

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|  
| :- | :- | :- |  
|Nom du titre de l'axe|坐标轴标题|Titre de l'axe|  
|Nom de l'unité de l'axe|百,千...|Centaines, Milliers...|  
|Nom du titre du graphique|图表标题|Titre du graphique|  
|Nom de Légende Augmentation|增加|Augmentation|  
|Nom de Légende Diminution|减少|Diminution|  
|Nom de Légende Total|汇总|Total|  
|Autre Nom|其他|Autre|  
|Nom de Série|系列|Série|
