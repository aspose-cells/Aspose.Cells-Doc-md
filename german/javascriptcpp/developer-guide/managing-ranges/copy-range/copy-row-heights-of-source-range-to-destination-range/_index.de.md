---
title: Zeilenhöhen des Quellbereichs in Zielbereich kopieren mit JavaScript via C++
linktitle: Quellenbereichszeilenhöhen in Zielbereich kopieren
type: docs
weight: 590
url: /de/javascript-cpp/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

Manchmal müssen Benutzer die Zeilenhöhen eines Quellbereichs in einen Zielbereich kopieren. Aspose.Cells for JavaScript via C++ bietet dazu die [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) Enumeration. Wenn Sie die Eigenschaft [**PasteOptions.pasteType**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/#pasteType--) mit [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) setzen, werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.

{{% /alert %}}

Das folgende Beispiel erklärt, wie man das [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) Enum verwendet, um die Zeilenhöhen des Quellbereichs in den Zielbereich zu kopieren. Sobald Sie die von diesem Code generierte Excel-Ausgabedatei in Microsoft Excel öffnen, werden Sie sehen, dass die Zeilenhöhen im Zielbereich genau die gleichen sind wie im Quellbereich.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Copy Row Heights Between Ranges</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PasteOptions, PasteType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            // Ensure Aspose.Cells is initialized
            await readyPromise;

            // Creating a new workbook
            const workbook = new Workbook();

            // Source worksheet (first worksheet)
            const srcSheet = workbook.worksheets.get(0);

            // Add destination worksheet
            const dstSheet = workbook.worksheets.add("Destination Sheet");

            // Set the row height of the 4th row (index 3). This row height will be copied to destination range
            srcSheet.cells.rows.get(3).height = 50;

            // Create source range to be copied
            const srcRange = srcSheet.cells.createRange("A1:D10");

            // Create destination range in destination worksheet
            const dstRange = dstSheet.cells.createRange("A1:D10");

            // PasteOptions, we want to copy row heights of source range to destination range
            const opts = new PasteOptions();
            opts.pasteType = PasteType.RowHeights;

            // Copy source range to destination range with paste options
            dstRange.copy(srcRange, opts);

            // Write informative message in cell D4 of destination worksheet
            const infoCell = dstSheet.cells.get("D4");
            infoCell.value = "Row heights of source range copied to destination range";

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
