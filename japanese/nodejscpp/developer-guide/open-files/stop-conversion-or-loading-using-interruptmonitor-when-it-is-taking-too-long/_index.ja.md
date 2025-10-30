---  
title: Node.js経由のC++を使ったInterruptMonitorによる変換や読み込みの停止  
linktitle: 時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: 作業ブックの変換を長時間かかる場合にInterruptMonitorを使って停止する方法について学びます Aspose.Cells for Node.js via C++。  
---  

## **可能な使用シナリオ**

Aspose.Cells for Node.js via C++は、変換に時間がかかる場合に[**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor)オブジェクトを使用してPDF、HTMLなどの様々な形式への変換を停止できます。変換プロセスはCPUとメモリを大量に使用しますが、リソースが限られている場合はこれを停止することが有効です。変換停止には[**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor)を、巨大なブックの読み込み停止には[**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--)プロパティを使用してください。保存の停止には[**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--)プロパティを使用してください。

## **時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください**

次のサンプルコードでは、[**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor)オブジェクトの使用方法について説明しています。多大なExcelファイルをPDFに変換します。このコードは、これらのコードの行のために変換が数秒かかります（すなわち*30秒以上*）。

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

【CSV】のセル**J1000000**はXLSXファイルではかなり遠いセルです。しかし、**waitForWhileAndThenInterrupt()**メソッドは10秒後に変換を中断し、プログラムは終了します。こちらのコードを使ってサンプルコードを実行してください。

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **サンプルコード**

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

{{< app/cells/assistant language="nodejs-cpp" >}}
