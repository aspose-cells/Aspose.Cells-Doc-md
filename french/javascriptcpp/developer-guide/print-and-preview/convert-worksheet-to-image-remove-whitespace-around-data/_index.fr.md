---
title: Convertir la feuille de calcul en image  Supprimer l espace blanc autour des données avec JavaScript via C++
linktitle: Convertir la feuille de calcul en image  Supprimer les espaces blancs autour des données
type: docs
weight: 40
url: /fr/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Apprenez comment convertir les feuilles de calcul Microsoft Excel en images et supprimer l espace blanc autour des données à l aide de Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Parfois, vous devez présenter des images de feuille de calcul dans des applications ou des pages web. Par exemple, vous pourriez avoir besoin d'insérer des images dans un document Word, un fichier PDF, une présentation PowerPoint ou un autre document. Fondamentalement, vous souhaitez afficher une feuille de calcul sous forme d'image afin de pouvoir la coller dans d'autres applications. Aspose.Cells vous permet de convertir des feuilles de calcul Microsoft Excel en images.

{{% /alert %}}

## **Supprimer les espaces vides autour des données**

L'API [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) convertit une feuille de calcul en un fichier image avec les attributs spécifiés, par exemple, le format de l'image, les feuilles paginées, etc. Plusieurs formats d'image sont pris en charge, notamment BMP, GIF, JPG, TIFF et EMF.

Lorsque vous utilisez la fonction de feuille à image, l'image de sortie comporte par défaut des espaces vides, c'est-à-dire une bordure. Vous pouvez supprimer cela en définissant les marges de mise en page supérieure, inférieure, gauche et droite pour la feuille source sur 0 et en spécifiant les attributs [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) en conséquence.

Le code suivant supprime les espaces vides autour des données dans l'image de sortie.

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

            // Set only one page would be rendered for the image
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
