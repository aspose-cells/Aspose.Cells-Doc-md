---
title: Spécification de la position absolue de l élément du tableau croisé dynamique
type: docs
weight: 50
url: /fr/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur doit spécifier la position absolue des éléments de pivot, l'API Aspose.Cells for JavaScript via C++ a exposé quelques nouvelles propriétés et une méthode pour répondre à cette exigence.

- Ajouté la propriété [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-) qui peut être utilisée pour spécifier l'index de position dans tous les PivotItems indépendamment du nœud parent. Ajouté la propriété [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) qui peut être utilisée pour spécifier l'index de position dans les PivotItems sous le même nœud parent.
- Ajout de la méthode [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) pour déplacer l'élément vers le haut ou vers le bas en fonction de la valeur du compteur, où le compteur est le nombre de positions pour déplacer l'élément du tableau croisé dynamique vers le haut ou vers le bas. Si la valeur du compteur est inférieure à zéro, l'élément sera déplacé vers le haut, alors que si la valeur du compteur est supérieure à zéro, l'élément du tableau croisé dynamique se déplacera vers le bas. Le paramètre de type booléen isSameParent spécifie si l'opération de déplacement doit être effectuée dans le même nœud parent ou non.
- La méthode *PivotItem.move(int count)* étant obsolète, il est recommandé d’utiliser la nouvelle méthode [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

Le code d'exemple suivant crée un tableau croisé dynamique et spécifie ensuite les positions des éléments du tableau croisé dynamique dans le même nœud parent. Vous pouvez télécharger les fichiers [Excel source](5112632.xlsx) et [Excel de sortie](5112619.xlsx) pour votre référence. Si vous ouvrez le fichier Excel de sortie, vous verrez l'élément du tableau croisé dynamique "4H12" est à la 0e position dans le parent "K11" et "DIF400" est à la 3e position. De même, CA32 est à la position 1 et AAA3 est à la position 2

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldType, PivotFieldSubtotalType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Add pivot worksheet and get data worksheet
            const wsPivot = workbook.worksheets.add("pvtNew Hardware");
            const wsData = workbook.worksheets.get("New Hardware - Yearly");

            // Get the pivottables collection for the pivot sheet
            const pivotTables = wsPivot.pivotTables;

            // Add PivotTable to the worksheet
            const index = pivotTables.add("='New Hardware - Yearly'!A1:D621", "A3", "HWCounts_PivotTable");

            // Get the PivotTable object
            const pvtTable = pivotTables.get(index);

            // Add vendor row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Vendor");

            // Add item row field
            pvtTable.addFieldToArea(PivotFieldType.Row, "Item");

            // Add data field
            pvtTable.addFieldToArea(PivotFieldType.Data, "2014");

            // Turn off the subtotals for the vendor row field
            const pivotField = pvtTable.rowFields.get("Vendor");
            pivotField.subtotals = PivotFieldSubtotalType.None;

            // Turn off grand total
            pvtTable.columnGrand = false;

            /*
             * Please call the PivotTable.refreshData() and PivotTable.calculateData()
             * before using PivotItem.setPosition,
             * PivotItem.setPositionInSameParentNode and PivotItem.move methods.
            */
            pvtTable.refreshData();
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("4H12").positionInSameParentNode = 0;
            pvtTable.rowFields.get("Item").pivotItems.get("DIF400").positionInSameParentNode = 3;

            /* 
             * As a result of using PivotItem.setPositionInSameParentNode,
             * it will change the original sort sequence.
             * So when you use PivotItem.setPositionInSameParentNode in another parent node.
             * You need call the method named "calculateData" again. 
            */
            pvtTable.calculateData();

            pvtTable.rowFields.get("Item").pivotItems.get("CA32").positionInSameParentNode = 1;
            pvtTable.rowFields.get("Item").pivotItems.get("AAA3").positionInSameParentNode = 2;

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">PivotTable created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Veuillez noter qu'il est nécessaire d'appeler les méthodes PivotTable.RefreshData et PivotTable.CalculateData avant d'utiliser les propriétés [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-), [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) et la méthode [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}
