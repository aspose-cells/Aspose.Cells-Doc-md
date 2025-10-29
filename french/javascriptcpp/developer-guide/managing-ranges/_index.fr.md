---
title: Gestion des plages avec JavaScript via C++
linktitle: Plages
type: docs
weight: 105
url: /fr/javascript-cpp/managing-ranges/
description: Apprenez à gérer les plages dans Excel en utilisant Aspose.Cells for JavaScript via C++. Créez des plages, définissez des valeurs, styles et effectuez diverses opérations.
---

## **Introduction**

 Dans Excel, vous pouvez sélectionner plusieurs cellules avec une sélection par boîte de souris ; l’ensemble des cellules sélectionnées est appelé "Plage".

Par exemple, vous pouvez cliquer sur le bouton gauche de la souris dans la cellule « A1 » d'Excel, puis faire glisser jusqu'à la cellule « C4 ». La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu'objet en utilisant Aspose.Cells for JavaScript via C++.

 Voici comment créer une plage, mettre une valeur, définir un style et effectuer d’autres opérations sur l’objet "Plage".

## **Gestion des plages avec Aspose.Cells for JavaScript via C++**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1:C4, vous pouvez utiliser le code suivant :

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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells (converted from getWorksheets().get(0).getCells() to properties)
            const cells = workbook.worksheets.get(0).cells;

            // Create Range A1:C4
            const range = cells.createRange("A1:C4");

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Range A1:C4 created successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Placer une valeur dans les cellules de la plage**

Imaginons que vous avez une plage de cellules qui s'étend sur A1:C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées de manière séquentielle : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Range Value Example</title>
    </head>
    <body>
        <h1>Range Value Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            const range = cells.createRange("A1:C4");

            range.get(0, 0).value = "A1";
            range.get(0, 1).value = "B1";
            range.get(0, 2).value = "C1";
            range.get(3, 0).value = "A4";
            range.get(3, 1).value = "B4";
            range.get(3, 2).value = "C4";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeValueTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **Définir le style des cellules de la plage**

 L’exemple suivant montre comment définir le style des cellules de la plage.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Style Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Gets Cells
            const cells = workbook.worksheets.get(0).cells;
            // Creates Range
            const range = cells.createRange("A1:C4");
            // Puts value
            range.get(0, 0).value = "A1";
            range.get(3, 2).value = "C4";
            // Sets Style
            let style00 = workbook.createStyle();
            style00.pattern = AsposeCells.BackgroundType.Solid;
            style00.foregroundColor = new AsposeCells.Color(255, 0, 0); // Red
            range.get(0, 0).style = style00;
            let style32 = workbook.createStyle();
            style32.pattern = AsposeCells.BackgroundType.HorizontalStripe;
            style32.foregroundColor = new AsposeCells.Color(0, 255, 0); // Green
            range.get(3, 2).style = style32;
            // Saves the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeStyleTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Obtenir la région actuelle de la plage**

CurrentRegion est une propriété qui renvoie un objet Range qui représente la région actuelle. 

La région actuelle est une plage délimitée par une combinaison de lignes vierges et de colonnes vierges. En lecture seule.

 En Excel, vous pouvez obtenir la zone CurrentRegion en :
 1. Sélectionnez une zone (range1) avec la boîte de souris.
 2. Cliquez sur "Accueil - Edition - Rechercher & Sélectionner - Aller à spécial - Région actuelle", ou utilisez "Ctrl+Shift+*", vous verrez Excel vous aider à sélectionner automatiquement une zone (range2). Une fois fait, range2 est la CurrentRegion de range1.

 Veuillez télécharger le fichier de test suivant, l’ouvrir dans Excel, utiliser la boîte de souris pour sélectionner une zone "A1:D7", puis cliquez sur "Ctrl+Shift+*", vous verrez la zone "A1:C3" sélectionnée.

[current_region.xlsx](current_region.xlsx)

 Essayez maintenant l'exemple suivant pour voir comment cela fonctionne avec Aspose.Cells :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Current Region Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Cells
            const cells = worksheet.cells;

            // Create Range
            const src = cells.createRange("A1:D7");

            // Get CurrentRegion (converted from getCurrentRegion())
            const A1C3 = src.currentRegion;

            // Save the workbook (no modifications were required by original code)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.current_region.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Current region obtained successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```


## **Sujets avancés**
- [Plage AutoFill du fichier Excel](/cells/fr/javascript-cpp/autofill-ranges/)
- [Copier des plages de cellules d'Excel](/cells/fr/javascript-cpp/copy-ranges-of-Excel/)
- [Copier uniquement les données de la plage](/cells/fr/javascript-cpp/copy-range-data-only/)
- [Copier les données de la plage avec le style](/cells/fr/javascript-cpp/copy-range-data-with-style/)
- [Copier uniquement le style de la plage](/cells/fr/javascript-cpp/copy-range-style-only/)
- [Créer l'union de la plage](/cells/fr/javascript-cpp/create-union-range/)
- [Couper et coller la plage](/cells/fr/javascript-cpp/cut-and-paste-cells/)
- [Supprimer les plages](/cells/fr/javascript-cpp/delete-ranges-from-Excel/)
- [Obtenir le nombre de cellules, le décalage de la plage entière de colonne et de ligne entière](/cells/fr/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insérer des plages](/cells/fr/javascript-cpp/insert-ranges-to-Excel/)
- [Fusionner ou séparer la plage de cellules](/cells/fr/javascript-cpp/merge-or-unmerge-range-of-cells/)
- [Déplacer une plage de cellules dans une feuille de calcul](/cells/fr/javascript-cpp/move-range-of-cells-in-a-worksheet/)
- [Créer des plages nommées en fonction du classeur et de la feuille de calcul](/cells/fr/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/javascript-cpp/search-and-replace-data-in-a-range/)
