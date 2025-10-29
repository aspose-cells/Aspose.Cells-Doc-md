---
title: Insérer ou supprimer des lignes dans une feuille Excel avec JavaScript via C++
linktitle: Insérer ou supprimer des lignes dans une feuille de calcul Excel
type: docs
weight: 20
url: /fr/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Cet article fournit du code JavaScript utilisant C++ pour insérer et supprimer des lignes dans une feuille Excel.
keywords: insérer ou supprimer des lignes dans une feuille Excel avec JavaScript, insérer ou supprimer des lignes dans Excel avec JavaScript, insérer des lignes dans Excel avec JavaScript, supprimer des lignes dans Excel avec JavaScript, insérer ou supprimer des lignes dans une feuille Excel avec JavaScript, insérer ou supprimer des lignes dans Excel avec JavaScript, insérer des lignes dans Excel avec JavaScript, supprimer des lignes dans Excel avec JavaScript
---

{{% alert color="primary" %}}  

Lors de la création d'une nouvelle feuille ou de la manipulation d'une feuille existante, vous pourriez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir les données. D'autres fois, vous pourriez avoir besoin de supprimer des lignes ou colonnes aux positions spécifiées dans la feuille.  

{{% /alert %}}  

Aspose.Cells for JavaScript via C++ offre deux méthodes pour insérer et supprimer des lignes : [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) et [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). Ces méthodes sont optimisées pour la performance et accomplissent leur tâche très rapidement.  

Pour insérer ou retirer un nombre de lignes, il est recommandé d'utiliser toujours les méthodes [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) et [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) au lieu des méthodes [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) ou [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) dans une boucle.  

Aspose.Cells fonctionne de la même manière que Microsoft Excel. Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est déplacé vers le bas et vers la droite. Lorsque des lignes ou des colonnes sont supprimées, le contenu de la feuille de calcul est déplacé vers le haut ou vers la gauche. Toutes les références dans les autres feuilles de calcul et cellules sont mises à jour lorsque des lignes sont ajoutées ou supprimées.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
