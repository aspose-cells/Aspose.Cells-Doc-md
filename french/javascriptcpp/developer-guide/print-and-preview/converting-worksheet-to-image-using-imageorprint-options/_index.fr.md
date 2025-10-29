---
title: Conversion de la feuille de calcul en image en utilisant les options ImageOuPrint avec JavaScript via C++
linktitle: Convertir une feuille de calcul en image en utilisant des options ImageOrPrint
type: docs
weight: 90
url: /fr/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Apprenez comment convertir une feuille de calcul en un fichier image et appliquer diverses options d image et d impression à l aide de Aspose.Cells for JavaScript via C++.   
---

{{% alert color="primary" %}}  
Ce document est conçu pour fournir une compréhension détaillée de la manière de convertir une feuille de calcul en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, comme la résolution, la compression TIFF, le format d'image et la qualité de page.  
{{% /alert %}}  

## **Enregistrement de feuilles de calcul en images - différentes approches**  

Parfois, vous pourriez avoir besoin de présenter vos feuilles de calcul sous forme de représentation imagée. Vous devez présenter les images de feuilles de calcul dans vos applications ou pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre contexte. Tout simplement, vous souhaitez une feuille de calcul rendue sous forme d'image afin de pouvoir l'utiliser ailleurs. Aspose.Cells prend en charge la conversion des feuilles de calcul dans des fichiers Excel en images. De plus, Aspose.Cells prend en charge la définition de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité d'image et d'autres options d'image et d'impression.  

Vous pouvez essayer l'automatisation Office, mais celle-ci présente ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple, sécurité, stabilité, évolutivité et vitesse, prix, et fonctionnalités. En résumé, il y a de nombreuses raisons, la principale étant que Microsoft recommande vivement de ne pas utiliser l'automatisation Office à partir de solutions logicielles.  

Cet article montre comment créer une application console dans Visual Studio .NET, effectuer la conversion d'une feuille de calcul en image en utilisant différentes options d'image et d'impression avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.  

La classe [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) représente une feuille de calcul pour rendre des images, elle a une méthode [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) surchargée qui peut convertir directement une feuille en fichier(s) image avec vos attributs ou options souhaités. Elle peut renvoyer un objet que vous pouvez enregistrer en image sur le disque/flux. Plusieurs formats d'image sont supportés, par exemple BMP, PNG, GIF, JPEG, TIFF, EMF, etc.  

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en image en utilisant des options ImageOrPrint.**  

### **Création d'un classeur modèle dans Microsoft Excel**  

J'ai créé un nouveau classeur dans MS Excel et ajouté des données dans la première feuille de calcul. Maintenant, je vais convertir la feuille de calcul du fichier modèle "Feuille1" en un fichier image "FeuilleImage.tiff" et appliquer différentes options d'image comme les résolutions horizontales et verticales, la compression Tiff, etc.  

### **Téléchargez et installez Aspose.Cells**  

Tout d'abord, vous devez [télécharger](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript via C++. Installez-le sur votre ordinateur de développement. Tous les composants [Aspose](http://www.aspose.com/) installés fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et injecte uniquement des filigranes dans les documents produits.  

### **Créer un projet**  

Démarrez votre environnement de développement préféré (par exemple, Visual Studio). Créez une nouvelle application console.  

### **Ajouter des références**  

Ce projet utilisera Aspose.Cells. Vous devez donc ajouter une référence au composant Aspose.Cells dans votre projet. Par exemple, ajoutez une référence à ….\Program Files\Aspose\Aspose.Cells for JavaScript via C++\Bin\Aspose.Cells.node  

### **Convertir une feuille de calcul en un fichier image**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **Options de conversion**  

Il est possible d'enregistrer des pages spécifiques en tant qu'images. Le code suivant convertit les première et deuxième feuilles de calcul dans un classeur en images JPG.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **Conversion d'image à l'aide de WorkbookRender**  

Une image TIFF peut contenir plus d’un cadre. Vous pouvez enregistrer tout le classeur dans une seule image TIFF avec plusieurs cadres ou pages :  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
