---
title: Hitta och uppdatera de inbäddade eller underordnade pivottabellerna i föräldrapivottabellen
type: docs
weight: 60
url: /sv/javascript-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Hur man hittar och uppdaterar inbäddade eller underordnade pivotdiagram av en föräldrapivotdiagram med Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells for JavaScript Excel, Excel JavaScript bibliotek, hitta och uppdatera inbäddade eller underordnade pivotdiagram av föräldrapivotdiagram med Aspose.Cells for JavaScript Excel bibliotek.
---

## **Möjliga användningsscenario**

Ibland använder en pivottabell en annan pivottabell som datakälla, så det kallas en underordnad pivottabell eller inbäddad pivottabell. Du kan hitta de underordnade pivottablerna i en föräldrapivottabell med hjälp av [**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--) metoden.

## **Här demonstreras funktionen med följande provkod genom att ladda den [prov-Excel-filen](61767747.xlsx) som innehåller tre pivot-tabeller. De två nedre pivot-tabellerna är barn till ovanstående pivot-tabell enligt visas i denna skärmbild. Koden hittar barnpivot-tabellerna med hjälp av {0}-metoden och sedan uppdaterar dem en efter en.**

Följande kod laddar den [prov-Eexcelfilen](61767747.xlsx) som innehåller tre pivottabeller. De två nedre pivottablerna är barn till den ovanstående pivottabellen som visas i denna skärmdump. Koden hittar de underordnade pivottablerna med hjälp av [**PivotTable.children**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#children--) metoden och uppdaterar dem en efter en.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Refresh Nested/Children Pivot Tables Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access third pivot table (index 2)
            const ptParent = ws.pivotTables.get(2);

            // Access the children of the parent pivot table
            const ptChildren = ptParent.children;

            // Refresh all the children pivot table
            for (let pivot of ptChildren) {
                pivot.refreshData();
                pivot.calculateData();
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables refreshed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
