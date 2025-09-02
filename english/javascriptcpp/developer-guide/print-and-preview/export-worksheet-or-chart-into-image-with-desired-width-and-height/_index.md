---
title: Export Worksheet or Chart into Image with Desired Width and Height via JavaScript
linktitle: Export Worksheet or Chart into Image with Desired Width and Height
type: docs
weight: 290
url: /javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Learn how to export a worksheet or chart to an image with specified width and height using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
You can use Aspose.Cells for JavaScript via C++ to export your worksheet or chart into an image with the desired width and height. It provides [**ImageOrPrintOptions.desiredSize(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#desiredSize-number-number-boolean-) method to set the desired width and height of the exported image. The width and height are specified in the unit of pixels.
{{% /alert %}}

The following code exports the worksheet into an image with 400x400 size.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image (Desired Size) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;
        
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

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set image or print options: one page per sheet, PNG, desired dimensions 400x400
            const opts = new ImageOrPrintOptions();
            opts.onePagePerSheet = true;
            opts.imageType = ImageType.Png;
            // Converted setter with multiple params to a single property assignment (array)
            opts.desiredSize = [400, 400, false];

            // Render sheet into image
            const sr = new SheetRender(worksheet, opts);
            const imageData = sr.toImage(0);

            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputWorksheetToImageDesiredSize.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```