---
title: Extract Images from Worksheets using ImageOrPrintOptions with JavaScript via C++
linktitle: Extract Images from Worksheets using ImageOrPrintOptions
type: docs
weight: 140
url: /javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Learn how to extract images from Excel worksheets and save them using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel users can add images to spreadsheets. With Aspose.Cells for JavaScript via C++, it's possible to read images from Microsoft Excel files and save them to a local drive. This article shows how.

{{% /alert %}} 

The sample code below shows how to extract images from an Excel file and save them.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Image from Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;
        
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

            // Open the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the first picture in the first worksheet
            const pic = worksheet.pictures.get(0);

            // Determine the picture format
            const picformat = pic.imageType.toString();

            // Define the ImageOrPrintOptions
            const printoption = new ImageOrPrintOptions();

            // Specify the image format (use JPEG as in original code)
            printoption.imageType = ImageType.Jpeg;

            // Export the picture to image bytes (the browser version returns image bytes when a path is not used)
            const outputData = pic.toImage(printoption);

            // Determine the file extension and MIME type
            let ext = picformat.toLowerCase();
            if (ext === 'jpeg') ext = 'jpg';
            let mime = 'image/jpeg';
            if (ext === 'png') mime = 'image/png';
            if (ext === 'gif') mime = 'image/gif';

            const filename = 'outputExtractImagesFromWorksheets.' + ext;

            const blob = new Blob([outputData], { type: mime });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = filename;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```