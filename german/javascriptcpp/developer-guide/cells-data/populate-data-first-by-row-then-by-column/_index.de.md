---
title: Füllen Sie zuerst die Daten nach Zeile und dann nach Spalte aus
type: docs
weight: 1000
url: /de/javascript-cpp/populate-data-first-by-row-then-by-column/
description: Lernen Sie, wie man Daten zuerst zeilenweise und dann spaltenweise mit der Aspose.Cells for JavaScript via C++ API befüllt.
keywords: Daten zuerst zeilenweise dann spaltenweise in JavaScript via C++, Daten zuerst zeilenweise dann spaltenweise in JavaScript via C++, Daten zuerst zeilenweise dann spaltenweise in JavaScript via C++, Hochleistungs Dateneinfügung in JavaScript via C++, Hochleistungs Datenaddition in JavaScript via C++
---

{{% alert color="primary" %}}  

Das Ausfüllen einer Tabelle mit Daten zuerst nach Zeile und dann nach Spalte verbessert die Gesamtperformance.  

{{% /alert %}}  

Das Einsetzen von Daten in die Folge A1, B1, A2, B2 ist schneller als A1, A2, B1, B2. Wenn es viele Zellen in einem Arbeitsblatt gibt und Sie die zweite Sequenz befolgen, das heißt, Sie füllen die Daten Zeile für Zeile ein, kann dieser Tipp das Programm wesentlich schneller machen.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Populate Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            // Create a new workbook (blank)
            const workbook = new Workbook();

            // Populate Data into Cells
            const cells = workbook.worksheets.get(0).cells;
            cells.get("A1").value = "data1";
            cells.get("B1").value = "data2";
            cells.get("A2").value = "data3";
            cells.get("B2").value = "data4";

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
