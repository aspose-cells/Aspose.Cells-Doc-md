---
title: Konvertera Excel till OFD-format
linktitle: Konvertera Excel till OFD-format
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylbladsfiler som stöder konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Den här artikeln visar hur man skapar Excel-innehåll och exporterar det som OFD, samt hur man konverterar befintliga Excel-filer till OFD med Aspose.Cells.
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, arbetsboksexport
type: docs
weight: 195
url: /sv/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel-arbetsböcker direkt till OFD-format (Open Fixed-layout Document) med hjälp av uppräkningsvärdet `SaveFormat.Ofd`. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, teckensnitt, färger, kantlinjer och talformat. Detta gör Aspose.Cells lämpligt för arkivering, utskrift, regulatorisk rapportering och myndighetsinlämningar som kräver utdata med fast layout.

{{% /alert %}}
## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i en fast, sidobaserad layout. Det har en roll som liknar PDF för användningsfall där det visuella utseendet på källdokumentet måste bevaras exakt som det skapades. OFD används i stor utsträckning för myndighetsinlämningar, regulatorisk rapportering, elektroniska fakturor och långtidsarkivering i Folkrepubliken Kina.

Att konvertera Excel-arbetsböcker till OFD är ett vanligt krav i scenarier där kalkylbladsinnehåll måste distribueras som ett skrivskyddat, layoutlåst dokument snarare än som ett redigerbart kalkylblad. Exempel inkluderar att skicka en färdig faktura till en kund, arkivera en kvartalsvis finansiell rapport eller skicka in ett budgetkalkylblad till en tillsynsmyndighet. Aspose.Cells hanterar detta krav genom uppräkningsvärdet `SaveFormat.Ofd`, som skriver arbetsboken direkt till OFD utan att kräva ett mellanliggande konverteringssteg. OFD-utdata bevarar cellvärden, sammanfogade intervall, teckensnitt, färger, kantlinjer, talformat och sidinställningar som konfigurerats på arbetsboken.

{{% alert color="primary" %}}

Den OFD-utdata som genereras av Aspose.Cells bevarar källarbetsbokens synliga layout, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering som teckensnitt, färger, kantlinjer, justering och talformat återges också i utdata med fast layout. Sidinställningar som konfigurerats på kalkylbladet, såsom pappersstorlek, orientering och utskriftsområde, påverkar layouten för det resulterande OFD-dokumentet.

{{% /alert %}}
## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt till OFD-format med hjälp av uppräkningen `SaveFormat.Ofd`. Följande exempel skapar en faktura från grunden. Den lägger till en företagslogotyp, rubrikinformation, en fakturaadresssektion, artikelrader och beräknade summor, och exporterar sedan arbetsboken till ett OFD-dokument.
### **Skapa en faktura med en logotyp**
Exemplet konstruerar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra området, fylla i företagsnamn och kontaktuppgifter, lägga till en "FAKTURA"-titel över sammanfogade celler, registrera fakturanummer och datum, lista fakturamottagaren, bygga en artikelradstabell med beskrivning, kvantitet, styckpris och totalsumma kolumner, samt beräkna delsumma, skatt och totalsumma med cellformler. Formatering som fetstilta rubriker, valutaformat för priser, kantlinjer och kolumnbredder tillämpas med hjälp av `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filändelsen `.ofd` med hjälp av `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// Skapa en ny arbetsbok
Workbook workbook = new Workbook();

// Hämta det första kalkylbladet
Worksheet worksheet = workbook.Worksheets[0];

// Ställ in kolumnbredder
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// Infoga företagslogotyp
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// Företagsnamn och kontaktuppgifter
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// FAKTURA-titel - sammanfoga celler
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// Fakturanummer och datum
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// Faktura till-sektion
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// Rubrik för radartiklar
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// Valutastil med kanter
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Enkel kantstil för beskrivnings-/kvantitetsceller
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Rader för radartiklar
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// Delsumma, skatt, totalsumma
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// Fetstil + valutastil för totalvärden
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// Fetstil för totaletiketter
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// Spara arbetsboken som en OFD-fil
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart för batchkonverteringsflöden, arkiveringsflöden och scenarier där källarbetsboken producerades av ett annat verktyg och bara behöver återutges som ett dokument med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av sidinställningar och sparar resultatet som ett OFD-dokument.

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// Öppna en befintlig Excel-arbetsbok från disk
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) Läs och visa värden från valda celler för att bekräfta att filen laddades
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) Iterera över Worksheets-samlingen för att räkna upp tillgängliga blad
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) Valfritt: uppdatera en tidsstämpelcell för att återspegla konverteringen
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// Lägg till en sammanfattningsrubrikrad överst i datablocket
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) Konfigurera PageSetup-egenskaper på arbetsbladet
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) Valfritt: ställ in utskriftsområdet för OFD-utdata
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) Spara arbetsboken som en OFD-fil
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Relaterade artiklar**
- [Dela upp Excel-filer i flera filer](/cells/sv/net/splitting-excel-files-into-multiple-files/)
- [Infoga en bild i en cell](/cells/sv/net/inserting-an-image-into-a-cell/)
- [Läsa och skriva DBF-filer](/cells/sv/net/dbf/)
- [Konvertera Sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}