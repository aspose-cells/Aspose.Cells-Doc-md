---  
title: 通过 C++ 使用 Node.js 监控运行中的程序  
linktitle: 监控运行中的程序  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/monitor-running-programs/  
---  

## **如何监控运行中的程序**

以下示例代码显示如何监控一个正在运行的程序。此代码可用于监控[工作簿](https://reference.aspose.com/cells/nodejs-cpp/workbook/)相关代码的运行情况。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/)类创建监控对象，使用[LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor/)函数将其加入到[LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/)的运行参数中，然后用[startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-)函数设置预期的中断时间（以毫秒为单位）。如果被监控代码的运行时间超过预期时间，程序将被中断并抛出异常。

## **示例代码**

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

