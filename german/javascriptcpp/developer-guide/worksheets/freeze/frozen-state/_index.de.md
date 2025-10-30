---
title: Wie man den eingefrorenen Zustand ohne Excel mit JavaScript via C++ überprüft
linktitle: Einfrierungsstatus
type: docs
weight: 190
url: /de/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: In diesem Artikel erfahren Sie, wie Sie den eingefrorenen Zustand eines Excel Arbeitsblattes programmatisch mit JavaScript und der C++ Bibliothek prüfen.
---

## **Einführung**

In diesem Artikel lernen wir, wie man den eingefrorenen Zustand eines Excel-Arbeitsblattes programmatisch prüft. Wir können einfach feststellen, ob das Arbeitsblatt eingefroren oder aufgeteilt ist in MS Excel. Gibt es jedoch eine Möglichkeit, ob es eingefroren oder aufgeteilt ist, mit JavaScript zu erkennen? Wir können es einfach mit Aspose.Cells for JavaScript via C++ machen.

## **Sind Fensterscheiben eingefroren?**
Mit Aspose.Cells for JavaScript via C++ können wir prüfen, ob das Fenster eingefroren ist und wie viele Zeilen und Spalten gesperrt sind.

Bitte verwenden Sie die Eigenschaft [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--), um den Zustand der Fensterscheiben zu überprüfen, und erhalten Sie gesperrte Zeilen und Spalten mit der Eigenschaft [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--).
1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Überprüfen Sie, ob das Arbeitsblatt eingefroren ist.
3. Die gesperrten Zeilen und Spalten abrufen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
