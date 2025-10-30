---
title: Monitora lo stato di avanzamento della conversione di Excel in TIFF con JavaScript tramite C++
linktitle: Monitora il progresso della conversione di Excel in TIFF
type: docs
weight: 190
url: /it/javascript-cpp/track-conversion-progress-of-excel-to-tiff/
description: Impara come monitorare lo stato di avanzamento della conversione di file Excel in TIFF usando Aspose.Cells for JavaScript tramite C++. Migliora l’esperienza utente durante il processo di conversione.
---

## **Possibili Scenari di Utilizzo**

A volte, la conversione di file Excel di grandi dimensioni può richiedere del tempo. Durante questo periodo, potresti voler mostrare lo stato di avanzamento della conversione del documento anziché solo una schermata di caricamento per migliorare l'usabilità della tua applicazione. Aspose.Cells for JavaScript tramite C++ supporta il tracciamento del processo di conversione del documento fornendo l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback). L'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback) offre i metodi [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) e [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) che puoi implementare nella tua classe personalizzata. Puoi anche controllare quali pagine vengono renderizzate come dimostrato nella classe personalizzata *TestPageSavingCallback*.

## **Monitora il progresso della conversione di Excel in TIFF**

 Il seguente esempio di codice carica il [file Excel origine](95584311.xlsx) e stampa il suo progresso di conversione nella console usando la classe personalizzata *TestPageSavingCallback* che implementa l'interfaccia [**IPageSavingCallback**](https://reference.aspose.com/cells/javascript-cpp/ipagesavingcallback). Il file di output generato è allegato per tua referenza.

[Output File](95584312.tiff)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to TIFF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="convertTiff">Convert to TIFF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookRender, ImageType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('convertTiff').addEventListener('click', async () => {
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

                // Create ImageOrPrintOptions and configure for TIFF conversion
                const opts = new ImageOrPrintOptions();

                // Define TestTiffPageSavingCallback
                class TestTiffPageSavingCallback {
                    // Implement pageSaving as a no-op handler; Aspose.Cells may call this during TIFF generation
                    pageSaving(args) {
                        // No-op: default behavior will be used for page saving
                        // If needed, args (like args.imageStream) can be modified here
                    }
                }

                // Assign callback and image type using property assignment (converted from setters)
                opts.pageSavingCallback = new TestTiffPageSavingCallback();
                opts.imageType = ImageType.Tiff;

                // Create WorkbookRender and generate the TIFF image
                const wr = new WorkbookRender(workbook, opts);
                const outputData = wr.toImage();

                // Create a Blob and provide a download link for the generated TIFF
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'DocumentConversionProgressForTiff_out.tiff';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download TIFF File';

                resultDiv.innerHTML = '<p style="color: green;">Conversion completed. Click the download link to save the TIFF.</p>';
            });
        });
    </script>
</html>
```

 Il seguente è il codice per la classe personalizzata *TestTiffPageSavingCallback*.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - TIFF Page Saving Callback</title>
    </head>
    <body>
        <h1>TIFF Page Saving Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Save as TIFF with Page Callback</button>
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

        class TestTiffPageSavingCallback {
            pageStartSaving(args) {
                console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // Don't output pages before page index 2.
                if (args.pageIndex < 2) {
                    args.isToOutput = false;
                }
            }

            pageEndSaving(args) {
                console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

                // Don't output pages after page index 8.
                if (args.pageIndex >= 8) {
                    args.hasMorePages = false;
                }
            }
        }

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

            // Create TIFF save options and assign the page saving callback
            const tiffOptions = new AsposeCells.TiffSaveOptions();
            tiffOptions.pageSavingCallback = new TestTiffPageSavingCallback();

            // Save the workbook as TIFF using the save options
            const outputData = workbook.save(SaveFormat.Tiff, tiffOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TIFF saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Output della console**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
