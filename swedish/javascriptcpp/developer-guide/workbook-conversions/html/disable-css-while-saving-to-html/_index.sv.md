---
title: Inaktivera CSS vid spara till HTML med JavaScript via C++
linktitle: Inaktivera CSS vid sparning till HTML
type: docs
weight: 320
url: /sv/javascript-cpp/disable-css-while-saving-to-html/
description: Lär dig hur du inaktiverar CSS när du sparar Excel filer till HTML med Aspose.Cells for JavaScript via C++. 
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till en enkel HTML-sida kommer CSS-elementen vanligtvis att inbäddas i HTML-filen och befinna sig i `<head>`-sektionen. Om du bifogar denna fil som innehåll/kropp i ett e-postmeddelande, kommer de flesta e-postklienter att ta bort CSS-elementen, vilket resulterar i felaktig rendering. Version 24.12 av Aspose.Cells introducerar ett alternativ som gör det möjligt att inaktivera CSS, vilket gör att stilar kan tillämpas direkt inom HTML-elementen. Om du vill använda HTML som innehåll/kropp i e-postmeddelandet, använd [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--)-egenskapen och ställ in den till **true**.

## **Inaktivera CSS vid sparning till HTML**

Följande exempel visar användningen av [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) egenskapen. 

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
