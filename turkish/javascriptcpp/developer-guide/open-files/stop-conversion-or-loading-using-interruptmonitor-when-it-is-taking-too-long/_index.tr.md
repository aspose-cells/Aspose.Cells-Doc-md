---
title: Çok zaman alan durumlarda InterruptMonitor kullanarak dönüşümü veya yüklemeyi durdurun JavaScript ve C++ kullanarak
linktitle: Çok uzun sürüyorsa, Durdur dönüşümü veya yüklemeyi kullanarak InterruptMonitor
type: docs
weight: 100
url: /tr/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Aspose.Cells for JavaScript ile C++ kullanarak, uzun sürdüğü zaman Workbook un çeşitli formatlara dönüştürülmesini InterruptMonitor ile durdurmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

 Aspose.Cells for JavaScript ile C++ kullanarak, Workbook'un PDF, HTML gibi çeşitli formatlara dönüştürmesini [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) nesnesi kullanarak durdurabilirsiniz. Dönüşüm süreci genellikle CPU ve Bellek yoğun olduğundan, kaynaklar sınırlıysa durdurmak faydalıdır. [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) hem dönüşümü durdurmak hem de büyük workbook'ları yüklemeyi durdurmak için kullanılabilir. Lütfen dönüşüm durdurmak için [**Workbook.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#interruptMonitor--) özelliğini, büyük workbook yüklemeyi durdurmak için [**LoadOptions.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor--) özelliğini kullanın.

## **Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun**

Aşağıdaki örnek kod, [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) nesnesinin kullanımını açıklar. Kod, oldukça büyük bir Excel dosyasını PDF'e dönüştürür. Bu kod satırları nedeniyle dönüştürülmesi birkaç saniye (yani, *30 saniyeden fazla*) sürecektir.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.cells.get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Gördüğünüz gibi **J1000000** XLSX dosyasında oldukça uzak bir hücredir. Ancak, **waitForWhileAndThenInterrupt()** yöntemi dönüşümü 10 saniye sonra durdurur ve program sona erer/sonlandırılır. Lütfen örnek kodu çalıştırmak için aşağıdaki kodu kullanın.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Örnek Kod**

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
