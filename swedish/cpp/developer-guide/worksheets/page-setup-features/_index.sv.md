---
title: Sidinställningsfunktioner med C++
linktitle: Siduppsättningsfunktioner
type: docs
weight: 60
url: /sv/cpp/page-setup-features/
description: Lär dig att konfigurera sidinställningsfunktioner i Excel filer med Aspose.Cells och C++.
---

## **Sidlayoutfunktioner**

Aspose.Cells erbjuder ett omfattande utbud av funktioner för att konfigurera sidinställningar i Excel-filer. Dessa funktioner låter dig kontrollera olika aspekter av sidlayouten, såsom marginaler, orientering, pappersstorlek och mer.

### **Ställa in sidmarginaler**

Du kan ange sidmarginalerna för ett arbetsblad med hjälp av `PageSetup`-klassen. Följande exempel visar hur man ställer in topp-, botten-, vänster- och högermarginaler:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Ställa in sidorientering**

Du kan ställa in sidans orientering till porträtt eller land/vägg med hjälp av `PageSetup`-klassen. Följande exempel visar hur man ställer in sidans orientering till landskap:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Ställa in pappersstorlek**

Du kan ställa in pappersstorleken för utskrift med hjälp av `PageSetup`-klassen. Följande exempel visar hur man ställer in pappersstorleken till A4:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Ställa in utskriftsområde**

Du kan definiera ett specifikt område av celler som ska skrivas ut med hjälp av `PageSetup`-klassen. Följande exempel visar hur man ställer in utskriftsområdet:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Ställa in sidbrytningar**

Du kan infoga sidbrytningar i ett kalkylblad för att kontrollera var sidorna slutar och nya börjar. Följande exempel visar hur du infogar en horisontell sidbrytning:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Ställa in sidhuvud och sidfot**

Du kan anpassa sidhuvudet och sidfoten i ett kalkylblad med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in ett anpassat sidhuvud och sidfot:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Ställa in utskriftstitlar**

Du kan ange rader eller kolumner för att upprepa sig längst upp eller till vänster på varje utskriven sida med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in utskriftstitlar:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Ställa in utskriftskvalitet**

Du kan ställa in utskriftskvaliteten för ett kalkylblad med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in utskriftskvaliteten:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Ställa in utskriftsordning**

Du kan ställa in utskriftsordningen för ett kalkylblad med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in utskriftsordning till "Över, sedan Ned":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Ställa in utskrivbara rutnätlinjer**

Du kan kontrollera om rutnätslinjer ska skrivas ut med hjälp av `PageSetup`-klassen. Följande exempel visar hur du aktiverar utskrift av rutnätslinjer:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Ställa in utskrivbara rubriker**

Du kan kontrollera om rad- och kolumnrubriker ska skrivas ut med hjälp av `PageSetup`-klassen. Följande exempel visar hur du aktiverar utskrift av rubriker:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Ställa in svartvitt utskrift**

Du kan kontrollera om kalkylbladet ska skrivas ut i svartvitt med hjälp av `PageSetup`-klassen. Följande exempel visar hur du aktiverar svartvit utskrift:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **Ställa in förhandsgranskning av utskrift**

Du kan kontrollera om kalkylbladet ska skrivas ut i utkastläge med hjälp av `PageSetup`-klassen. Följande exempel visar hur du aktiverar utskrift i utkastläge:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Ställa in utskrivbara kommentarer**

Du kan kontrollera om kommentarer ska skrivas ut med hjälp av `PageSetup`-klassen. Följande exempel visar hur du aktiverar utskrift av kommentarer:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Ställa in utskriftsfelhantering**

Du kan kontrollera hur fel hanteras vid utskrift med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in felhanteringsalternativet:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Ställa in utskriftsområde för att passa sidor**

Du kan kontrollera om utskriftsområdet skalas för att passa ett specifikt antal sidor med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in utskriftsområdet för att passa en sida brett och en sida högt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Ställa in utskriftsomfång**

Du kan ställa in utskriftsomfånget för ett kalkylblad med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in utskriftsomfånget till 50 %:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Ställa in utskriftscentrum horisontellt och vertikalt**

Du kan kontrollera om kalkylbladet ska centreras horisontellt och vertikalt på den utskrivna sidan med hjälp av `PageSetup`-klassen. Följande exempel visar hur man centrerar kalkylbladet horisontellt och vertikalt:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **Ställa in första sidnummer för utskrift**

Du kan ställa in det första sidnumret för utskrift med hjälp av `PageSetup`-klassen. Följande exempel visar hur du ställer in det första sidnumret:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Ställa in sidnummer för utskrift**

Du kan kontrollera om sidnummer ska skrivas ut med hjälp av `PageSetup`-klassen. Följande exempel visar hur man aktiverar utskrift av sidnummer:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Anger utskriftsordning för sidor**

Du kan ställa in i vilken ordning sidor skrivs ut med hjälp av `PageSetup`-klassen. Följande exempel visar hur man ställer in sidordning till "Nedåt, sedan över":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
{{< app/cells/assistant language="cpp" >}}
