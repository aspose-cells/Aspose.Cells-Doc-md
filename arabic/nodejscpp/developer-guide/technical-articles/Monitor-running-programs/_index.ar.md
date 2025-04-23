---  
title: مراقبة البرامج التي تعمل باستخدام Node.js عبر C++  
linktitle: مراقبة البرامج الجارية  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/monitor-running-programs/  
---  

## **كيفية مراقبة برنامج جاري**

يعرض رمز النموذج التالي كيفية مراقبة برنامج قيد التشغيل. يمكن استخدام هذا الرمز لمراقبة تشغيل كود [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/). ببساطة استخدم فئة [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) لإنشاء كائن مراقبة، واستخدم وظيفة [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor/) لإضافته إلى معلمات التشغيل الخاصة بـ [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/)، ثم استخدم وظيفة [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) لتعيين وقت الانقطاع المتوقع (بالميلي ثانية). إذا تجاوز وقت تشغيل الكود المراقب الوقت المتوقع، سيتم مقاطعة البرنامج ورفع استثناء.

## **الكود المثالي**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Large.xlsx");

const monitor = new AsposeCells.SystemTimeInterruptMonitor(false);
const lopts = new AsposeCells.LoadOptions();
lopts.setInterruptMonitor(monitor);
monitor.startMonitor(1000); // time limit is 1 second

// Loads the workbook with the specified load options
const wb = new AsposeCells.Workbook(filePath, lopts);
// if the time cost of loading the template file exceeds one second, interruption will be required and exception will be thrown here
// otherwise starts to monitor the save procedure
monitor.startMonitor(1500); // time limit is 1.5 seconds
wb.save("result.xlsx");
```  

