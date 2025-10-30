---
title: Inserire o eliminare righe in un foglio di lavoro Excel con JavaScript via C++
linktitle: Inserisci o elimina righe in un foglio Excel
type: docs
weight: 20
url: /it/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Questo articolo fornisce codice JavaScript usando C++ per inserire ed eliminare righe in un foglio di lavoro Excel.
keywords: javascript inserisce o elimina righe in fogli di lavoro Excel, javascript inserisce o elimina righe in Excel, javascript inserisce righe in Excel, javascript elimina righe in Excel, inserisci o elimina righe in foglio di lavoro Excel con javascript, inserisci o elimina righe in Excel con javascript, inserisci righe in Excel con javascript, elimina righe in Excel con javascript
---

{{% alert color="primary" %}}  

Quando si crea un nuovo foglio di lavoro o si lavora con un foglio esistente, potrebbe essere necessario aggiungere righe o colonne extra per contenere i dati. Altre volte, potrebbe essere necessario eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.  

{{% /alert %}}  

Lo Script Aspose.Cells for JavaScript via C++ offre due metodi per inserire e eliminare righe: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) e [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). Questi metodi sono ottimizzati per le prestazioni e svolgono il lavoro molto rapidamente.  

Per inserire o rimuovere un numero di righe, si consiglia di usare sempre i metodi [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) e [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) piuttosto che usare i metodi [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) o [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) in un ciclo.  

Aspose.Cells funziona allo stesso modo di Microsoft Excel. Quando vengono aggiunte righe o colonne, i contenuti del foglio di lavoro vengono spostati verso il basso e verso destra. Quando vengono rimosse righe o colonne, i contenuti del foglio di lavoro vengono spostati verso l'alto o verso sinistra. Eventuali riferimenti in altri fogli di lavoro e celle vengono aggiornati quando vengono aggiunte o rimosse righe.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
