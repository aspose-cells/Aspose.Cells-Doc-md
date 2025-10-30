---
title: Sammanslå filer med JavaScript via C++
linktitle: Slå samman filer
type: docs
weight: 20
url: /sv/javascript-cpp/merge-files/
---

## **Introduktion**

Aspose.Cells tillhandahåller olika metoder för att slå ihop filer. För enkla filer med data, formatering och formler kan [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-)-metoden användas för att kombinera flera arbetsböcker, och [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-)-metoden för att kopiera kalkylblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att sammanfoga kan du märka att de tar mycket systemresurser. För att undvika detta, använd den [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) statiska metoden, ett mer effektivt sätt att slå ihop flera filer.

## **Sammanslå filer med Aspose.Cells for JavaScript via C++**

Följande kodexempel visar hur man sammanfogar stora filer med [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-)-metoden. Det tar två enkla men stora filer, Book1.xls och Book2.xls. Filmerna innehåller endast formaterad data och formler.

{{% alert color="primary" %}}

Metoden [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) stöder endast sammanfogning av data, format, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte sammanfogas med denna metod. Dessutom används en cachelagrad fil för att lagra tillfälliga data för processen.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Excel Files and Rename Sheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" multiple />
        <button id="runExample">Merge and Rename Sheets</button>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length || fileInput.files.length < 2) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least two Excel files to merge.</p>';
                return;
            }

            // Read selected files into Uint8Array array
            const files = [];
            for (let i = 0; i < fileInput.files.length; i++) {
                const file = fileInput.files[i];
                const arrayBuffer = await file.arrayBuffer();
                files.push(new Uint8Array(arrayBuffer));
            }

            // Create cacheFile name and destination name (virtual in browser)
            const cacheFile = "test.txt";
            const dest = "output.xlsx";

            // Call CellsHelper.mergeFiles with file byte arrays, cacheFile name and destination name
            // Note: In the browser environment mergeFiles is expected to accept file byte arrays and return merged file bytes.
            const mergedData = CellsHelper.mergeFiles(files, cacheFile, dest);

            // Log cacheFile as in original code
            console.log(cacheFile);

            // Load the merged workbook from returned bytes
            const workbook = new Workbook(new Uint8Array(mergedData));

            // Rename sheets sequentially starting at 1
            let i = 1;
            const worksheets = workbook.worksheets;
            for (let j = 0; j < worksheets.count; j++) {
                worksheets.get(j).name = `Sheet1${i}`;
                i++;
            }

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged and Renamed Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Files merged and sheets renamed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
