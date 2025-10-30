---  
title: Cargar libro con tamaño de papel de impresora especificado vía Node.js y C++  
linktitle: Cargar libro de trabajo con tamaño de papel de impresora especificado  
type: docs  
weight: 430  
url: /es/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Aprenda cómo establecer el tamaño de papel de la impresora al cargar un libro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Puede especificar el tamaño de papel de la impresora de su elección al cargar su libro usando el método [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Tenga en cuenta, si crea un archivo nuevo en MS Excel, verá que el tamaño de papel es el mismo que el ajuste de la impresora predeterminada en su máquina.  
{{% /alert %}}  

El siguiente código de ejemplo ilustra el uso del método [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Primero crea un libro, luego lo guarda en un flujo de memoria en formato XLSX. Luego lo carga con tamaño de papel A5 y lo guarda en formato PDF. Después, lo carga nuevamente con tamaño de papel A3 y lo guarda en PDF. Si abre los PDFs de salida y verifica su tamaño de papel, verá que son diferentes. Uno es A5 y el otro es A3. Por favor, descargue el [PDF de salida A5](5115234.pdf) y el [PDF de salida A3](5115233.pdf) generados por el código para su referencia.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
