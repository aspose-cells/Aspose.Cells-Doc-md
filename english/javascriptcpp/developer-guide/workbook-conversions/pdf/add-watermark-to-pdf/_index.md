---
title: Add Watermark To PDF with JavaScript via C++
linktitle: Add Watermark To PDF
type: docs
weight: 9
url: /javascript-cpp/add-watermark-to-pdf/
description: Learn how to add text and image watermark to PDF while converting Excel to PDF using Aspose.Cells for JavaScript via C++.
---

While converting an Excel file to PDF, you may have requirements to add a watermark to the PDF file. The following examples show how to add text and image watermarks to the PDF while rendering.

##  **Add text watermark to PDF**

You can easily add a text watermark to a PDF by specifying the text and the corresponding font. Also, you can set alignment, offset, rotation, opacity, foreground/background, and scale to page in [RenderingWatermark](https://reference.aspose.com/cells/javascript-cpp/renderingwatermark/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text Watermark to PDF Example</h1>
        <p>Select a workbook file (optional). The example will also create a new workbook with 3 pages and apply a text watermark, then save to PDF.</p>
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
            // If a file is provided, load it (this mirrors loading sample.xlsx in the Node example)
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                // Loads the workbook which contains hidden external links (if user provided a file)
                const workbook = new Workbook(new Uint8Array(arrayBuffer));
                document.getElementById('result').innerHTML = '<p>Input workbook loaded from file.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>No input file provided. Proceeding with creating a new workbook.</p>';
            }

            // prepare a workbook with 3 pages.
            const wb = new Workbook();
            wb.worksheets.get(0).cells.get("A1").value = "Page1";
            let index = wb.worksheets.add();
            wb.worksheets.get(index).cells.get("A1").value = "Page2";
            index = wb.worksheets.add();
            wb.worksheets.get(index).cells.get("A1").value = "Page3";
            wb.worksheets.get(index).pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA3;

            // create a font for watermark, and specify bold, italic, color.
            const font = new AsposeCells.RenderingFont("Calibri", 68);
            font.italic = true;
            font.bold = true;
            font.color = AsposeCells.Color.Blue;

            // create a watermark from text and the specified font.
            const watermark = new AsposeCells.RenderingWatermark("Watermark", font);

            // specify horizontal and vertical alignment
            watermark.hAlignment = AsposeCells.TextAlignmentType.Center;
            watermark.vAlignment = AsposeCells.TextAlignmentType.Center;

            // specify rotation
            watermark.rotation = 30;

            // specify opacity
            watermark.opacity = 0.6;

            // specify the scale to page(e.g. 100, 50) in percent.
            watermark.scaleToPagePercent = 50;

            // specify watermark for rendering to pdf.
            const options = new AsposeCells.PdfSaveOptions();
            options.watermark = watermark;

            // Save the workbook to PDF with the watermark
            const outputData = wb.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_text_watermark.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF with Watermark';

            document.getElementById('result').innerHTML += '<p style="color: green;">PDF with watermark created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Add image watermark to PDF**

You can add an image watermark to a PDF just by specifying the image bytes of an image. Also, you can set alignment, offset, rotation, opacity, foreground/background, and scale to page in [RenderingWatermark](https://reference.aspose.com/cells/javascript-cpp/renderingwatermark/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Image Watermark</title>
    </head>
    <body>
        <h1>Image Watermark Example</h1>
        <p>Select an optional Excel file (not required) and an image file to use as watermark (SVG/PNG/JPG).</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*,.svg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, RenderingWatermark, PaperSizeType, Utils } = AsposeCells;
        
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
            const imageInput = document.getElementById('imageInput');
            if (!imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an image file to use as watermark.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageBuffer);

            // Prepare a workbook with 3 pages.
            const wb = new Workbook();
            wb.worksheets.get(0).cells.get("A1").putValue("Page1");
            let index = wb.worksheets.add();
            wb.worksheets.get(index).cells.get("A1").putValue("Page2");
            index = wb.worksheets.add();
            wb.worksheets.get(index).cells.get("A1").putValue("Page3");
            wb.worksheets.get(index).pageSetup.paperSize = PaperSizeType.PaperA3;

            // Create a watermark from image bytes.
            const watermark = new RenderingWatermark(imageBytes);

            // Specify offset to alignment.
            watermark.offsetX = 100;
            watermark.offsetY = 200;

            // Specify rotation.
            watermark.rotation = 30;

            // Specify watermark to background.
            watermark.isBackground = true;

            // Specify opacity.
            watermark.opacity = 0.6;

            // Specify the scale to page (e.g. 100, 50) in percent.
            watermark.scaleToPagePercent = 50;

            // Specify watermark for rendering to pdf.
            const options = new PdfSaveOptions();
            options.watermark = watermark;

            // Save workbook to PDF with watermark
            const outputData = wb.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_image_watermark.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```