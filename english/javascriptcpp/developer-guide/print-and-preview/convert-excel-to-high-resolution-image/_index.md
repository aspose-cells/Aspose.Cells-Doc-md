---
title: Convert Excel to High-Resolution Image with JavaScript via C++
linktitle: Convert Excel to High-Resolution Image
type: docs
weight: 100
url: /javascript-cpp/convert-excel-to-high-resolution-image/
description: Learn how to convert Excel files to high‑resolution images using Aspose.Cells for JavaScript via C++.
---

With the increasing prevalence of high‑resolution screens, images generated at the default 96 DPI often appear blurry and unclear. To ensure clarity on high‑resolution screens, it is essential to generate images at a higher DPI. Aspose.Cells for JavaScript via C++ provides the functionality to set [**ImageOrPrintOptions.horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--) and [**ImageOrPrintOptions.verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--), allowing you to create high‑quality images from Excel files that look sharp on high‑resolution displays.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Sheet to Image</title>
    </head>
    <body>
        <h1>Convert Worksheet to PNG Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Image</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;
        
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create ImageOrPrintOptions and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 300;
            options.verticalResolution = 300;
            options.imageType = ImageType.Png;

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Create SheetRender instance
            const render = new SheetRender(sheet, options);

            // Generate an image for the first page/index (0)
            const imageData = render.toImage(0);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```