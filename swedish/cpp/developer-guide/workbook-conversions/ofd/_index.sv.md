---
title: Konvertering av Excel till OFD-format
linktitle: OFD
description: Aspose.Cells är ett C++-bibliotek för arbete med kalkylarksfiler som stöder konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Den här artikeln visar hur du skapar Excel-innehåll och exporterar det som OFD, samt hur du konverterar befintliga Excel-filer till OFD med Aspose.Cells.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, export av arbetsböcker
type: docs
weight: 195
url: /sv/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder direkt konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document) med hjälp av enumerationsvärdet `SaveFormat.Ofd`. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, teckensnitt, färger, ramar och talformat. Det gör Aspose.Cells lämpligt för flöden för arkivering, utskrift, regulatoriska ärenden och myndighetsinlämningar som kräver utdata med fast layout.
{{% /alert %}}

## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i en fast, sidbaserad layout. Den har en funktion som liknar PDF:s i användningsfall där källodokumentets visuella utseende måste bevaras exakt som det har utformats. OFD används i stor utsträckning för myndighetsinlämningar, regulatoriska ärenden, elektroniska fakturor och arkivering för långtidsbevarande i Folkrepubliken Kina.
Att konvertera Excel-arbetsböcker till OFD är ett vanligt behov i situationer där kalkylarksinnehåll måste distribueras som en skrivskyddad artefakt med låst layout i stället för som ett redigerbart kalkylblad. Exempel är att skicka en färdig faktura till en kund, arkivera en kvartalsvis finansiell rapport eller lämna in ett kalkylblad med en budget till en tillsynsmyndighet. Aspose.Cells tillgodoser detta behov med hjälp av enumerationsvärdet `SaveFormat.Ofd`, som skriver arbetsboken direkt till OFD utan att ett mellanliggande konverteringssteg krävs. OFD-utdata bevarar cellvärden, sammanfogade intervall, teckensnitt, färger, ramar, talformat och sidinställningsalternativ som har konfigurerats i arbetsboken.

{{% alert color="primary" %}}
OFD-utdata som genereras av Aspose.Cells bevarar den synliga layouten i källarbetsboken, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering, till exempel teckensnitt, färger, ramar, justering och talformat, återges också i utdatan med fast layout. Sidinställningar som har konfigurerats i kalkylbladet, till exempel pappersstorlek, orientering och utskriftsområde, påverkar layouten i det resulterande OFD-dokumentet.
{{% /alert %}}

## **Skapa en Excel-arbetsbok och spara den som OFD**
Aspose.Cells låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt i OFD-format med hjälp av enumerationsvärdet `SaveFormat.Ofd`. Följande exempel skapar en faktura helt från grunden. Exemplet lägger till en företagslogotyp, rubrikinformation, ett avsnitt med faktureringsmottagare, artikelposter och beräknade summor och exporterar sedan arbetsboken till ett OFD-dokument.

### **Bygga en faktura med en logotyp**
Exemplet skapar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra hörnet, fylla i företagsnamn och kontaktuppgifter, lägga till rubriken "INVOICE" i sammanfogade celler, ange fakturanummer och datum, redovisa faktureringsmottagaren, bygga en tabell med artikelposter och kolumnerna beskrivning, antal, enhetspris och summa samt beräkna delsumma, skatt och slutsumma med cellformler. Formatering, till exempel rubriker i fetstil, valutaformat för priser, ramar och kolumnbredder, tillämpas med hjälp av `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filtillägget `.ofd` med hjälp av `SaveFormat.Ofd`.

```cpp
// Aspose.Cells for C++ example
// Compile with Aspose.Cells 26.6.0 (or later) and a C++17 (or later) compiler
#include "Aspose.Cells.h"
#include <string>
#include <ctime>
using namespace Aspose::Cells;
int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();
    // Directory for resources and output
    const char16_t* dataDir = u"C:\\Temp\\";
    // Create a new workbook
    Workbook workbook;
    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Set column widths
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);
    // Insert company logo
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");
    // Company name and contact details
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");
    // INVOICE title - merge cells
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");
    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);
    // Invoice number and date
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));
    // Bill-to section
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");
    // Line items header
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");
    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");
    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0xff, 0x00, 0x00, 0x80});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);
    // Currency style with borders
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // Plain border style for description/quantity cells
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // Line items rows
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };
    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);
        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);
        std::string formula = "C" + std::to_string(row + 1) + "*D" + std::to_string(row + 1);
        totalCell.SetFormula(U16String(formula.c_str()));
        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }
    // Subtotal, tax, grand total
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E21:E23)");
    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");
    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");
    // Bold + currency style for total values
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");
    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);
    // Bold style for total labels
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);
    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);
    // Save the workbook as an OFD file
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);
    // Cleanup Aspose.Cells resources
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart i batchkonverterings- och arkiveringsflöden samt i situationer där källarbetsboken har skapats med ett annat verktyg och endast behöver exporteras på nytt som en artefakt med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av sidinställningarna och sparar resultatet som ett OFD-dokument.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>
using namespace Aspose::Cells;
std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}
int main() {
    Aspose::Cells::Startup();
    std::string dataDir = "C:\\Examples\\";
    // Open an existing Excel workbook from disk
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));
    // (1) Read and display values from selected cells to confirm the file was loaded
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");
    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;
    // (2) Iterate over the Worksheets collection to enumerate available sheets
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }
    // (3) Optionally update a timestamp cell to reflect the conversion
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));
    // Append a summary header row at the top of the data block
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");
    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));
    // (4) Configure PageSetup properties on the worksheet
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);
    // (5) Optionally set the print area for the OFD output
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;
    // (6) Save the workbook as an OFD file
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Relaterade artiklar**
- [Dela upp Excel-filer i flera filer](/cells/sv/cpp/splitting-excel-files-into-multiple-files/)
- [Infoga en bild i en cell](/cells/sv/cpp/inserting-an-image-into-a-cell/)
- [Läsa och skriva DBF-filer](/cells/sv/cpp/dbf/)

{{< app/cells/assistant language="cpp" >}}