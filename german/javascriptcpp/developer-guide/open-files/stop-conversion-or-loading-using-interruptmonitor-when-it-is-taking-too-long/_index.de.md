---
title: Unterbrechen der Konvertierung oder des Ladens mit InterruptMonitor, wenn es zu lange dauert, mit JavaScript über C++
linktitle: Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert
type: docs
weight: 100
url: /de/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Lernen Sie, wie Sie die Konvertierung einer Arbeitsmappe in verschiedene Formate mit InterruptMonitor stoppen, wenn es zu lange dauert, mit Aspose.Cells for JavaScript über C++.
---

## **Mögliche Verwendungsszenarien**

 Die Aspose.Cells for JavaScript API über C++ ermöglicht es, die Konvertierung der Arbeitsmappe in verschiedene Formate wie PDF, HTML usw. mit dem Objekt [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) zu stoppen, wenn sie zu lange dauert. Der Konvertierungsprozess ist oft sowohl CPU- als auch speicherintensiv, und es ist oft nützlich, ihn bei begrenzten Ressourcen abzubrechen. Sie können [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) sowohl zum Stoppen der Konvertierung als auch zum Stoppen des Ladens großer Arbeitsmappen verwenden. Bitte verwenden Sie [**Workbook.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#interruptMonitor--), um die Konvertierung zu stoppen, und [**LoadOptions.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor--) für das Laden großer Arbeitsmappen.

## ** Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert**

Der folgende Beispielscode erläutert die Verwendung des [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor)-Objekts. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert einige Sekunden (d.h. *mehr als 30 Sekunden*), um sie zu konvertieren, aufgrund dieser Codezeilen.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.cells.get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Wie Sie sehen, **J1000000** ist eine ziemlich entfernte Zelle in der XLSX-Datei. Die Methode **waitForWhileAndThenInterrupt()** unterbricht die Konvertierung nach 10 Sekunden und das Programm endet/beendet. Bitte verwenden Sie den folgenden Code, um den Beispiels-Code auszuführen.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Stop Conversion Using InterruptMonitor Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, InterruptMonitor } = AsposeCells;

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

        class StopConversionOrLoadingUsingInterruptMonitor {
            static outputDir = "output"; // browser uses filename directly

            constructor() {
                // Create InterruptMonitor object
                this.im = new InterruptMonitor();
                this._timeoutId = null;
            }

            // This function will create workbook and convert it to Pdf format
            async createWorkbookAndConvertItToPdfFormat(monitorThread, fileUint8Array) {
                // Create a workbook object
                let wb;
                if (fileUint8Array) {
                    // Opening the Excel file through the file stream
                    wb = new Workbook(fileUint8Array);
                } else {
                    wb = new Workbook();
                }

                // Assign it InterruptMonitor object
                wb.interruptMonitor = this.im;

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Access cell J1000000 and add some text inside it.
                const cell = ws.cells.get("J1000000");
                cell.value = "This is text.";

                // Save the workbook to Pdf format (async) and provide download
                const outputData = await wb.saveAsync(SaveFormat.Pdf);
                const blob = new Blob([outputData], { type: "application/pdf" });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output_InterruptMonitor.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Excel to PDF - Successful Conversion. Click the download link to get the PDF file.</p>';

                // Stop monitor thread (clear scheduled interrupt)
                if (monitorThread && typeof monitorThread.interrupt === 'function') {
                    monitorThread.interrupt();
                }
            }

            // This function will interrupt the conversion process after 10s
            waitForWhileAndThenInterrupt() {
                // schedule an interrupt after 10 seconds
                this._timeoutId = setTimeout(() => {
                    this.im.interrupt();
                }, 1000 * 10);

                // return a monitorThread object that can cancel the scheduled interrupt
                return {
                    interrupt: () => {
                        if (this._timeoutId !== null) {
                            clearTimeout(this._timeoutId);
                            this._timeoutId = null;
                        }
                    }
                };
            }

            async testRun(fileUint8Array) {
                const monitorThread = this.waitForWhileAndThenInterrupt();
                await this.createWorkbookAndConvertItToPdfFormat(monitorThread, fileUint8Array);
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            // Basic input validation: proceed even if no file (will create a new workbook)
            let fileUint8Array = null;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                fileUint8Array = new Uint8Array(arrayBuffer);
            }

            const example = new StopConversionOrLoadingUsingInterruptMonitor();
            // Let errors propagate (no try-catch) as required
            await example.testRun(fileUint8Array);
        });
    </script>
</html>
```
