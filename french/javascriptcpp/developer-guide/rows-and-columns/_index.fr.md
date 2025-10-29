---
title: Mettre en forme les lignes et les colonnes avec JavaScript via C++
linktitle: Lignes et colonnes
type: docs
weight: 100
url: /fr/javascript-cpp/adjusting-row-height-and-column-width/
description: Aspose.Cells for JavaScript via C++ peut supporter le changement de la hauteur des lignes ou de la largeur des colonnes, ainsi que l application de la mise en forme sur les lignes ou colonnes.
keywords: Définir la hauteur de ligne et la largeur de colonne, ajuster la hauteur de ligne et la largeur de colonne, changer la hauteur de ligne ou la largeur de colonne, formater les lignes et les colonnes, comment définir la hauteur de ligne et la largeur de colonne.
---

{{% alert color="primary" %}}
Lors de la manipulation de feuilles de calcul et de l'ajout de données dans des lignes ou colonnes, il peut être nécessaire de modifier la hauteur des lignes ou la largeur des colonnes. Parfois, appliquer un format sur des lignes ou colonnes implique que la hauteur ou la largeur actuelles doivent changer pour afficher les données. En général, les utilisateurs ajustent la hauteur des lignes et la largeur des colonnes dans un environnement WYSIWYG en utilisant Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations à l'exécution.
{{% /alert %}}

## **Travailler avec des lignes**

### **Comment ajuster la hauteur de ligne**

Aspose.Cells for JavaScript via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) qui représente toutes les cellules de la feuille.

La collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) offre plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille. Certaines de ces méthodes sont décrites ci-dessous plus en détail.

### **Comment définir la hauteur d'une ligne**

Il est possible de définir la hauteur d'une seule ligne en appelant la méthode [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). La méthode [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) prend les paramètres suivants :

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Row Height Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.rows.get(1).height = 13;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Comment définir la hauteur de toutes les lignes dans une feuille de calcul**

Si les développeurs ont besoin de définir la même hauteur de ligne pour toutes les lignes de la feuille, ils peuvent utiliser la propriété [**standardHeight()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardHeight--) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Standard Row Height</title>
    </head>
    <body>
        <h1>Set Standard Row Height Example</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the height of all rows in the worksheet to 15
            worksheet.cells.standardHeight = 15;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Standard row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Travailler avec les colonnes**

### **Comment définir la largeur d'une colonne**

Définissez la largeur d'une colonne en appelant la méthode [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). La méthode [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) prend les paramètres suivants :

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Column Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Column Width</button>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of the second column to 17.5
            worksheet.cells.columns.get(1).width = 17.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Comment définir la largeur de colonne en pixels**

Définissez la largeur d'une colonne en appelant la méthode [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). La méthode [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) prend les paramètres suivants :

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée en pixels.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Column Width In Pixels</title>
    </head>
    <body>
        <h1>Set Column Width In Pixels</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the width of the column in pixels
            // Converted from: worksheet.getCells().setColumnWidthPixel(7, 200);
            // UNIVERSAL GETTER/SETTER CONVERSION applied:
            worksheet.cells.columnWidthPixel = [7, 200];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetColumnWidthInPixels_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Comment définir la largeur de toutes les colonnes dans une feuille de calcul**

Pour définir la même largeur de colonne pour toutes les colonnes dans la feuille de calcul, utilisez la propriété [**standardWidth()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardWidth--) de la collection [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Standard Width Example</title>
    </head>
    <body>
        <h1>Set Standard Width Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of all columns in the worksheet to 20.5
            worksheet.cells.standardWidth = 20.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Standard width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Ajuster automatiquement les lignes et les colonnes](/cells/fr/javascript-cpp/autofit-rows-and-columns/)
- [Convertir du texte en colonnes à l'aide de Aspose.Cells](/cells/fr/javascript-cpp/convert-text-to-columns-using-aspose-cells/)
- [Copier des lignes et des colonnes](/cells/fr/javascript-cpp/copying-rows-and-columns/)
- [Supprimer les lignes et les colonnes vides dans une feuille de calcul](/cells/fr/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/)
- [Regrouper et dégrouper les lignes et les colonnes](/cells/fr/javascript-cpp/grouping-and-ungrouping-rows-and-columns/)
- [Masquer et afficher des lignes et des colonnes](/cells/fr/javascript-cpp/hiding-and-showing-rows-and-columns/)
- [Insérer ou supprimer des lignes dans une feuille de calcul Excel](/cells/fr/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/)
- [Insérer et supprimer des lignes et des colonnes d'un fichier Excel](/cells/fr/javascript-cpp/inserting-and-deleting-rows-and-columns/)
- [Supprimer les lignes en double dans une feuille de calcul](/cells/fr/javascript-cpp/remove-duplicate-rows-in-a-worksheet/)
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul](/cells/fr/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
