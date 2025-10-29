---
title: Supprimer le tableau croisé dynamique d une feuille de calcul
type: docs
weight: 60
url: /fr/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Utiliser le code Script via C++ pour supprimer un tableau croisé dynamique dans des feuilles Excel
keywords: Script via C++ pour Excel, bibliothèque JavaScript Excel, supprimer un tableau croisé dynamique d’une feuille, comment supprimer un tableau croisé dynamique avec Script via C++, supprimer un tableau croisé dynamique, supprimer un tableau croisé dynamique d’Excel, supprimer un tableau croisé dynamique, Script via C++ pour supprimer un tableau croisé dynamique, supprimer un tableau croisé dynamique, comment supprimer un tableau croisé dynamique
---

{{% alert color="primary" %}}

Script via C++ pour Excel offre une fonction pour supprimer ou retirer un tableau croisé dynamique d’une feuille. Vous pouvez supprimer le tableau croisé dynamique en utilisant l’objet tableau croisé dynamique ou sa position. Veuillez utiliser la méthode [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) pour supprimer le tableau croisé dynamique en utilisant l’objet tableau croisé dynamique et la méthode [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) pour supprimer l’objet tableau croisé dynamique en utilisant sa position dans la collection.

{{% /alert %}}

## **Comment supprimer un tableau croisé dynamique d'une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++**

Le code d'exemple suivant supprime deux tableaux croisés dynamiques de la feuille de calcul. D'abord, il supprime un tableau croisé dynamique en utilisant la méthode [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) et ensuite il supprime un tableau croisé dynamique en utilisant la méthode [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
