---
title: Convertir des données numériques sous forme de texte en nombre
type: docs
weight: 900
url: /fr/javascript-cpp/convert-text-numeric-data-to-number/
description: Apprenez à convertir les nombres stockés sous forme de texte dans Excel en nombres en utilisant l API Aspose.Cells for JavaScript via C++.
keywords: excel convertir le texte en nombre, code JavaScript pour convertir le texte en nombre dans Excel, convertir les données numériques sous forme de texte en nombre dans Excel, code JavaScript pour convertir le texte numérique en nombre, convertir le texte numérique en nombre dans Excel avec le code JavaScript, convertir la chaîne numérique en nombre dans Excel avec le code JavaScript, convertir le texte numérique en nombre avec le code JavaScript, convertir le texte numérique en nombre dans Excel avec le code JavaScript, convertir la chaîne numérique en nombre dans Excel avec le code JavaScript, convertir le texte numérique en nombre dans Excel avec le code JavaScript, convertir le texte numérique en nombre dans Excel avec le code JavaScript
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez convertir des données numériques saisies en tant que texte en nombres. Vous pouvez saisir des nombres en tant que texte dans Microsoft Excel en mettant un apostrophe avant le nombre, par exemple **'12345**. Excel traite alors le nombre comme une chaîne. Aspose.Cells for JavaScript via C++ vous permet de convertir des chaînes en nombres.


## Comment convertir des nombres stockés sous forme de texte en nombres dans Excel
Vous pouvez convertir les nombres stockés sous forme de texte en nombres en suivant quelques étapes simples.
1. Sélectionnez une cellule unique ou une plage de cellules comportant un indicateur d'erreur dans le coin supérieur gauche.
1. À côté de la cellule ou de la plage de cellules sélectionnée, cliquez sur le bouton d'erreur qui apparaît. Dans le menu, cliquez sur Convertir en nombre. 
<br>
<img src="4.png" width=70% />
1. Si le bouton d'alerte n'est pas disponible, sélectionnez une colonne présentant ce problème. Si vous ne voulez pas convertir toute la colonne, vous pouvez sélectionner une ou plusieurs cellules à la place. Assurez-vous simplement que les cellules que vous sélectionnez se trouvent dans la même colonne, sinon ce processus ne fonctionnera pas. Le bouton Texte en colonnes est généralement utilisé pour diviser une colonne, mais il peut également être utilisé pour convertir une seule colonne de texte en nombres. Sur l'onglet Données, cliquez sur Texte en colonnes.
<br>
<img src="1.png" width=70% />
1. Cliquez sur le bouton Terminer dans la boîte de dialogue.
<br>
<img src="2.png" width=70% />
1. Les nombres stockés sous forme de texte sont transformés en nombres.
<br>
<img src="3.png" width=70% />

## Comment convertir les nombres stockés sous forme de texte en nombres en utilisant Aspose.Cells for JavaScript via C++
Aspose.Cells for JavaScript via C++ fournit la méthode [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) qui peut être utilisée pour convertir toutes les données numériques sous forme de chaîne ou de texte en nombres.

La capture d'écran suivante montre des nombres sous forme de chaînes dans les cellules **A1:A17**. Les nombres sous forme de chaînes sont alignés à gauche.
<br>
<img src="5.png" width=70% />

Ces nombres sous forme de chaînes ont été convertis en nombres en utilisant [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/javascript-cpp/cells/#convertStringToNumericValue--) dans la capture d'écran suivante. Comme vous pouvez le voir, ils sont maintenant alignés à droite.
<br>
<img src="6.png" width=70% />

## Code JavaScript pour convertir des données numériques sous forme de chaîne en nombres réels

Le code d'exemple suivant illustre comment convertir toutes les données numériques en chaîne en nombres réels dans toutes les feuilles de calcul.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Strings to Numeric Values in All Sheets</h1>
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

            // Instantiate workbook object with the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;
            const sheetcount = sheets.count;

            // Iterate through all worksheets and convert strings to numeric values
            for (let i = 0; i < sheetcount; i++) {
                const sheet = sheets.get(i);
                sheet.cells.convertStringToNumericValue();
            }

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
