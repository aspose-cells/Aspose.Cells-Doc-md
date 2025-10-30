---
title: Lettura di file CSV con più codifiche usando JavaScript via C++
linktitle: Lettura di file CSV con codifiche multiple
type: docs
weight: 200
url: /it/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Impara come leggere file CSV con più codifiche usando Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

A volte, il tuo file CSV contiene più codifiche (Unicode, ANSI, UTF8, UTF7, ecc). Aspose.Cells ti permette di caricare questi file CSV e convertirli in altri formati, ad esempio PDF o XLSX.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--), che devi impostare su **true** per caricare correttamente il tuo file CSV con più encodings.

La seguente schermata mostra un esempio di file CSV che contiene due righe. La prima riga è in codifica **ANSI** e la seconda riga è in codifica **Unicode**

|**File di input**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Lo screenshot seguente mostra il file XLSX convertito dal file CSV sopra senza impostare la proprietà [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) su **true**. Come puoi vedere, il testo Unicode non è stato convertito correttamente.

|**File di output 1: nessuna modifica per la codifica multipla**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Lo screenshot seguente mostra il file XLSX convertito dal CSV sopra dopo aver impostato la proprietà [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) su **true**. Come puoi vedere, ora il testo Unicode viene convertito correttamente.

|**File di output 2: IsMultiEncoded è impostato su true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Di seguito è riportato il codice di esempio che converte il precedente file CSV nel formato XLSX correttamente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## Articoli correlati

- [Apertura dei file CSV](/cells/it/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
