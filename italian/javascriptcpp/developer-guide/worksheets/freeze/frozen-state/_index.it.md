---
title: Come verificare lo stato di congelamento senza Excel usando JavaScript tramite C++
linktitle: Stato congelato
type: docs
weight: 190
url: /it/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: In questo articolo, imparerai come controllare lo stato di congelamento di un foglio di lavoro Excel programmaticamente usando JavaScript con libreria C++.
---

## **Introduzione**

 In questo articolo, impareremo come verificare lo stato di congelamento di un foglio di lavoro Excel programmaticamente. Possiamo semplicemente determinare se il foglio di lavoro è congelato o diviso in MS Excel. Ma c'è un modo per scoprire se è congelato o diviso con JavaScript? Possiamo farlo facilmente con Aspose.Cells for JavaScript tramite C++.

## **Le riquadri della finestra sono congelati**
 Con Aspose.Cells for JavaScript tramite C++, possiamo verificare se la finestra è congelata e quante righe e colonne sono bloccate.

 Si prega di usare la proprietà [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) per verificare lo stato dei riquadri della finestra e ottenere le righe e le colonne bloccate con la proprietà [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. Costruire il Workbook per aprire il file.
2. Verificare se il foglio di lavoro è congelato.
3. Ottieni le righe e le colonne bloccate.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
