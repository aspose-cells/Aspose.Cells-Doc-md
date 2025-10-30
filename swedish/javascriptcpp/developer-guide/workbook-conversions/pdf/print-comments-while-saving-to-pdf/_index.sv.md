---
title: Skriv ut kommentarer vid sparande till PDF med JavaScript via C++
linktitle: Skriv ut kommentarer vid sparning till PDF
type: docs
weight: 10
url: /sv/javascript-cpp/print-comments-while-saving-to-pdf/
description: Lär dig hur man skriver ut kommentarer när man sparar Excel dokument till PDF med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Microsoft Excel låter dig skriva ut kommentarer när du skriver ut eller sparar till PDF-format med följande alternativ  

- Ingen  
- I slutet av bladet  
- Enligt visad på kalkylbladet  

Aspose.Cells tillhandahåller [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)-enum för att stödja samma funktion. [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype)-enum har följande medlemmar  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Skriv ut kommentarer vid sparande till PDF**  

Följande exempel kod visar hur man använder [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) för att skriva ut kommentarer när man sparar till PDF.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Print Comments to PDF</title>
    </head>
    <body>
        <h1>Print Comments While Saving to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            const worksheet = workbook.worksheets.get(0);

            worksheet.pageSetup.printComments = AsposeCells.PrintCommentsType.PrintSheetEnd;

            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PrintCommentWhileSavingToPdf_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved to PDF with comments printed at sheet end. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
