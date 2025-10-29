---  
title: Surveiller les programmes en cours d exécution avec Node.js via C++  
linktitle: Surveiller l exécution des programmes  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/monitor-running-programs/  
---  

## **Comment surveiller l'exécution d'un programme**

Le code d'exemple suivant montre comment surveiller un programme en cours d'exécution. Ce code peut être utilisé pour surveiller l'exécution du code lié à [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/). Utilisez simplement la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) pour créer un objet de surveillance, utilisez la fonction [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor-) pour l'ajouter aux paramètres d'exécution de [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/), puis utilisez la fonction [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) pour définir le temps d'interruption prévu (en millisecondes). Si le temps d'exécution du code surveillé dépasse le temps prévu, le programme sera interrompu et une exception sera levée.

## **Code d'exemple**

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
