---
title: JavaScriptをC++経由で使用して、処理に時間がかかりすぎるときにInterruptMonitorを使用して変換または読み込みを停止する
linktitle: 時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください
type: docs
weight: 100
url: /ja/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Aspose.Cells for JavaScriptをC++で使用して、処理に時間がかかりすぎるときにワークブックの変換を停止する方法を学ぶ
---

## **可能な使用シナリオ**

Aspose.Cells for JavaScriptをC++で使用して、[**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor)オブジェクトを使用して、処理に時間がかかりすぎるときにワークブックの変換を停止したり、HTMLやPDFなどさまざまなフォーマットへの変換を停止したりできます。変換処理はCPUとメモリの両方を多く消費することが多いため、リソースが限られているときに停止するのが有効です。変換停止には [**Workbook.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#interruptMonitor--) プロパティ、ファイルの読み込み停止には [**LoadOptions.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor--) プロパティを使用してください。

## **時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください**

次のサンプルコードでは、[**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor)オブジェクトの使用方法について説明しています。多大なExcelファイルをPDFに変換します。このコードは、これらのコードの行のために変換が数秒かかります（すなわち*30秒以上*）。

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.cells.get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

【CSV】のセル**J1000000**はXLSXファイルではかなり遠いセルです。しかし、**waitForWhileAndThenInterrupt()**メソッドは10秒後に変換を中断し、プログラムは終了します。こちらのコードを使ってサンプルコードを実行してください。

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **サンプルコード**

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
