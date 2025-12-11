---
title: Load a Web Image from a URL into an Excel Worksheet with JavaScript via C++
linktitle: Load a Web Image from a URL into an Excel Worksheet
type: docs
weight: 30
url: /javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: How to convert an image from a URL to an actual Excel image using Aspose.Cells for JavaScript via C++.
keywords: excel show image from url, excel url to image, show image in excel from url, excel insert image from url, convert url to image in excel, excel image from url, load image from url in excel, JavaScript, Excel
---

## Load an Image from a URL into an Excel Worksheet

Aspose.Cells for JavaScript via C++ provides a simple and easy way to load images from URLs into Excel Worksheets. This article explains downloading the image data into a stream and then inserting it into the worksheet using the Aspose.Cells API. Using this method, the images become a part of the Excel file and are not downloaded every time the worksheet is opened.

## Sample Code

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
There may be cases where you want the image to be updated from a URL each time the worksheet is opened. To achieve this, you may follow the instructions given in the [Insert a Linked Picture from Web Address](/cells/javascript-cpp/insert-a-linked-picture-from-web-address/) article. By following this method, the image is loaded from the URL each time the worksheet is opened.
{{% /alert %}}