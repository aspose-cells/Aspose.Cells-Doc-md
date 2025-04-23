---  
title: 当转换或加载耗时过长时，可以使用 Node.js 通过 C++ 的 InterruptMonitor 来中断操作。  
linktitle: 在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: 学习如何在耗时过长时，使用 Aspose.Cells for Node.js via C++ 的 InterruptMonitor 停止工作簿转换到各种格式（如 PDF、HTML 等）。  
---  

## **可能的使用场景**

Aspose.Cells for Node.js via C++ 允许您在转换过程中，使用 [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) 对象停止工作簿到各种格式的转换，例如 PDF、HTML 等。当转换过程常常既占用 CPU 又占用内存时，限定资源时中止操作非常有用。可以用 [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) 来停止转换，也可以停止加载大型工作簿。请使用 [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) 属性停止转换，[**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) 属性停止加载大型工作簿。

## **在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载**

以下示例代码解释了使用 [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) 对象的用法。该代码将大型Excel文件转换为PDF。由于这些代码行的原因，转换需要几秒钟（即*超过30秒*）。

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

如你所见，**J1000000** 在 XLSX 文件中是一个较远的单元格。然而，**waitForWhileAndThenInterrupt()** 方法在 10 秒后中断转换，程序结束/终止。请使用以下代码运行示例。

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **示例代码**

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

