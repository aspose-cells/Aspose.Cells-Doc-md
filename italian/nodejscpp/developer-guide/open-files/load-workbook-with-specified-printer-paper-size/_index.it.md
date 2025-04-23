---  
title: Carica Workbook con dimensione carta predefinita della stampante tramite Node.js e C++  
linktitle: Carica il Documento di Lavoro con il Formato Carta del Stampante Specificato  
type: docs  
weight: 430  
url: /it/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Impara come impostare la dimensione del foglio di carta della stampante durante il caricamento di un workbook usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
È possibile specificare la dimensione della carta della stampante desiderata durante il caricamento del libro di lavoro utilizzando il metodo [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Si noti che se si crea un nuovo file in MS Excel, si noterà che la dimensione della carta è la stessa dell'impostazione della stampante predefinita nel computer.  
{{% /alert %}}  

Il seguente esempio illustra l’uso del metodo [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Prima crea un workbook, quindi lo salva in un flusso di memoria in formato XLSX. Poi lo carica con formato di pagina A5 e lo salva in formato PDF. Successivamente lo ricarica con formato di pagina A3 e lo salva nuovamente in PDF. Se si aprono i PDF di output e si verifica la loro dimensione, si noterà che sono differenti. Uno è A5 e l’altro A3. Si scarichino i [PDF di output A5](5115234.pdf) e [PDF di output A3](5115233.pdf) generati dal codice come riferimento.  

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

