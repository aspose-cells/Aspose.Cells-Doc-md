---
title: Mostra Elenco puntato impostando il Valore della Cella utilizzando HTML
type: docs
weight: 130
url: /it/javascript-cpp/display-bullets-by-setting-cell-value-using/
description: Aggiungi punti elenco alle celle Excel usando HTML con l uso facile di Aspose.Cells for JavaScript tramite API C++.
keywords: aggiungi punti elenco in Excel JavaScript tramite C++, visualizza i punti elenco in Excel JavaScript tramite C++, aggiungi punti elenco in Excel con HTML JavaScript tramite C++, visualizza i punti elenco in Excel con HTML JavaScript tramite C++, aggiungi punti elenco in Excel usando HTML JavaScript tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells supporta la visualizzazione di punti con codice HTML. Questo articolo spiegherà come visualizzare i punti impostando il valore della cella usando HTML. Utilizzeremo il metodo [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) per impostare il valore della cella con il nostro HTML.

{{% /alert %}}

## Codice JavaScript per visualizzare i punti elenco impostando il valore della cella usando HTML

Il codice seguente utilizza il codice HTML per impostare il valore della cella. Una volta eseguito questo codice, otterrai il risultato come mostrato nell'immagine sottostante.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Bullets In Cells</title>
    </head>
    <body>
        <h1>Bullets In Cells Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set the HTML string (converted from setHtmlString -> htmlString property)
            cell.htmlString = "<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>";

            // Auto fit the Columns
            worksheet.autoFitColumns();

            // Save the workbook to a Blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'BulletsInCells_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File: BulletsInCells_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Output generato dal codice di esempio

Lo screenshot seguente mostra l'output del codice di esempio precedente.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
