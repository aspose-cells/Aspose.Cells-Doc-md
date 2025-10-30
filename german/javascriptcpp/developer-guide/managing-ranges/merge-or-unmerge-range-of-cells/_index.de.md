---
title: Zellenbereich zusammenfügen oder entkoppeln mit JavaScript via C++
linktitle: Bereich von Zellen zusammenführen oder trennen
type: docs
weight: 190
url: /de/javascript-cpp/merge-or-unmerge-range-of-cells/
description: Zellen in einem Bereich in Excel mit JavaScript über C++ Code zusammenführen und trennen.
keywords: JavaScript Zellen in einem Bereich zusammenführen und trennen, JavaScript Zellen im Bereich zusammenführen und trennen, Zellen im Bereich mit JavaScript zusammenführen und trennen, Zellen in Excel mit JavaScript zusammenführen und trennen, Zellen in Excel mit JavaScript zusammenführen und trennen, JavaScript Zellen in Excel zusammenführen und trennen, JavaScript Zellen in Excel zusammenführen, JavaScript Zellen in Excel trennen, Zellen im Bereich mit JavaScript zusammenführen
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um einen Bereich von Zellen zusammenzuführen oder aufzuteilen. Aspose.Cells bietet die Methoden [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) und [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) für diesen Zweck. Dieser Artikel erklärt, wie Sie einen Bereich von Zellen in eine einzige Zelle zusammenführen können.

{{% /alert %}}

## **Beispiel**

Der folgende Beispielcode erstellt zuerst einen Bereich - A1:D4 - und führt dann die Zellen im Bereich mit der [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--)-Methode zusammen. Ebenso können Sie Zellen aufteilen, indem Sie einen Bereich erstellen und die [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--)-Methode aufrufen.

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
