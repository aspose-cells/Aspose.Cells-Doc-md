---
title: Supprimer des plages nommées avec JavaScript via C++
linktitle: Supprimer les plages nommées
type: docs
weight: 90
url: /fr/javascript-cpp/Delete-named-ranges/
description: Vous pouvez apprendre comment supprimer des noms définis ou des plages nommées des fichiers Excel ou OpenOffice avec Aspose.Cells for JavaScript via C++.
---

## **Introduction**
S'il y a trop de noms définis ou de plages nommées dans les fichiers Excel, nous devons en effacer certains car ils ne sont plus référencés.

## **Supprimer une plage nommée dans MS Excel**

Pour supprimer une plage nommée dans Excel, suivez les étapes suivantes :
1. Ouvrez Microsoft Excel et ouvrez le classeur contenant la plage nommée.
2. Allez à l'onglet "Formules" dans le ruban Excel.
3. Cliquez sur le bouton "Gestionnaire de noms" dans le groupe "Noms définis". Cela ouvrira la boîte de dialogue Gestionnaire de noms.
4. Dans la boîte de dialogue Gestionnaire de noms, sélectionnez la plage nommée que vous souhaitez supprimer.
5. Cliquez sur le bouton "Supprimer". Confirmez la suppression lorsqu'on vous le demande.
6. Cliquez sur le bouton "Fermer" pour fermer la boîte de dialogue Gestionnaire de noms.
7. Enregistrez le classeur pour conserver les modifications.

## **Supprimer une plage nommée en utilisant Aspose.Cells for JavaScript via C++**
Avec Aspose.Cells for JavaScript via C++, vous pouvez supprimer des plages nommées ou des noms définis par [texte](https://reference.aspose.com/cells/javascript-cpp/namecollection/#remove-string-) ou [index](https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-) dans la liste.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Named Ranges Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted a named range by text.
            worksheets.names.remove("NamedRange");

            // Deleted a defined name by index. Ensure to check the count before removal.
            if (worksheets.names.count > 0) {
                worksheets.names.removeAt(0);
            }

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Remarque : si le nom défini est référencé par des formules, il ne peut pas être supprimé. Nous pouvons uniquement supprimer la formule du nom défini.

## **Supprime certaines plages nommées**
Lorsque nous supprimons un nom défini, nous devons vérifier s'il est référencé par toutes les formules du fichier.
Pour améliorer les performances de suppression des plages nommées, nous pouvons en supprimer plusieurs en même temps.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Named Ranges Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Delete some defined names.
            worksheets.names.remove(["NamedRange1", "NamedRange2"]);

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Supprimer les noms définis en double**
Certains fichiers Excel se corrompent car certains noms définis sont en double. Nous pouvons donc supprimer ces doublons pour réparer le fichier.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Duplicate Defined Names</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted some defined names.
            worksheets.names.removeDuplicateNames();

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Duplicate defined names removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
