---
title: Convertire foglio di lavoro in immagine  Rimuovere lo spazio bianco intorno ai dati con JavaScript tramite C++
linktitle: Converti foglio elettronico in immagine  Rimuovi spazi vuoti intorno ai dati
type: docs
weight: 40
url: /it/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Impara come convertire i fogli di Excel di Microsoft in immagini e rimuovere gli spazi vuoti attorno ai dati usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}}

A volte è necessario presentare immagini del foglio elettronico in applicazioni o pagine web. Ad esempio, potresti aver bisogno di inserire immagini in un documento di Word, un file PDF, una presentazione PowerPoint o qualche altro documento. Fondamentalmente, desideri renderizzare un foglio elettronico come un'immagine in modo che possa essere incollato in altre applicazioni. Aspose.Cells ti consente di convertire i fogli di lavoro di Microsoft Excel in immagini.

{{% /alert %}}

## **Rimuovi spazi vuoti intorno ai dati**

L'API [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) converte un foglio elettronico in un file immagine con eventuali attributi specificati, ad esempio formato immagine, fogli paginati, ecc. Sono supportati diversi formati di immagine, come BMP, GIF, JPG, TIFF e EMF.

Quando si utilizza la funzione foglio-in-immagine, l'immagine di output ha spazi vuoti, cioè un bordo, attorno ad essa per impostazione predefinita. È possibile rimuovere questo impostando i margini di impaginazione superiore, inferiore, sinistro e destro del foglio di lavoro di origine a 0 e specificando [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) attributi di conseguenza.

Il seguente frammento di codice rimuove gli spazi vuoti intorno ai dati nell'immagine di output.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
