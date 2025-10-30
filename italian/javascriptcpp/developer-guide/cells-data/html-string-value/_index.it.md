---
title: Aggiunta di testo ricco HTML all interno della cella
linktitle: Valore stringa HTML
type: docs
weight: 50
url: /it/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Impara come aggiungere testo HTML Ricco all interno della Cell attraverso l API Aspose.Cells for JavaScript tramite C++.
keywords: Aggiungi testo HTML Ricco all interno della Cell JavaScript tramite C++, Imposta testo HTML Ricco all interno della Cell JavaScript tramite C++, Aggiungi testo HTML Ricco in Cella JavaScript tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di HTML orientato a Microsoft Excel in formato XLS/XLSX. Significa che l'HTML generato da Microsoft Excel può essere convertito indietro in formato XLS/XLSX usando Aspose.Cells.

Allo stesso modo, se c'è un HTML semplice, Aspose.Cells può convertirlo in testo ricco HTML. Aspose.Cells fornisce la proprietà [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) che può prendere un HTML semplice e convertirlo in un testo di cella formattato.

{{% /alert %}}

Il seguente esempio di codice ti mostra come aggiungere testo ricco in HTML all'interno della cella. Si prega di consultare lo screenshot del file Excel di output.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Articoli correlati

- [Visualizza pallini impostando il valore della cella utilizzando HTML](/cells/it/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Ottieni una stringa HTML5 dalla cella](/cells/it/javascript-cpp/get-html5-string-from-cell/)
