---
title: Angabe der absoluten Position des Pivot Elements
type: docs
weight: 50
url: /de/javascript-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer die absolute Position der Pivot-Elemente angeben. Aspose.Cells for JavaScript via C++ hat einige neue Eigenschaften und eine Methode veröffentlicht, um dieses Bedürfnis zu erfüllen.

- Hinzugefügte [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-) Eigenschaft, die verwendet werden kann, um den Position-Index in allen Pivot-Elementen unabhängig vom übergeordneten Knoten anzugeben. Hinzugefügte [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) Eigenschaft, die verwendet werden kann, um den Position-Index in den Pivot-Elementen unter dem gleichen übergeordneten Knoten anzugeben.
- Hinzugefügte [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) Methode, um das Element basierend auf dem Zählwert nach oben oder unten zu bewegen, wobei der Zählwert die Anzahl der Positionen angibt, um das Pivot-Element nach oben oder unten zu bewegen. Wenn der Zählwert kleiner als null ist, wird das Element nach oben verschoben, wenn der Zählwert größer als null ist, wird das Pivot-Element nach unten verschoben. Der boolesche Typ-Parameter isSameParent gibt an, ob die Verschiebungsoperation im gleichen übergeordneten Knoten durchgeführt werden soll oder nicht.
- Die *PivotItem.move(int count)* Methode ist veraltet, daher wird empfohlen, stattdessen die neu hinzugefügte Methode [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) zu verwenden.

{{% /alert %}}

Der folgende Beispielcode erstellt ein Pivot-Table und legt dann die Positionen der Pivot-Elemente im gleichen übergeordneten Knoten fest. Sie können die [Quell-Excel-Datei](5112632.xlsx) und die [Ausgabe-Excel-Datei](5112619.xlsx) für Ihre Referenz herunterladen. Wenn Sie die Ausgabe-Excel-Datei öffnen, sehen Sie, dass das Pivot-Element "4H12" sich an der 0. Position im übergeordneten Knoten "K11" befindet und "DIF400" sich an der 3. Position befindet. Ebenso befindet sich CA32 an Position 1 und AAA3 an Position 2.

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

Bitte beachten Sie, dass es notwendig ist, die Methoden PivotTable.RefreshData und PivotTable.CalculateData aufzurufen, bevor Sie die [**PivotItem.position**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#position-number-), [**PivotItem.positionInSameParentNode**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#positionInSameParentNode-number-) Eigenschaften und [**PivotItem.move**](https://reference.aspose.com/cells/javascript-cpp/pivotitem/#move-number-boolean-) Methode verwenden.

{{% /alert %}}
