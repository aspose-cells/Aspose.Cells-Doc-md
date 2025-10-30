---
title: Zeitachse einfügen
linktitle: Zeitachsen
type: docs
weight: 170
url: /de/javascript-cpp/create-timeline/
description: Erfahren Sie, wie Sie eine Timeline mit Aspose.Cells for JavaScript via C++ erstellen.
---

## **Mögliche Verwendungsszenarien**

Anstelle von Filter anzupassen, um Daten nach Datum anzuzeigen, können Sie eine PivotTable-Zeitleiste — eine dynamische Filteroption — verwenden, mit der Sie einfach nach Datum/Zeit filtern und mit einem Schieberegler in den gewünschten Zeitraum zoomen können. Microsoft Excel ermöglicht das Erstellen einer Timeline, indem Sie eine Pivot-Tabelle auswählen und dann auf *Einfügen > Zeitleiste* klicken. Aspose.Cells for JavaScript via C++ ermöglicht auch die Erstellung einer Timeline mit der Methode [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Erstellen Sie eine Zeitleiste für eine Pivottabelle**

Siehe folgenden Beispielcode. Es lädt die [Beispieldatei Excel](input.xlsx), die die Pivot-Tabelle enthält. Dann erstellt es die Timeline basierend auf dem ersten Basis-Pivotfeld. Schließlich speichert es die Arbeitsmappe im [Ausgabe XLSX](output.xlsx) Format. Der folgende Screenshot zeigt die mit Aspose.Cells for JavaScript via C++ erstellte Timeline in der Ausgabedatei Excel.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
