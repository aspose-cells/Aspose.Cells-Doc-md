---
title: Gérez les feuilles de calcul des fichiers Microsoft Excel avec JavaScript via C++
linktitle: Feuilles de calcul
type: docs
weight: 90
url: /fr/javascript-cpp/manage-worksheets/
description: Ajoutez, supprimez et activez des feuilles de calcul en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans les fichiers Microsoft Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Ce sujet décrit les approches pour ajouter et supprimer des feuilles de calcul dans les fichiers Microsoft Excel.
{{% /alert %}}

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles.

## **Ajout de feuilles de calcul à un nouveau fichier Excel**

Pour créer un nouveau fichier Excel de manière programmatique:

1. Créez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).  
2. Appelez la méthode [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#add-sheettype-) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). Une feuille de calcul vide est ajoutée automatiquement au fichier Excel. Elle peut être référencée en passant l'indice de la feuille de calcul dans la collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--).  
3. Obtenir une référence à une feuille de calcul.  
4. Effectuez des opérations sur les feuilles de calcul.  
5. Enregistrez le nouveau fichier Excel avec de nouvelles feuilles de calcul en appelant la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Worksheet Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Get current worksheet count (converted from getWorksheets().getCount())
            const i = workbook.worksheets.count;

            // Add a new worksheet (converted from getWorksheets().add())
            workbook.worksheets.add();

            // Obtain the newly added worksheet by index (converted from getWorksheets().get(i))
            const worksheet = workbook.worksheets.get(i);

            // Set the name of the newly added worksheet (converted from setName)
            worksheet.name = "My Worksheet";

            // Save the workbook to XLS format and prepare download
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Ajout de feuilles de calcul à une feuille de calcul Designer**

Le processus d'ajout de feuilles dans un classeur de conception est le même que celui d'ajouter une nouvelle feuille, sauf que le fichier Excel existe déjà et doit être ouvert avant d'ajouter des feuilles. Un fichier de conception peut être ouvert par la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Worksheet</title>
    </head>
    <body>
        <h1>Add Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Setting the name of the newly added worksheet
            worksheet.name = "My Worksheet";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Accéder aux feuilles de calcul en utilisant le nom de la feuille**

Accédez à n'importe quelle feuille de calcul en spécifiant son nom ou son index.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example: Read Cell Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing a worksheet using its sheet name
            const worksheet = workbook.worksheets.get("Sheet1");
            const cell = worksheet.cells.get("A1");

            console.log(cell.value);
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.value}</p>`;
        });
    </script>
</html>
```

## **Suppression des feuilles de calcul en utilisant le nom de la feuille**

Pour supprimer des feuilles d'un fichier, appelez la méthode [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection). Passez le nom de la feuille à la méthode [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) pour supprimer une feuille spécifique.

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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet name
            workbook.worksheets.removeAt("Sheet1");

            // Save workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**

Supprimer des feuilles par nom fonctionne bien lorsque le nom de la feuille est connu. Si vous ne connaissez pas le nom de la feuille, utilisez une version surchargée de la méthode [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#removeAt-string-) qui prend l’indice de la feuille de calcul plutôt que son nom.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Remove First Worksheet</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Removing a worksheet using its sheet index
            workbook.worksheets.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Activation des feuilles et mise en place d'une cellule active dans la feuille de calcul**

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsque l'utilisateur ouvre un fichier Microsoft Excel dans Excel. De même, vous pourriez vouloir activer une cellule spécifique et régler les barres de défilement pour montrer cette cellule active. Aspose.Cells est capable d'effectuer toutes ces tâches.

Une **feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.

Une **cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.

### **Activation des feuilles et mise en avant d'une cellule**

Aspose.Cells fournit des appels API spécifiques pour activer une feuille et une cellule. Par exemple, la propriété [**WorksheetCollection.activeSheetIndex**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#activeSheetIndex--) est utile pour définir la feuille active dans un classeur. De même, la propriété [**Worksheet.activeCell**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#activeCell--) est utilisée pour définir et obtenir une cellule active dans la feuille de calcul.

Pour vous assurer que les barres de défilement horizontales ou verticales soient à la position d'index de ligne et de colonne que vous souhaitez pour afficher des données spécifiques, utilisez les propriétés [**Worksheet.firstVisibleRow**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleRow--) et [**Worksheet.firstVisibleColumn**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#firstVisibleColumn--).

L'exemple suivant montre comment activer une feuille de calcul et mettre en avant une cellule active. Dans la sortie générée, les barres de défilement seront scrollées pour que la 2ème ligne et la 2ème colonne soient leur première ligne et colonne visibles.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Add a worksheet if collection is empty
            const worksheets = workbook.worksheets;
            if (worksheets.count === 0) {
                worksheets.add();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = worksheets.get(0);

            // Get the cells in the worksheet.
            const cells = worksheet1.cells;

            // Input data into B2 cell.
            const cell = cells.get(1, 1);
            cell.value = "Hello World!";

            // Set the first sheet as an active sheet.
            worksheets.activeSheetIndex = 0;

            // Set B2 cell as an active cell in the worksheet.
            worksheet1.activeCell = "B2";

            // Set the B column as the first visible column in the worksheet.
            worksheet1.firstVisibleColumn = 1;

            // Set the 2nd row as the first visible row in the worksheet.
            worksheet1.firstVisibleRow = 1;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Copier et Déplacer des Feuilles de calcul](/cells/fr/javascript-cpp/copying-and-moving-worksheets/)  
- [Compter le nombre de cellules dans la feuille de calcul](/cells/fr/javascript-cpp/count-number-of-cells-in-the-worksheet/)  
- [Détection des Feuilles de calcul vides](/cells/fr/javascript-cpp/detecting-empty-worksheets/)  
- [Trouver si la Feuille de calcul est une Feuille de dialogue](/cells/fr/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Obtenir l'identifiant unique de la feuille de calcul](/cells/fr/javascript-cpp/get-worksheet-unique-id/)  
- [Créer, Manipuler ou Supprimer des Scénarios des Feuilles de calcul](/cells/fr/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Gestion des Sauts de Page](/cells/fr/javascript-cpp/managing-page-breaks/)  
- [Fonctionnalités de Configuration de Page](/cells/fr/javascript-cpp/page-setup-features/)  
- [Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells](/cells/fr/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Vues de Feuille de calcul](/cells/fr/javascript-cpp/worksheet-views/)
