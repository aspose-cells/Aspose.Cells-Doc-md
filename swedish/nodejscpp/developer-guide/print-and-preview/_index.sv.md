---  
title: Förhandsgranska arbetsbok med Node.js via C++  
linktitle: Förhandsgranska arbetsbok 
type: docs  
weight: 70  
url: /sv/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells stödjer utskrift och förhandsgranskning av Excel filer utan Microsoft Excel installation med Node.js via C++.  
---  

## **Förhandsgranska utskrift**  

Det kan finnas fall där Excel-filer med miljontals sidor måste konverteras till PDF eller bilder. Behandling av sådana filer tar mycket tid och resurser. I sådana fall kan funtionen för arbetsboks- och bladutsiktsförhandsgranskning vara användbar. Innan konvertering kan användaren kontrollera det totala sidantalet och bestämma om filen ska konverteras eller inte. Denna artikel fokuserar på att använda klasserna [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) för att ta reda på det totala antalet sidor.  

Aspose.Cells tillhandahåller utskriftsförhandsgranskning. För detta använder API:et [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) klasser. För att skapa en förhandsgranskning av hela arbetsboken, skapa en instans av [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) klassen genom att passera [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) objekt till konstruktorn. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) klassen tillhandahåller en [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) metod som returnerar antalet sidor i den genererade förhandsgranskningen. Liknande [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) klassen, används [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) klassen för att generera en utskriftsförhandsgranskning för ett specifikt blad. För att skapa utskriftsförhandsgranskning av ett blad, skapa en instans av [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) klassen genom att passera [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) objekt till konstruktorn. [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) klassen tillhandahåller också en [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) metod som returnerar antalet sidor i den genererade förhandsgranskningen.  

Följande kodexempel demonstrerar användningen av både [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) klasser genom att använda [provläsnings Excel-fil](94896177.xlsx).  

### **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

Följande är utdatan som genereras genom att köra ovanstående kod.  

### **Konsoloutput**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Fortsatta ämnen**  
- [Konfigurera typsnitt för att rendera kalkylblad](/cells/sv/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Konvertera arbetsblad till bild - Ta bort mellanrum runt data](/cells/sv/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Konvertera kalkylblad till bild och kalkylblad till bild per sida](/cells/sv/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Konvertera arbetsblad till bild med hjälp av ImageOrPrint Options](/cells/sv/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Exportera område av celler i en arbetsbok till bild](/cells/sv/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extrahera bilder från arbetsblad med hjälp av ImageOrPrintOptions](/cells/sv/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generera miniatyrbild av arbetsbladet](/cells/sv/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Utdata tom sida när det inte finns något att skriva ut](/cells/sv/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Sidlayout- och utskriftsalternativ](/cells/sv/nodejs-cpp/page-setup-and-printing-options/)  
- [Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions](/cells/sv/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Rendera kalkylblad till grafiskt sammanhang](/cells/sv/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation](/cells/sv/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

