---
title: Skapa transparent bild av Excel ark med JavaScript via C++
linktitle: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /sv/javascript-cpp/create-transparent-image-of-excel-worksheet/
description: Lär dig hur man genererar en transparent bild av ett Excel ark med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Ibland behöver du generera bilden av ditt arbetsblad som en transparent bild. Du vill applicera transparens på alla celler som inte har fyllnadsfärger. Aspose.Cells tillhandahåller egenskapen [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--) för att applicera transparens på arbetsbilden. När denna egenskap är **false**, då ritas celler utan fyllnadsfärger med vit färg och när den är **true**, ritas celler utan fyllnadsfärger transparent.

{{% /alert %}}

I följande arbetsbladsbild har inte transparens tillämpats. Celler utan fyllfärger är ritade vita.

|**Utdata utan transparens: cellens bakgrund är vit**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Medan i följande arbetsbladsbild har transparens tillämpats. Cellerna utan fyllfärger är transparenta.

|**Utdata med aktiverad transparens**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Följande exempelkod genererar en transparent bild från ett Excel-ark.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Create Transparent Image Example</title>
    </head>
    <body>
        <h1>Create Transparent Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Create Transparent PNG</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

            // Create workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = wb.worksheets.get(0);

            // Apply different image or print options
            const imgOption = new ImageOrPrintOptions();
            imgOption.imageType = ImageType.Png;
            imgOption.horizontalResolution = 200;
            imgOption.verticalResolution = 200;
            imgOption.onePagePerSheet = true;

            // Apply transparency to the output image
            imgOption.transparent = true;

            // Create image after applying image or print options
            const sr = new SheetRender(sheet, imgOption);
            const outputData = await sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateTransparentImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image created successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
