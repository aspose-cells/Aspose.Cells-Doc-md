---
title: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 140
url: /de/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: Lernen Sie, wie Sie Warnhinweise beim Sortieren von Daten mit der Aspose.Cells for JavaScript via C++ API angeben.
keywords: Sortierwarnung hinzufügen beim Sortieren von Daten, Sortierwarnung beim Sortieren von Daten festlegen, Sortierwarnung beim Sortieren von Daten auswählen.
---

## **Mögliche Verwendungsszenarien**

Bitte beachten Sie diese Textdaten, d.h. {11, 111, 22}. Diese Textdaten werden sortiert, weil 111 vor 22 kommt, wenn man sie als Text betrachtet. Wenn Sie diese Daten jedoch als Zahlen sortieren möchten, lautet die Sortierung {11, 22, 111}, da numerisch 111 nach 22 kommt. Die Aspose.Cells for JavaScript via C++ bietet die Eigenschaft {0} zur Behandlung dieses Problems. Stellen Sie diese Eigenschaft **auf true**, und Ihre Textdaten werden als numerische Daten sortiert. Das folgende Screenshot zeigt die Warnmeldung, die Microsoft Excel anzeigt, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

Der folgende Beispielscode veranschaulicht die Verwendung der [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-)-Eigenschaft wie zuvor erläutert. Bitte überprüfen Sie die [Beispieldatei Excel](43352075.xlsx) und die [Ausgabedatei Excel](43352076.xlsx) für mehr Hilfe.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
