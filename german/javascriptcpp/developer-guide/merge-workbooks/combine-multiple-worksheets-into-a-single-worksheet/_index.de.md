---
title: Mehrere Arbeitsblätter in einem einzigen Arbeitsblatt mit JavaScript via C++ zusammenfassen
linktitle: Mehrere Arbeitsblätter zu einem einzigen Arbeitsblatt zusammenfassen
type: docs
weight: 160
url: /de/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Lernen Sie, wie Sie mit Aspose.Cells for JavaScript via C++ mehrere Arbeitsblätter in ein einzelnes zusammenfassen. 
---

{{% alert color="primary" %}} 

Manchmal müssen mehrere Arbeitsblätter in einem einzigen Arbeitsblatt zusammengeführt werden. Dies kann einfach über die Aspose.Cells API erreicht werden. In diesem Artikel wird Ihnen ein Codebeispiel gezeigt, das eine Quellarbeitsmappe liest und die Daten aller Quellarbeitsblätter in einem Zieltabellenblatt innerhalb einer Ziellarbeitsmappe zusammenführt.

{{% /alert %}} 

Der folgende Code-Schnipsel zeigt Ihnen, wie Sie mehrere Arbeitsblätter in ein einziges Arbeitsblatt kombinieren können.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Worksheets into One Workbook</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const destWorkbook = new Workbook();
            const destSheet = destWorkbook.worksheets.get(0);

            let TotalRowCount = 0;

            for (let i = 0; i < workbook.worksheets.count; i++) {
                const sourceSheet = workbook.worksheets.get(i);

                const sourceRange = sourceSheet.cells.maxDisplayRange;
                const destRange = destSheet.cells.createRange(
                    sourceRange.firstRow + TotalRowCount,
                    sourceRange.firstColumn,
                    sourceRange.rowCount,
                    sourceRange.columnCount
                );

                destRange.copy(sourceRange);
                TotalRowCount += sourceRange.rowCount;
            }

            const outputData = destWorkbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook merged successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
