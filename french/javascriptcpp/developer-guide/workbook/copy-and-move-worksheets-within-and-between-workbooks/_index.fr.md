---
title: Copier et déplacer des feuilles de calcul au sein et entre des classeurs avec JavaScript via C++
linktitle: Copier et Déplacer des Feuilles de Calcul Dans et Entre des Classeurs
type: docs
weight: 80
url: /fr/javascript-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Apprenez comment copier et déplacer des feuilles dans le même classeur ou entre plusieurs classeurs en utilisant Aspose.Cells for JavaScript via C++. Gérez efficacement la structure de vos classeurs.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme commune et une saisie de données. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il y a une façon de faire cela : en créant une feuille, puis en la copiant trois fois.

Aspose.Cells for JavaScript via C++ supporte la copie ou le déplacement de feuilles dans le même classeur ou entre classeurs. Les feuilles, y compris les données, le formatage, les tableaux, les matrices, les graphiques, les images et autres objets, sont copiées avec la plus grande précision.

{{% /alert %}}

## **Copier et Déplacer des Feuilles de calcul**

### **Copier une Feuille de Calcul à l'Intérieur d'un Classeur**

Les étapes initiales sont les mêmes pour tous les exemples.

1. Créez deux classeurs avec des données dans Microsoft Excel. Dans le cadre de cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi certaines données dans les feuilles de calcul.

- FirstWorkbook.xlsx (3 feuilles de calcul).
- SecondWorkbook.xlsx (1 feuille de calcul).

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for JavaScript via C++](https://downloads.aspose.com/cells/javascript-cpp).
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.
1. Créer un projet :
   1. Démarrez votre environnement de développement.
   1. Créez une nouvelle application console.
1. Ajouter des références:
   1. Ajoutez une référence à Aspose.Cells dans le projet.
      Par exemple, ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Copiez la feuille de calcul dans un classeur
   Le premier exemple copie la première feuille de calcul (Copie) dans FirstWorkbook.xlsx.

Lors de l'exécution du code, la feuille de calcul nommée Copie est copiée dans FirstWorkbook.xlsx avec le nom Dernière Feuille.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheet Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Example</h1>
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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Copy the first sheet of the first book within the workbook
            workbook.worksheets.get(2).copy(workbook.worksheets.get("Copy"));

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Déplacer une feuille de calcul dans un classeur**

Le code ci-dessous montre comment déplacer une feuille de calcul d'une position à une autre dans un classeur. En exécutant le code, la feuille de calcul appelée Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xlsx.

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Move the first sheet to index 1
            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            worksheet.moveTo(1);

            // Saving the modified Excel file and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookMoved_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Copier une feuille de calcul entre des classeurs**

L'exécution du code copie la feuille nommée Copy dans SecondWorkbook.xlsx avec le nom Sheet2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
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
            // Create two workbooks
            const excelWorkbook3 = new Workbook();
            const excelWorkbook4 = new Workbook();

            // Create source worksheet
            excelWorkbook3.worksheets.add("Copy");

            // Add new worksheet into second Workbook
            excelWorkbook4.worksheets.add();

            // Copy the first sheet of the first book into second book.
            excelWorkbook4.worksheets.get(1).copy(excelWorkbook3.worksheets.get("Copy"));

            // Save the file.
            const outputData = excelWorkbook4.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheets copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Déplacer une feuille de calcul entre des classeurs**

En exécutant le code, la feuille de calcul nommée Déplacer de FirstWorkbook.xlsx est déplacée vers SecondWorkbook.xlsx avec le nom Feuille3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download First Workbook</a>
        <a id="downloadLink2" style="display: none;">Download Second Workbook</a>
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
            // Create new workbooks instead of opening existing files
            const excelWorkbook5 = new Workbook();
            const excelWorkbook6 = new Workbook();

            // Add New Worksheet
            excelWorkbook6.worksheets.add();

            // Copy the sheet from first book into second book.
            excelWorkbook6.worksheets.get(0).copy(excelWorkbook5.worksheets.get(0));

            // Remove the copied worksheet from first workbook
            excelWorkbook5.worksheets.removeAt(0);

            // Save the first workbook
            const outputData1 = excelWorkbook5.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'FirstWorkbookWithMove_out.xlsx';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download FirstWorkbookWithMove_out.xlsx';

            // Save the second workbook
            const outputData2 = excelWorkbook6.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SecondWorkbookWithMove_out.xlsx';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download SecondWorkbookWithMove_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks processed successfully. Click the download links to retrieve the files.</p>';
        });
    </script>
</html>
```
