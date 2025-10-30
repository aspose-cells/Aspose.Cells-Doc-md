---
title: Caratteristiche di impostazione pagina con JavaScript tramite C++
linktitle: Caratteristiche della configurazione pagina
type: docs
weight: 60
url: /it/javascript-cpp/page-setup-features/
description: Esplora le funzionalità di impostazione pagina usando Aspose.Cells for JavaScript tramite C++. Impara come configurare le dimensioni della pagina, le orientazioni e le impostazioni.
keywords: Caratteristiche di impostazione pagina JavaScript tramite C++, configura dimensioni pagina JavaScript tramite C++, impostazioni orientamento pagina JavaScript tramite C++
---

## **Introduzione**
Con Aspose.Cells for JavaScript tramite C++, puoi manipolare varie funzionalità di impostazione pagina di un libro di lavoro Excel. Queste funzionalità includono la definizione delle dimensioni della pagina, l'orientamento, i margini e altro ancora. Una corretta configurazione di queste funzionalità permette una migliore stampa e visualizzazione.

## **Imposta dimensione e orientamento della pagina**
Puoi specificare la dimensione e l'orientamento della pagina di un foglio di lavoro utilizzando la classe `PageSetup`. Fornisce varie proprietà per gestire le dimensioni della pagina e il layout.

### **Codice di esempio**
Ecco un esempio di codice che dimostra come impostare la dimensione e l'orientamento della pagina.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Impostazione margini**
Puoi anche impostare i margini della pagina utilizzando la stessa classe `PageSetup`. I margini possono essere regolati per il lato sinistro, destro, superiore e inferiore.

### **Codice di esempio**
Ecco come puoi impostare i margini di un foglio di lavoro.
