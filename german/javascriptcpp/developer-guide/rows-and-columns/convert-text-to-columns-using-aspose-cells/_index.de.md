---
title: Text in Spalten mit Aspose.Cells for JavaScript über C++ umwandeln
linktitle: Text in Spalten konvertieren
type: docs
weight: 30
url: /de/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: Erfahren Sie, wie Sie Text in Excel mit Aspose.Cells for JavaScript über C++ in Spalten umwandeln.
---

## **Mögliche Verwendungsszenarien**  

Sie können Ihren Text mithilfe von Microsoft Excel in Spalten umwandeln. Diese Funktion ist im Menü *Daten* unter *Datentools* verfügbar. Um den Inhalt einer Spalte in mehrere Spalten aufzuteilen, muss die Daten einen bestimmten Trenner enthalten, beispielsweise ein Komma (oder ein anderes Zeichen), anhand dessen Microsoft Excel den Inhalt einer Zelle in mehrere Zellen aufteilt. Aspose.Cells for JavaScript über C++ bietet diese Funktion ebenfalls über [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Text in Spalten mit Aspose.Cells for JavaScript über C++ umwandeln**  

Der folgende Beispielcode erklärt die Nutzung der [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) Methode. Der Code fügt zunächst einige Personennamen in Spalte A des ersten Arbeitsblatts ein. Vor- und Nachname sind durch ein Leerzeichen getrennt. Anschließend wendet er die [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) Methode auf Spalte A an und speichert das Ergebnis in eine Ausgabedatei. Wenn Sie die [Ausgabedatei](25395213.xlsx) öffnen, sehen Sie, dass die Vornamen in Spalte A sind, während die Nachnamen in Spalte B stehen, wie in diesem Screenshot gezeigt.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
