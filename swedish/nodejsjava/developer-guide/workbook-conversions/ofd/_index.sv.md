---
title: Konvertera Excel till OFD-format
linktitle: Konvertera Excel till OFD-format
description: Aspose.Cells for Node.js via Java är ett kalkylarksbibliotek för arbete med kalkylarksfiler som stöder konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Den här artikeln visar hur man skapar Excel-innehåll och exporterar det som OFD, samt hur man konverterar befintliga Excel-filer till OFD med Aspose.Cells.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylark, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, arbetsboksexport
type: docs
weight: 195
url: /sv/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Excel-arbetsböcker direkt till OFD-format (Open Fixed-layout Document) med hjälp av `SaveFormat.Ofd`-uppräkningsvärdet. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, teckensnitt, färger, kanter och talformat. Detta gör Aspose.Cells lämpligt för arkivering, utskrift, regulatorisk rapportering och myndighetsinlämning som kräver en utdata med fast layout.

{{% /alert %}}
## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i ett fast, sidobaserat layoutformat. Den har en liknande roll som PDF för användningsfall där det visuella utseendet hos källdokumentet måste bevaras exakt som det skapades. OFD används i stor utsträckning för myndighetsinlämningar, regulatorisk rapportering, elektroniska fakturor och långtidsarkivering i Folkrepubliken Kina.

Att konvertera Excel-arbetsböcker till OFD är ett vanligt krav i scenarier där kalkylarksinnehåll måste distribueras som ett skrivskyddat, layoutlåst dokument snarare än som ett redigerbart kalkylark. Exempel inkluderar att skicka en färdig faktura till en kund, arkivera en kvartalsrapport eller skicka in ett budgetkalkylblad till en tillsynsmyndighet. Aspose.Cells hanterar detta krav genom `SaveFormat.Ofd`-uppräkningsvärdet, som skriver arbetsboken direkt till OFD utan att kräva ett mellanliggande konverteringssteg. OFD-utdata bevarar cellvärden, sammanfogade intervall, teckensnitt, färger, kanter, talformat och sidinställningar som konfigurerats på arbetsboken.

{{% alert color="primary" %}}

Den OFD-utdata som genereras av Aspose.Cells bevarar den synliga layouten för källarbetsboken, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering som teckensnitt, färger, kanter, justering och talformat renderas också i utdata med fast layout. Sidinställningar som konfigurerats på kalkylbladet, såsom pappersstorlek, orientering och utskriftsområde, påverkar layouten för det resulterande OFD-dokumentet.

{{% /alert %}}
## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt i OFD-format med hjälp av `SaveFormat.Ofd`-uppräkningsvärdet. Följande exempel skapar en faktura från grunden. Det lägger till en företagslogotyp, rubrikinformation, en faktureringsadresssektion, radobjekt och beräknade summor, och exporterar sedan arbetsboken till ett OFD-dokument.
### **Bygga en faktura med en logotyp**
Exemplet konstruerar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra området, fylla i företagsnamn och kontaktuppgifter, lägga till en "INVOICE"-titel över sammanfogade celler, registrera fakturanummer och datum, lista faktureringsmottagarens uppgifter, bygga en tabell med radobjekt och kolumner för beskrivning, antal, styckpris och totalsumma, samt beräkna delsumma, skatt och totalbelopp med cellformler. Formatering som feta rubriker, valutaformat för priser, kanter och kolumnbredder tillämpas med `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filändelsen `.ofd` med `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// Skapa en ny arbetsbok
let workbook = new AsposeCells.Workbook();

// Hämta det första kalkylbladet
let worksheet = workbook.getWorksheets().get(0);

// Ställ in kolumnbredder
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// Infoga företagets logotyp
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// Företagsnamn och kontaktuppgifter
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// FAKTURATITEL - sammanfoga celler
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Fakturanummer och datum
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// Faktureras till-sektion
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Rubrik för rader
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
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Valutastil med kanter
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Enkel kantstil för beskrivnings-/kvantitetsceller
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// Rader för fakturarader
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
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

// Delsumma, skatt, totalbelopp
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Fet + valutastil för totalvärden
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Fet stil för totaletiketter
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart för batchkonverteringsflöden, arkiveringsflöden och scenarier där källarbetsboken producerades av ett annat verktyg och endast behöver återutges som ett dokument med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av sidinställningar och sparar resultatet som ett OFD-dokument.

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// Öppna en befintlig Excel-arbetsbok från disk
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) Läs och visa värden från valda celler för att bekräfta att filen laddades
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) Iterera över Worksheets-samlingen för att räkna upp tillgängliga ark
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) Valfritt: uppdatera en tidsstämpelcell för att återspegla konverteringen
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// Lägg till en sammanfattningsrubrikrad överst i datablocket
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) Konfigurera PageSetup-egenskaper på kalkylbladet
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) Valfritt: ställ in utskriftsområdet för OFD-utdata
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **Relaterade artiklar**
- [Dela Excel-filer i flera filer](/cells/sv/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Infoga en bild i en cell](/cells/sv/nodejs-java/inserting-an-image-into-a-cell/)
- [Läsa och skriva DBF-filer](/cells/sv/nodejs-java/dbf/)
- [Konvertera Sparkline till bild och HTML i Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}