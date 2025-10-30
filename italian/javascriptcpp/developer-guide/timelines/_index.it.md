---
title: Inserisci la timeline
linktitle: Timeline
type: docs
weight: 170
url: /it/javascript-cpp/create-timeline/
description: Scopri come creare una timeline con Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Invece di regolare i filtri per mostrare le date, puoi usare una Timeline pivot——un'opzione di filtro dinamico che permette di filtrare facilmente per data/orario e zoomare sul periodo desiderato con un controllo a cursore. Microsoft Excel consente di creare una timeline selezionando una tabella pivot e cliccando su *Inserisci > Timeline*. Aspose.Cells for JavaScript tramite C++ permette anche di creare una timeline usando il metodo [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Creare una timeline per una tabella pivot**

Vedi il seguente esempio di codice. Carica il file Excel di esempio ([input.xlsx](input.xlsx)) che contiene la tabella pivot. Poi crea la timeline basata sul primo campo pivot di base. Infine, salva il workbook nel formato [output XLSX](output.xlsx). La schermata seguente mostra la timeline creata da Aspose.Cells for JavaScript tramite C++ nel file Excel di output.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
