---  
title: Interrompi la conversione o il caricamento usando InterruptMonitor quando impiega troppo tempo con Node.js tramite C++  
linktitle: Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando ci vuole troppo tempo  
type: docs  
weight: 100  
url: /it/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Impara come fermare la conversione di Workbook in vari formati usando InterruptMonitor quando impiega troppo tempo con Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**

Aspose.Cells for Node.js via C++ permette di fermare la conversione di Workbook in vari formati come PDF, HTML ecc. usando l'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) quando richiede troppo tempo. Il processo di conversione è spesso intensivo sia in CPU che in memoria ed è spesso utile interromperlo quando le risorse sono limitate. Puoi usare [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) sia per fermare la conversione che per fermare il caricamento di grandi workbook. Usa la proprietà [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) per fermare la conversione e [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) per il caricamento di grandi workbook.

## **Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo**

Il seguente codice di esempio illustra l'uso dell'oggetto [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor). Il codice converte un file Excel abbastanza grande in PDF. Ci vorranno diversi secondi (più di 30 secondi) per completare la conversione a causa di queste righe di codice.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Come puoi vedere, **J1000000** è una cella abbastanza lontana nel file XLSX. Tuttavia, il metodo **waitForWhileAndThenInterrupt()** interrompe la conversione dopo 10 secondi e il programma termina/si interrompe. Usa il seguente codice per eseguire l'esempio.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Codice di Esempio**

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

