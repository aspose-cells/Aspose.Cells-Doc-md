---
title: Rendera anpassat datumformat mönster g och ge mm dd
linktitle: Rendera anpassat datumformat mönster g och ge mm dd  
description: Lär dig hur man renderar anpassade datumformatmönster g och ge i Aspose.Cells for JavaScript via C++ för att kontrollera datumsvisning i kalkylblad.  
keywords: Aspose.Cells, JavaScript bibliotek, elektroniskt kalkylblad, anpassat datumformat, rendering, mönster g , mönster ge , kontrollera visning    
type: docs  
weight: 160  
url: /sv/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells kan nu rendera anpassade datumformatmallar som g, ge.mm.dd och liknande. Vänligen kontrollera den bifogade [källkalkylbladsfilen](5112361.xlsx) och den [konverterade PDF:en](5112360.pdf) av Aspose.Cells för din referens.

{{% /alert %}}  

Följande exempelkod konverterar [källkalkylbladsfilen](5112361.xlsx) som innehåller datumvärden med anpassade formatmallar som g och ge.mm.dd till [utdata-PDF:en](5112360.pdf).  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
