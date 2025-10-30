---
title: Konvertering av ark till bild och ark till bild per sida med JavaScript via C++
linktitle: Konvertera kalkylblad till bild och Kalkylblad till bild per sida
type: docs
weight: 80
url: /sv/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Detta dokument är avsett att ge utvecklare en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil och ett kalkylblad med flera sidor till en bildfil per sida.

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kanske behöver infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Kort sagt, du vill rendera kalkylbladet som en bild. Aspose.Cells stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells konvertering av en arbetsbok till flera bildfiler, en per sida.

Du kan använda Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt, det finns många skäl, men det främsta är att Microsoft själva starkt rekommenderar att inte använda Office Automation.
{{% /alert %}}

## **Använda Aspose.Cells for JavaScript via C++ för att konvertera ark till bildfil**

Denna artikel visar hur man skapar en konsolapplikation, konverterar ett kalkylblad till en bild och konverterar ett kalkylblad till en bild för varje kalkylblad med några få och enkla kodrader med Aspose.Cells API.

Du behöver importera flera värdefulla klasser relaterade till renderingfunktioner till ditt program eller projekt, såsom [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/) och så vidare. Klassen [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) representerar ett ark för att rendera bilder för arket och har en överbelastad [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) metod som kan konvertera ett ark till bildfiler direkt med vilka som helst attribut eller inställningar. Den kan returnera ett bildobjekt och du kan spara en bildfil till disken/strömmen. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF och andra.

Den här artikeln förklarar hur man:

- Konvertera ett kalkylblad till en bild
- Konvertera varje sida i ett kalkylblad till en bild

Det här exemplet visar hur man använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbok till en bildfil.

### **Installationsprojekt**

1. Först, [ladda ner Aspose.Cells for JavaScript via C++](https://downloads.aspose.com/cells/javascript-cpp).
1. Installera det på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsgräns och infogar endast vattentmärken i producerade dokument. Starta nu din utvecklingsmiljö och skapa ett nytt konsolprogram. Detta exempel använder ett JavaScript-konsolprogram, men du kan använda valfri setup som integrerar med JavaScript. Lägg till referens till Aspose.Cells i det skapade projektet.

### **Konvertera kalkylblad till bildfil**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första kalkylbladet: **Testbook.xlsx** (1 kalkylblad). Nästa steg är att konvertera mallfilens kalkylblad Sheet1 till en bildfil som kallas SheetImage.jpg.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i **Testbook.xlsx** till en bildfil för att förklara hur enkel denna konvertering är.

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

## **Använda Aspose.Cells for JavaScript via C++ för att konvertera ark till bildfil per sida**

Detta exempel visar hur man använder Aspose.Cells för att konvertera ett arbetsblad från en mallarbok som har flera sidor till en bildfil per sida.

### **Konvertera kalkylblad till bild per sida**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första arbetsbladet: **Testbook2.xlsx** (1 arbetsblad).

Nu, konvertera mallfilens arbetsblad Sheet1 till bildfiler (en fil per sida). Eftersom jag redan skapat konsolapplikationen för att utföra kopieringsuppgiften, kommer jag att hoppa över de stegen för att skapa konsolapplikationen och gå direkt till arbetsbladskonverteringsstegen.

Följande är koden som används av komponenten för att slutföra uppgiften. Den konverterar Sheet1 i Testbook2.xlsx till bildfiler per sida.

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
