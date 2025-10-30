---
title: Angabe der signifikanten Ziffern, die in Excel Datei mit JavaScript via C++ gespeichert werden sollen
linktitle: Angabe von signifikanten Ziffern, die in der Excel Datei gespeichert werden sollen
type: docs
weight: 30
url: /de/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Lernen Sie, wie Sie die signifikanten Ziffern für eine Excel Datei mit Aspose.Cells for JavaScript via C++ festlegen.
---

## **Mögliche Verwendungsszenarien**  

Standardmäßig speichert Aspose.Cells for JavaScript via C++ 17 signifikante Ziffern von Double-Werten in der Excel-Datei, im Gegensatz zu MS-Excel, das nur 15 signifikante Ziffern speichert. Sie können das Standardverhalten von Aspose.Cells von 17 auf 15 signifikante Ziffern mit der [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--)-Eigenschaft ändern.  

## **Angabe von signifikanten Ziffern, die in der Excel-Datei gespeichert werden sollen**  

Der folgende Beispielcode erzwingt, dass Aspose.Cells 15 signifikante Ziffern beim Speichern von Double-Werten in der Excel-Datei verwendet. Überprüfen Sie die [Ausgabedatei](22774105.xlsx). Ändern Sie die Erweiterung auf .zip, entpacken Sie sie und Sie sehen, dass nur 15 signifikante Ziffern in der Excel-Datei gespeichert sind. Die folgende Abbildung zeigt die Wirkung der [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--)-Eigenschaft auf die Ausgabedatei.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
