---
title: Sätta Utskriftsalternativ med C++
linktitle: Inställning av utskriftsalternativ
type: docs
weight: 40
url: /sv/cpp/setting-print-options/
description: Denna artikel visar hur man programatiskt ställer in Utskriftsalternativen för Excel arkets Sidan Setup funktion via C++ API och bibliotek. Du kan ställa in Utskriftsområde, Utskriftsrubriker och Sidordning.
keywords: Sätt excel utskriftsområde c++, sätt excel utskriftsrubriker c++, sätt excel sidordning c++
---

{{% alert color="primary" %}}

Microsoft Excels sidoinställningsinställningar ger flera utskriftsalternativ (även kallade kalkylblad) som låter användare styra hur kalkylbladssidor skrivs ut.

{{% /alert %}}

## **Ställa in utskriftsalternativ**

Dessa utskriftsalternativ låter användare:

- Välja ett specifikt utskriftsområde på en arbetsbok.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Aspose.Cells stöder alla utskriftsalternativ som erbjuds av Microsoft Excel, och utvecklare kan enkelt konfigurera dessa alternativ för kalkblad med hjälp av egenskaperna som erbjuds av [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klassen. Hur dessa egenskaper används diskuteras nedan i mer detalj.

### **Ange utskriftsområde**

Som standard omfattar utskriftsområdet alla områden på kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde för kalkylbladet.

För att välja ett specifikt utskriftsområde, använd klassens [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/)-egenskap. Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ställ in utskriftstitlar**

Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor av ett utskrivet kalkylblad. Gör så genom att använda klassens [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) och [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/)-egenskaper.

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ange andra utskriftsalternativ**

Klassen [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) erbjuder också flera andra egenskaper för att ställa in generella utskriftsalternativ enligt följande:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): En Boolean-egenskap som avgör om rutnätlinjer ska skrivas ut eller ej.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): en boolesk egenskap som definierar om kalkylbladet ska skrivas ut i svartvitt läge eller inte.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): definierar om utskriftskommentarerna ska visas på kalkylbladet eller i slutet av kalkylbladet.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): En boolean-egenskap som avgör om bladet ska skrivas ut utan grafik.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): definierar om cellfel ska skrivas ut som de visas, blankt, bindestreck eller N/A.

För att ställa in [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) och [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) egenskaperna, erbjuder Aspose.Cells även två enumerations, [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) och [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/), som innehåller fördefinierade värden att tilldela [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) och [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) egenskaperna respektive.

De fördefinierade värdena i uppräkningen [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) listas nedan med deras beskrivningar.

|**Kommentarstyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintInPlace|Specificerar att skriva ut kommentarer som visas på kalkylbladet.|
|PrintNoComments|Specificerar att inte skriva ut kommentarer.|
|PrintSheetEnd|Specificerar att skriva ut kommentarer i slutet av kalkylbladet.|

De fördefinierade värdena i uppräkningen [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) listas nedan med deras beskrivningar.

|**Feltyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintErrorsBlank|Anger inte att skriva ut felmeddelanden.|
|PrintErrorsDash|Anger att skriva ut fel som "--".|
|PrintErrorsDisplayed|Anger att skriva ut fel som visas.|
|PrintErrorsNA|Anger att skriva ut fel som "#N/A".|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ange sidordning**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) klassen tillhandahåller [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) egenskapen som används för att ordna flera sidor av din kalkyl att skrivas ut. Det finns två möjligheter att beställa sidorna enligt följande.

- **Nedåt sedan över:** skriver ut alla sidor nedåt innan några sidor till höger skrivs ut.
- **Över sedan nedåt:** skriver sidor från vänster till höger innan sidorna nedanför skrivs ut.

Aspose.Cells tillhandahåller en uppräkning, [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) som innehåller alla fördefinierade ordningstyper.

De fördefinierade värdena i [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) uppräkningen listas nedan.

|**Utskriftsordningstyper**|**Beskrivning**|
| :- | :- |
|DownThenOver|Representerar utskriftsordning nedåt och sedan över.|
|OverThenDown|Representerar utskriftsordning över och sedan nedåt.|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
