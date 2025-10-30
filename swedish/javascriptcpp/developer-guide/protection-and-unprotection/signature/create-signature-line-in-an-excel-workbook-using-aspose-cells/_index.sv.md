---
title: Skapa signaturlinje i en Excel arbetsbok med Aspose.Cells for JavaScript via C++
linktitle: Skapa signaturlinje i en Excel arbetsbok med hjälp av Aspose.Cells
type: docs
weight: 150
url: /sv/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Denna artikel beskriver hur man skapar en signaturlinje i en Excel arbetsbok med JavaScript och Aspose.Cells for JavaScript via C++.
keywords: Skapa signaturlinje i en Excel arbetsbok JavaScript via C++, Hur man skapar signaturlinje i en Excel arbetsbok, Hur man lägger till signaturlinje, Hur man lägger till signaturlinje till Excel fil.
---

## **Introduktion**  

Microsoft Excel tillhandahåller en funktion för att lägga till **Signature Line** i Excel-arbetsböcker. Du kan lägga till en signaturlinje genom att klicka på fliken **Infoga** och sedan välja **Signaturlinje** från gruppen **Text**.  

## **Hur man skapar en signeringsrad för Excel**  

Aspose.Cells for JavaScript via C++ tillhandahåller också denna funktion och har exponerat egenskapen [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) för detta ändamål. Denna artikel förklarar hur man använder denna egenskap för att lägga till en signaturlinje med Aspose.Cells.  

 Följande exempel kod lägger till en underskriftslinje med [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--)-egenskapen och sparar arbetsboken.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
