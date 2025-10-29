---  
title: Мониторинг запущенных программ с Node.js через C++  
linktitle: Мониторинг работающих программ  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/monitor-running-programs/  
---  

## **Как отслеживать работающую программу**

Следующий пример показывает, как мониторить запущенную программу. Этот код можно использовать для отслеживания выполнения [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/). Просто используйте класс [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) для создания объекта мониторинга, вызовите функцию [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor/), чтобы добавить его в параметры выполнения [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/), и затем используйте функцию [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-), чтобы указать ожидаемое время прерывания (в миллисекундах). Если время выполнения мониторируемого кода превышает ожидаемое, программа будет прервана и возникнет исключение.

## **Образец кода**

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
