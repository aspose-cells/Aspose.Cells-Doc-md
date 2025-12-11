---
title: Setting Different Headers and Footers For Different Pages with JavaScript via C++
linktitle: Setting Different Headers and Footers For Different Pages
type: docs
weight: 35
url: /javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: This article provides sample code that shows how to programmatically set headers and footers of an Excel worksheet's Page Setup using Aspose.Cells for JavaScript via C++. Set headers and footers for the first, odd, and even pages.
keywords: set excel header footer first page JavaScript via C++, set excel header footer odd pages JavaScript via C++, set excel header footer even pages JavaScript via C++
---

{{% alert color="primary" %}}

MS Excel supports setting different headers and footers for the first page, odd pages, and even pages since Excel 2007.  
Aspose.Cells for JavaScript via C++ supports the same feature.

{{% /alert %}}

## **Setting Different Headers and Footers in MS Excel**

**![Setting Different Headers and Footers](difpage.png)**

1. Click **Page Layout > Print Titles > Header/Footer**.  
2. Check **Different Odd and Even Pages** or **Different First Page**.  
3. Enter different headers and footers.

## **Setting Different Headers and Footers with Aspose.Cells for JavaScript via C++**

Aspose.Cells behaves the same as Excel.  

1. Set the flags [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) and [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--)  
2. Enter different headers and footers.

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