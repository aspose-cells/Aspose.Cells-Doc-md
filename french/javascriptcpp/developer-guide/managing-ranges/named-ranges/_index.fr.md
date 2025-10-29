---
title: Créer des plages nommées à portée du classeur et de la feuille de calcul avec JavaScript via C++
linktitle: Plage nommée
type: docs
weight: 40
url: /fr/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Apprenez comment créer des plages nommées à portée du classeur et de la feuille de calcul en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux portées différentes : le classeur (également appelé portée globale) et la feuille de calcul.

- Les plages nommées avec une portée de classeur peuvent être accédées à partir de n'importe quelle feuille de calcul au sein de ce classeur en utilisant simplement son nom.
- Les plages nommées avec une portée de feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elle a été créée.

Aspose.Cells for JavaScript via C++ offre la même fonctionnalité que Microsoft Excel pour ajouter des plages nommées à portée du classeur et de la feuille de calcul. Lors de la création d'une plage nommée à portée de la feuille, la référence à la feuille doit être utilisée dans la plage nommée pour la spécifier comme plage nommée à portée de la feuille.

{{% /alert %}} 
## **Ajout d'une plage nommée au niveau du classeur**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>WorkbookScope Named Range Example</title>
    </head>
    <body>
        <h1>WorkbookScope Named Range Example</h1>
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

            // If a file is provided, load it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells from Cell A1 to C10
            const workbookScope = cells.createRange("A1", "C10");

            // Assign the name to workbook scope named range
            workbookScope.name = "workbookScope";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookScope.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range "workbookScope" created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
## **Ajout d'une plage nommée avec une portée de feuille de calcul**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Assign Range Name Example</h1>
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

            // Create new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells
            const localRange = cells.createRange("A1", "C10");

            // Assign name to range with sheet reference
            localRange.name = "Sheet1!local";

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Créer un accès et copier des plages nommées](/cells/fr/javascript-cpp/create-access-and-copy-named-ranges/)
- [Formater et modifier des plages nommées](/cells/fr/javascript-cpp/format-and-modify-named-ranges/)
- [Obtenir une plage avec des liens externes](/cells/fr/javascript-cpp/get-range-with-external-links/)
- [Mise en œuvre de plages non séquentielles](/cells/fr/javascript-cpp/implementing-non-sequential-ranges/)
