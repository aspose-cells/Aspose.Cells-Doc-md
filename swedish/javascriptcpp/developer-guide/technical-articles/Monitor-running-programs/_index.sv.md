---
title: Övervaka körande program med JavaScript via C++
linktitle: Bevaka körande program
type: docs
weight: 20
url: /sv/javascript-cpp/monitor-running-programs/
---

## **Hur du övervakar ett körande program**

Följande exempel visar hur man övervakar ett aktuellt program. Denna kod kan användas för att övervaka körning av [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/) relaterad kod. Använd enkelt [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/) klassen för att skapa ett övervakningsobjekt, använd metoden [LoadOptions.interruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor-abstractinterruptmonitor-) för att lägga till det i [LoadOptions](https://reference.aspose.com/cells/javascript-cpp/loadoptions/), och använd sedan [startMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/#startMonitor-number-) för att sätta den förväntade avbrottstiden (i millisekunder). Om den körda tiden för den övervakade koden överskrider den förväntade tiden, avbryts programmet och ett undantag kastas.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Interrupt Monitor Example</title>
    </head>
    <body>
        <h1>Interrupt Monitor Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SystemTimeInterruptMonitor, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create interrupt monitor and load options
            const monitor = new SystemTimeInterruptMonitor(false);
            const lopts = new LoadOptions();
            lopts.interruptMonitor = monitor;
            monitor.startMonitor(1000); // time limit is 1 second

            // Load the workbook with the specified load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), lopts);

            // If loading completed within time, start monitoring save
            monitor.startMonitor(1500); // time limit is 1.5 seconds
            const outputData = wb.save(SaveFormat.Xlsx);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the resulting file.</p>';
        });
    </script>
</html>
```
