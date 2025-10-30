---
title: Slå ihop eller upplös cellområde med JavaScript via C++
linktitle: Slå samman eller dela upp cellintervall
type: docs
weight: 190
url: /sv/javascript-cpp/merge-or-unmerge-range-of-cells/
description: Sammanfoga och avsammanfoga celler i ett område i Excel med JavaScript via C++ kod.
keywords: JavaScript sammanslå och avsammanslå celler i ett område, JavaScript sammanslå och avsammanslå celler i område, sammanslå och avsammanslå celler i område med JavaScript, sammanslå och avsammanslå celler i område med JavaScript, sammanslå och avsammanslå celler i excel med JavaScript, sammanslå och avsammanslå celler i excel med JavaScript, JavaScript sammanslå och avsammanslå celler i excel, JavaScript sammanslår celler i excel, JavaScript avsammanslår celler i excel, sammanfoga celler i område med JavaScript
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att slå samman eller dela upp ett cellintervall. Aspose.Cells tillhandahåller [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) och [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) metoder för detta ändamål. Denna artikel förklarar hur man slår samman ett cellintervall till en enda cell.

{{% /alert %}}

## **Exempel**

Följande exempel skapar först ett område - A1:D4 - och fusionerar sedan cellerna i området till en enda cell med hjälp av [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--)-metoden. På liknande sätt kan du dela upp celler genom att skapa ett område och använda [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--)-metoden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create and Merge Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeInitialized = false;
        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeInitialized = true;
            runButton.disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait.</p>';
                return;
            }

            // Creating a workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range
            const range = worksheet.cells.createRange("A1:D4");

            // Merge range into a single cell
            range.merge();

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range merged successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
