---
title: Image avec JavaScript via C++
linktitle: Image
type: docs
weight: 300
url: /fr/javascript-cpp/convert-excel-to-image/
---

{{% alert color="primary" %}}  
Aspose.Cells vous permet d'exporter une feuille de calcul du classeur et de la convertir en différents formats. Cet article explique comment convertir une feuille de calcul en différents formats.  
{{% /alert %}}  

## Conversion du classeur en TIFF  

 Un fichier Excel peut contenir plusieurs feuilles avec plusieurs pages. [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender) vous permet de convertir Excel en TIFF avec plusieurs pages. De plus, vous pouvez contrôler plusieurs options pour TIFF, comme [ImageOrPrintOptions.tiffCompression](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffCompression--), [ImageOrPrintOptions.tiffColorDepth](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#tiffColorDepth--), Résolution ([ImageOrPrintOptions.horizontalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--), [ImageOrPrintOptions.verticalResolution](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--)).  

Le code ci-dessous montre comment convertir Excel en TIFF avec plusieurs pages. Les [fichier Excel source](workbook-to-tiff-with-mulitiple-pages.xlsx) et [image TIFF générée](workbook-to-tiff-with-mulitiple-pages.tiff) sont joints à titre de référence.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook to TIFF (Multiple Pages) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, TiffCompression, WorkbookRender } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Configure image/print options
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Tiff;
            imgOptions.horizontalResolution = 200;
            imgOptions.verticalResolution = 200;
            imgOptions.tiffCompression = TiffCompression.CompressionLZW;

            // Render workbook to image (TIFF)
            const workbookRender = new WorkbookRender(wb, imgOptions);

            // Obtain image data (multi-page TIFF)
            const outputData = workbookRender.toImage();

            const blob = new Blob([outputData], { type: "image/tiff" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'workbook-to-tiff-with-mulitiple-pages.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TIFF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Conversion de la feuille de calcul en image**  

Les feuilles de calcul contiennent des données que vous souhaitez analyser. Par exemple, une feuille de calcul peut contenir des paramètres, des totaux, des pourcentages, des exceptions et des calculs.  

En tant que développeur, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d'images. Par exemple, une feuille de calcul peut être utilisée comme une image dans une application ou une page web. Vous pourriez vouloir insérer une image dans un document Microsoft Word, un fichier PDF, une présentation PowerPoint ou un autre type de document. En résumé, vous souhaitez que la feuille de calcul soit rendue sous forme d'image afin de pouvoir l'utiliser ailleurs.  

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender)

La classe [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) représente une feuille de calcul à rendre en images. Elle possède une méthode surchargée, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-string-), qui peut convertir une feuille de calcul en fichier(s) image avec différents attributs ou options. Elle renvoie un objet Buffer et vous pouvez enregistrer un fichier image sur le disque ou le diffuser. Plusieurs formats d'image sont supportés, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en fichier image.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet To Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet To Images By Page</h1>
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
            const resultDiv = document.getElementById('result');
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

            // Preparing image/print options
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);
            const pageCount = sr.pageCount;

            if (pageCount === 0) {
                resultDiv.innerHTML = '<p style="color: red;">No pages found to render.</p>';
                return;
            }

            const linksContainer = document.createElement('div');
            linksContainer.innerHTML = '<p style="color: green;">Conversion completed. Download the generated images below:</p>';
            for (let j = 0; j < pageCount; j++) 
            {
                // sr.toImage(pageIndex) returns image bytes in browser build
                const imageData = sr.toImage(j);
                const blob = new Blob([imageData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);

                const link = document.createElement('a');
                link.href = url;
                link.download = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
                link.textContent = "Download Image Page " + (j + 1);
                link.style.display = 'block';
                linksContainer.appendChild(link);
            }

            resultDiv.appendChild(linksContainer);
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Actuellement, l'API de conversion des feuilles de calcul en images ne prend pas en charge les graphiques à bulles en 3D.  
{{% /alert %}}  

## **Conversion de feuille de calcul en SVG**  

SVG signifie Scalable Vector Graphics. SVG est une spécification basée sur les normes XML pour les graphiques vectoriels bidimensionnels. Il s'agit d'une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.  

Aspose.Cells for JavaScript via C++ a pu convertir des feuilles de calcul en image SVG depuis la version 7.1.0. Le code suivant montre comment convertir une feuille de calcul dans un fichier Excel en un fichier image SVG.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to SVG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetType } = AsposeCells;

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
            // Instantiate a workbook
            const workbook = new Workbook();

            // Put sample text in the first cell of the first worksheet in the newly created workbook
            workbook.worksheets.get(0).cells.get("A1").putValue("DEMO TEXT ON SHEET1");

            // Add second worksheet in the workbook
            workbook.worksheets.add(SheetType.Worksheet);

            // Set text in the first cell of the second sheet
            workbook.worksheets.get(1).cells.get("A1").putValue("DEMO TEXT ON SHEET2");

            // Set currently active sheet index to 1 i.e. Sheet2
            workbook.worksheets.activeSheetIndex = 1;

            // Save workbook to SVG. It shall render the active sheet only to SVG
            const outputData = workbook.save(SaveFormat.Svg);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertWorksheetToSVG_out.svg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download SVG File';

            document.getElementById('result').innerHTML = '<p style="color: green;">SVG generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Sujets avancés**  
- [Convertir un graphique Excel en image](/cells/fr/javascript-cpp/convert-an-excel-chart-to-image/)  
- [Conversion de graphique en image au format SVG](/cells/fr/javascript-cpp/converting-chart-to-image-in-svg-format/)  
- [Exportation du graphique en SVG avec l'attribut viewBox](/cells/fr/javascript-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Suivre la progression de la conversion d'Excel en TIFF](/cells/fr/javascript-cpp/track-conversion-progress-of-excel-to-tiff/)
