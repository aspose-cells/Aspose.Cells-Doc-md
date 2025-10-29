---
title: Conversion entre le nom de cellule et l index de ligne/colonne
linktitle: Conversion entre le nom de cellule et l index
type: docs
weight: 10
url: /fr/javascript-cpp/names-and-indices/
description: Apprenez à obtenir la conversion entre le nom de la cellule et l indice de ligne/colonne via l API Aspose.Cells for JavaScript en C++.
keywords: JavaScript via C++ Obtenir le nom de la cellule à partir des indices de ligne et de colonne, Obtenir les indices de ligne et de colonne à partir du nom de la cellule, Créer des noms de feuille de calcul sécurisés, Ajouter des noms de feuille de calcul sécurisés
---

## **Obtenir le nom de cellule à partir des indices de ligne et de colonne**
Il est possible de trouver le nom d'une cellule en donnant l'index de ligne et de colonne. Cet article explique comment faire.
Aspose.Cells for JavaScript via C++ fournit la méthode CellsHelper.cellIndexToName qui permet aux développeurs d'obtenir le nom d'une cellule si ils fournissent l'indice de ligne et de colonne.

{{% alert color="primary" %}} 

Microsoft Excel commence à compter les indices de ligne et de colonne à partir de 1. Contrairement à Microsoft Excel, Aspose.Cells for JavaScript via C++ commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

Le code exemple ci-dessous illustre comment utiliser CellsHelper.cellIndexToName pour accéder au nom de la cellule étant donné un index de ligne et de colonne connus. Le code génère la sortie suivante.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            // Original logic converted to browser JavaScript
            var row = 3;
            var column = 5;
            var name = AsposeCells.CellsHelper.cellIndexToName(row, column);
            console.log("Cell name: " + name);
            document.getElementById('result').innerHTML = '<p>Cell name: ' + name + '</p>';
        });
    </script>
</html>
```
## **Obtenir les indices de ligne et de colonne à partir du nom de la cellule**
Il est possible de trouver un indice de ligne et de colonne de la cellule à partir de son nom. Cet article explique comment.
Aspose.Cells for JavaScript via C++ fournit la méthode CellsHelper.cellNameToIndex qui permet aux développeurs d'obtenir un indice de ligne et de colonne à partir du nom de la cellule.

{{% alert color="primary" %}} 

Microsoft Excel commence à compter les indices de ligne et de colonne à partir de 1. Contrairement à Microsoft Excel, Aspose.Cells for JavaScript via C++ commence à compter les indices de ligne et de colonne à partir de 0.

{{% /alert %}} 

Le code d'exemple suivant illustre comment utiliser CellsHelper.cellNameToIndex pour obtenir l'indice de ligne et de colonne à partir du nom de la cellule. Le code génère la sortie suivante.



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Row and Column from Cell Name</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <div>
            <label for="cellName">Cell Name:</label>
            <input type="text" id="cellName" value="C4" />
        </div>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

        let asposeInitialized = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            asposeInitialized = true;
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const name = document.getElementById('cellName').value || "C4";

            const rowCol = CellsHelper.cellNameToIndex(name);
            const currRow = rowCol[0];
            const currCol = rowCol[1];
            console.log("Row: " + currRow + " , Column: " + currCol);

            document.getElementById('result').innerHTML = `<p>Row: ${currRow} , Column: ${currCol}</p>`;
        });
    </script>
</html>
```

## **Créer des noms de feuille sécurisés**
Il arrive parfois qu'il soit nécessaire d'assigner le nom de la feuille en temps d'exécution. Dans ce scénario, il peut y avoir des noms de feuilles qui contiennent des caractères supplémentaires comme <>+(?”. Il est nécessaire de remplacer tout caractère non autorisé comme nom de feuille par un caractère prédéfini fourni par l'utilisateur. De même, la longueur peut dépasser 31 caractères et doit être tronquée. Apache POI fournit certaines fonctionnalités pour créer des noms sécurisés, c'est pourquoi une fonction similaire est fournie par Aspose.Cells for JavaScript via C++ pour gérer toutes ces problématiques. Le code d'exemple suivant démontre cette fonctionnalité :



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Safe Sheet Name</title>
    </head>
    <body>
        <h1>Create Safe Sheet Name Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Long name will be truncated to 31 characters
            var name1 = AsposeCells.CellsHelper.createSafeSheetName("this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

            // Any invalid character will be replaced with _
            var name2 = AsposeCells.CellsHelper.createSafeSheetName(' <> + (adj.Private ? " Private" : ")', '_');

            // Display results in the page
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p><strong>Safe Name 1:</strong> ' + name1 + '</p>' +
                                  '<p><strong>Safe Name 2:</strong> ' + name2 + '</p>';
        });
    </script>
</html>
```

Sortie :

c'est le premier nom qui est créé

`  ` <> + (adj. Privé _ "Privé"
