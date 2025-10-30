---
title: Specifica come gestire la sovrapposizione di stringhe nell HTML di output usando HtmlCrossType con JavaScript tramite C++
linktitle: Specificare come attraversare la stringa nell output HTML usando HtmlCrossType
type: docs
weight: 140
url: /it/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Impara come controllare il overflow di stringhe in HTML impostando HtmlCrossType in Aspose.Cells for JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in HTML, puoi controllare questo trabocco specificando il tipo di attraversamento usando l'enumerazione [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Ha i seguenti valori:

- **HtmlCrossType.Default**: Mostra come MS Excel; dipende dalla cella successiva. Se la cella successiva è nulla, la stringa attraversa o verrà troncata.

- **HtmlCrossType.MSExport**: Visualizza la stringa come esportazione HTML di MS Excel.

- **HtmlCrossType.Cross**: Mostra la stringa incrociata in HTML; le prestazioni per la creazione di grandi file HTML saranno più di dieci volte più veloci rispetto all'impostazione del valore su Default o FitToCell.

- **HtmlCrossType.FitToCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType**

Il codice di esempio seguente carica il [file Excel di esempio](51740732.xlsx) e lo salva in formato HTML specificando diversi [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Si prega di scaricare gli [HTML di output](51740734.zip) generati con questo codice. Il file Excel di esempio contiene l'immagine bordata di colore rosso come mostrato in questo screenshot che mostra l'effetto dei valori [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) sull'HTML di output.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
