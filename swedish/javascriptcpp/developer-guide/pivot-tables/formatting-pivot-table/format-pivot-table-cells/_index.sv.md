---
title: Formatera pivot tabellceller
type: docs
weight: 30
url: /sv/javascript-cpp/format-pivot-table-cells/
description: Hur man formaterar pivottabellceller med Aspose.Cells for JavaScript via C++.
keywords: Formatera pivot tabellceller.
---

{{% alert color="primary" %}}

Ibland vill du formatera pivottabellceller. Till exempel vill du tillämpa bakgrundsfärg på pivottabellceller. Aspose.Cells for JavaScript via C++ erbjuder två metoder [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) och [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-), som du kan använda för detta ändamål.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) tillämpar stilen på hela pivot-tabellen medan [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-) tillämpar stilen på en enskild cell i pivot-tabellen.

{{% /alert %}}
Följande exempelkod läser in [exemplet Excel-fil](pivot_format.xlsx) som innehåller två pivot-tabeller och uppnår operationen att formatera hela pivot-tabellen och formatera individuella celler i pivot-tabellen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Formatting Example</title>
    </head>
    <body>
        <h1>Pivot Table Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the worksheet by its name
            const worksheet = workbook.worksheets.get("Sheet1");

            // Access the pivot table (second pivot table, index 1)
            const pivotTable = worksheet.pivotTables.get(1);

            // Create a style object with background color light blue
            const style = workbook.createStyle();
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.backgroundColor = AsposeCells.Color.LightBlue;

            // Format entire pivot table with light blue color
            pivotTable.formatAll(style);

            // Create another style object with yellow color
            const style2 = workbook.createStyle();
            style2.pattern = AsposeCells.BackgroundType.Solid;
            style2.backgroundColor = AsposeCells.Color.Yellow;

            // Access the first pivot table (index 0)
            const pivotTable2 = worksheet.pivotTables.get(0);

            // Format the cell of pivot table at row 16, column 5 (0-based indices)
            pivotTable2.format(16, 5, style2);

            // Saving the workbook object and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot tables formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Relaterade artiklar

- [Formatering av Pivottabell](/cells/sv/javascript-cpp/formatting-pivot-table/)
- [Arbete med dataformat för DataField i pivot-tabell](/cells/sv/javascript-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
