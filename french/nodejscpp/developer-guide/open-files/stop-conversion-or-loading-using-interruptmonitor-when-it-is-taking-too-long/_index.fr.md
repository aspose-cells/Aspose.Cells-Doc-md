---  
title: Arrêtez la conversion ou le chargement à l aide d InterruptMonitor lorsqu il prend trop de temps avec Node.js via C++  
linktitle: Arrêter la conversion ou le chargement à l aide d InterruptMonitor lorsqu elle prend trop de temps  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Apprenez comment arrêter la conversion du classeur vers différents formats en utilisant InterruptMonitor lorsqu il prend trop de temps avec Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**

Aspose.Cells for Node.js via C++ vous permet d'arrêter la conversion du classeur vers différents formats tels que PDF, HTML, etc., en utilisant l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) lorsqu'elle prend trop de temps. Le processus de conversion est souvent gourmand en CPU et mémoire, il est donc utile de le suspendre lorsque les ressources sont limitées. Vous pouvez utiliser [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) à la fois pour arrêter la conversion ainsi que pour arrêter le chargement d'un grand classeur. Veuillez utiliser la propriété [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) pour arrêter la conversion et la propriété [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) pour charger un grand classeur.

## **Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps**

Le code d'exemple suivant explique l'utilisation de l'objet [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor). Le code convertit un fichier Excel assez volumineux en PDF. Cela prendra plusieurs secondes (c'est-à-dire *plus de 30 secondes*) pour le convertir en raison de ces lignes de code.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Comme vous le voyez, **J1000000** est une cellule assez éloignée dans le fichier XLSX. Cependant, la méthode **waitForWhileAndThenInterrupt()** interrompt la conversion après 10 secondes et le programme se termine/arrête. Veuillez utiliser le code suivant pour exécuter le code d'exemple.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Code d'exemple**

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
