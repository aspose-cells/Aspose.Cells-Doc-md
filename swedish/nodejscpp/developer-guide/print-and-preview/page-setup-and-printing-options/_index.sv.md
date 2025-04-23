---  
title: Siduppsättning och utskriftsalternativ med Node.js via C++  
linktitle: Sidlayout och utskriftsalternativ  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
Ibland behöver utvecklare konfigurera sidlayout och utskriftsalternativ för att kontrollera utskriftsprocessen. Sidlayouts- och utskriftsalternativen erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.  

Denna artikel visar hur man skapar en konsolapplikation i Node.js via C++, och tillämpar siduppsättning och utskriftsalternativ på ett arbetsblad med några enkla kodrader med Aspose.Cells API.  
{{% /alert %}}  

## **Arbeta med Sid- och Utskriftsalternativ**  

För detta exempel har vi skapat ett arbetsbok i Microsoft Excel och använt Aspose.Cells för att ställa in siduppsättning och utskriftsalternativ.  

### **Användning av Aspose.Cells för att ställa in sidlayoutalternativ**  

Skapa först ett enkelt arbetsblad i Microsoft Excel. Tillämpa sedan sidlayoutalternativ på det. När koden utförs ändras sidlayoutalternativen enligt skärmdumpen nedan.  

|**Utdatafil.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Skapa ett arbetsblad med viss data i Microsoft Excel:  
   1. Öppna en ny arbetsbok i Microsoft Excel.  
   1. Lägg till viss data.  
1. Ange sidlayoutalternativ:  
   Tillämpa sidlayoutalternativ på filen. Här är en skärmdump av de förvalda alternativen, innan de nya alternativen tillämpas.  

|**Standard sidlayoutalternativ.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Ladda ner och installera Aspose.Cells:  
   1. [Ladda ner](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. Installera det på din utvecklingsdator.  
      Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.  
1. Skapa ett projekt:  
   1. Starta din Node.js-miljö.  
   1. Skapa en ny konsolapplikation.  
      Detta exempel visar en Node.js-konsolapplikation, men du kan även använda C++-bindningar.  
1. Lägg till referenser:  
   1. Detta exempel använder Aspose.Cells så lägg till en referens till den komponenten i projektet. Till exempel:  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. Skriv applikationen som använder API:et:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **Inställa utskriftsalternativ**  

Sidlayoutinställningar ger också flera utskriftsalternativ (även kallade bladalternativ) som låter användarna styra hur arksidor skrivs ut. De tillåter användarna att:  

- Välj ett specifikt utskriftsområde av ett kalkylblad.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.  

Exemplet som följer tillämpar utskriftsalternativ på filen skapad i exemplet ovan (PageSetup.xls). Skärmdumpen nedan visar de standardutskriftsalternativen innan nya alternativ tillämpas.  

|**Inmatningsdokument**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Körning av koden ändrar utskriftsalternativen.  

|**Utmatningsfil**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

