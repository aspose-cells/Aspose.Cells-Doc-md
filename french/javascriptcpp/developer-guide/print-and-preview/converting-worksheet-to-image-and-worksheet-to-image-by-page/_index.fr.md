---
title: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page avec JavaScript via C++
linktitle: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page
type: docs
weight: 80
url: /fr/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la manière de convertir une feuille de calcul en un fichier image et une feuille à pages multiples en un fichier image par page.

Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul en tant qu'images, par exemple, pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Fondamentalement, vous voulez afficher la feuille de calcul sous forme d'image. Aspose.Cells prend en charge la conversion des feuilles de calcul dans les fichiers Microsoft Excel en images. De plus, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

Vous pourriez utiliser l'automatisation Office pour y parvenir, mais l'automatisation Office a ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, la scalabilité/la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, mais la principale est que Microsoft elle-même déconseille fortement l'automatisation Office.
{{% /alert %}}

## **Utilisation de Aspose.Cells for JavaScript via C++ pour convertir une feuille de calcul en fichier image**

Cet article montre comment créer une application console, convertir une feuille de calcul en image, et convertir une feuille en une seule image pour chaque feuille avec quelques lignes de code simples en utilisant l'API Aspose.Cells.

Vous devez importer plusieurs classes précieuses liées aux fonctionnalités de rendu dans votre programme ou projet, telles que [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/), etc. La classe [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) représente une feuille de calcul pour rendre des images de la feuille et dispose d'une méthode [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) surchargeable qui peut convertir une feuille en fichiers images directement avec tous attributs ou options définis. Elle peut retourner un objet image et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'images sont pris en charge, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, et autres.

Cet article explique comment :

- Convertir une feuille de calcul en une image
- Convertir chaque page d'une feuille de calcul en une image

Cette tâche montre comment utiliser Aspose.Cells pour convertir une feuille de calcul à partir d'un classeur modèle en un fichier image.

### **Configurer le projet**

1. Tout d'abord, [téléchargez Aspose.Cells for JavaScript via C++](https://downloads.aspose.com/cells/javascript-cpp).
1. Installez-le sur votre ordinateur de développement. Tous les composants [Aspose](http://www.aspose.com/) installés fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et injecte uniquement des filigranes dans les documents produits. Démarrez votre environnement de développement et créez une nouvelle application console. Cet exemple utilise une application console JavaScript, mais vous pouvez utiliser toute configuration qui s'intègre avec JavaScript. Ajoutez une référence à Aspose.Cells dans le projet créé.

### **Convertir une feuille de calcul en un fichier image**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook.xlsx** (1 feuille de calcul). Ensuite, convertissez la feuille de calcul du fichier modèle en un fichier image appelé SheetImage.jpg.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit la Feuille1 dans **Testbook.xlsx** en un fichier image pour expliquer à quel point cette conversion est facile.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## ** Utilisation de Aspose.Cells for JavaScript via C++ pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul d'un classeur modèle comportant plusieurs pages en un fichier image unique par page.

### **Convertir une feuille de calcul en image par page**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook2.xlsx** (1 feuille de calcul).

Maintenant, convertissez la feuille de calcul du fichier modèle en fichiers image (un fichier par page). Comme j'ai déjà créé l'application console pour effectuer la tâche de copie, je vais ignorer ces étapes de création de l'application console et passer directement aux étapes de conversion de la feuille de calcul.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 dans Testbook2.xlsx en fichiers image par page.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
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
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
