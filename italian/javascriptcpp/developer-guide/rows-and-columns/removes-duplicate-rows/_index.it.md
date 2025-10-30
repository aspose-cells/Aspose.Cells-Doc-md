---
title: Rimuovi righe duplicate in un foglio di lavoro con JavaScript tramite C++
linktitle: Rimuovere righe duplicate in un foglio di lavoro
type: docs
weight: 370
url: /it/javascript-cpp/remove-duplicate-rows-in-a-worksheet/
description: Impara come rimuovere righe duplicate in un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++ e selezionare colonne specifiche per i controlli di duplicati.
---

Rimuovere righe duplicate è una delle molte funzionalità utili di Microsoft Excel. Consente agli utenti di rimuovere righe duplicate in un Foglio di lavoro, e puoi scegliere quali colonne devono essere controllate per informazioni duplicate.

Aspose.Cells for JavaScript tramite C++ fornisce il metodo `Cells.removeDuplicates()` per questo scopo. Puoi anche impostare `startRow`, `startColumn`, `endRow` e `endColumn` per specificare l’intervallo di colonne da controllare per i duplicati.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[removeduplicates.xlsx](removeduplicates.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Duplicates Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Create workbook from uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Remove Duplicate (converted getters to properties)
            book.worksheets.get(0).cells.removeDuplicates(0, 0, 5, 3);

            // Save result and provide download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'removeduplicates-result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            resultDiv.innerHTML = '<p style="color: green;">Duplicates removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
