---
title: Sparkline durch Angabe des Datenbereichs und des Standorts der Sparkline Gruppe mit JavaScript über C++ kopieren
linktitle: Sparkline kopieren durch Festlegen des Datenbereichs und des Speicherorts der Sparkline Gruppe
type: docs
weight: 300
url: /de/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Erfahren Sie, wie Sie eine Sparkline in Excel durch Angabe des Datenbereichs und des Standorts der Sparkline Gruppe mit Aspose.Cells for JavaScript über C++ kopieren.
---

{{% alert color="primary" %}}
Microsoft Excel ermöglicht es Ihnen, eine Sparkline zu kopieren, indem Sie den Datenbereich und den Speicherort einer Sparkline-Gruppe angeben. Aspose.Cells unterstützt diese Funktion.
{{% /alert %}}

Um eine Sparkline in andere Zellen in Microsoft Excel zu kopieren:

1. Wählen Sie die Zelle aus, die die Sparkline enthält.  
1. Wählen Sie **Daten bearbeiten** im **Sparkline**-Abschnitt des **Entwurfs**-Registers aus.  
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.  
1. Geben Sie den Datenbereich und den Speicherort an.  
1. Klicken Sie auf **OK**.

Aspose.Cells bietet die `SparklineCollection.add(dataRange, row, column)`-Methode, um einen Datenbereich und einen Standort für eine Sparkline-Gruppe festzulegen. Der folgende Beispielcode lädt die Quelldatei Excel wie im Screenshot oben, greift auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Standorte in die Sparkline-Gruppe ein. Schließlich schreibt er die Ausgabedatei auf die Festplatte, die auch im Screenshot oben zu sehen ist.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
