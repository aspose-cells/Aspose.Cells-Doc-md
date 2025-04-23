---  
title: Überwachen laufender Programme mit Node.js via C++  
linktitle: Überwachen laufender Programme  
type: docs  
weight: 20  
url: /de/nodejs-cpp/monitor-running-programs/  
---  

## **Wie man ein laufendes Programm überwacht**

Der folgende Beispielcode zeigt, wie man ein laufendes Programm überwacht. Dieser Code kann verwendet werden, um das Laufverhalten von [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/) bezogenen Code zu überwachen. Verwenden Sie einfach die [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/)-Klasse, um ein Überwachungsobjekt zu erstellen, die Funktion [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor-) aufzurufen, um es zu den laufenden Parametern hinzuzufügen, und dann die Funktion [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) zu verwenden, um die erwartete Unterbrechungszeit (in Millisekunden) festzulegen. Überschreitet die Laufzeit des überwachten Codes die erwartete Zeit, wird das Programm unterbrochen und eine Ausnahme ausgelöst.

## **Beispielcode**

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

