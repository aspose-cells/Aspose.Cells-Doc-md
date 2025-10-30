---
title: JavaScriptとC++を使用して、ソース範囲の行の高さを宛先範囲にコピーします
linktitle: ソース範囲の行の高さを宛先範囲にコピー
type: docs
weight: 590
url: /ja/javascript-cpp/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

時には、ユーザーがソース範囲の行の高さを宛先範囲にコピーする必要があります。Aspose.Cells for JavaScriptを用いたC++はこの目的のために[**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/)列挙型を提供します。[**PasteOptions.pasteType**](https://reference.aspose.com/cells/javascript-cpp/pasteoptions/#pasteType--) プロパティを [**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/) で設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

{{% /alert %}}

以下のサンプルコードは、[**PasteType.RowHeights**](https://reference.aspose.com/cells/javascript-cpp/pastetype/)列挙型を使用して、ソース範囲の行の高さを宛先範囲にコピーする方法を示しています。このコードで生成されたExcelファイルをMicrosoft Excelで開くと、宛先範囲の行の高さがソース範囲と完全に一致していることがわかります。

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
