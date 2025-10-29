---
title: Comment imprimer Excel en pages ajustées en largeur et en hauteur avec JavaScript via C++
linktitle: Comment imprimer Excel en pages adaptées en largeur et en hauteur
type: docs
weight: 200
url: /fr/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Cet article vous montre du code expliquant comment définir FitToPagesWide et FitToPagesTall en utilisant Aspose.Cells for JavaScript via C++.
keywords: JavaScript via C++ Comment définir FitToPagesWide et FitToPagesTall, Comment ajouter FitToPagesWide et FitToPagesTall en JavaScript, Comment définir FitToPagesWide et FitToPagesTall dans Excel, Comment effacer FitToPagesWide et FitToPagesTall dans Excel, Comment imprimer Excel en pages ajustées en largeur et en hauteur, Comment imprimer la feuille en une seule page, Comment imprimer toutes les colonnes de la feuille en une seule page.
---

## **Introduction**

Les réglages FitToPagesWide et FitToPagesTall sont utilisés dans les applications de tableur (comme Microsoft Excel) pour contrôler la mise à l'échelle d'une feuille lors de l'impression. Ces réglages aident à s'assurer que votre sortie imprimée rentre dans un nombre spécifié de pages, horizontalement et verticalement. Voici une explication de chaque réglage :

1. FitToPagesWide : Ce réglage spécifie le nombre de pages en largeur dans lesquelles le contenu imprimé doit tenir. Par exemple, définir FitToPagesWide à 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule largeur de page, peu importe la largeur de la feuille.
2. FitToPagesTall : Ce paramètre indique le nombre de pages en hauteur dans lesquelles le résultat imprimé doit s'adapter. Par exemple, définir FitToPagesTall sur 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule hauteur de page, indépendamment du nombre de lignes.

## **Pourquoi utiliser FitToPagesWide et FitToPagesTall**
Voici quelques raisons de définir FitToPagesWide et FitToPagesTall :
1. Contrôle de la mise en page imprimée : En spécifiant le nombre de pages en largeur et en hauteur, vous pouvez vous assurer que votre document imprimé est facile à lire et bien organisé, sans que des colonnes ou lignes soient mal réparties sur plusieurs pages.
2. Cohérence : Si vous imprimez plusieurs feuilles ou rapports, l'utilisation de ces paramètres permet de maintenir un format cohérent, facilitant la comparaison et l'analyse des documents imprimés.
3. Présentation professionnelle : La mise à l'échelle appropriée et la taille du contenu pour un nombre spécifique de pages peuvent donner une présentation plus professionnelle et soignée de vos données.

## **Comment imprimer un fichier en pages adaptées en largeur et en hauteur dans Excel**

Pour définir les paramètres FitToPagesWide et FitToPagesTall dans Microsoft Excel, suivez ces étapes :

1. Ouvrez votre classeur Excel et allez à la feuille que vous souhaitez imprimer.
2. Accédez à l'onglet Mise en page dans le ruban.
3. Dans le groupe Mise en page, cliquez sur la petite flèche en bas à droite pour ouvrir la boîte de dialogue Mise en page.
4. Dans la boîte de dialogue Mise en page, allez à l'onglet Page.
5. Sous Échelle, sélectionnez l'option "Ajuster à" puis spécifiez le nombre de pages en largeur et en hauteur souhaité : Entrez le nombre de pages en largeur dans la première case (Ajuster à x pages en largeur). Entrez le nombre de pages en hauteur dans la deuxième case (Ajuster à y pages en hauteur).
<br>
<img src="2.png" width=60% />

6. Cliquez sur OK pour appliquer les paramètres.

## **Comment imprimer Excel en pages ajustées en largeur et en hauteur en utilisant Aspose.Cells for JavaScript via C++**

Pour définir FitToPagesWide et FitToPagesTall dans une feuille de calcul spécifique : Tout d'abord, chargez le [fichier exemple](input.xlsx), puis vous devez modifier les propriétés [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) et [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) de l'objet [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) pour la feuille souhaitée. Voici un exemple en JavaScript :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Le résultat en sortie :
<br>
<img src="1.png" width=60% />

## **Comment imprimer une feuille de calcul en une seule page en utilisant Aspose.Cells for JavaScript via C++**

Pour imprimer la feuille de calcul en une seule page : Tout d'abord, chargez le [fichier exemple](sample.xlsx), puis vous devez définir la propriété [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Voici un exemple en JavaScript :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Le résultat en sortie :
<br>
<img src="3.png" width=60% />

## **Comment imprimer toutes les colonnes de la feuille de calcul sur une seule page en utilisant Aspose.Cells for JavaScript via C++**

Pour imprimer toutes les colonnes de la feuille de calcul sur une seule page : Tout d'abord, chargez le [fichier d'exemple](sample.xlsx), puis vous devez définir la propriété [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Voici un exemple en JavaScript :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Le résultat en sortie :
<br>
<img src="4.png" width=60% />
