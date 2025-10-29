---
title: Copier et déplacer des feuilles de calcul avec JavaScript via C++
linktitle: Copier et Déplacer des Feuilles de calcul
type: docs
weight: 10
url: /fr/javascript-cpp/copying-and-moving-worksheets/
description: Cet article inclut un exemple de code et décrit comment copier et déplacer des feuilles de calcul de manière programmatique, à la fois dans un classeur Excel et entre des classeurs Excel en utilisant l API JavaScript via C++.
keywords: copier feuille JavaScript, déplacer feuille JavaScript
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il y a un moyen de le faire : en créant une feuille, puis en la copiant.

 Le script Aspose.Cells for Java via C++ supporte la copie et le déplacement de feuilles de calcul dans ou entre des classeurs. Les feuilles de calcul, avec toutes leurs données, formats, tableaux, matrices, graphiques, images et autres objets, sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Déplacement ou Copie de feuilles à l'aide de Microsoft Excel**

Voici les étapes à suivre pour copier et déplacer des feuilles de calcul à l'intérieur ou entre des classeurs dans Microsoft Excel.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou copier la feuille**.
1. Dans la boîte de dialogue **Vers le classeur**, cliquez sur le classeur qui recevra les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées vers un nouveau classeur, cliquez sur **Nouveau Classeur**.
1. Dans la zone **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.

### ** Copier des feuilles dans un classeur avec le script Aspose.Cells for Java via C++**

Aspose.Cells fournit une méthode surchargée, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#addCopy-number-), qui est utilisée pour ajouter une feuille de calcul à la collection et copier les données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille source comme paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille existante dans un classeur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Sheet Within Workbook</title>
    </head>
    <body>
        <h1>Copy Sheet Within Workbook Example</h1>
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

            // Open an existing Excel file.
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = wb.worksheets;

            // Copy data to a new sheet from an existing sheet within the Workbook.
            sheets.addCopy("Sheet1");

            // Save the Excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWithinWorkbook_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Sheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Copier des feuilles de calcul entre des classeurs**

Aspose.Cells fournit une méthode, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-), utilisée pour copier les données et la mise en forme d'une feuille source vers une autre feuille dans ou entre des classeurs. La méthode prend l'objet feuille source comme paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur à un autre.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheets Between Workbooks</title>
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
        <p>Select the source Excel file (book1.xls) to copy its first worksheet into a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (book1.xls).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook from the uploaded file (source workbook)
            const excelWorkbook0 = new Workbook(new Uint8Array(arrayBuffer));

            // Create another Workbook (destination workbook)
            const excelWorkbook1 = new Workbook();

            // Copy the first sheet of the first book into second book.
            excelWorkbook1.worksheets.get(0).copy(excelWorkbook0.worksheets.get(0));

            // Save the file as Excel 97-2003 (.xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Copied Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Between Workbooks Example</h1>
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
            // Create a new Workbook.
            const excelWorkbook0 = new Workbook();

            // Get the first worksheet in the book.
            const ws0 = excelWorkbook0.worksheets.get(0);

            // Put some data into header rows (A1:A4)
            for (let i = 0; i < 5; i++) {
                ws0.cells.get(i, 0).value = `Header Row ${i}`;
            }

            // Put some detail data (A5:A999)
            for (let i = 5; i < 1000; i++) {
                ws0.cells.get(i, 0).value = `Detail Row ${i}`;
            }

            // Define a pagesetup object based on the first worksheet.
            const pagesetup = ws0.pageSetup;

            // The first five rows are repeated in each page...
            // It can be seen in print preview.
            pagesetup.printTitleRows = "$1:$5";

            // Create another Workbook.
            const excelWorkbook1 = new Workbook();

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Name the worksheet.
            ws1.name = "MySheet";

            // Copy data from the first worksheet of the first workbook into the
            // first worksheet of the second workbook.
            ws1.copy(ws0);

            // Saving the modified Excel file
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetFromWorkbookToOther_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and worksheet copied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Déplacer des feuilles de calcul dans un classeur**

Aspose.Cells fournit une méthode [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#moveto-number-) qui permet de déplacer une feuille vers un autre emplacement dans la même feuille de calcul. La méthode prend l'indice de la feuille cible comme paramètre.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = wb.worksheets;

            // Get the first worksheet
            const worksheet = sheets.get(0);

            // Move the first sheet to the third position (index 2)
            worksheet.moveTo(2);

            // Save the modified workbook in Excel97-2003 format
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MoveWorksheet_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
