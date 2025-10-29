---
title: Convertir Excel en PDF, en image et dans d autres formats
linktitle: Conversions de classeur
type: docs
weight: 65
url: /fr/javascript-cpp/convert-workbook-to-different-formats/
description: Convertir des fichiers Excel en Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML et plus encore en utilisant JavaScript via C++.
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la conversion entre de nombreux formats. Techniquement, la conversion consiste à charger un classeur dans un format de fichier et à le sauvegarder dans un autre.
{{% /alert %}}

## **Convertir un classeur Excel en PDF**
Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As PDF Example</title>
    </head>
    <body>
        <h1>Save Excel as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en JPG**
Aspose.Cells prend en charge la conversion de fichiers Excel en JPG. L'exemple de code ci-dessous montre comment enregistrer un classeur en JPG.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert Workbook to JPG Example</title>
    </head>
    <body>
        <h1>Convert Workbook to JPG Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JPG</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Convert workbook to JPG image
            const outputData = workbook.save(SaveFormat.Jpeg);
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Image1.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JPG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the download link to get the JPG image.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en image**
Aspose.Cells prend en charge la conversion de fichiers Excel en images. L'exemple de code ci-dessous montre comment enregistrer un classeur en images.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Convert Workbook to Images</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Images</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="downloads"></div>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            document.getElementById('result').innerHTML = '<p>Converting workbook to images...</p>';
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define desired image formats
            const formats = [
                { fmt: SaveFormat.Bmp, name: 'Image1.bmp', mime: 'image/bmp' },
                { fmt: SaveFormat.Jpeg, name: 'Image1.jpg', mime: 'image/jpeg' },
                { fmt: SaveFormat.Png, name: 'Image1.png', mime: 'image/png' },
                { fmt: SaveFormat.Emf, name: 'Image1.emf', mime: 'image/emf' },
                { fmt: SaveFormat.Gif, name: 'Image1.gif', mime: 'image/gif' }
            ];

            const downloadsDiv = document.getElementById('downloads');
            downloadsDiv.innerHTML = '';

            // Convert and create download links for each image format
            for (const f of formats) {
                const outputData = workbook.save(f.fmt);
                const blob = new Blob([outputData], { type: f.mime });
                const url = URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.download = f.name;
                a.textContent = 'Download ' + f.name;
                a.style.display = 'block';
                downloadsDiv.appendChild(a);
            }

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed. Click the links below to download the images.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en XPS**
Le format de document XPS se compose de balises XML structurées qui définissent la mise en page d'un document et l'apparence visuelle de chaque page, ainsi que des règles de rendu pour la distribution, l'archivage, le rendu, le traitement et l'impression de documents.

Le langage de balisage pour XPS est un sous-ensemble de XAML qui lui permet d'incorporer des éléments graphiques vectoriels dans des documents, en utilisant XAML pour baliser les primitives de la Fondation Windows Presentation (WPF). Les éléments utilisés sont décrits en termes de chemins et d'autres primitives géométriques.

Un fichier XPS est en fait une archive ZIP Unicode utilisant les Conventions d'Emballage Ouvert, contenant les fichiers constituant le document. Il comprend un fichier de balisage XML pour chaque page, du texte, des polices intégrées, des images raster, des graphiques vectoriels 2D, ainsi que des informations de gestion des droits numériques. Le contenu d'un fichier XPS peut être examiné simplement en l'ouvrant avec une application prenant en charge les fichiers ZIP.

À partir de Aspose.Cells 6.0.0, la conversion de Microsoft Excel en XPS est prise en charge.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render to XPS</title>
    </head>
    <body>
        <h1>Render Worksheet / Workbook to XPS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkSheet" style="display: none; margin-right: 10px;">Download Sheet XPS</a>
            <a id="downloadLinkWorkbook" style="display: none;">Download Workbook XPS</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XpsSaveOptions, SheetSet } = AsposeCells;

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
            const downloadLinkSheet = document.getElementById('downloadLinkSheet');
            const downloadLinkWorkbook = document.getElementById('downloadLinkWorkbook');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Render the sheet to XPS
            const options = new XpsSaveOptions();
            const sheetSet = new SheetSet([sheet.index]);
            options.sheetSet = sheetSet;
            const outputDataSheet = workbook.save(SaveFormat.Xps, options);
            const blobSheet = new Blob([outputDataSheet], { type: 'application/vnd.ms-xps' });
            downloadLinkSheet.href = URL.createObjectURL(blobSheet);
            downloadLinkSheet.download = 'out_printingxps.out.xps';
            downloadLinkSheet.style.display = 'inline-block';
            downloadLinkSheet.textContent = 'Download Sheet XPS';

            // Export the whole workbook to XPS
            const outputDataWorkbook = workbook.save(SaveFormat.Xps, new XpsSaveOptions());
            const blobWorkbook = new Blob([outputDataWorkbook], { type: 'application/vnd.ms-xps' });
            downloadLinkWorkbook.href = URL.createObjectURL(blobWorkbook);
            downloadLinkWorkbook.download = 'out_whole_printingxps.out.xps';
            downloadLinkWorkbook.style.display = 'inline-block';
            downloadLinkWorkbook.textContent = 'Download Workbook XPS';

            resultDiv.innerHTML = '<p style="color: green;">XPS files generated. Use the links above to download the sheet and workbook XPS files.</p>';
        });
    </script>
</html>
```

## **Convertir Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells prend en charge la conversion de fichiers Excel en fichiers Ods, Sxc et Fods. L'exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichier Ods, Sxc et Fods.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save As Multiple Formats Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Save As ODS / SXC / FODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert and Download</button>
        <div style="margin-top: 10px;">
            <a id="downloadLinkOds" style="display: none; margin-right: 10px;">Download ODS</a>
            <a id="downloadLinkSxc" style="display: none; margin-right: 10px;">Download SXC</a>
            <a id="downloadLinkFods" style="display: none; margin-right: 10px;">Download FODS</a>
        </div>
        <div id="result" style="margin-top: 10px;"></div>

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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ods file
            const outputOds = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([outputOds]);
            const downloadLinkOds = document.getElementById('downloadLinkOds');
            downloadLinkOds.href = URL.createObjectURL(blobOds);
            downloadLinkOds.download = 'Out.ods';
            downloadLinkOds.style.display = 'inline-block';
            downloadLinkOds.textContent = 'Download ODS File';

            // Save as sxc file
            const outputSxc = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([outputSxc]);
            const downloadLinkSxc = document.getElementById('downloadLinkSxc');
            downloadLinkSxc.href = URL.createObjectURL(blobSxc);
            downloadLinkSxc.download = 'Out.sxc';
            downloadLinkSxc.style.display = 'inline-block';
            downloadLinkSxc.textContent = 'Download SXC File';

            // Save as fods file
            const outputFods = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([outputFods]);
            const downloadLinkFods = document.getElementById('downloadLinkFods');
            downloadLinkFods.href = URL.createObjectURL(blobFods);
            downloadLinkFods.download = 'Out.fods';
            downloadLinkFods.style.display = 'inline-block';
            downloadLinkFods.textContent = 'Download FODS File';

            result.innerHTML = '<p style="color: green;">Files converted successfully! Click the download links to get the converted files.</p>';
        });
    </script>
</html>
```

## **Conversion de Classeur Excel en Fichiers MHTML**
Le format MHTML combine du HTML normal avec des ressources externes (c'est-à-dire du contenu généralement lié tel que des images, des animations, de l'audio, etc.) dans un seul fichier. Ils sont utilisés pour les e-mails avec l'extension de fichier .mht.

Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier MHTML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to MHT Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            window.asposeCellsReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!window.asposeCellsReady) {
                resultDiv.innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a workbook and open the uploaded XLSX file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify the HTML Saving Options
            const sv = new HtmlSaveOptions(SaveFormat.MHtml);

            // Save the MHT file (returns binary data)
            const outputData = workbook.save(SaveFormat.MHtml, sv);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `${file.name}.out.mht`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">MHT file generated successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Conversion de Classeur Excel en HTML**
L’API Aspose.Cells offre un support pour l’exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) pour offrir la flexibilité de contrôler plusieurs aspects du HTML de sortie.

L'exemple de code ci-dessous montre comment enregistrer un classeur sous forme de fichier HTML.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

## **Configuration des Préférences d'Image pour le HTML**
Depuis la version 8.0.2, Aspose.Cells expose [**imageOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#imageOptions--) pour la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions), permettant aux développeurs de spécifier les préférences d’image lors de l’enregistrement de feuilles de calcul en HTML.

Ci-dessous sont détaillés certains des réglages d'image qui peuvent être appliqués,

- [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/): Spécifie le type d'image. Veuillez noter que toutes les formes, y compris les graphiques, sont rendues sous forme d'images dans le HTML de sortie.
- [**quality**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#quality--) : Spécifie la qualité de l'image entre 0 et 100, lorsque [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) est spécifié en tant que Jpeg.
- [**verticalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#verticalResolution--): Obtient ou définit la résolution verticale de l'image en points par pouce.
- [**horizontalResolution**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#horizontalResolution--): Obtient ou définit la résolution horizontale de l'image en points par pouce.
- [**TiffCompression**](https://reference.aspose.com/cells/javascript-cpp/tiffcompression/) : Obtient ou définit le type de compression pour les images lorsque [**ImageType**](https://reference.aspose.com/cells/javascript-cpp/imagetype/) est défini comme Tiff.
- [**transparent**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#transparent--): Indique si l'arrière-plan d'une image doit être transparent lorsque ImageFormat est spécifié comme Png.

## **Convertir un classeur Excel en Markdown**
L'API Aspose.Cells offre la prise en charge de l'exportation de feuilles de calcul au format Markdown. Pour exporter la feuille active en Markdown, passez [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/markdownsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul en Markdown.

L'exemple de code suivant montre comment exporter la feuille active en Markdown en utilisant le membre d'énumération [**SaveFormat.Markdown**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Veuillez voir le [fichier Markdown de sortie](md_sample.txt) généré par le code pour référence.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as Markdown</title>
    </head>
    <body>
        <h1>Save Excel as Markdown Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to Markdown</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving as Markdown
            const outputData = workbook.save(SaveFormat.Markdown);
            const blob = new Blob([outputData], { type: 'text/markdown' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.md';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Markdown File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the Markdown file.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en JSON**
Aspose.Cells supporte la conversion d'un classeur en fichier Json (JavaScript Object Notation).

L'exemple de code suivant montre comment exporter la feuille active en Json en utilisant le membre d'énumération [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Veuillez voir le code pour convertir le [fichier source](Book1.xlsx) en [fichier Json de sortie](Book1.Json) pour référence.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Convert the workbook to JSON format
            const outputData = workbook.save(SaveFormat.Json);

            // Create a downloadable blob for the JSON result
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Convertir Excel en XML**
Aspose.Cells prend en charge la conversion d'un classeur en XML de feuille de calcul Excel 2003 et en données XML brutes.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Workbook to XML Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Spreadsheet XML</a>
        <a id="downloadLink2" style="display: none;">Download Data XML</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, XmlSaveOptions } = AsposeCells;

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

            // Save as Excel 2003 Spreadsheet XML
            const spreadsheetData = workbook.save(SaveFormat.Excel2003Xml);
            const blob1 = new Blob([spreadsheetData]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Spreadsheet.xml';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Spreadsheet XML';

            // Save as plain XML data with XmlSaveOptions
            const xmlSaveOptions = new XmlSaveOptions();
            const dataXml = workbook.save(SaveFormat.SpreadsheetML, xmlSaveOptions);
            const blob2 = new Blob([dataXml]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'data.xml';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Data XML';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Use the links above to download the generated XML files.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en TIFF**
Aspose.Cells prend en charge la conversion d'un classeur en fichier TIFF.

Le code ci-dessous montre comment convertir Excel en TIFF :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to TIFF</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to TIFF format
            const outputData = workbook.save(SaveFormat.Tiff);
            const blob = new Blob([outputData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to TIFF successfully! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en DOCX**
L'API Aspose.Cells prend en charge la conversion de feuilles de calcul en format DOCX. Pour exporter le classeur en DOCX, passez [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/docxsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en DOCX.

L'exemple de code suivant montre comment exporter la feuille active en DOCX en utilisant le membre d'énumération [**SaveFormat.Docx**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Veuillez voir le [fichier DOCX généré](Book1.docx) pour référence.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as DOCX (Markdown/Docx conversion per original code)
            const outputData = workbook.save(SaveFormat.Docx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.docx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Docx File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the DOCX file.</p>';
        });
    </script>
</html>
```

## **Convertir un classeur Excel en PPTX**
L'API Aspose.Cells prend en charge la conversion de feuilles de calcul en format PPTX. Pour exporter le classeur en PPTX, passez [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pptxsaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en PPTX.

L'exemple de code suivant montre comment exporter la feuille active en PPTX en utilisant le membre d'énumération [**SaveFormat.Pptx**](https://reference.aspose.com/cells/javascript-cpp/saveformat). Veuillez voir le [fichier PPTX généré](Book1.pptx) pour référence.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Save as PPTX Example</title>
    </head>
    <body>
        <h1>Save Excel as PPTX Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PPTX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as PPTX
            const outputData = workbook.save(SaveFormat.Pptx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/\.[^/.]+$/, "");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.pptx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted PPTX File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the PPTX file.</p>';
        });
    </script>
</html>
```

## **Convertir le classeur Excel en EPUB**
L'API Aspose.Cells offre la prise en charge de la conversion de feuilles de calcul en format EPUB. Pour exporter le classeur en EPUB, passez [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en Epub.

L'exemple de code suivant montre comment exporter la feuille active en EPUB en utilisant le membre d'énumération [**SaveFormat.Epub**](https://reference.aspose.com/cells/javascript-cpp/saveformat).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Converting To EPUB Files</title>
    </head>
    <body>
        <h1>Converting To EPUB Files</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EPUB</button>
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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in EPUB format
            const outputData = workbook.save(SaveFormat.Epub);

            const blob = new Blob([outputData], { type: 'application/epub+zip' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.epub';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EPUB File';

            result.innerHTML = '<p style="color: green;">File converted to EPUB successfully! Click the download link to get the EPUB file.</p>';
        });
    </script>
</html>
```

## **Convertir le classeur Excel en AZW3**
L'API Aspose.Cells supporte la conversion de feuilles de calcul en format AZW3. Pour exporter le classeur en AZW3, passez [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveoptions-). Vous pouvez également utiliser la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/ebooksaveoptions) pour spécifier des paramètres supplémentaires pour l'exportation en AZW3.

L'exemple de code suivant montre comment exporter la feuille active en AZW3 en utilisant le membre d'énumération [**SaveFormat.Azw3**](https://reference.aspose.com/cells/javascript-cpp/saveformat).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Convert to AZW3 Example</title>
    </head>
    <body>
        <h1>Convert Excel to AZW3 (EPUB) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to AZW3</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in AZW3 format
            const outputData = wb.save(SaveFormat.Azw3);
            const blob = new Blob([outputData]);

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToEPUBFiles_out.azw3';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download AZW3 File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the AZW3 file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Convertir la révision de XLSB en XLSM](/cells/fr/javascript-cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/fr/javascript-cpp/convert-excel-to-html/)
- [Image](/cells/fr/javascript-cpp/convert-excel-to-image/)
- [Json](/cells/fr/javascript-cpp/convert-workbook-to-json/)
- [Convertir un classeur Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice calc).](/cells/fr/javascript-cpp/convert-excel-to-ods/)
- [Pdf](/cells/fr/javascript-cpp/convert-excel-workbook-to-pdf/)
- [Convertir Excel en CSV, TSV et Txt](/cells/fr/javascript-cpp/convert-excel-to-csv-tsv-and-txt/)
- [Suivre la progression de la conversion des documents](/cells/fr/javascript-cpp/track-document-conversion-progress/)
- [Convertir CSV, TSV et TXT en Excel](/cells/fr/javascript-cpp/convert-csv-tsv-and-txt-to-excel/)
