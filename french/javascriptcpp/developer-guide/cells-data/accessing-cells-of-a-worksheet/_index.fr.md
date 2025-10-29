---
title: Accès aux cellules d une feuille de calcul
type: docs
weight: 10
url: /fr/javascript-cpp/accessing-cells-of-a-worksheet/
description: Cet article montre comment obtenir la plage de visualisation maximale de la feuille de calcul et accéder aux cellules via l API Aspose.Cells for JavaScript via C++.
keywords: Obtenir un objet de cellule, Accéder aux cellules, Obtenir la plage d affichage maximale de la feuille de calcul. 
---

{{% alert color="primary" %}}

Nous savons que toutes les feuilles de calcul peuvent contenir des données qui sont essentiellement stockées dans les cellules (à partir desquelles une feuille de calcul est composée). Une cellule est une partie fondamentale d'une feuille de calcul utilisée pour construire l'ensemble de la feuille en une séquence de lignes et de colonnes. Avant d'essayer d'accéder aux données d'une feuille, nous devons accéder à ses cellules. Donc, dans ce sujet, nous discuterons de quelques approches de base pour accéder aux cellules de la feuille à l'exécution en utilisant Aspose.Cells for JavaScript via C++.

{{% /alert %}}

## **Comment accéder aux cellules**

Aspose.Cells for JavaScript via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) qui représente toutes les cellules de la feuille.

Nous pouvons utiliser la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) pour accéder aux cellules d'une feuille. Aspose.Cells for JavaScript via C++ propose trois approches de base pour accéder aux cellules d'une feuille :

1. Utiliser le nom de la cellule.
2. Utiliser l'index de la ligne et de la colonne de la cellule.
1. En utilisant un indice de cellule dans la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)

 Nous avons mentionné que la 3ème approche est la plus rapide et que la 1ère approche est la plus lente. La différence de performances entre les approches est très faible, alors ne vous inquiétez pas de la dégradation des performances, quelle que soit l'approche que vous utilisez.

### **Comment obtenir l'objet de cellule par le nom de la cellule**

Les développeurs peuvent accéder à une cellule spécifique en passant son nom de cellule à la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) comme index.

Si vous créez une feuille vide au départ, le nombre de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) est zéro. Lors de l'utilisation de cette approche pour accéder à une cellule, il vérifiera si cette cellule existe dans la collection ou non. Si oui, elle renvoie l'objet cellule dans la collection sinon, elle crée un nouvel objet [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell), l'ajoute à la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) puis retourne l'objet. Cette approche est la plus simple pour accéder à la cellule si vous êtes familier avec Microsoft Excel, mais c'est la plus lente comparée aux autres approches.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Comment obtenir l'objet de cellule par l'index de la ligne et de la colonne de la cellule**

Les développeurs peuvent accéder à une cellule spécifique en passant ses indices de ligne et de colonne à la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Cette approche fonctionne de la même manière que la première approche.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **Comment obtenir l'objet de cellule par l'index de la cellule dans la collection de cellules**

Une cellule peut également être accessible en passant son index numérique à la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

Si vous utilisez cette approche pour accéder aux cellules, une exception peut être levée si l'index numérique de la cellule est hors de portée. Cette approche est la plus rapide pour accéder aux cellules, mais il faut savoir qu'en utilisant cette méthode pour accéder à un objet cellule, l'index numérique peut changer après l'ajout de nouvelles cellules à la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Les objets cellules dans la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) sont triés en interne par indices de ligne et de colonne.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **Comment obtenir la plage d'affichage maximale de la feuille de calcul**

Aspose.Cells for JavaScript via C++ permet aux développeurs d’accéder à la plage d’affichage maximale d’une feuille. La plage d’affichage maximale — la plage de cellules entre la première et la dernière cellule contenant du contenu — est utile lorsque vous devez copier, sélectionner ou afficher l’intégralité du contenu d’une feuille dans une image.

Vous pouvez accéder à la plage d’affichage maximale d’une feuille à l’aide de [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). Le code d’exemple ci-dessous illustre comment accéder à la propriété [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--).

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
