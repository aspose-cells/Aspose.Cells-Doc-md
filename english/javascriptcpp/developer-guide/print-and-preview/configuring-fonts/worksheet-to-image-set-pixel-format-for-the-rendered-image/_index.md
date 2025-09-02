---
title: Worksheet to Image - Set Pixel Format for the Rendered Image with JavaScript via C++
linktitle: Worksheet to Image - Set Pixel Format for the Rendered Image
type: docs
weight: 200
url: /javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/
---

{{% alert color="primary" %}}  
Sometimes you want to specify the pixel format when rendering a worksheet to image format. By default, Aspose.Cells uses 32 bits per pixel. Aspose.Cells allows you to customize the pixel format (bit depth) using options for the rendered image.  
{{% /alert %}}  

Please see the sample code below that demonstrates how to set the desired pixel format while rendering images of the sheets.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Pixel Format Rendered Image</title>
    </head>
    <body>
        <h1>Set Pixel Format Rendered Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ColorDepth, ImageType } = AsposeCells;
        
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the ImageOrPrintOptions with desired color depth (24 bits per pixel) and image format type
            const opts = new ImageOrPrintOptions();
            opts.tiffColorDepth = ColorDepth.Format24bpp;
            opts.imageType = ImageType.Tiff;

            // Instantiate SheetRender object based on the first worksheet
            const sheetRender = new SheetRender(worksheet, opts);

            // Render the first page of the sheet to an image (returns binary data)
            const imageData = sheetRender.toImage(0);

            // Create a blob and provide a download link for the rendered TIFF image
            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetPixelFormatRenderedImage.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Rendered TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```