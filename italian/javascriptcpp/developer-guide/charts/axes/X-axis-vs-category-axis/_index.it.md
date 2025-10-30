---
title: Asse X vs. Asse di Categoria con JavaScript tramite C++
linktitle: Asse X vs. Asse delle categorie
description: Impara come differenziare tra l asse X e l asse di categoria in Aspose.Cells for JavaScript tramite C++. La nostra guida ti aiuterà a comprendere le differenze nel loro utilizzo e proprietà, e come configurarli secondo le tue esigenze.
keywords: Aspose.Cells for JavaScript tramite C++, asse X, asse di categoria, differenze, utilizzo, proprietà, configurazione.
type: docs
weight: 180
url: /it/javascript-cpp/X-axis-vs-category-axis/
---

## **Possibili Scenari di Utilizzo**
Ci sono diversi tipi di assi X. Mentre l'asse Y è un asse di tipo Valore, l'asse X può essere un asse di tipo Categoria o un asse di tipo Valore. Utilizzando un asse di tipo Valore, i dati sono trattati come dati numerici continuamente variabili, e il marcatore è posizionato in un punto lungo l'asse che varia in base al suo valore numerico. Utilizzando un asse di tipo Categoria, i dati sono trattati come una sequenza di etichette di testo non numeriche, e il marcatore è posizionato in un punto lungo l'asse in base alla sua posizione nella sequenza. Il codice di esempio qui sotto illustra la differenza tra Assi di Valore e di Categoria.
I nostri dati di esempio sono mostrati nella [tabella di esempio](sample.png) di seguito. La prima colonna contiene i nostri dati asse X, che possono essere trattati come Categorie o come Valori. Nota che i numeri non sono equispaziati, né appaiono in ordine numerico.

![todo:image_alt_text](sample.png)
## **Gestire l'asse X e il'asse delle categorie come Microsoft Excel**
Mostreremo questi dati su due tipi di grafico, il primo grafico è XY (Scatter) con asse X come asse dei valori, il secondo grafico è a linee con asse X come asse Categoria.

![todo:image_alt_text](compare.png)
## **Codice di Esempio**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Charts and X Axis</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, LegendPositionType, FillType, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Access the first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Put the sample values used in charts
            worksheet.cells.get("A2").putValue(1);
            worksheet.cells.get("A3").putValue(3);
            worksheet.cells.get("A4").putValue(2.5);
            worksheet.cells.get("A5").putValue(3.5);
            worksheet.cells.get("B1").putValue("Cats");
            worksheet.cells.get("C1").putValue("Dogs");
            worksheet.cells.get("D1").putValue("Fishes");
            worksheet.cells.get("B2").putValue(7);
            worksheet.cells.get("B3").putValue(6);
            worksheet.cells.get("B4").putValue(5);
            worksheet.cells.get("B5").putValue(4);
            worksheet.cells.get("C2").putValue(7);
            worksheet.cells.get("C3").putValue(5);
            worksheet.cells.get("C4").putValue(4);
            worksheet.cells.get("C5").putValue(3);
            worksheet.cells.get("D2").putValue(8);
            worksheet.cells.get("D3").putValue(7);
            worksheet.cells.get("D4").putValue(3);
            worksheet.cells.get("D5").putValue(2);

            // Create Line Chart: X as Category Axis
            let pieIdx = worksheet.charts.add(ChartType.LineWithDataMarkers, 6, 15, 20, 21);
            // Retrieve the Chart object
            let chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set the category data
            chart.nSeries.categoryData = "=Sheet1!$A$2:$A$5";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Create XY (Scatter) Chart: X as Value Axis
            pieIdx = worksheet.charts.add(ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
            // Retrieve the Chart object
            chart = worksheet.charts.get(pieIdx);
            // Add Series
            chart.nSeries.add("B2:D5", true);
            // Set X values for series 
            chart.nSeries.get(0).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(1).xValues = "{1,3,2.5,3.5}";
            chart.nSeries.get(2).xValues = "{1,3,2.5,3.5}";
            // Set the first series name
            chart.nSeries.get(0).name = "Cats";
            // Set the second series name
            chart.nSeries.get(1).name = "Dogs";
            // Set the third series name
            chart.nSeries.get(2).name = "Fishes";
            // Set the Legend at the bottom of the chart area
            chart.legend.position = LegendPositionType.Bottom;
            // Fill the PlotArea area with nothing 
            chart.plotArea.area.fillFormat.fillType = FillType.None;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'XAxis.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
