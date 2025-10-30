---
title: Zeilen in einem Excel Arbeitsblatt mit JavaScript über C++ einfügen oder löschen
linktitle: Ein oder Löschen von Zeilen in einem Excel Arbeitsblatt
type: docs
weight: 20
url: /de/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Dieser Artikel bietet JavaScript Code unter Verwendung von C++, um Zeilen in einem Excel Arbeitsblatt einzufügen und zu löschen.
keywords: JavaScript Zeilen in Excel Arbeitsblatt einfügen oder löschen, JavaScript Zeilen in Excel einfügen oder löschen, Zeilen in Excel mit JavaScript einfügen, Zeilen in Excel mit JavaScript löschen, Zeilen in Excel Arbeitsblatt mit JavaScript einfügen oder löschen, Zeilen in Excel mit JavaScript einfügen oder löschen, Zeilen in Excel mit JavaScript einfügen, Zeilen in Excel mit JavaScript löschen
---

{{% alert color="primary" %}}  

Beim Erstellen eines neuen Arbeitsblatts oder bei der Arbeit mit einem bestehenden Arbeitsblatt könnte es notwendig sein, zusätzliche Zeilen oder Spalten hinzuzufügen, um Daten aufzunehmen. Manchmal ist es auch notwendig, Zeilen oder Spalten an bestimmten Stellen im Arbeitsblatt zu löschen.  

{{% /alert %}}  

Das Aspose.Cells for JavaScript über C++ bietet zwei Methoden zum Einfügen und Löschen von Zeilen: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) und [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). Diese Methoden sind auf Leistung optimiert und erledigen die Aufgabe sehr schnell.  

Um eine Anzahl von Zeilen einzufügen oder zu entfernen, empfehlen wir, immer die Methoden [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) und [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) anstelle der Methoden [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) oder [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) in einer Schleife zu verwenden.  

Aspose.Cells arbeitet genauso wie Microsoft Excel. Wenn Zeilen oder Spalten hinzugefügt werden, wird der Inhalt des Arbeitsblatts nach unten und nach rechts verschoben. Wenn Zeilen oder Spalten entfernt werden, wird der Inhalt des Arbeitsblatts nach oben oder nach links verschoben. Referenzen in anderen Arbeitsblättern und Zellen werden aktualisiert, wenn Zeilen hinzugefügt oder entfernt werden.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
