---
title: Прекращение конвертации или загрузки с помощью InterruptMonitor, если процесс занимает слишком много времени с помощью JavaScript через C++
linktitle: Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени
type: docs
weight: 100
url: /ru/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Узнайте, как остановить преобразование рабочей книги в различные форматы с помощью InterruptMonitor, если оно занимает слишком много времени с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Aspose.Cells for JavaScript через C++ позволяет остановить преобразование рабочей книги в различные форматы, такие как PDF, HTML и другие, используя объект [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor), когда оно занимает слишком много времени. Процесс преобразования часто является интенсивным по CPU и памяти, и имеет смысл останавливать его при ограниченных ресурсах. Вы можете использовать [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor) как для остановки преобразования, так и для остановки загрузки большого файла. Пожалуйста, используйте свойство [**Workbook.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#interruptMonitor--) для остановки преобразования и свойство [**LoadOptions.interruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor--) для загрузки большого файла.

## **Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени**

В следующем образце кода объясняется использование объекта [**InterruptMonitor**](https://reference.aspose.com/cells/javascript-cpp/interruptmonitor). Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т.е. *более 30 секунд*) для преобразования из-за этих строк кода.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.cells.get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Как вы видите, **J1000000** — это довольно удаленная ячейка в файле XLSX. Однако метод **waitForWhileAndThenInterrupt()** прерывает преобразование через 10 секунд, и программа завершается. Пожалуйста, используйте следующий код для выполнения примерного кода.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Образец кода**

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
