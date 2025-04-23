---  
title: إيقاف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً مع Node.js عبر C++  
linktitle: توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/  
description: تعلم كيفية إيقاف تحويل دفتر العمل إلى صيغ مختلفة باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً مع Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**

يتيح لك Aspose.Cells for Node.js via C++ إيقاف تحويل دفتر العمل إلى صيغ مختلفة مثل PDF و HTML باستخدام كائن [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) عندما يستغرق وقتًا طويلاً. غالبًا ما يكون عملية التحويل مكثفة من حيث CPU والذاكرة ومن المفيد غالبًا وقفها عندما تكون الموارد محدودة. يمكنك استخدام [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor) لوقف التحويل وأيضًا لإيقاف تحميل دفتر عمل ضخم. يرجى استخدام الخاصية [**Workbook.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getInterruptMonitor--) لإيقاف التحويل والخاصية [**LoadOptions.getInterruptMonitor()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getInterruptMonitor--) لوقف تحميل دفتر العمل الضخم.

## **توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

يشرح الكود العينة التالي استخدام كائن [**InterruptMonitor**](https://reference.aspose.com/cells/nodejs-cpp/interruptmonitor). يحول الكود ملف إكسل كبير إلى PDF. سيستغرق عدة ثوانٍ (أي *أكثر من 30 ثانية*) لتحويله بسبب هذه الأسطر من الكود.

{{< highlight javascript >}}

// Access cell J1000000 and add some text inside it.

let cell = ws.getCells().get("J1000000");

cell.putValue("This is text.");

{{< /highlight >}}

كما ترى **J1000000** هو خلية بعيدة جدًا في ملف XLSX. ومع ذلك، توقف طريقة **waitForWhileAndThenInterrupt()** التحويل بعد 10 ثوانٍ وتنتهي/تُنهى البرنامج. يرجى استخدام الشفرة التالية لتنفيذ الشفرة النموذجية.

{{< highlight javascript >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **الكود المثالي**

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

