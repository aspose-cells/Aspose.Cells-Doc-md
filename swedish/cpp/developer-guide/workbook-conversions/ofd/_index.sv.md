---
title: Konvertera Excel till OFD-format
linktitle: Konvertera Excel till OFD-format
description: Aspose.Cells är ett C++-bibliotek för att arbeta med kalkylbladsfiler som stöder konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Den här artikeln visar hur man skapar Excel-innehåll och exporterar det som OFD, samt hur man konverterar befintliga Excel-filer till OFD med Aspose.Cells.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, arbetsboksexport
type: docs
weight: 195
url: /sv/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel-arbetsböcker direkt till OFD-format (Open Fixed-layout Document) med hjälp av uppräkningsvärdet `SaveFormat.Ofd`. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, teckensnitt, färger, kantlinjer och nummerformat. Detta gör Aspose.Cells lämpligt för arkivering, utskrift, regulatorisk inlämning och myndighetsinlämningar som kräver utdata med fast layout.

{{% /alert %}}
## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i en fast, sidbaserad layout. Det har en roll som liknar PDF för användningsfall där det visuella utseendet på källdokumentet måste bevaras exakt som det skapades. OFD används i stor utsträckning för myndighetsinlämningar, regulatoriska inlämningar, elektroniska fakturor och långsiktig arkivering i Folkrepubliken Kina.

Att konvertera Excel-arbetsböcker till OFD är ett vanligt krav i scenarier där kalkylbladsinnehåll måste distribueras som en skrivskyddad, layoutlåst artefakt snarare än som ett redigerbart kalkylblad. Exempel inkluderar att skicka en färdig faktura till en kund, arkivera en kvartalsrapport, eller lämna in ett budgetkalkylblad till en regulatorisk myndighet. Aspose.Cells hanterar detta krav genom uppräkningsvärdet `SaveFormat.Ofd`, som skriver arbetsboken direkt till OFD utan att kräva ett mellanliggande konverteringssteg. OFD-utdata bevarar cellvärden, sammanfogade intervall, teckensnitt, färger, kantlinjer, nummerformat och sidinställningar som konfigurerats på arbetsboken.

{{% alert color="primary" %}}

OFD-utdata som genereras av Aspose.Cells bevarar den synliga layouten av källarbetsboken, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering som teckensnitt, färger, kantlinjer, justering och nummerformat renderas också i utdata med fast layout. Sidinställningar som konfigurerats på kalkylbladet, såsom pappersstorlek, orientering och utskriftsområde, påverkar layouten för det resulterande OFD-dokumentet.

{{% /alert %}}
## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt till OFD-format med hjälp av uppräkningsvärdet `SaveFormat.Ofd`. Följande exempel skapar en faktura från grunden. Det lägger till en företagslogotyp, rubrikinformation, en mottagarsektion, artikelrader och beräknade summor, och exporterar sedan arbetsboken till ett OFD-dokument.
### **Bygga en faktura med en logotyp**
Exemplet konstruerar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra området, fylla i företagsnamn och kontaktuppgifter, lägga till en "INVOICE"-titel över sammanfogade celler, registrera fakturanumret och datumet, lista fakturamottagaren, bygga en tabell med artikelrader med kolumner för beskrivning, kvantitet, enhetspris och total, samt beräkna delsumma, skatt och totalsumma med cellformler. Formatering som feta rubriker, valutaformat för priser, kantlinjer och kolumnbredder tillämpas med hjälp av `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filändelsen `.ofd` med hjälp av `SaveFormat.Ofd`.

```cpp
// Aspose.Cells för C++-exempel
// Kompilera med Aspose.Cells 26.6.0 (eller senare) och en C++17-kompilator (eller senare)

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Initiera Aspose.Cells
    Aspose::Cells::Startup();

    // Katalog för resurser och utdata
    const char16_t* dataDir = u"C:\\Temp\\";

    // Skapa en ny arbetsbok
    Workbook workbook;

    // Hämta det första kalkylbladet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Ange kolumnbredder
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Infoga företagets logotyp
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Företagets namn och kontaktuppgifter
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // FAKTURA-titel - sammanfoga celler
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Fakturanummer och datum
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Faktura till-sektion
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Huvudrad för rader
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
    headerStyle.SetForegroundColor(Color{0, 0, 128});
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

    // Valutastil med kanter
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Enkel kantstil för beskrivnings-/kvantitetsceller
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Radrader
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

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Delsumma, skatt, totalsumma
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Fetstil + valutastil för totalvärden
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Fetstilsstil för totaletiketter
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Spara arbetsboken som en OFD-fil
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Rensa upp Aspose.Cells-resurser
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart för batchkonverteringspipelines, arkiveringsarbetsflöden och scenarier där källarbetsboken producerades av ett annat verktyg och bara behöver återges som en artefakt med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria sidinställningsjusteringar och sparar resultatet som ett OFD-dokument.

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

    // Öppna en befintlig Excel-arbetsbok från disk
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Läs och visa värden från valda celler för att bekräfta att filen laddades
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Iterera över Worksheets-samlingen för att räkna upp tillgängliga blad
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Valfritt: uppdatera en tidsstämpelcell för att återspegla konverteringen
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Lägg till en rubrikrad för sammanfattning överst i datablocket
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Konfigurera PageSetup-egenskaper på arbetsbladet
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) Valfritt: ställ in utskriftsområdet för OFD-utdata
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Spara arbetsboken som en OFD-fil
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Relaterade artiklar**
- [Splitting Excel Files into Multiple Files](/cells/sv/cpp/splitting-excel-files-into-multiple-files/)
- [Inserting an Image into a Cell](/cells/sv/cpp/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/sv/cpp/dbf/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for C++](/cells/sv/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}