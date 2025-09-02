---
title: Insert Background Image to Excel with JavaScript via C++
linktitle: Insert Background Image to Excel
type: docs
weight: 90
url: /javascript-cpp/insert-background-image-to-excel/
description: "How to insert background image to Excel using Aspose.Cells for JavaScript via C++."
---

{{% alert color="primary" %}} 

You can make a worksheet more appealing by adding a picture as a worksheet background. This feature can be quite effective if you have a special corporate graphic that adds a hint of the background without obscuring the data on the sheet. You can set background picture for a sheet using Aspose.Cells API.

{{% /alert %}} 

## **Setting Sheet Background in Microsoft Excel**

To set a sheet's background image in Microsoft Excel (for example, Microsoft Excel 2019):

1. From the **Page Layout** menu, find the **Page Setup** option, and then click the **Background** option.
1. Select a picture to set the sheet's background picture.

   **Setting a sheet background**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Setting Sheet Background with Aspose.Cells for JavaScript via C++**

The code below sets a background image using an image from a stream.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## Related Articles

- [Working with Background in ODS Files](/cells/javascript-cpp/working-with-background-in-ods-files/)