---
title: Specificare il massimo numero di righe di una formula condivisa con JavaScript tramite C++
linktitle: Specificare il Numero Massimo di Righe della Formula Condivisa
type: docs
weight: 40
url: /it/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Impara come specificare il massimo numero di righe per le formule condivise usando Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**  

Il numero massimo di righe predefinito per la formula condivisa è 64. Può essere qualsiasi numero, ad esempio 1000. La performance della formula condivisa varia in base al numero di righe. Perciò, Aspose.Cells fornisce la proprietà [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--) che può essere usata per specificare il numero massimo di righe. La formula condivisa sarà suddivisa in più formule condivise se il numero totale di righe supera questo limite, come mostrato nello screenshot seguente.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Specificare il numero massimo di righe della formula condivisa**  

Il codice di esempio seguente spiega come usare la proprietà [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). Imposta il numero massimo di righe della formula condivisa a 5, aggiunge la formula condivisa nella cella D1 per 100 righe e salva in [file Excel di output](61767856.xlsx). Se estrai il contenuto del file Excel di output e controlli *sheet1.xml*, vedrai che la formula condivisa si suddivide ogni 5 righe come evidenziato nello screenshot sopra.  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
