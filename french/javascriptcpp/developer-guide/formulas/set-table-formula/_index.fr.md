---
title: Propager la formule dans un tableau ou un objet liste automatiquement lors de la saisie de nouvelles données avec JavaScript via C++
linktitle: Définit la formule de tableau
type: docs
weight: 260
url: /fr/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Apprenez comment propager automatiquement les formules dans les tableaux ou objets liste lors de la saisie de nouvelles données en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez qu'une formule dans votre tableau ou objet liste se propage automatiquement aux nouvelles lignes lors de la saisie de nouvelles données. C'est le comportement par défaut de Microsoft Excel. Pour obtenir la même fonctionnalité avec Aspose.Cells for JavaScript via C++, veuillez utiliser la propriété [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--).

## **Propagation automatique de la formule dans un tableau ou objet de liste lors de la saisie de nouvelles données**
Le code d'exemple suivant crée un tableau ou objet de liste de manière à ce que la formule dans la colonne B se propage automatiquement aux nouvelles lignes lorsque vous saisissez de nouvelles données. Veuillez vérifier le [fichier Excel généré](5115469.xlsx) avec ce code. Si vous entrez un quelconque chiffre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
