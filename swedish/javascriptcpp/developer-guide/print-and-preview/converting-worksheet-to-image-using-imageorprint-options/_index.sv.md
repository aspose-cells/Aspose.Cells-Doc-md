---
title: Konvertera ark till bild med ImageOrPrint alternativ med JavaScript via C++
linktitle: Konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift
type: docs
weight: 90
url: /sv/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Lär dig hur man konverterar ett ark till en bildfil och tillämpar olika bild och utskriftsalternativ med Aspose.Cells for JavaScript via C++.   
---

{{% alert color="primary" %}}  
Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och tillämpar olika bild- och utskriftsalternativ för bilden, såsom upplösning, TIFF-komprimering, bildformat och sidkvalitet.  
{{% /alert %}}  

## **Spara arbetsblad till bilder - Olika tillvägagångssätt**  

Ibland kan det hända att du behöver presentera dina arbetsblad som en bildlig representation. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem på annat sätt. Du vill helt enkelt ha ett arbetsblad renderat som en bild så att du kan använda det någon annanstans. Aspose.Cells stödjer konvertering av arbetsblad i Excel-filer till bilder. Dessutom stödjer Aspose.Cells inställning av olika alternativ som bildformat, upplösning (både vertikal och horisontell), bildkvalitet och andra bild- och utskriftsalternativ.  

Du kan prova Office Automation, men det har sina nackdelar. Det finns flera skäl och problem: till exempel säkerhet, stabilitet, skalbarhet och hastighet, pris och funktioner. Kort sagt, det finns många skäl, varav det viktigaste är att Microsoft själva starkt rekommenderar att undvika Office-automation från mjukvarulösningar.  

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio .NET, utför konvertering av ett arbetsblad till bild med olika bild- och utskriftsalternativ med några enkla kodrader med hjälp av Aspose.Cells API.  

Klassen [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) representerar ett kalkylblad för att rendera bilder för kalkylbladet, den har en överlastad [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) metod som direkt kan konvertera ett kalkylblad till bildfil(er) med angivna attribut eller alternativ. Den kan returnera ett objekt som du kan spara som en bildfil till disk/ström. Flera bildformat stöds, t.ex BMP, PNG, GIFF, JPEG, TIFF, EMF och andra.  

## **Använda Aspose.Cells för att konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift**  

### **Skapa en mallarbok i Microsoft Excel**  

Jag skapade en ny arbetsbok i MS Excel och lade till lite data i det första arbetsbladet. Nu kommer jag att konvertera mallfilens arbetsblad “Sheet1” till en bildfil “SheetImage.tiff” och tillämpa olika bildalternativ som horisontell och vertikal upplösning, TiffCompression med mera.  

### **Ladda ner och installera Aspose.Cells**  

Först, behöver du [ladda ner](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript via C++. Installera det på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/) komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och infogar endast vattentmärken i producerade dokument.  

### **Skapa ett projekt**  

Starta din föredragna utvecklingsmiljö (t.ex. Visual Studio). Skapa ett nytt konsolprogram.  

### **Lägg till referenser**  

Detta projekt kommer att använda Aspose.Cells. Så, du måste lägga till en referens till Aspose.Cells-komponenten i ditt projekt. Till exempel, lägg till en referens till ….\Programfiler\Aspose\Aspose.Cells for JavaScript via C++\Bin\Aspose.Cells.node  

### **Konvertera arbetsblad till en bildfil**  

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

## **Konverteringsalternativ**  

Det är möjligt att spara specifika sidor som bild. Följande kod konverterar arbetsböckerets första och andra kalkylblad till JPG-bilder.  

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

## **Bildkonvertering med användning av WorkbookRender**  

Ett TIFF-bild kan innehålla mer än en frame. Du kan spara hela arbetsboken som en enskild TIFF-bild med flera frames eller sidor:  

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
