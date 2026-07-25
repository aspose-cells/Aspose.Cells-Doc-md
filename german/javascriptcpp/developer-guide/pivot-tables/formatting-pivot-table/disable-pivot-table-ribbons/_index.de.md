---
title: Pivot Tabellen Ribbons deaktivieren
type: docs
weight: 90
url: /de/javascript-cpp/disable-pivot-table-ribbons/
description: Wie man Pivot Tabellen Bänder mit Aspose.Cells for JavaScript via C++ deaktiviert.
keywords: Aspose.Cells for JavaScript via C++ Excel, Excel JavaScript via C++ Bibliothek, Deaktivieren der Pivot Tabellen Bänder mit Aspose.Cells for JavaScript via C++ Excel Bibliothek.
---

{{% alert color="primary" %}}

Berichte auf Pivot-Tabellenbasis sind nützlich, aber anfällig für Fehler, wenn die Zielnutzer kein detailliertes Wissen über Excel haben, um diese Berichte zu konfigurieren. In solchen Fällen möchten Organisationen, dass die Nutzer nicht in der Lage sind, ein auf Pivot-Tabellen basierendes Bericht zu ändern. Gängige Funktionen der Pivot-Tabelle wie das Hinzufügen zusätzlicher Filter, Slicer, Felder oder das Ändern der Reihenfolge bestimmter Elemente im Bericht sind meist nicht für jeden Nutzer empfohlen. Andererseits sollen diese Nutzer auch in der Lage sein, den Bericht zu aktualisieren und vorhandene Filter oder Slicer zu verwenden. Aspose.Cells for JavaScript via C++ bietet diese Fähigkeit, um Entwicklern das Einschränken der Nutzer beim Ändern dieser Berichte beim Erstellen dieser Berichte zu ermöglichen. Zu diesem Zweck stellt Excel eine Funktion bereit, um das Pivot-Tabellen-Ribbon zu deaktivieren, was ebenfalls durch Aspose.Cells for JavaScript via C++ ermöglicht wird, d.h. der Entwickler kann das Ribbon, das Steuerungen zur Bearbeitung dieser Berichte enthält, deaktivieren.

{{% /alert %}}

## **Wie man das Pivot-Tabellen-Ribbon mit Aspose.Cells for JavaScript via C++ deaktiviert**

Der folgende Code demonstriert diese Funktion, indem er auf eine Pivot-Tabelle aus einem Blatt zugreift und dann [**enableWizard**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#enableWizard-boolean-) auf **false** setzt. Die Beispieldatei für die Pivot-Tabelle kann von diesem [Link](pivot_table_test.xlsx) heruntergeladen werden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Pivot Table Wizard Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the pivot table in the first sheet
            const pt = workbook.worksheets.get(0).pivotTables.get(0);

            // Disable ribbon for this pivot table
            pt.enableWizard = false;

            // Save output file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table wizard disabled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
