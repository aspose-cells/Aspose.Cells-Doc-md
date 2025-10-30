---  
title: Monitorea programas en ejecución con Node.js vía C++  
linktitle: Monitorizar programas en ejecución  
type: docs  
weight: 20  
url: /es/nodejs-cpp/monitor-running-programs/  
---  

## **Cómo monitorizar un programa en ejecución**

El siguiente código de ejemplo muestra cómo monitorizar un programa en ejecución. Este código puede usarse para supervisar la ejecución de código relacionado con [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/). Simplemente usa la clase [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) para crear un objeto de monitoreo, usa la función [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setInterruptMonitor-abstractinterruptmonitor-) para agregarlo a los parámetros de ejecución de [LoadOptions](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/) y luego usa la función [startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) para establecer el tiempo esperado de interrupción (en milisegundos). Si el tiempo de ejecución del código monitoreado excede el tiempo esperado, el programa será interrumpido y se lanzará una excepción.

## **Código de muestra**

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
