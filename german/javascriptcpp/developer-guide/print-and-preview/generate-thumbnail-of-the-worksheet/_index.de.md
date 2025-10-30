---
title: Miniaturansicht des Arbeitsblatts mit JavaScript via C++ erstellen
linktitle: Thumbnail des Arbeitsblatts generieren
type: docs
weight: 110
url: /de/javascript-cpp/generate-thumbnail-of-the-worksheet/
description: Erfahren Sie, wie Sie mit Aspose.Cells for JavaScript via C++ eine Miniaturansicht eines Arbeitsblatts erstellen. Erstellen Sie kleine Bilder für Vorschauen in Dokumenten und Präsentationen.
---

{{% alert color="primary" %}} 

Es kann nützlich sein, Miniaturansichten aus Arbeitsblättern zu generieren. Eine Miniaturansicht ist ein kleines Bild, das in ein Word-Dokument oder eine PowerPoint-Präsentation eingefügt werden kann, um eine Vorschau dessen zu geben, was sich auf dem Arbeitsblatt befindet. Sie kann einer Webseite mit einem Link zum Download des Originaldokuments hinzugefügt werden und hat viele weitere Verwendungsmöglichkeiten.

{{% /alert %}} 

Aspose.Cells for JavaScript via C++ ermöglicht es, Arbeitsblätter in Bilder zu exportieren, wodurch das Erstellen einer Miniaturansicht einfach wird. Der Beispielcode unten zeigt, wie man Arbeitsblätter in Bilddateien exportiert.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Generate Worksheet Thumbnail Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Generate Thumbnail</button>
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

            // Instantiate and open an Excel file from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Set the vertical and horizontal resolution
            imgOptions.verticalResolution = 200;
            imgOptions.horizontalResolution = 200;

            // One page per sheet is enabled
            imgOptions.onePagePerSheet = true;

            // Set desired thumbnail dimensions (converted to a property assignment)
            imgOptions.desiredSize = [600, 600, true];

            // Get the first worksheet
            const sheet = book.worksheets.get(0);

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateThumbnailOfWorksheet.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Thumbnail Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Thumbnail generated successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
