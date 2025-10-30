---
title: Congela la riga superiore(a) del foglio di lavoro di Excel con JavaScript tramite C++
linktitle: Congelare righe
type: docs
weight: 190
url: /it/javascript-cpp/how-to-freeze-rows-of-excel-worksheet
description: In questo articolo, imparerai come congelare le righe superiori dei fogli di lavoro di Excel programmaticamente usando la libreria JavaScript con API C++.
keywords: Congela le righe superiori, congela la prima riga in JavaScript tramite C++.
---

## **Introduzione**

In questo articolo, impareremo come congelare la/riga/rice superiore(i). Quando hai una grande quantità di dati sotto una intestazione comune, non puoi vedere l'intestazione quando scorri verso il basso il foglio di lavoro. Puoi congelare le righe superiori in modo da poter vedere quella parte congelata anche quando il resto dei dati viene sceso. Puoi facilmente vedere le intestazioni nelle righe superiori.

## **Congelare le righe in Excel**

**![Congelare la/e riga/e superiore/i in Excel](Freeze-Rows.png)**

1. Se vuoi bloccare le righe superiori, seleziona prima la riga sotto la riga che deve essere bloccata.
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela riga superiore.
4. Se scorri verso il basso, la prima riga rimane sempre visibile in alto.

**![Riga congelata](Frozen-Row.png)**

Come puoi vedere, la prima riga è congelata; la prima riga rimane sempre in cima alla visualizzazione quando scorri verso il basso.

Congelare le righe ti permette di visualizzare i tuoi grandi dati senza tenere traccia dell'etichetta della riga.

## **Congela righe con Aspose.Cells for JavaScript tramite C++**
 È semplice congelare la(r) riga(e) con Aspose.Cells for JavaScript tramite C++. 
Si prega di usare il metodo [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) per congelare riga/righe alla riga selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Congela la prima riga con il metodo Worksheet.freezePanes().
3. Salvare il file.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Freeze Panes</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Freezing panes at the cell B2 on the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.freezePanes("A2", 1, 0);

            // Saving the file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'frozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Frozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

File Excel di esempio allegato(../Freeze.xlsx).
