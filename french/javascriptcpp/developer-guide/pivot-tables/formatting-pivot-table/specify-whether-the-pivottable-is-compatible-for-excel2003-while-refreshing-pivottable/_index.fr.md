---
title: Précisez si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique
type: docs
weight: 80
url: /fr/javascript-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ fournit la propriété [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) que vous pouvez utiliser pour spécifier si le PivotTable est compatible pour Excel2003 lors du rafraîchissement du PivotTable. Si vrai, une chaîne doit comporter 255 caractères ou moins, donc si la chaîne dépasse 255 caractères, elle sera tronquée. Si **false**, une chaîne ne sera pas soumise à cette restriction. La valeur par défaut est **true**.

{{% /alert %}}

## **Spécifiez si le PivotTable est compatible pour Excel2003 lors de l'actualisation du PivotTable**

Le code d'exemple suivant explique l'utilisation de la propriété [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-). La chaîne d'origine fait 383 caractères de long. Mais lorsque la propriété [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) est définie sur **vrai** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères de long. Cependant, lorsque la propriété [**PivotTable.isExcel2003Compatible**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isExcel2003Compatible-boolean-) est définie sur **faux** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specify Compatibility</title>
    </head>
    <body>
        <h1>Specify Compatibility Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (e.g., sample-pivot-table.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet that contains pivot table data
            const dataSheet = workbook.worksheets.get(0);

            // Access cell A3 and sets its data
            const cells = dataSheet.cells;
            let cell = cells.get("A3");
            cell.value = "FooBar";

            // Access cell B3, sets its data. We set B3 a very long string which has more than 255 characters
            const longStr = "Very long text 1. very long text 2. very long text 3. very long text 4. very long text 5. very long text 6. very long text 7. very long text 8. very long text 9. very long text 10. very long text 11. very long text 12. very long text 13. very long text 14. very long text 15. very long text 16. very long text 17. very long text 18. very long text 19. very long text 20. End of text.";
            cell = cells.get("B3");
            cell.value = longStr;

            // Print the length of cell B3 string
            console.log("Length of original data string: "  + cell.stringValue.length);

            // Access cell C3 and sets its data
            cell = cells.get("C3");
            cell.value = "closed";

            // Access cell D3 and sets its data
            cell = cells.get("D3");
            cell.value = "2016/07/21";

            // Access the second worksheet that contains pivot table
            const pivotSheet = workbook.worksheets.get(1);

            // Access the pivot table
            const pivotTable = pivotSheet.pivotTables.get(0);

            // IsExcel2003Compatible property tells if PivotTable is compatible for Excel2003 while refreshing PivotTable.
            // If it is true, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters,
            // it will be truncated. If false, a string will not have the aforementioned restriction. The default value is true.
            pivotTable.isExcel2003Compatible = true;
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Check the value of cell B5 of pivot sheet.
            // It will be 255 because we have set IsExcel2003Compatible property to true. All the data after 255 characters has been truncated
            let b5 = pivotSheet.cells.get("B5");
            console.log("Length of cell B5 after setting IsExcel2003Compatible property to True: "  + b5.stringValue.length);

            // Now set IsExcel2003Compatible property to false and again refresh
            pivotTable.isExcel2003Compatible = false;
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Now it will print the original length of cell data. The data has not been truncated now.
            b5 = pivotSheet.cells.get("B5");
            console.log("Length of cell B5 after setting IsExcel2003Compatible property to False: "  + b5.stringValue.length);

            // Set the row height and column width of cell B5 and also wrap its text
            pivotSheet.cells.setRowHeight(b5.row, 100);
            pivotSheet.cells.setColumnWidth(b5.column, 65);

            const st = b5.style;
            st.isTextWrapped = true;
            b5.style = st;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyCompatibility_out_.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
