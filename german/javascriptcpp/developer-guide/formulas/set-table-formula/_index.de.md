---
title: Automatisches Propagieren von Formeln in Tabellen oder Listenobjekten Beim Eingeben von Daten in Neue Zeilen mit JavaScript via C++
linktitle: Tabellenformel festlegen
type: docs
weight: 260
url: /de/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Erfahren Sie, wie Sie Formeln beim Eingeben neuer Daten in Tabellen oder Listenobjekten mit Aspose.Cells for JavaScript via C++ automatisch propagieren.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass eine Formel in Ihrer Tabelle oder Ihrem Listenobjekt beim Eingeben neuer Daten automatisch auf neue Zeilen übertragen wird. Dies ist das Standardverhalten von Microsoft Excel. Um dieselbe Funktionalität mit Aspose.Cells for JavaScript via C++ zu erreichen, verwenden Sie bitte die [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--) Eigenschaft.

## **Formel automatisch in Tabelle oder Listenobjekt propagieren, während Sie Daten in neuen Zeilen eingeben**
Der folgende Beispielcode erstellt eine Tabelle oder Listenobjekt so, dass die Formel in Spalte B automatisch auf neue Zeilen übertragen wird, wenn Sie neue Daten eingeben. Bitte überprüfen Sie die [Ausgabedatei] (5115469.xlsx), die mit diesem Code generiert wurde. Wenn Sie eine beliebige Zahl in Zelle A3 eingeben, werden Sie sehen, dass die Formel in Zelle B2 automatisch nach B3 propagiert wird.

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
