---  
title: Detener la conversión o carga usando InterruptMonitor cuando toma demasiado tiempo con Node.js vía C++  
linktitle: Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado  
type: docs  
weight: 100  
url: /es/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Aprende cómo detener la conversión de Workbook a varios formatos usando InterruptMonitor cuando toma demasiado tiempo con Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**

Aspose.Cells for Node.js via C++ te permite detener la conversión de Workbook a varios formatos como PDF, HTML, etc., usando el objeto [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) cuando tarda demasiado. El proceso de conversión es a menudo intensivo tanto en CPU como en memoria, y suele ser útil detenerlo cuando los recursos son limitados. Puedes usar [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) tanto para detener la conversión como para detener la carga de un libro grande. Por favor, usa la propiedad [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) para detener la conversión y la propiedad [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) para cargar un libro grande.

## **Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado**

El siguiente código de muestra explica el uso del objeto [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor). El código convierte un archivo de Excel bastante grande a PDF. Tomará varios segundos (es decir, *más de 30 segundos*) en convertirse debido a estas líneas de código.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Como puedes ver, **J1000000** es una celda bastante lejana en el archivo XLSX. Sin embargo, el método **waitForWhileAndThenInterrupt()** interrumpe la conversión después de 10 segundos y termina el programa. Usa el siguiente código para ejecutar el ejemplo.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Código de muestra**

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

