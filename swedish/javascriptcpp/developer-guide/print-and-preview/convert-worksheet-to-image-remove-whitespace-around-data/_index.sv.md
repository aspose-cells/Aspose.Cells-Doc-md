---
title: Konvertera kalkylblad till bild  Ta bort tomrum runt data med JavaScript via C++
linktitle: Konvertera kalkylblad till bild  Ta bort mellanrum runt data
type: docs
weight: 40
url: /sv/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Lär dig hur man konverterar Microsoft Excel ark till bilder och tar bort mellanrum runt data med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Ibland måste du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga bilder i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I huvudsak vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells gör det möjligt att konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

## **Ta bort mellanrum runt data**

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)-API:en konverterar ett kalkylblad till en bildfil med vilka attribut som helst, till exempel bildformat, sidade kalkylblad, osv. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder funktionen ark-till-bild har den resulterande bilden ett mellanrum, det vill säga en ram, runt den som standard. Du kan ta bort detta genom att ställa in de översta, understa, vänstra och högra sidmarginalerna för källkalkylbladet till 0 och ange [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)-attribut därefter.

Följande kodsippa tar bort mellanrummet runt datan i den resulterande bilden.

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
