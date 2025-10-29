---
title: Copier des lignes et des colonnes avec JavaScript via C++
linktitle: Copier des lignes et des colonnes
type: docs
weight: 40
url: /fr/javascript-cpp/copying-rows-and-columns/
description: Cet article montre comment copier des lignes et des colonnes via Aspose.Cells for JavaScript utilisant l API C++.
keywords: JavaScript via C++, Comment copier des lignes et des colonnes, Copier des lignes en JavaScript, Copier des colonnes avec JavaScript, Comment coller des lignes et des colonnes en utilisant Aspose.Cells for JavaScript via C++, Coller plusieurs lignes et colonnes, Comment copier et coller une seule ligne ou colonne.
---

## **Introduction**  

Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier toute la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes à l'intérieur ou entre les classeurs.  
Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, la mise en forme, les cellules masquées, les images et autres objets graphiques sont également copiés.  

## **Comment copier des lignes et des colonnes avec Microsoft Excel**  

1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.  
1. Pour copier des lignes ou des colonnes, cliquez sur **Copier** dans la barre d'outils **Standard**, ou appuyez sur **CTRL**+**C**.  
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.  
1. Lorsque vous copiez des lignes ou des colonnes, cliquez sur **Cellules copiées** dans le menu **Insérer**.  

{{% alert color="primary" %}}  
Si vous cliquez sur **Coller** dans la barre d'outils **Standard** ou appuyez sur **CTRL**+**V** au lieu de cliquer sur une commande dans le menu **Insérer**, tout contenu des cellules de destination est remplacé.  
{{% /alert %}}  

## **Comment coller des lignes et des colonnes en utilisant les options de collage avec Microsoft Excel**  

1. Sélectionnez les cellules contenant les données ou autres attributs que vous souhaitez copier.  
1. Sur l'onglet Accueil, cliquez sur **Copier**.  
1. Cliquez sur la première cellule dans la zone où vous souhaitez **coller** ce que vous avez copié.  
1. Sur l'onglet Accueil, cliquez sur la flèche à côté de **Coller**, puis sélectionnez **Collage** spécial.  
1. Sélectionnez les **options** que vous souhaitez.  

## **Comment copier des lignes et des colonnes en utilisant Aspose.Cells for JavaScript via C++**  

## **Comment copier des lignes uniques**  

Aspose.Cells fournit la méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) de la classe [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Cette méthode copie tous types de données, y compris formules, valeurs, commentaires, formats de cellules, cellules cachées, images et autres objets de dessin de la ligne source vers la ligne de destination.  

La méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) prend les paramètres suivants :  

- l’objet [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) source,  
- l'indice de ligne source, et  
- l'indice de ligne de destination.  

Utilisez cette méthode pour copier une ligne au sein d’une feuille ou vers une autre feuille. La méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) fonctionne de manière similaire à Microsoft Excel. Par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.  

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un fichier Excel Microsoft de modèle et copie la deuxième ligne (avec ses données, son formatage, ses commentaires, ses images, etc.) et la colle à la 12e ligne de la même feuille.  

Vous pouvez sauter l’étape consistant à obtenir la hauteur de la ligne source en utilisant la méthode [**Cells.rowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-boolean-cellsunittype-) puis définir la hauteur de la ligne de destination avec la méthode [**Cells.rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-), car la méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRow-cells-number-number-) s’occupe automatiquement de la hauteur de la ligne.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Row</title>
    </head>
    <body>
        <h1>Copy Row Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook.
            const wsTemplate = workbook.worksheets.get(0);

            // Copy the second row (index 1) with data, formatting, images and drawing objects
            // To the 16th row (index 15) in the worksheet.
            wsTemplate.cells.copyRow(wsTemplate.cells, 1, 15);

            // Save the excel file in Excel97To2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
Lors de la copie de lignes, il est important de noter les images, les graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :  

1. Si l'indice de la ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'indice de début de la ligne est 4 et l'indice de fin de la ligne est 6).  
1. Les images existantes, les graphiques, etc. dans la ligne de destination ne seront pas supprimés.  
{{% /alert %}}  

## **Comment copier plusieurs lignes**  

Vous pouvez également copier plusieurs lignes vers une nouvelle destination en utilisant la méthode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) qui prend un paramètre supplémentaire de type entier pour préciser le nombre de lignes sources à copier.  

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

            // Instantiate workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the cells collection of first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Copy the first 3 rows to 7th row (indexes are zero-based)
            cells.copyRows(cells, 0, 6, 3);

            // Save the result and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Comment copier des colonnes**  

Aspose.Cells fournit la méthode [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) de la classe [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), cette méthode copie tous types de données, y compris les formules - avec références mises à jour - et les valeurs, commentaires, formats de cellules, cellules cachées, images et autres objets de dessin de la colonne source vers la colonne de destination.  

La méthode [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) prend les paramètres suivants :  

- l’objet [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) source,  
- indice de la colonne source, et  
- indice de la colonne de destination.  

Utilisez la méthode [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumn-cells-number-number-) pour copier une colonne au sein d’une feuille ou vers une autre feuille.  

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Column Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const excelWorkbook1 = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Copy the first column from the first worksheet into the third column of the same worksheet.
            const cells = ws1.cells;
            cells.copyColumn(cells, cells.columns.get(0).index, cells.columns.get(2).index);

            // Autofit the column.
            ws1.autoFitColumn(2);

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Comment copier plusieurs colonnes**  

Semblable à la méthode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-), les API Aspose.Cells proposent également la méthode [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) afin de copier plusieurs colonnes source vers un nouvel emplacement.  

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an instance of Workbook class by loading the existing spreadsheet
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Copy the first 3 columns to the 7th column
            cells.copyColumns(cells, 0, 6, 3);

            // Save the result and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Comment coller des lignes et des colonnes avec des options de collage**  

Aspose.Cells fournit maintenant [**PasteOptions**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/) tout en utilisant les fonctions [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-) et [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Il permet de définir une option de collage appropriée similaire à Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Change Chart Data Source</title>
    </head>
    <body>
        <h1>Change Chart Data Source Example</h1>
        <p>Select an Excel file (sampleChangeChartDataSource.xlsx) from your local machine.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteType, CopyOptions, PasteOptions } = AsposeCells;

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

            // Access the first sheet which contains chart
            const source = workbook.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = workbook.worksheets.add("DestSheet");

            // Set CopyOptions.ReferToDestinationSheet to true
            const options = new CopyOptions();
            options.referToDestinationSheet = true;

            // Set PasteOptions
            const pasteOptions = new PasteOptions();
            pasteOptions.pasteType = PasteType.Values;
            pasteOptions.onlyVisibleCells = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options, pasteOptions);

            // Save workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataSource.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
