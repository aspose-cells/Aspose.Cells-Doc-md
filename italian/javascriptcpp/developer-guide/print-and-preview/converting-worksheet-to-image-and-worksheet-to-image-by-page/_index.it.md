---
title: Conversione del Foglio di Lavoro in Immagine e del Foglio di Lavoro in Immagine per Pagina con JavaScript tramite C++
linktitle: Convertire foglio elettronico in immagine e foglio elettronico in immagine per pagina
type: docs
weight: 80
url: /it/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e anche come gestire più pagine di un foglio di lavoro convertendole in immagini separate.

A volte potresti dover presentare i fogli elettronici come immagini, ad esempio per utilizzarli in applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. In sostanza, desideri rendere il foglio elettronico come un'immagine. Aspose.Cells supporta la conversione dei fogli in file Microsoft Excel in immagini. Inoltre, Aspose.Cells supporta la conversione di un libro di lavoro in più file immagine, uno per pagina.

Potresti usare l'automazione di Office per ottenere questo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. In sintesi, ci sono molte ragioni, ma la principale è che Microsoft stessa sconsiglia fortemente l'automazione di Office.
{{% /alert %}}

## **Utilizzando Aspose.Cells for JavaScript tramite C++ per Convertire il Foglio di Lavoro in un File Immagine**

Questo articolo mostra come creare un'applicazione console, convertire un foglio di lavoro in un'immagine e trasformare un foglio di lavoro in una singola immagine per ogni foglio con poche linee di codice semplici utilizzando l'API di Aspose.Cells.

You need to import several valuable classes related to rendering functionalities into your program or project, such as [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/), and so on. The [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) class represents a worksheet to render images for the worksheet and has an overloaded [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) method that can convert a worksheet to image files directly with any attributes or options set. It can return an image object and you can save an image file to the disk/stream. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, and others.

Questo articolo spiega come:

- Convertire un foglio di lavoro in un'immagine
- Convertire ogni pagina in un foglio di lavoro in un'immagine

Questo compito mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro in un file di immagine.

### **Progetto di installazione**

1. Per prima cosa, [scarica Aspose.Cells for JavaScript tramite C++](https://downloads.aspose.com/cells/javascript-cpp).
1. Installa sul tuo computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti. Ora avvia il tuo ambiente di sviluppo e crea una nuova applicazione console. Questo esempio utilizza un'applicazione console JavaScript, ma puoi usare qualsiasi configurazione che integri JavaScript. Aggiungi un riferimento a Aspose.Cells nel progetto creato.

### **Converti Foglio di Lavoro in File Immagine**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook.xlsx** (1 foglio di lavoro). Successivamente, converti il foglio di lavoro del file modello chiamato Sheet1 in un file immagine chiamato SheetImage.jpg.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in **Testbook.xlsx** in un file immagine per spiegare quanto sia facile questa conversione.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## **Utilizzando Aspose.Cells for JavaScript tramite C++ per Convertire il Foglio di Lavoro in un File Immagine per Pagina**

Questo esempio mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro che ha diverse pagine in un file immagine per pagina.

### **Convertire Foglio di Lavoro in Immagine per Pagina**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook2.xlsx** (1 foglio di lavoro).

Ora, converti il foglio di lavoro del file modello in file immagine (un file per pagina). Poiché ho già creato l'applicazione console per eseguire il compito di copia, salterò quei passaggi di creazione dell'applicazione console e passerò direttamente ai passaggi di conversione del foglio di lavoro.

Di seguito è riportato il codice utilizzato dalla componente per completare il compito. Converte Sheet1 in Testbook2.xlsx in file immagine per pagina.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
