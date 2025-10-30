---
title: Gestione degli assi nei grafici di Excel con JavaScript tramite C++
description: Impara come configurare gli assi dei grafici in Aspose.Cells for JavaScript tramite C++. La nostra guida ti mostrerà come regolare gli assi primario e secondario, impostare i loro intervalli e modificare le loro proprietà per migliorare i tuoi grafici.
keywords: Script via C++, assi, assi degli grafici, configurazione, assi principali, assi secondari, intervallo, proprietà.
linktitle: Assi
type: docs
weight: 50
url: /it/javascript-cpp/chart-axes/
---

{{% alert color="primary" %}}  

Nei grafici Excel, ci sono 3 tipi di assi:  
1. Asse Orizzontale (Categoria): Asse X  
1. Asse verticale (valore): asse Y  
1. Asse di profondità (serie): asse Z  

{{% /alert %}}  

## **Opzioni dell'asse**  
Script via C++ consente anche di gestire gli assi del grafico in fase di esecuzione. Con l'oggetto [Axis](https://reference.aspose.com/cells/javascript-cpp/axis/) puoi modificare tutte le opzioni dell'asse come fatto in Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Gestisci gli assi X e Y**  
 Nel grafico di Excel, gli assi orizzontale e verticale sono i due assi più popolari da usare.  

Il seguente esempio di codice dimostra come impostare le opzioni degli assi X e Y.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart Axes</title>
    </head>
    <body>
        <h1>Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType } = AsposeCells;

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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding sample values to cells
            worksheet.cells.get("A1").value = "Series1";
            worksheet.cells.get("A2").value = 50;
            worksheet.cells.get("A3").value = 100;
            worksheet.cells.get("A4").value = 150;
            worksheet.cells.get("B1").value = "Series2";
            worksheet.cells.get("B2").value = 60;
            worksheet.cells.get("B3").value = 32;
            worksheet.cells.get("B4").value = 50;

            // Adding a chart to the worksheet
            const chartIndex = worksheet.charts.add(ChartType.Column, 5, 0, 15, 5);

            // Accessing the instance of the newly added chart
            const chart = worksheet.charts.get(chartIndex);

            // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
            chart.chartDataRange = ["A1:B4", true];

            // Hiding X axis
            chart.categoryAxis.isVisible = false;

            // Setting max value of Y axis
            chart.valueAxis.maxValue = 200;
            // Setting major unit
            chart.valueAxis.majorUnit = 50;

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart_axes.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```  

## **Argomenti avanzati**  
- [Cambia la direzione delle etichette di graduazione](/cells/it/javascript-cpp/change-tick-label-direction/)  
- [Determina quali assi esistono nel grafico.](/cells/it/javascript-cpp/determine-which-axis-exists-in-the-chart/)  
- [Gestire le unità automatiche dell'asse del grafico come Microsoft Excel](/cells/it/javascript-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Leggere le etichette dell'asse dopo il calcolo del grafico](/cells/it/javascript-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Come impostare l'asse delle categorie nel grafico Excel](/cells/it/javascript-cpp/how-to-set-category-axis/)
