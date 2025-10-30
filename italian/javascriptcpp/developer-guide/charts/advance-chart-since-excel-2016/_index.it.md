---
title: Leggi e manipola grafici di Excel 2016 con JavaScript tramite C++
linktitle: Lettura e manipolazione dei grafici di Excel 2016
description: Impara come leggere e manipolare i grafici di Excel 2016 usando Aspose.Cells for JavaScript tramite C++. Questa guida ti mostrerà come accedere e modificare varie proprietà dei grafici.
keywords: Aspose.Cells for JavaScript tramite C++, grafici di Excel 2016, leggere, manipolare, etichette dei dati, colori della serie, layout, grafici gerarchici, grafici circolari.
type: docs
weight: 48
url: /it/javascript-cpp/read-and-manipulate-excel-2016-charts/
---

## **Possibili Scenari di Utilizzo**  
Aspose.Cells supporta ora la lettura e la manipolazione dei grafici di Microsoft Excel 2016 che non sono presenti in Microsoft Excel 2013 o nelle versioni precedenti.  
## **Lettura e manipolazione dei grafici di Excel 2016**  
Il seguente esempio di codice carica il [file excel sorgente](22774101.xlsx) che contiene grafici Excel 2016 nel primo foglio di lavoro. Legge tutti i grafici uno ad uno e cambia il suo titolo in base al tipo di grafico. Lo screenshot seguente mostra il file excel di origine prima dell'esecuzione del codice. Come puoi vedere, il titolo del grafico è lo stesso per tutti.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

La seguente schermata mostra il [file excel di output](22774104.xlsx) dopo l'esecuzione del codice. Come puoi vedere, il titolo del grafico è stato cambiato in base al tipo di grafico.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Codice di Esempio**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read and Update Chart Titles</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet which contains the charts
            const sheet = workbook.worksheets.get(0);

            // Access all charts one by one and read their types
            const chartsCount = sheet.charts.count;
            let logHtml = '<ul>';
            for (let i = 0; i < chartsCount; i++) {
                // Access the chart
                const ch = sheet.charts.get(i);

                // Read chart type
                const typeStr = ch.type.toString();
                console.log(typeStr);

                // Change the title of the chart
                ch.title.text = "Chart Type is " + typeStr;

                logHtml += `<li>Chart ${i}: ${typeStr}</li>`;
            }
            logHtml += '</ul>';

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_excel2016Charts.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Charts updated successfully! Click the download link to get the modified file.</p>' + logHtml;
        });
    </script>
</html>
```  
## **Output della console**  


{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Argomenti avanzati**  
- [Creazione del grafico a cascata](/cells/it/javascript-cpp/creating-waterfall-chart/)  
- [Creazione del grafico Mappa a blocchi](/cells/it/javascript-cpp/creating-treemap-chart/)  
- [Creazione del grafico Radiali](/cells/it/javascript-cpp/creating-sunburst-chart/)
