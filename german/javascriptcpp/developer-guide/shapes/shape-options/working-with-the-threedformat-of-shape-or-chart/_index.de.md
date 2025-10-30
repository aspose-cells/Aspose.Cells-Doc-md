---
title: Arbeiten mit dem ThreeDFormat von Shape oder Chart mit JavaScript via C++
linktitle: Arbeiten mit dem 3D Format von Form oder Diagramm
type: docs
weight: 250
url: /de/javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells for JavaScript via C++ bietet die Eigenschaft [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) zusammen mit der Klasse [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat), um mit dem 3D-Format von Formen oder Diagrammen zu arbeiten. Die Klasse [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) enthält verschiedene Eigenschaften, die je nach Anwendungsanforderungen eingestellt werden können.

## **Arbeiten mit dem ThreeDFormat von Shape oder Diagramm**
Der folgende Beispielcode lädt die [Quel-Excel-Datei](5115419.xlsx) und greift auf die erste Form im ersten Arbeitsblatt zu, setzt die Untereigenschaften der Eigenschaft [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) und speichert dann die Arbeitsmappe in der [Ausgabedatei für Excel](5115410.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
