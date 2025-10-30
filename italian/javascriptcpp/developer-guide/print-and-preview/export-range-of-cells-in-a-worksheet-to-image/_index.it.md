---
title: Esporta l’Intervallo di Celle in un Foglio di Lavoro in Immagine con JavaScript tramite C++
linktitle: Esporta un intervallo di celle in un foglio di lavoro in un immagine
type: docs
weight: 60
url: /it/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/
---

## **Possibili Scenari di Utilizzo**  

Puoi creare un'immagine di un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++. Tuttavia, a volte è necessario esportare solo un intervallo di celle di un foglio di lavoro in un'immagine. Questo articolo spiega come farlo.  

## **Esportare un intervallo di celle in un foglio di lavoro in un'immagine**  

Per catturare un'immagine di un intervallo, imposta l'area di stampa sull'intervallo desiderato e poi imposta tutti i margini a 0. Imposta anche [**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#onePagePerSheet--) su **true**. Il seguente codice prende un'immagine dell'intervallo D8:G16. Di seguito uno screenshot del [file Excel di esempio](47153160.xlsx) usato nel codice. Puoi provare il codice con qualsiasi file Excel.  

## **Screenshot del file di Excel di esempio e la sua immagine esportata**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Eseguendo il codice viene creata un'immagine dell'intervallo D8:G16 soltanto.  

**![todo:image_alt_text](Output-Image.png)**  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Range To Image</title>
    </head>
    <body>
        <h1>Export Range Of Cells In Worksheet To Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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

            // Create workbook from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the print area with your desired range
            worksheet.pageSetup.printArea = "D8:G16";

            // Set all margins as 0
            worksheet.pageSetup.leftMargin = 0;
            worksheet.pageSetup.rightMargin = 0;
            worksheet.pageSetup.topMargin = 0;
            worksheet.pageSetup.bottomMargin = 0;

            // Set OnePagePerSheet option as true and image options
            const options = new ImageOrPrintOptions();
            options.onePagePerSheet = true;
            options.imageType = ImageType.Jpeg;
            options.horizontalResolution = 200;
            options.verticalResolution = 200;

            // Take the image of your worksheet
            const sr = new SheetRender(worksheet, options);
            const outputData = sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportRangeOfCellsInWorksheetToImage.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image exported successfully! Click the download link to download the image.</p>';
        });
    </script>
</html>
```
