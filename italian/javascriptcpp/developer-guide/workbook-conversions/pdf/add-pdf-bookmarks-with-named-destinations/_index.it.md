---
title: Aggiungi segnalibri PDF con Destinazioni Nominative usando JavaScript tramite C++
linktitle: Aggiungi Segnalibri PDF con Destinazioni con Nome
type: docs
weight: 20
url: /it/javascript-cpp/add-pdf-bookmarks-with-named-destinations/
description: Impara come aggiungere segnalibri PDF con destinazioni nominate usando Aspose.Cells for JavaScript tramite C++. Assicurati che i segnalibri rimangano integri indipendentemente dalle modifiche di pagina.
---

## **Possibili Scenari di Utilizzo**

Le Destinazioni con Nome sono un tipo speciale di segnalibri o collegamenti nei PDF che non dipendono dalle pagine PDF. Ciò significa che, se vengono aggiunte o eliminate pagine dal PDF, i segnalibri possono diventare non validi ma le destinazioni con nome rimarranno integre. Per creare una Destinazione con Nome, si prega di impostare la proprietà [**PdfBookmarkEntry.destinationName**](https://reference.aspose.com/cells/javascript-cpp/pdfbookmarkentry/#destinationName--).

## **Aggiungi Segnalibri PDF con Destinazioni con Nome**

Si prega di consultare il codice di esempio seguente, il [file Excel di origine](50528348.xlsx) e il [file PDF di output](50528349.pdf). La schermata mostra i segnalibri e le destinazioni con nome all'interno del PDF di output. La schermata descrive anche come visualizzare le Destinazioni con Nome e che è necessaria la versione Professionale di Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Bookmark Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PDF Bookmark Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfBookmarkEntry, PdfSaveOptions } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell C5
            let cell = worksheet.cells.get("C5");

            // Create Bookmark and Destination for this cell
            const bookmarkEntry = new PdfBookmarkEntry();
            bookmarkEntry.text = "Text";
            bookmarkEntry.destination = cell;
            bookmarkEntry.destinationName = "AsposeCells--" + cell.name;

            // Access cell G56
            cell = worksheet.cells.get("G56");

            // Create Sub-Bookmark and Destination for this cell
            const subbookmarkEntry1 = new PdfBookmarkEntry();
            subbookmarkEntry1.text = "Text1";
            subbookmarkEntry1.destination = cell;
            subbookmarkEntry1.destinationName = "AsposeCells--" + cell.name;

            // Access cell L4
            cell = worksheet.cells.get("L4");

            // Create Sub-Bookmark and Destination for this cell
            const subbookmarkEntry2 = new PdfBookmarkEntry();
            subbookmarkEntry2.text = "Text2";
            subbookmarkEntry2.destination = cell;
            subbookmarkEntry2.destinationName = "AsposeCells--" + cell.name;

            // Add Sub-Bookmarks in list
            const list = [];
            list.push(subbookmarkEntry1);
            list.push(subbookmarkEntry2);

            // Assign Sub-Bookmarks list to Bookmark Sub-Entry
            bookmarkEntry.subEntries = bookmarkEntry.subEntries || [];
            bookmarkEntry.subEntries.push(...list);

            // Create PdfSaveOptions and assign Bookmark to it
            const opts = new PdfSaveOptions();
            opts.bookmark = bookmarkEntry;

            // Save the workbook in Pdf format with given pdf save options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPdfBookmarkEntry_DestinationName.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to download the file.</p>';
        });
    </script>
</html>
```
