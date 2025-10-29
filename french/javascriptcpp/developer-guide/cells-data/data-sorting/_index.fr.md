---
title: Tri des données
type: docs
weight: 130
url: /fr/javascript-cpp/sort-data-of-excel/
description: Apprenez comment trier des données en utilisant l API Aspose.Cells for JavaScript via C++.
keywords: Trier les données par ordre croissant ou décroissant, trier les données en fonction de la couleur de fond
---

{{% alert color="primary" %}}

Le tri des données est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Il permet aux utilisateurs d'organiser les données pour faciliter leur consultation. Aspose.Cells for JavaScript via C++ permet aux développeurs de trier les données de la feuille de calcul par ordre alphabétique ou numérique, ce qui fonctionne de la même manière que Microsoft Excel pour trier des données.

{{% /alert %}}

## **Triage des données dans Microsoft Excel**

Pour trier les données dans Microsoft Excel :

1. Sélectionnez **Données** dans le menu **Trier**. La boîte de dialogue Trier s'affiche.
1. Sélectionnez une option de tri.

En général, le tri est effectué sur une liste - définie comme un groupe de données contiguës où les données sont affichées dans des colonnes.

## **Trier les données avec Aspose.Cells**

Aspose.Cells for JavaScript via C++ fournit la classe [**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter) utilisée pour trier les données en ordre croissant ou décroissant. La classe possède quelques membres importants, comme des propriétés telles que Key1 ... Key3 et Order1 ... Order3. Ces membres sont utilisés pour définir les clés triées et préciser l'ordre de tri.

Vous devez définir les clés et définir l'ordre de tri avant de mettre en œuvre le tri des données. La classe fournit la méthode [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) utilisée pour effectuer le tri des données en fonction des données de cellule dans une feuille de calcul.

La méthode [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) accepte les paramètres suivants :

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), les cellules de la feuille de calcul sous-jacente.
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea), la plage de cellules. Définissez la zone de cellules avant d'appliquer le tri des données.

Cet exemple utilise le fichier modèle "Book1.xls" créé dans Microsoft Excel. Après l'exécution du code ci-dessous, les données sont triées correctement.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si vous souhaitez trier *de gauche à droite*, utilisez l'attribut [**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-).

{{% /alert %}}

### **Tri des données avec couleur de fond**

Excel offre des fonctionnalités pour trier les données en fonction de la couleur de fond. La même fonctionnalité est disponible via Aspose.Cells for JavaScript via C++ en utilisant DataSorter où [**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor peut être utilisé dans [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) pour trier les données en fonction de la couleur de fond. Toutes les cellules contenant la couleur spécifiée dans la fonction [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) sont placées en haut ou en bas selon le paramètre SortOrder, et l'ordre des autres cellules ne change pas du tout.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Trier les données dans une colonne avec une liste de tri personnalisée](/cells/fr/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [Spécifier un avertissement de tri lors du tri des données](/cells/fr/javascript-cpp/specifying-sort-warning-while-sorting-data/)
