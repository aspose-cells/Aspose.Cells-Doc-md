---
title: Arrêter la conversion ou le chargement en utilisant InterruptMonitor lorsqu’il prend trop de temps avec JavaScript via C++
linktitle: Arrêter la conversion ou le chargement à l aide d InterruptMonitor lorsqu elle prend trop de temps
type: docs
weight: 100
url: /fr/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Apprenez comment arrêter la conversion du classeur en divers formats en utilisant InterruptMonitor lorsqu’il prend trop de temps avec Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

 Aspose.Cells for JavaScript via C++ vous permet d’arrêter la conversion du classeur en divers formats comme PDF, HTML, etc., en utilisant l’objet [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) lorsque cela prend trop de temps. Le processus de conversion étant souvent intensif en CPU et en mémoire, il est souvent utile de l'interrompre lorsque les ressources sont limitées. Vous pouvez utiliser [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) à la fois pour arrêter la conversion et pour arrêter le chargement de gros classeurs. Veuillez utiliser la propriété [**Workbook.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#interruptMonitor--) pour arrêter la conversion et la propriété [**LoadOptions.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor--) pour arrêter le chargement d’un gros classeur.

## **Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps**

Le code d'exemple suivant explique l'utilisation de l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor). Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire *plus de 30 secondes*) pour le convertir en raison de ces lignes de code.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.cells.get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Comme vous le voyez, **J1000000** est une cellule assez éloignée dans le fichier XLSX. Cependant, la méthode **waitForWhileAndThenInterrupt()** interrompt la conversion après 10 secondes et le programme se termine/arrête. Veuillez utiliser le code suivant pour exécuter le code d'exemple.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Code d'exemple**

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
