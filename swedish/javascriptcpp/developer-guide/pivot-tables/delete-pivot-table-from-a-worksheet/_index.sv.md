---
title: Ta bort pivottabell från ett arbetsblad
type: docs
weight: 60
url: /sv/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for JavaScript via C++ kod för att ta bort pivottabell för Excel ark
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript bibliotek, ta bort pivottabell från kalkylblad, ta bort pivottabell från Excel, hur man tar bort pivottabell med Aspose.Cells for JavaScript via C++, ta bort pivottabell, ta bort pivottabell från Excel, ta bort pivottabell, Aspose.Cells for JavaScript via C++ tar bort pivottabell, ta bort pivottabell, ta bort pivottabell, hur man tar bort pivottabell
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ tillhandahåller en funktion för att ta bort eller radera pivottabell från ett kalkylblad. Du kan ta bort pivottabellen med hjälp av pivottabellobjektet eller pivottabellens position. Använd [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-)-metoden för att ta bort pivottabellen med pivottabellobjektet och [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)-metoden för att ta bort pivottabellobjektet baserat på dess position inom pivottabellkollektionen.

{{% /alert %}}

## **Hur man tar bort pivotdiagram från kalkylblad med Aspose.Cells for JavaScript via C++**

Följande kodexempel tar bort två pivottabeller från arbetsbladet. Först tar det bort pivottabellen med hjälp av [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) -metoden och sedan tar det bort pivottabellen med hjälp av [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) -metoden

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
