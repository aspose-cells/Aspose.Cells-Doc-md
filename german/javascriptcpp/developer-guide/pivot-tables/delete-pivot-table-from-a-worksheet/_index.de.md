---
title: Pivot Tabelle aus einem Arbeitsblatt löschen
type: docs
weight: 60
url: /de/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for JavaSkript via C++ Code, um PivotTable für Excel Arbeitsblätter zu entfernen
keywords: Aspose.Cells for JavaSkript via C++ Excel, Excel JavaScript Bibliothek, Pivot Tabelle aus Arbeitsblatt entfernen, Pivot Tabelle aus Excel entfernen, wie man Pivot Tabelle mit Aspose.Cells for JavaSkript via C++ löscht, Pivot Tabelle löschen, Pivot Tabelle aus Excel löschen, Pivot Tabelle löschen, Aspose.Cells for JavaSkript via C++ entfernt Pivot Tabelle, Pivot Tabelle entfernen, Pivot Tabelle löschen, wie man Pivot Tabelle löscht
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ provides a feature to delete or remove Pivot Table from a Worksheet. You can delete the pivot table using pivot table object or pivot table position. Please use the [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) method to delete the pivot table using pivot table object and [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) method to delete pivot table object using its position inside the pivot table collection.

{{% /alert %}}

## **Wie man Pivot-Tabelle im Arbeitsblatt mit Aspose.Cells for JavaScript via C++ löscht**

Der folgende Beispielcode löscht zwei Pivot-Tabellen aus dem Arbeitsblatt. Zuerst entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-)-Methode und dann entfernt er die Pivot-Tabelle unter Verwendung der [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)-Methode

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
