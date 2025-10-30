---
title: Zellenausrichtung ändern und bestehendes Format beibehalten
linktitle: Zellenausrichtung ändern und bestehendes Format beibehalten
description: Verwenden Sie die Aspose.Cells Bibliothek, um die Zellenausrichtung zu ändern und das vorhandene Format beizubehalten, JavaScript via C++
keywords: Aspose.Cells, JavaScript via C++, Zellenausrichtung, vorhandenes Format beibehalten
type: docs
weight: 340
url: /de/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Mögliche Verwendungsszenarien**

 Manchmal möchten Sie die Ausrichtung mehrerer Zellen ändern, dabei aber das bestehende Format beibehalten. Aspose.Cells for JavaScript via C++ ermöglicht dies mit der Methode [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-). Wenn Sie es auf **true** setzen, erfolgen Änderungen in der Ausrichtung, andernfalls nicht. Bitte beachten Sie, dass das Objekt [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) als Parameter an die [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-) Methode übergeben wird, die die Formatierung auf einen Zellbereich anwendet.

## **Zellenausrichtung ändern und vorhandenes Format beibehalten**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338585.xlsx), erstellt den Bereich und zentriert ihn horizontal und vertikal und behält das vorhandene Format bei. Der folgende Screenshot vergleicht die Beispiel-Excel-Datei und die [Ausgabedatei](67338586.xlsx) und zeigt, dass das gesamte vorhandene Format der Zellen gleich bleibt, außer dass die Zellen jetzt horizontal und vertikal zentriert sind.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
