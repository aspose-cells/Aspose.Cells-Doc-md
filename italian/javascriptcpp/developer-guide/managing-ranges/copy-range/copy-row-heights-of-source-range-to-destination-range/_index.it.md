---
title: Copia altezza delle righe dell intervallo sorgente nell intervallo destinazione con JavaScript tramite C++
linktitle: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione
type: docs
weight: 590
url: /it/javascript-cpp/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

A volte gli utenti hanno bisogno di copiare le altezze delle righe di un intervallo sorgente in un intervallo di destinazione. Aspose.Cells for JavaScript tramite C++ fornisce l'`enum` [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) per questo scopo. Quando imposti la proprietà [**PasteOptions.pasteType**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/#pasteType--) con [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/), le altezze di tutte le righe all'interno dell'intervallo sorgente verranno copiate nell'intervallo di destinazione.

{{% /alert %}}

Il seguente esempio di codice spiega come usare l'enumerazione [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) per copiare le altezze delle righe dall'intervallo di origine a quello di destinazione. Quando apri il file Excel generato da questo codice in Microsoft Excel, vedrai che le altezze delle righe dell'intervallo di destinazione sono esattamente uguali a quelle dell'intervallo di origine.

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
