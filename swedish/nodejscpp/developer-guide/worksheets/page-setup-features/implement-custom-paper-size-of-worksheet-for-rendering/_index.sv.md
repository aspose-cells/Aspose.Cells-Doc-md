---  
title: Implementera anpassad pappersstorlek för arbetsblad för rendering med Node.js via C++  
linktitle: Implementera Anpassad Papperstorlek på Arbetsbladet för Rendering  
type: docs  
weight: 70  
url: /sv/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Denna artikel förklarar hur man använder Node.js API via C++ för att ställa in en anpassad pappersstorlek för de önskade arbetsbladen när man renderar en Excel fil till PDF format programmässigt.  
keywords: ställer in anpassad pappersstorlek vid rendering av Excel till PDF Node.js via C++  
---  

## **Möjliga användningsscenario**  

Det finns inget direkt alternativ för att skapa anpassade pappersstorlekar i MS Excel, men du kan ställa in en anpassad pappersstorlek för dina önskade arbetsblad när du renderar en Excel-fil till PDF. Detta dokument förklarar hur man sätter en anpassad pappersstorlek för ett arbetsblad med hjälp av Aspose.Cells API:er.  

## **Implementera anpassad pappersstorlek för arbetsblad för rendering**  

Aspose.Cells låter dig implementera din önskade pappersstorlek för arbetsbladet. Du kan använda [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-)-metoden av [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)-klassen för att specificera en anpassad sidstorlek. Följande exempel kod visar hur man specificerar en anpassad pappersstorlek för det första arbetsbladet i arbetsboken. Se också den [utgångs PDF](45056028.pdf) som genererades med koden för referens.  

## **Skärmdump**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
