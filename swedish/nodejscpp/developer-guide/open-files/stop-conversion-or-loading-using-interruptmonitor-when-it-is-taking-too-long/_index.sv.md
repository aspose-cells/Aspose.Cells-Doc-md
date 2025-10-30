---  
title: Stoppa konvertering eller laddning med InterruptMonitor när det tar för lång tid med Node.js via C++  
linktitle: Stoppa konvertering eller inläsning med avbrottsövervakning när det tar för lång tid  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Lär dig hur man stoppar konverteringen av arbetsböcker till olika format med InterruptMonitor när det tar för lång tid med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**

Aspose.Cells for Node.js via C++ tillåter dig att stoppa konverteringen av arbetsböcker till olika format som PDF, HTML etc. med hjälp av [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor)-objektet när det tar för lång tid. Konverteringsprocessen är ofta både CPU- och minnesintensiv, och det är ofta användbart att stoppa den när resurser är begränsade. Du kan använda [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) för att stoppa konverteringen samt för att stoppa laddningen av stora arbetsböcker. Använd [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--)-egenskapen för att stoppa konverteringen och [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--)-egenskapen för att ladda stora arbetsböcker.

## **Stoppa konvertering eller laddning med hjälp av InterruptMonitor när det tar för lång tid**

Följande kodexempel förklarar användningen av [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) -objektet. Koden konverterar en ganska stor Excel-fil till PDF. Det tar flera sekunder (det vill säga *mer än 30 sekunder*) att konvertera den på grund av dessa kodrader.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Som du ser **J1000000** är ganska långt cell i XLSX-filen. Dock avbryts **waitForWhileAndThenInterrupt()** metoden konverteringen efter 10 sekunder och programmet avslutas/avslutas. Vänligen använd följande kod för att köra exempel-koden.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Exempelkod**

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
