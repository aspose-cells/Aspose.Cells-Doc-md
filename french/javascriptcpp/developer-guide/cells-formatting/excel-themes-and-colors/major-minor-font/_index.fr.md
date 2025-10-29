---
title: Police de thème pour les en têtes et le corps
linktitle: Police de thème pour les en têtes et le corps
description: Aspose.Cells est une bibliothèque JavaScript via C++ pour travailler avec des fichiers de feuille de calcul. Elle supporte la paramétrisation des polices de thème pour l’en tête et le corps dans les documents Excel, permettant aux utilisateurs de personnaliser l’apparence et le style du document. Cet article expliquera comment utiliser la bibliothèque Aspose.Cells pour travailler avec les polices de thème d’en tête et de corps dans les documents Excel.
keywords: Aspose.Cells, Document Excel, En tête, Corps, Police de Thème, Apparence, Style, JavaScript via C++
type: docs
weight: 120
url: /fr/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La police par défaut changera automatiquement lorsque le paramètre régionale est modifié.

Si la police par défaut est modifiée, la hauteur de la ligne et la largeur de la colonne seront également modifiées, et cela pourrait même perturber la mise en page.

Qu'est-ce qui a causé le changement de la police par défaut?

Si la police de thème Excel est définie, Excel basculera automatiquement entre différentes polices en fonction de l'environnement linguistique actuel.

{{% /alert %}}

## **Polices de thème pour les en-têtes et le corps dans Excel**

Dans Excel, sélectionnez l'onglet Accueil, cliquez sur le menu déroulant de la police, vous verrez « Polices de thème » avec deux polices de thème : Calibri Light (En-têtes) et Calibri (Corps) en haut avec le paramètre régional en anglais.

**![Polices de thème](Theme-Fonts.png)**

Si la police de thème est sélectionnée, le nom de la police s'affichera différemment selon les régions. Si vous ne souhaitez pas que la police change automatiquement en fonction des régions, ne sélectionnez pas les deux polices de thème.

## **Modifier la police des titres et du corps de manière programmée**
Avec Aspose.Cells for JavaScript via C++, nous pouvons vérifier si la police par défaut est une police de thème ou définir la police de thème avec la méthode [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-).

Le code exemple suivant montre comment manipuler la police de thème.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Récupération dynamique de la police de thème locale de manière programmatique**
Parfois, nos serveurs et les machines des utilisateurs ne sont pas dans la même région. Comment pouvons-nous obtenir la même police que les utilisateurs souhaitent pour le traitement de fichiers?

Nous devons définir les paramètres régionaux du système avant de charger le fichier avec la méthode [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-).

Le code d'exemple suivant montre comment obtenir la police de thème locale.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
