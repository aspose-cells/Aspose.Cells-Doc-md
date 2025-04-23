---  
title: Abbruch der Konvertierung oder des Ladens mittels InterruptMonitor, wenn es zu lange dauert mit Node.js via C++  
linktitle: Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert  
type: docs  
weight: 100  
url: /de/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Lernen, wie man die Konvertierung des Arbeitsbuchs in verschiedene Formate bei längerer Dauer mit InterruptMonitor stoppt, mit Aspose.Cells for Node.js via C++.  
---  

## **Mögliche Verwendungsszenarien**

Aspose.Cells for Node.js via C++ ermöglicht es, die Konvertierung eines Arbeitsbuchs in verschiedene Formate wie PDF, HTML usw. beim langen Dauer mit dem [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor)-Objekt zu stoppen. Der Konvertierungsprozess ist oft CPU- und speicherintensiv und es ist oft nützlich, ihn bei begrenzten Ressourcen zu unterbrechen. Sie können [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) sowohl zum Stoppen der Konvertierung als auch zum Laden großer Arbeitsbücher verwenden. Bitte verwenden Sie die [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--)-Eigenschaft zum Stoppen der Konvertierung und die [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--)-Eigenschaft zum Laden großer Arbeitsbücher.

## ** Konvertierung oder Laden mit InterruptMonitor stoppen, wenn es zu lange dauert**

Der folgende Beispielscode erläutert die Verwendung des [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor)-Objekts. Der Code konvertiert eine ziemlich große Excel-Datei in PDF. Es dauert einige Sekunden (d.h. *mehr als 30 Sekunden*), um sie zu konvertieren, aufgrund dieser Codezeilen.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Wie Sie sehen, **J1000000** ist eine ziemlich entfernte Zelle in der XLSX-Datei. Die Methode **waitForWhileAndThenInterrupt()** unterbricht die Konvertierung nach 10 Sekunden und das Programm endet/beendet. Bitte verwenden Sie den folgenden Code, um den Beispiels-Code auszuführen.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Beispielcode**

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

