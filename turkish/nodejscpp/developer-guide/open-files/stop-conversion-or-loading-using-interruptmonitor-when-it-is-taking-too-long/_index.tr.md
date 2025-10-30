---  
title: Çevrimi durdurmak veya Node.js ve C++ ile çok uzun sürüyorsa yüklemeyi InterruptMonitor kullanarak durdurun  
linktitle: Çok uzun sürüyorsa, Durdur dönüşümü veya yüklemeyi kullanarak InterruptMonitor  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: Aspose.Cells for Node.js via C++ kullanılarak, işlemin çok uzun sürdüğü durumlarda WorkBook un çeşitli formatlara dönüştürülmesini InterruptMonitor ile nasıl durduracağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**

Aspose.Cells for Node.js via C++, çok uzun sürdüğü durumlarda [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) nesnesini kullanarak WorkBook'un çeşitli formatlara (PDF, HTML vb.) dönüştürülmesini durdurmanıza izin verir. Dönüştürme işlemi genellikle CPU ve Bellek açısından yoğundur ve kaynaklar kısıtlıysa durdurmak faydalı olur. Hem dönüştürmeyi durdurmak hem de büyük boyutlu çalışma kitabı yüklemeyi durdurmak için [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) kullanabilirsiniz. Lütfen durdurma işlemi için [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) özelliğini, büyük boyutlu çalışma kitabını yüklemek için ise [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) özelliğini kullanın.

## **Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun**

Aşağıdaki örnek kod, [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) nesnesinin kullanımını açıklar. Kod, oldukça büyük bir Excel dosyasını PDF'e dönüştürür. Bu kod satırları nedeniyle dönüştürülmesi birkaç saniye (yani, *30 saniyeden fazla*) sürecektir.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Gördüğünüz gibi **J1000000** XLSX dosyasında oldukça uzak bir hücredir. Ancak, **waitForWhileAndThenInterrupt()** yöntemi dönüşümü 10 saniye sonra durdurur ve program sona erer/sonlandırılır. Lütfen örnek kodu çalıştırmak için aşağıdaki kodu kullanın.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Örnek Kod**

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
