---
title: Rendera gradientfyllning för WordArt när du konverterar kalkylblad till HTML med JavaScript via C++
linktitle: Rendera Gradient Fill för WordArt vid konvertering av kalkylblad till HTML
type: docs
weight: 90
url: /sv/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Lär dig hur man renderar gradientfyllning för WordArt vid konvertering av kalkylblad till HTML med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  
 Före Aspose.Cells 17.1 renderades inte gradientfyllningen för WordArt när Excel-filen konverterades till HTML-format. Sedan Aspose.Cells 17.1 stöds WordArt-gradientfyllning. Följande skärmbild jämför effekten av gradientfyllning vid konvertering av Excel-filen med Aspose.Cells 17.1 och äldre version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Rendera Gradient Fill för WordArt vid konvertering av kalkylblad till HTML**  
 Följande exempel kod konverterar den [käll Excel-filen](22774111.xlsx) till [utdata HTML-format](22774109.zip). Källxle-filen innehåller ett WordArt-objekt med gradientfyllning som visas i ovanstående skärmbild.  

## **Exempelkod**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
