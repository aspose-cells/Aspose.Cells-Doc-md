---
title: Convert Worksheet to Image - Remove whitespace around data with JavaScript via C++
linktitle: Convert Worksheet to Image - Remove whitespace around data
type: docs
weight: 40
url: /javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Learn how to convert Microsoft Excel worksheets to images and remove whitespace around data using Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation, or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells allows you to convert Microsoft Excel worksheets to images.

{{% /alert %}}

## **Remove Whitespace around Data**

The [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) API converts a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.

When you use the sheet‑to‑image feature, the output image has whitespace, that is, a border, around it by default. You can remove this by setting the top, bottom, left, and right page‑setup margins for the source worksheet to 0 and specifying [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) attributes accordingly.

The following code snippet removes the whitespace around the data in the output image.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;
        
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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Only one page will be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```