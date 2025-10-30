---
title: Doppelte Zeilen in einem Arbeitsblatt mit JavaScript über C++ entfernen
linktitle: Doppelte Zeilen in einem Arbeitsblatt entfernen
type: docs
weight: 370
url: /de/javascript-cpp/remove-duplicate-rows-in-a-worksheet/
description: Lernen Sie, wie Sie doppelte Zeilen in einem Arbeitsblatt mit Aspose.Cells for JavaScript über C++ entfernen und bestimmte Spalten für Duplikatüberprüfungen auswählen.
---

Das Entfernen doppelter Zeilen ist eine der vielen nützlichen Funktionen von Microsoft Excel. Es ermöglicht Benutzern, doppelte Zeilen in einem Arbeitsblatt zu entfernen, und Sie können auswählen, welche Spalten auf doppelte Informationen überprüft werden sollen.

Aspose.Cells for JavaScript über C++ bietet die `Cells.removeDuplicates()`-Methode für diesen Zweck. Sie können auch `startRow`, `startColumn`, `endRow` und `endColumn` festlegen, um den Bereich der Spalten zur Duplikatsprüfung zu spezifizieren.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[removeduplicates.xlsx](removeduplicates.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Duplicates Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Remove Duplicate (converted getters to properties)
            book.worksheets.get(0).cells.removeDuplicates(0, 0, 5, 3);

            // Save result and provide download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'removeduplicates-result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            resultDiv.innerHTML = '<p style="color: green;">Duplicates removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
