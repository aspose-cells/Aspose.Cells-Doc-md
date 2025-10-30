---
title: Bereich in einem Arbeitsblatt mit JavaScript über C++ verschieben
linktitle: Bereich von Zellen in einem Arbeitsblatt verschieben
type: docs
weight: 370
url: /de/javascript-cpp/move-range-of-cells-in-a-worksheet/
description: Lernen Sie, wie Sie einen Bereich von Zellen in einem Arbeitsblatt mit Aspose.Cells for JavaScript über C++ verschieben.
---

{{% alert color="primary" %}}
In diesem Artikel wird gezeigt, wie man einen Bereich von Zellen in einem Arbeitsblatt verschiebt.
{{% /alert %}}

## **Bereich von Zellen in einem Arbeitsblatt verschieben**
Der Beispielcode verwendet eine Vorlagendatei, um die Aufgabe zu demonstrieren.

**Die Eingabedatei**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Bitte sehen Sie die folgende generierte Datei mit dem Bereich A1:B5, der nach C1:D5 verschoben wurde.

**Die Ausgabedatei**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook object. Open the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const cells = workbook.worksheets.get(0).cells;

            const range = cells.createRange("A1", "B5");
            // move the range to right.
            range.moveTo(0, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
