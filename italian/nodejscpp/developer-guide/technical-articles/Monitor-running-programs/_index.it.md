---  
title: Monitorare programmi in esecuzione con Node.js via C++  
linktitle: Monitorare i programmi in esecuzione  
type: docs  
weight: 20  
url: /it/nodejs-cpp/monitor-running-programs/  
---  

## **Come monitorare un programma in esecuzione**

 Il seguente esempio di codice mostra come monitorare un programma in esecuzione. Questo codice può essere utilizzato per monitorare l'esecuzione di codice relativo a [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/). Usa semplicemente la classe [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) per creare un oggetto di monitoraggio, utilizza la funzione [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor-) per aggiungerlo ai parametri di caricamento di [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/), e poi usa la funzione [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) per impostare il tempo di interruzione previsto (in millisecondi). Se il tempo di esecuzione del codice monitorato supera il tempo previsto, il programma verrà interrotto e verrà sollevata un'eccezione.

## **Codice di Esempio**

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
