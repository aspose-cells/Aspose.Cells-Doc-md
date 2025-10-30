---
title: Rendera kalkylblad till grafikkontext med JavaScript via C++
linktitle: Rendera arbetsblad till grafiskt sammanhang
type: docs
weight: 300
url: /sv/javascript-cpp/render-worksheet-to-graphic-context/
description: Lär dig hur du renderar ett kalkylblad till grafikkontext med Aspose.Cells for JavaScript via C++. Detta inkluderar rendering till bildfiler, skärmar och skrivare.
---

{{% alert color="primary" %}}

Aspose.Cells kan nu rendera kalkylblad till grafisk kontext. Grafisk kontext kan vara vad som helst, som en bildfil, skärm eller skrivare osv. Använd någon av följande två metoder för att rendera ett kalkylblad till grafisk kontext.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Följande kod visar hur man använder Aspose.Cells för att rendera ett kalkylblad till grafisk kontext. När du kör koden kommer den att skriva ut hela kalkylbladet och fylla återstående tomt utrymme med blå färg i den grafiska kontexten och spara bilden som **OutputImage_out_.png**. Du kan använda vilken Excel-fil som helst för att prova detta. Läs också gärna kommentarerna i koden för bättre förståelse.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Worksheet to Image</title>
    </head>
    <body>
        <h1>Render Worksheet to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, Utils } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create empty image buffer options
            const bmpOptions = new ImageOrPrintOptions();
            bmpOptions.onePagePerSheet = true;

            // Render worksheet to image
            const sheetRender = new SheetRender(worksheet, bmpOptions);
            const imageData = sheetRender.toImage(0);

            // Create blob and provide download link for PNG
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputImage_out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to download the PNG.</p>';
        });
    </script>
</html>
```
