---
title: Aggiornare i giorni preservando la cronologia delle revisioni in un workbook condiviso con JavaScript tramite C++
linktitle: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso
type: docs
weight: 80
url: /it/javascript-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Scopri come aggiornare i giorni per preservare la cronologia delle revisioni nei workbook condivisi usando lo Script Aspose.Cells for Java tramite C++.
---

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, viene visualizzata un'opzione chiamata ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nel seguente screenshot. Puoi aggiornare il numero di giorni per preservare la cronologia usando lo Script Aspose.Cells for Java tramite C++ con la proprietà [**WorksheetCollection.daysPreservingHistory**](https://reference.aspose.com/cells/javascript-cpp/revisionlogcollection/#daysPreservingHistory--). 

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, quindi lo condivide e aggiorna i giorni di registro di revisione preservando la cronologia a 7 giorni, di solito 30 giorni. Consulta il [file Excel di output](60489773.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Shared Workbook</title>
    </head>
    <body>
        <h1>Shared Workbook - DaysPreservingHistory Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Shared Workbook</button>
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
            // Create empty workbook
            const workbook = new Workbook();

            // Share the workbook
            workbook.settings.shared = true;

            // Update DaysPreservingHistory of RevisionLogs
            workbook.worksheets.revisionLogs.daysPreservingHistory = 7;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputShared_DaysPreservingHistory.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and configured. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
