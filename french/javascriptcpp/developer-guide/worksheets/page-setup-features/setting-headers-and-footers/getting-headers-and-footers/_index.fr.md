---
title: Obtenir des en têtes ou des pieds de page avec JavaScript via C++
linktitle: Obtenir les en têtes ou pieds de page
type: docs
weight: 30
url: /fr/javascript-cpp/get-headers-or-footers/
description: Cet article explique comment récupérer programmatiquement les en têtes et pieds de page des fichiers Excel ou OpenOffice en utilisant l API JavaScript via C++.
---

{{% alert color="primary" %}}

Les en-têtes et pieds de page ne s'affichent qu'en mode Mise en page, Aperçu avant impression et sur les pages imprimées. 

Vous pouvez également utiliser la boîte de dialogue Mise en page si vous souhaitez afficher les en-têtes ou pieds de page pour plus d'une feuille de calcul à la fois. 

Pour d'autres types de feuilles, tels que les feuilles de graphique ou les graphiques, vous pouvez insérer des en-têtes et pieds de page uniquement en utilisant la boîte de dialogue Mise en page.

{{% /alert %}}

## **Obtenir des en-têtes et des pieds de page dans MS Excel**
1. Cliquez sur la feuille de calcul où vous souhaitez afficher ou modifier les en-têtes ou les pieds de page.
2. Dans l’onglet Affichage, dans le groupe Vues du classeur, cliquez sur Mise en page.
   Excel affiche la feuille de calcul en mode Mise en page.
3. Pour afficher ou modifier un en-tête ou un pied de page, cliquez sur la zone de texte de l'en-tête ou du pied de page de gauche, du centre ou de droite en haut ou en bas de la page de la feuille de calcul (sous En-tête ou au-dessus de Pied de page).


## **Obtenir des en-têtes et pieds de page en utilisant Aspose.Cells for JavaScript via C++**
Avec les méthodes [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) et [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-), les développeurs JavaScript peuvent simplement obtenir les en-têtes ou pieds de page du fichier.

1. Construisez un classeur pour ouvrir le fichier.
2. Obtenez la feuille de calcul où vous souhaitez obtenir les en-têtes ou pied de page.
3. Obtenez l’en-tête ou le pied de page avec un ID de section spécifique.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **Analyser les en-têtes et les pieds de page en liste de commandes**
Le texte dans l'en-tête ou le pied de page peut contenir des commandes spéciales, par exemple un espace réservé pour le numéro de page, la date actuelle ou les attributs de mise en forme du texte.

Les commandes spéciales sont représentées par une seule lettre précédée d'un esperluette ("&").

Les chaînes d'en-tête et de pied de page sont construites en utilisant la grammaire ABNF. Il n'est pas facile de comprendre sans un visualiseur.

Aspose.Cells for JavaScript via C++ fournit la méthode [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) pour analyser les en-têtes et pieds de page en tant que liste de commandes.

Les codes suivants montrent comment analyser l'en-tête ou le pied de page en tant que liste de commandes et traiter les commandes :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
