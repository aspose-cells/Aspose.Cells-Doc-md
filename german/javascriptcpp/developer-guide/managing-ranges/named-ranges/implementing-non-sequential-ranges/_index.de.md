---
title: Implementierung von nicht sequenziellen Bereichen mit JavaScript via C++
linktitle: Implementieren von nicht sequentiellen Bereich
type: docs
weight: 700
url: /de/javascript-cpp/implementing-non-sequential-ranges/
description: Lernen Sie, wie man benannte nicht sequenzielle Bereiche mit Aspose.Cells for JavaScript via C++ erstellt. Verwenden Sie effektiv nicht angrenzende Zellbereiche.
---

{{% alert color="primary" %}} 

Normalerweise sind benannte Bereiche rechteckig mit zusammenhängenden und benachbarten Zellen. Manchmal müssen Sie jedoch einen nicht-sequenziellen Zellbereich verwenden, bei dem die Zellen nicht benachbart sind. Aspose.Cells for JavaScript via C++ unterstützt die Erstellung eines benannten Bereichs mit nicht-benachbarten Zellen.

{{% /alert %}} 

Das folgende Codebeispiel zeigt, wie man mit Aspose.Cells for JavaScript via C++ einen benannten nicht-sequenziellen Bereich erstellt.


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
