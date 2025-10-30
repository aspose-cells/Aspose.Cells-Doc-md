---  
title: Ladda arbetsbok med angiven pappersstorlek för skrivare med Node.js och C++  
linktitle: Ladda arbetsboken med angiven skrivarpappersstorlek  
type: docs  
weight: 430  
url: /sv/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Lär dig hur du ställer in skrivarpapperstorlek när du laddar en arbetsbok med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Du kan ange skrivarpappersstorlek efter eget val när du laddar din arbetsbok med hjälp av [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-) metoden. Observera att om du skapar en ny fil i MS Excel, kommer du att se att papperstorleken är densamma som inställningen för standardskrivaren på din dator.  
{{% /alert %}}  

Följande exempel använder [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-)-metoden. Det skapar först en arbetsbok, sparar den i minnesström i XLSX-format. Sedan laddas den med A5-pappersstorlek och sparas i PDF-format. Sedan laddas den igen med A3-pappersstorlek och sparas i PDF-format. Om du öppnar de genererade PDF:erna och kontrollerar pappersstorleken, kommer du att se att de är olika. En är A5 och den andra är A3. Vänligen ladda ner [A5 PDF](5115234.pdf) och [A3 PDF](5115233.pdf) som genererats av koden för din referens.  

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
