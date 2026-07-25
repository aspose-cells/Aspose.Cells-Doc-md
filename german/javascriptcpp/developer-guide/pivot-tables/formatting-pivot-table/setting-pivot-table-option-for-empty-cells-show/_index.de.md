---
title: Pivot Tabellen Option einstellen – Leere Zellen anzeigen
type: docs
weight: 40
url: /de/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Sie können verschiedene Pivot-Tabellen-Optionen mithilfe von Aspose.Cells for JavaScript via C++ konfigurieren. Eine dieser Optionen ist "Bei leeren Zellen anzeigen". Durch das Festlegen dieser Option werden alle leeren Zellen in einer Pivot-Tabelle als eine angegebene Zeichenfolge angezeigt.

{{% /alert %}}

## **Pivot-Tabellen-Option in Microsoft Excel einstellen**

Um diese Option in Microsoft Excel zu finden und einzustellen:

1. Wählen Sie eine Pivot-Tabelle aus und klicken Sie mit der rechten Maustaste.
1. Wählen Sie **PivotTable-Optionen** aus.
1. Wählen Sie das Registerkarte **Layout & Format** aus.
1. Wählen Sie die Option **Leere Zellen anzeigen** aus und geben Sie einen Text an.

## **Konfigurieren der Pivot-Tabellen-Optionen mit Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ stellt die [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-)- und [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-)-Eigenschaften bereit, um die Option "Bei leeren Zellen anzeigen" in der Pivot-Tabelle festzulegen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## Verwandte Artikel

- [Pivot-Tabelle formatieren](/cells/de/javascript-cpp/formatting-pivot-table/)
