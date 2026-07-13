---
title: Konvertera Excel till OFD-format
linktitle: Konvertera Excel till OFD-format
description: Aspose.Cells är ett Node.js-bibliotek för att arbeta med kalkylbladsfiler som stöder konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Den här artikeln visar hur man skapar Excel-innehåll och exporterar det som OFD, samt hur man konverterar befintliga Excel-filer till OFD med hjälp av Aspose.Cells.
keywords: Aspose.Cells, Node.js-bibliotek, kalkylblad, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, export av arbetsbok
type: docs
weight: 195
url: /sv/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel-arbetsböcker direkt till OFD-format (Open Fixed-layout Document) med hjälp av `SaveFormat.Ofd`-uppräkningsvärdet. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, teckensnitt, färger, kanter och talformat. Detta gör Aspose.Cells lämpligt för arkivering, utskrift, regulatorisk rapportering och myndighetsinlämningar som kräver utdata med fast layout.

{{% /alert %}}
## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i en fast, sidobaserad layout. Den tjänar en roll som liknar PDF för användningsfall där det visuella utseendet på källdokumentet måste bevaras exakt som det skapades. OFD är vitt spritt för myndighetsinlämningar, regulatorisk rapportering, elektroniska fakturor och långtidsarkivering i Folkrepubliken Kina.

Att konvertera Excel-arbetsböcker till OFD är ett vanligt krav i scenarier där kalkylbladsinnehåll måste distribueras som en skrivskyddad, layoutlåst artefakt snarare än som ett redigerbart kalkylblad. Exempel inkluderar att skicka en slutförd faktura till en kund, arkivera en kvartalsvis finansiell rapport, eller skicka in ett budgetkalkylblad till en tillsynsmyndighet. Aspose.Cells hanterar detta krav genom `SaveFormat.Ofd`-uppräkningsvärdet, som skriver arbetsboken direkt till OFD utan att kräva ett mellanliggande konverteringssteg. OFD-utdata bevarar cellvärden, sammanfogade intervall, teckensnitt, färger, kanter, talformat och alternativ för siduppsättning som konfigurerats på arbetsboken.

{{% alert color="primary" %}}

OFD-utdata som genereras av Aspose.Cells bevarar den synliga layouten av källarbetsboken, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering som teckensnitt, färger, kanter, justering och talformat renderas också i utdata med fast layout. Alternativ för siduppsättning som konfigurerats på kalkylbladet, såsom pappersstorlek, orientering och utskriftsområde, påverkar layouten för det resulterande OFD-dokumentet.

{{% /alert %}}
## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt i OFD-format med hjälp av `SaveFormat.Ofd`-uppräkningen. Följande exempel skapar en faktura från grunden. Det lägger till en företagslogotyp, rubrikinformation, en faktureringssektion, rader och beräknade summor, och exporterar sedan arbetsboken till ett OFD-dokument.
### **Bygga en faktura med en logotyp**
Exemplet konstruerar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra området, fylla i företagsnamn och kontaktuppgifter, lägga till en "INVOICE"-rubrik över sammanfogade celler, registrera fakturanummer och datum, lista faktureringskunden, bygga en tabell med rader som innehåller beskrivning, kvantitet, enhetspris och totalsumma, samt beräkna delsumma, skatt och totalsumma med hjälp av cellformler. Formatering som feta rubriker, valutaformat för priser, kanter och kolumnbredder tillämpas med hjälp av `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filändelsen `.ofd` med hjälp av `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Skapa en ny arbetsbok
let workbook = new AsposeCells.Workbook();

// Hämta det första arbetsbladet
let worksheet = workbook.getWorksheets().get(0);

// Ställ in kolumnbredder
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Infoga företagslogotyp
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Företagsnamn och kontaktuppgifter
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// FAKTURAtitel - sammanfoga celler
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);

// Fakturanummer och datum
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);

// Faktureras till-sektion
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Rubrik för radartiklar
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Valutastil med kanter
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Enkel kantstil för beskrivnings-/kvantitetsceller
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);

// Rader för radartiklar
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++) {
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);

    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);

    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}

// Delsumma, skatt, totalsumma
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Fetstil + valutastil för totalvärden
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Fetstil för totaletiketter
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart för batchkonverteringspipelines, arkiveringsarbetsflöden och scenarier där källarbetsboken producerades av ett annat verktyg och bara behöver återutges som en artefakt med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av siduppsättningen och sparar resultatet som ett OFD-dokument.

```javascript
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Läs och visa värden från valda celler för att bekräfta att filen laddades
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Iterera över Worksheets-samlingen för att räkna upp tillgängliga kalkylblad
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Valfritt: uppdatera en tidsstämpelcell för att återspegla konverteringen
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Konfigurera PageSetup-egenskaper på kalkylbladet
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Valfritt: ange utskriftsområde för OFD-utdata
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **Relaterade artiklar**
- [Dela Excel-filer i flera filer](/cells/sv/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Infoga en bild i en cell](/cells/sv/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Läsa och skriva DBF-filer](/cells/sv/nodejs-cpp/dbf/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Node.js via C++](/cells/sv/nodejs-cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}