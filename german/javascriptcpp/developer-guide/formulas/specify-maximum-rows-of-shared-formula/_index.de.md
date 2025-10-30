---
title: Geben Sie die maximale Zeilenanzahl der gemeinsamen Formel mit JavaScript via C++ an
linktitle: Maximale Zeilen der gemeinsamen Formel angeben
type: docs
weight: 40
url: /de/javascript-cpp/specify-maximum-rows-of-shared-formula/
description: Erfahren Sie, wie Sie die maximale Zeilenanzahl für gemeinsame Formeln mit Aspose.Cells for JavaScript via C++ festlegen.
---

## **Mögliche Verwendungsszenarien**  

Die Standard-Maximalzahl der Zeilen für gemeinsame Formeln ist 64. Es kann eine beliebige Zahl sein, z.B. 1000. Die Leistung der gemeinsamen Formel ändert sich mit unterschiedlicher Zeilenanzahl. Daher bietet Aspose.Cells die Eigenschaft [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--), um die maximale Zeilenanzahl für die gemeinsame Formel festzulegen. Die gemeinsame Formel wird in mehrere gemeinsame Formeln aufgeteilt, wenn die Gesamtzahl der Zeilen der gemeinsamen Formel größer ist als diese Zahl, wie im folgenden Screenshot gezeigt.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Maximale Zeilen der gemeinsamen Formel angeben**  

Der folgende Beispielcode erklärt die Verwendung der Eigenschaft [**WorkbookSettings.maxRowsOfSharedFormula**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRowsOfSharedFormula--). Er setzt die maximale Zeilenanzahl der gemeinsamen Formel auf 5 und fügt die gemeinsame Formel in Zelle D1 für 100 Zeilen ein und speichert sie in [Ausgabedatei] (61767856.xlsx). Wenn Sie den Inhalt der Ausgabedatei extrahieren und die *sheet1.xml* überprüfen, sehen Sie, wie die gemeinsame Formel alle 5 Zeilen aufgesplittet wird, wie im oberen Screenshot hervorgehoben.  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Maximum Rows Of Shared Formula Example</title>
    </head>
    <body>
        <h1>Specify Maximum Rows Of Shared Formula Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Set the max rows of shared formula to 5
            workbook.settings.maxRowsOfSharedFormula = 5;

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access cell D1
            const cell = ws.cells.get("D1");

            // Set the shared formula in 100 rows
            cell.sharedFormula = ["=Sum(A1:A2)", 100, 1];

            // Save the output Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyMaximumRowsOfSharedFormula.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
