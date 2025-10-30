---
title: Sidinställningar och utskriftsalternativ med C++
linktitle: Sidlayout och utskriftsalternativ
type: docs
weight: 60
url: /sv/cpp/page-setup-and-printing-options/
description: Konfigurera sidinställningar och utskriftsinställningar för att kontrollera utskriftsprocessen med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland behöver utvecklare konfigurera sidlayout och utskriftsalternativ för att kontrollera utskriftsprocessen. Sidlayouts- och utskriftsalternativen erbjuder olika alternativ och stöds fullt ut i Aspose.Cells.

Denna artikel visar hur man skapar en konsolapp i Visual Studio och använder några enkla kodrader för att tillämpa sidinställningar och utskriftsalternativ på ett kalkylblad med Aspose.Cells API.

{{% /alert %}}

## **Arbeta med Sid- och Utskriftsalternativ**

För detta exempel skapade vi en arbetsbok i Microsoft Excel och använde Aspose.Cells för att ställa in sidlayouts- och utskriftsalternativ.

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
   1. [Ladda ner](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Installera det på din utvecklingsdator.
      Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.
1. Skapa ett projekt:
   1. Starta Visual Studio.
   1. Skapa en ny konsolapplikation.
      Detta exempel visar en C++-konsolapplikation.
1. Lägg till referenser:
   1. Detta exempel använder Aspose.Cells så lägg till en referens till den komponenten i projektet. Till exempel:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Skriv applikationen som använder API:et:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
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

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
