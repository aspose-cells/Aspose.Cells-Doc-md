---
title: Zeilen oder Spalten mit JavaScript via C++ entsperren
linktitle: Fenster fixieren
type: docs
weight: 190
url: /de/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In diesem Artikel lernen Sie, wie Sie Zeilen, Spalten oder Bereiche von Excel Tabellen programmatisch mit der JavaScript API und C++ entsperren.
keywords: Bereiche entsperren, Zeilen entsperren, Spalten entsperren, Fenster entsperren JavaScript via C++.
---

## **Einführung**

In diesem Artikel lernen wir, wie man Zeilen, Spalten und Bereiche aufhebt. Wenn Tabellen in Excel eingefroren sind, möchten wir manchmal die Sperre aufheben oder eingefrorene Zeilen, Spalten oder Bereiche anpassen.


## **In Excel**

1. Klicken Sie auf die Registerkarte Ansicht > Fenster fixieren > Fenster nicht fixieren.

**![Fenster nicht fixieren in Excel](Unfreeze-Panes.png)**




## **Zeilen, Spalten oder Bereiche mit Aspose.Cells for JavaScript via C++ entsperren**
Das Entsperren von Bereichen mit Aspose.Cells for JavaScript via C++ ist einfach. Bitte verwenden Sie die [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--) Methode, um Bereiche zu entsperren.

1. Arbeitsmappe erstellen, um die gefrorene Datei zu öffnen.
2. Bereiche mit der Methode Worksheet.unFreezePanes() entsperren.
3. Die Datei speichern.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Angehängte [Beispiel-Excel-Quelldatei](Frozen.xlsx).
