---  
title: Прекратить конвертацию или загрузку с помощью InterruptMonitor, если процесс занимает слишком много времени, с Node.js через C++  
linktitle: Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Узнайте, как останавливать конвертацию рабочей книги в разные форматы с помощью InterruptMonitor, если она занимает слишком много времени, с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**

Aspose.Cells for Node.js via C++ позволяет останавливать конвертацию рабочей книги в различные форматы, такие как PDF, HTML и др., с использованием объекта [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor), когда процесс затягивается. Процесс конвертации требует значительных ресурсов CPU и памяти, и его можно приостановить, когда ресурсов мало. Используйте [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) для остановки конвертации и для прерывания загрузки больших рабочих книг, а также используйте свойства [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) и [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) для завершения соответствующих процессов.

## **Прекратите преобразование или загрузку с использованием объекта InterruptMonitor, если это занимает слишком много времени**

В следующем образце кода объясняется использование объекта [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor). Код преобразует довольно большой файл Excel в PDF. Это займет несколько секунд (т.е. *более 30 секунд*) для преобразования из-за этих строк кода.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Как вы видите, **J1000000** — это довольно удаленная ячейка в файле XLSX. Однако метод **waitForWhileAndThenInterrupt()** прерывает преобразование через 10 секунд, и программа завершается. Пожалуйста, используйте следующий код для выполнения примерного кода.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class StopConversionOrLoadingUsingInterruptMonitor {
// Output directory
static outputDir = StopConversionOrLoadingUsingInterruptMonitor.getOutputDirectory();

constructor() {
// Create InterruptMonitor object
this.im = new AsposeCells.InterruptMonitor();
}

// This function will create workbook and convert it to Pdf format
async createWorkbookAndConvertItToPdfFormat(threadObj) {
const monitorThread = threadObj;

// Create a workbook object
const wb = new AsposeCells.Workbook();

// Assign it InterruptMonitor object
wb.setInterruptMonitor(this.im);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell J1000000 and add some text inside it.
const cell = ws.getCells().get("J1000000");
cell.putValue("This is text.");

try {
// Save the workbook to Pdf format
await wb.saveAsync(path.join(StopConversionOrLoadingUsingInterruptMonitor.outputDir, "output_InterruptMonitor.pdf"));

// Show successful message
console.log("Excel to PDF - Successful Conversion");

// Stop monitor thread
monitorThread.interrupt();
} catch (ex) {
if (ex.code === AsposeCells.ExceptionType.Interrupted) {
console.log("Conversion process is interrupted - Message: " + ex.message);
} else {
throw ex;
}
}
}

// This function will interrupt the conversion process after 10s
waitForWhileAndThenInterrupt() {
try {
setTimeout(() => {
this.im.interrupt();
}, 1000 * 10);
} catch (e) {
console.log("Monitor thread is interrupted - Message: " + e.message);
}
}

async testRun() {
const monitorThread = new Promise((resolve) => {
this.waitForWhileAndThenInterrupt();
resolve();
```  

