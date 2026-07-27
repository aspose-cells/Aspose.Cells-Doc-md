---
title: Abrufen des Zellenobjekts nach Anzeigenamen des PivotField der Pivot Tabelle
type: docs
weight: 70
url: /de/javascript-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Wie man das Cell Objekt anhand des Anzeigenamens des PivotFields des Pivot Table mit Aspose.Cells for JavaScript via C++ erhält.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript Bibliothek, Cell Objekt anhand des Anzeigenamens des PivotFields des Pivot Table mit Aspose.Cells for JavaScript via C++ Excel Library.
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ bietet die Methode [**PivotTable.cellByDisplayName(string)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#cellByDisplayName-string-), mit der Sie auf das Cell-Objekt anhand des Anzeige-Namens des Pivot-Felds zugreifen können. Diese Methode ist nützlich, wenn Sie Ihren Pivot-Feld-Header hervorheben oder formatieren möchten. Dieser Artikel erklärt, wie man das Cell-Objekt anhand des Anzeigenamens des Datenfelds abruft und anschließend formatiert.

{{% /alert %}}

## **Wie man das Zellenobjekt anhand des Anzeigenamens des PivotField der PivotTable erhält**

Der folgende Code greift auf die erste Pivot-Tabelle des Arbeitsblatts zu und ruft dann die Zelle über den Anzeigenamen des zweiten Datenfelds der Pivot-Tabelle ab. Ehe ändert er die Füllfarbe und Schriftfarbe der Zelle jeweils in Hellblau und Schwarz. Unten sind Screenshots, die zeigen, wie die Pivot-Tabelle vor und nach der Ausführung des Codes aussieht.

|**Pivot-Tabelle - Vorher**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Cell Styling Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table inside the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Access cell by display name of 2nd data field of the pivot table
            const dataFieldDisplayName = pivotTable.dataFields.get(1).displayName;
            const cell = pivotTable.cellByDisplayName(dataFieldDisplayName);

            // Access cell style and set its fill color and font color
            const style = cell.style;
            style.foregroundColor = AsposeCells.Color.LightBlue;
            style.font.color = AsposeCells.Color.Black;

            // Set the style of the cell
            pivotTable.format(cell.row, cell.column, style);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

|**Pivot-Tabelle - Nachher**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
