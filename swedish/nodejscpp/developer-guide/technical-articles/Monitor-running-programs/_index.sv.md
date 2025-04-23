---  
title: Övervaka körande program med Node.js via C++  
linktitle: Bevaka körande program  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/monitor-running-programs/  
---  

## **Hur du övervakar ett körande program**

Följande exempel visar hur du övervakar ett körande program. Denna kod kan användas för att övervaka körningen av [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) relaterad kod. Använd helt enkelt [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) för att skapa ett övervakningsobjekt, använd funktionen [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor-) för att lägga till det i [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/) och använd sedan [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) för att sätta den förväntade avbrottstiden (i millisekunder). Om den körda tiden för den övervakade koden överskrider den förväntade tiden, avbryts programmet och ett undantag kastas.

## **Exempelkod**

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

