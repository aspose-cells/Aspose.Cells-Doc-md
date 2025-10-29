---
title: Générer une miniature de la feuille de calcul avec JavaScript via C++
linktitle: Générer une miniature de la feuille de calcul
type: docs
weight: 110
url: /fr/javascript-cpp/generate-thumbnail-of-the-worksheet/
description: Apprenez comment générer une image miniature à partir d une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++. Créez de petites images pour les aperçus dans les documents et présentations.
---

{{% alert color="primary" %}} 

Il peut être utile de générer des miniatures à partir de feuilles de calcul. Une miniature est une petite image qui peut être collée dans un document Word ou une présentation PowerPoint pour donner un aperçu de ce qui se trouve sur la feuille de calcul. Elle peut être ajoutée à une page web avec un lien pour télécharger le document original et avoir une multitude d'autres utilisations.

{{% /alert %}} 

Aspose.Cells for JavaScript via C++ vous permet d’exporter des feuilles de calcul en fichiers image, facilitant ainsi la création de miniatures. Le code d'exemple ci-dessous montre comment exporter des feuilles de calcul en fichiers image.

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
