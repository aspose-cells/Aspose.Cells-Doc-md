---
title: Ställa in olika rubriker och sidfötter för olika sidor med JavaScript via C++
linktitle:  Inställ olika sidhuvuden och sidfötter för olika sidor 
type: docs
weight: 35
url: /sv/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Denna artikel visar exempel på kod som demonstrerar hur man programmässigt ställer in rubriker och sidfötter för Excel kalkylbladets sidinställningar med Aspose.Cells for JavaScript via C++. Ställ in rubriker och sidfötter för första, ojämna och jämna sidor.
keywords: Ställa in Excel huvud och sidfot för första sidan JavaScript via C++, ställa in Excel huvud och sidfot för udda sidor JavaScript via C++, ställa in Excel huvud och sidfot för jämna sidor JavaScript via C++
---

{{% alert color="primary" %}}

MS Excel stöder att ställa in olika rubriker och fotnoter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells for JavaScript via C++ stöder samma funktion.

{{% /alert %}}

## **Inställning av olika sidhuvuden och sidfötter i MS Excel**

**![Inställning av olika sidhuvuden och sidfötter](difpage.png)**

1. Klicka på **Sidlayout > Sidhuvud/fot > Sidhuvud/sidfot**.
1. Kontrollera **Different Odd and Even Pages** eller **Different first page**.
1. Ange olika sidhuvuden och sidfötter.

## **Ställa in olika rubriker och sidfötter med Aspose.Cells for JavaScript via C++**

Aspose.Cells beter sig på samma sätt som Excel.
1. Sätter flaggorna [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) och [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) 
1. Ange olika sidhuvuden och sidfötter.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
