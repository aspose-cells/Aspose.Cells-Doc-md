---  
title: Node.js üzerinden C++ ile çalışan programları izleme  
linktitle: Çalışan Programları İzleme  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/monitor-running-programs/  
---  

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod, çalışan bir programın nasıl izlenileceğini gösterir. Bu kod, [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) ile ilgili kodların izlenmesi için kullanılabilir. Basitçe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) sınıfını kullanarak bir izleme nesnesi oluşturun, [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)] fonksiyonunu kullanarak buna erişim sağlayın ve ardından [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) fonksiyonunu kullanarak beklenen kesinti süresini (milisaniye cinsinden) ayarlayın. İzlenen kodun çalışma süresi, beklenenden fazla ise program kesilir ve bir istisna atılır.

## **Örnek Kod**

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

{{< app/cells/assistant language="nodejs-cpp" >}}
