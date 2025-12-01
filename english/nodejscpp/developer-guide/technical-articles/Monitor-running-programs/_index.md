---  
title: Monitor running programs with Node.js via C++  
linktitle: Monitor running programs  
type: docs  
weight: 20  
url: /nodejs-cpp/monitor-running-programs/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **How to monitor a running program**

The following sample code shows how to monitor a running program. This code can be used to monitor the running of [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) related code. Simply use the [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) class to create a monitoring object, use the [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor-) function to add it to the [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/) running parameters, and then use the [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) function to set the expected interruption time (in milliseconds). If the running time of the monitored code exceeds the expected time, the program will be interrupted and an exception will be thrown.

## **Sample Code**

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
