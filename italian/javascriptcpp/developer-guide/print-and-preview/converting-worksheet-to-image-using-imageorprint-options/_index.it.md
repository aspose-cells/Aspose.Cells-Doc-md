---
title: Conversione del Foglio di Lavoro in Immagine usando Opzioni ImageOrPrint con JavaScript tramite C++
linktitle: Conversone del Foglio di Lavoro in Immagine utilizzando le Opzioni Immagine o Stampa
type: docs
weight: 90
url: /it/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Impara come convertire un foglio di lavoro in un file immagine e applicare varie opzioni di immagine e stampa usando Aspose.Cells for JavaScript tramite C++.   
---

{{% alert color="primary" %}}  
Questo documento è progettato per fornire una comprensione dettagliata su come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, come risoluzione, compressione TIFF, formato immagine e qualità della pagina.  
{{% /alert %}}  

## **Salvataggio Fogli di lavoro in Immagini - Diverse Approcci**  

A volte potresti aver bisogno di presentare i tuoi fogli di lavoro come rappresentazione pittorica. Devi presentare le immagini del foglio di lavoro nelle tue applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint, o utilizzarle in qualche altro scenario. Semplicemente desideri un foglio di lavoro rappresentato come un'immagine in modo da poterlo utilizzare altrove. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel in immagini. Inoltre, Aspose.Cells supporta impostare diverse opzioni come formato immagine, risoluzione (sia verticale che orizzontale), qualità dell'immagine e altre opzioni di immagine e stampa.  

Potresti provare l'Automazione Office ma l'automazione Office ha i suoi svantaggi. Ci sono diverse ragioni e problemi coinvolti: ad esempio, sicurezza, stabilità, scalabilità e velocità, prezzo e funzionalità. In breve, ci sono molte ragioni, con la principale che Microsoft stessa raccomanda fortemente di non utilizzare l'automazione Office da soluzioni software.  

Questo articolo mostra come creare un'applicazione console in Visual Studio .NET, eseguire la conversione di un foglio di lavoro in un'immagine utilizzando diverse opzioni di immagine e stampa con poche e semplici righe di codice utilizzando l'API Aspose.Cells.  

La classe [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) rappresenta un foglio di lavoro per renderizzare immagini, dispone di un metodo [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) sovraccarico che può convertire direttamente un foglio di lavoro in uno o più file immagine specificati con i tuoi attributi o opzioni desiderate. Può restituire un oggetto su cui puoi salvare un file immagine su disco/stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPEG, TIFF, EMF e altri.  

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in immagine utilizzando le opzioni ImageOrPrint.**  

### **Creazione di un libro di lavoro modello in Microsoft Excel**  

Ho creato un nuovo libro di lavoro in MS Excel e aggiunto alcuni dati nel primo foglio di lavoro. Ora, convertirò il foglio di lavoro del file modello "Foglio1" in un file immagine "FoglioImmagine.tiff" e applicherò diverse opzioni di immagine come risoluzioni orizzontali e verticali, compressione Tiff, ecc.  

### **Scarica e installa Aspose.Cells**  

Per prima cosa, devi [scaricare](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript tramite C++. Installalo sul tuo computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.  

### **Crea un Progetto**  

Avvia il tuo ambiente di sviluppo preferito (ad esempio, Visual Studio). Crea una nuova applicazione console.  

### **Aggiungi Riferimenti**  

Questo progetto utilizzerà Aspose.Cells. Quindi, devi aggiungere un riferimento al componente Aspose.Cells nel tuo progetto. Ad esempio, aggiungi un riferimento a …\.\Program Files\Aspose\Aspose.Cells for JavaScript tramite C++\Bin\Aspose.Cells.node  

### **Convertire un foglio di lavoro in un file immagine**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **Opzioni di conversione**  

È possibile salvare pagine specifiche in immagine. Il codice seguente converte il primo e il secondo foglio di lavoro in un libro di lavoro in immagini JPG.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **Conversione dell'immagine utilizzando WorkbookRender**  

Un'immagine TIFF può contenere più di un frame. È possibile salvare l'intero workbook in un’unica immagine TIFF con più frame o pagine:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
