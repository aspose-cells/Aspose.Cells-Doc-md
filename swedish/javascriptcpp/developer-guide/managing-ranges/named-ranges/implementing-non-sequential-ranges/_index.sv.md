---
title: Implementera icke sekventiella områden med JavaScript via C++
linktitle: Implementera icke sekventiella intervaller
type: docs
weight: 700
url: /sv/javascript-cpp/implementing-non-sequential-ranges/
description: Lär dig hur du skapar namngivna icke sekventiella områden med Aspose.Cells for JavaScript via C++. Använd icke anslutna cellområden effektivt.
---

{{% alert color="primary" %}} 

Vanligtvis är namngivna områden rektangulära med celler som är kontinuerliga och intill varandra. Men ibland kan du behöva använda ett icke-sekventiellt cellområde där cellerna inte är intill varandra. Aspose.Cells for JavaScript via C++ stöder skapande av ett namngivet område med icke-sekventiella celler.

{{% /alert %}} 

Exemplet nedan visar hur man skapar ett namngivet icke-sekventiellt område med Aspose.Cells for JavaScript via C++.


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

            // Adding a Name for non sequenced range
            const index = workbook.worksheets.names.add("NonSequencedRange");

            const name = workbook.worksheets.names.get(index);

            // Creating a non sequence range of cells
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
