---  
title: Stop conversion or loading using InterruptMonitor when it is taking too long with Node.js via C++  
linktitle: Stop conversion or loading using InterruptMonitor when it is taking too long  
type: docs  
weight: 100  
url: /nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Learn how to stop the conversion of Workbook to various formats using InterruptMonitor when it is taking too long with Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**

Aspose.Cells for Node.js via C++ allows you to stop the conversion of Workbook to various formats like PDF, HTML, etc. using the [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) object when it is taking too long. The conversion process is often both CPU- and memory‑intensive, and it is useful to halt it when resources are limited. You can use [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) both for stopping conversion as well as for stopping the loading of a huge workbook. Please use [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) property for stopping conversion and [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) property for loading a huge workbook.

## **Stop conversion or loading using InterruptMonitor when it is taking too long**

The following sample code explains the usage of [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) object. The code converts quite a large Excel file to PDF. It will take several seconds (i.e. *more than 30 seconds*) to get it converted because of these lines of code.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

As you can see, **J1000000** is a far cell in the XLSX file. However, the **waitForWhileAndThenInterrupt()** method interrupts the conversion after 10 seconds and the program ends/terminates. Please use the following code to run the sample.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Sample Code**

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

// Assign it the InterruptMonitor object
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
