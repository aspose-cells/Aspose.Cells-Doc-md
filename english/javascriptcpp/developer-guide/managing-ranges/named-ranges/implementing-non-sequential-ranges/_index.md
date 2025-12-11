---
title: Implementing Non-Sequential Ranges with JavaScript via C++
linktitle: Implementing Non-Sequential Ranges
type: docs
weight: 700
url: /javascript-cpp/implementing-non-sequential-ranges/
description: Learn how to create named non‑sequential ranges with Aspose.Cells for JavaScript via C++. Use non‑adjacent cell ranges effectively.
---

{{% alert color="primary" %}} 

Normally, named ranges are rectangular with cells continuous and adjacent to each other. But sometimes, you may need to use a non‑sequential cell range in which cells are not adjacent. Aspose.Cells for JavaScript via C++ supports creating a named range with non‑adjacent cells.

{{% /alert %}} 

The code sample below shows how to create a named non‑sequential range with Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add NonSequenced Range Name</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a name for a non‑sequenced range
            const index = workbook.worksheets.names.add("NonSequencedRange");

            const name = workbook.worksheets.names.get(index);

            // Creating a non‑sequenced range of cells
            name.refersTo = "=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6";

            // Saving the workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and name added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```