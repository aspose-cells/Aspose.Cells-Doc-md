---
title: Popola prima i dati per riga e poi per colonna
type: docs
weight: 1000
url: /it/javascript-cpp/populate-data-first-by-row-then-by-column/
description: Impara come Popolare Dati Prima per Riga poi per Colonna tramite l’API Aspose.Cells for JavaScript in C++.
keywords: Popolare Dati Prima per Riga poi per Colonna JavaScript in C++, Inserisci Dati Prima per Riga poi per Colonna JavaScript in C++, Aggiungi Dati Prima per Riga poi per Colonna JavaScript in C++, Inserimento dati ad alte prestazioni JavaScript in C++, Aggiunta di dati ad alte prestazioni JavaScript in C++
---

{{% alert color="primary" %}}  

Popolare un foglio di calcolo con i dati prima per riga e poi per colonna migliora le prestazioni complessive.  

{{% /alert %}}  

Inserire i dati nella sequenza A1, B1, A2, B2 è più veloce rispetto a A1, A2, B1, B2. Se ci sono molte celle in un foglio di lavoro e si segue la seconda sequenza, ovvero si riempiono i dati riga per riga, questo suggerimento può rendere il programma molto più veloce.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
