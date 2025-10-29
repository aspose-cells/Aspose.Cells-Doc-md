---
title: Utiliser la classe ChartGlobalizationSettings pour définir différentes langues pour les composants du graphique avec JavaScript via C++
linktitle: Utilisation de la classe ChartGlobalizationSettings pour définir une langue différente pour le composant de graphique
description: Apprenez à utiliser la classe ChartGlobalizationSettings dans Aspose.Cells for JavaScript via C++ pour définir différentes langues pour les composants du graphique. Notre guide vous aidera à comprendre comment localiser les éléments du graphique, les étiquettes et les légendes.
keywords: Aspose.Cells for JavaScript via C++, création de graphiques, mondialisation du graphique, langues, localisation, ChartGlobalizationSettings, éléments, étiquettes, légendes.
type: docs
weight: 2200
url: /fr/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Scénarios d'utilisation possibles**  

Les API Aspose.Cells ont exposé la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) pour gérer les scenarios où l'utilisateur souhaite configurer les composants du graphique en différentes langues et créer des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul.  

## **Introduction à la classe ChartGlobalizationSettings**  

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) propose actuellement les 8 méthodes suivantes qui peuvent être surchargées dans une classe personnalisée pour traduire, par exemple, le nom de AxisTitle, le nom de AxisUnit, le nom de ChartTitle, etc., dans différentes langues.  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--) : Obtient le nom du titre de l'axe.  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-) : Obtient le nom de l'unité d'axe.  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--) : Obtient le nom du titre du graphique.  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--) : Obtient le nom de la diminution pour la légende.  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--) : obtient le nom de Increase pour la légende.  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--) : Obtient le nom du total pour la légende.  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--) : Obtient le nom des étiquettes "Autre" pour le graphique.  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--) : Obtient le nom des séries dans le graphique.  

### **Traduction personnalisée**  
Voici, nous allons créer un graphique en cascade basé sur les données suivantes. Les noms des composants du graphique seront affichés en anglais dans le graphique. Nous utiliserons un exemple de langue turque pour montrer comment afficher le titre du graphique, les noms d'augmentation/diminution de la légende, le nom total et le titre de l'axe en turc.   

![todo:image_alt_text](sample.png)  

## **Code d'exemple**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](waterfall.xlsx).  

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

## Sortie générée par le code d'exemple  

Il s'agit de la sortie de la console du code d'exemple ci-dessus.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
