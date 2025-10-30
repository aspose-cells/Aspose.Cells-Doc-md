---
title: Avbryt konvertering eller inläsning med InterruptMonitor om det tar för lång tid med JavaScript via C++
linktitle: Stoppa konvertering eller inläsning med avbrottsövervakning när det tar för lång tid
type: docs
weight: 100
url: /sv/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Lär dig hur du stoppar konverteringen av arbetsbok till olika format med InterruptMonitor när det tar för lång tid med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

 Aspose.Cells for JavaScript via C++ tillåter att du stoppar konverteringen av arbetsboken till olika format som PDF, HTML etc. med hjälp av [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor)-objektet när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minnesintensiv, och det är ofta användbart att stoppa den när resurserna är begränsade. Du kan använda [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) både för att stoppa konverteringen och för att stoppa laddningen av stort arbetsbok. Använd gärna [**Workbook.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#interruptMonitor--)-egenskapen för att stoppa konverteringen och [**LoadOptions.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor--)-egenskapen för att ladda en stor arbetsbok.

## **Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid**

Följande kodexempel förklarar användningen av [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) -objektet. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (det vill säga *mer än 30 sekunder*) att konvertera den på grund av dessa kodrader.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.cells.get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Som du ser **J1000000** är ganska långt cell i XLSX-filen. Dock avbryts **waitForWhileAndThenInterrupt()** metoden konverteringen efter 10 sekunder och programmet avslutas/avslutas. Vänligen använd följande kod för att köra exempel-koden.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Exempelkod**

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
