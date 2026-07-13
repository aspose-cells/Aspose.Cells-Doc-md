---
title: Konvertera Excel till OFD-format
linktitle: Konvertera Excel till OFD-format
description: Aspose.Cells for Python via Java är ett bibliotek för att arbeta med kalkylbladsfiler som stödjer konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Denna artikel visar hur man skapar Excel-innehåll och exporterar det som OFD, samt hur man konverterar befintliga Excel-filer till OFD med Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java library, kalkylblad, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, arbetsboksexport
type: docs
weight: 195
url: /sv/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java stödjer direkt konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document) med hjälp av uppräkningsvärdet `SaveFormat.Ofd`. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanslagna celler, kolumnbredder, radhöjder, typsnitt, färger, kanter och talformat. Detta gör Aspose.Cells for Python via Java lämpligt för arkivering, utskrift, regulatorisk inlämning och statliga inskickarbetsflöden som kräver en utdata med fast layout.

{{% /alert %}}
## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i en fast, sidbaserad layout. Den tjänar en liknande roll som PDF för användningsfall där det visuella utseendet hos källdokumentet måste bevaras exakt som det skapades. OFD är vitt spritt för statliga inskick, regulatoriska anmälningar, elektroniska fakturor och långsiktig arkivering i Folkrepubliken Kina.

Att konvertera Excel-arbetsböcker till OFD är ett vanligt krav i scenarier där kalkylbladsinnehåll måste distribueras som ett skrivskyddat, layoutlåst artefakt snarare än som ett redigerbart kalkylblad. Exempel inkluderar att skicka en färdig faktura till en kund, arkivera en kvartalsvis finansiell rapport, eller skicka in ett budgetkalkylblad till en tillsynsmyndighet. Aspose.Cells for Python via Java hanterar detta krav genom uppräkningsvärdet `SaveFormat.Ofd`, som skriver arbetsboken direkt till OFD utan att kräva ett mellanliggande konverteringssteg. OFD-utdata bevarar cellvärden, sammanslagna intervall, typsnitt, färger, kanter, talformat och sidinställningar som konfigurerats på arbetsboken.

{{% alert color="primary" %}}

OFD-utdata som genereras av Aspose.Cells for Python via Java bevarar den synliga layouten hos källarbetsboken, inklusive cellinnehåll, sammanslagna celler, kolumnbredder och radhöjder. Cellformatering som typsnitt, färger, kanter, justering och talformat renderas också i utdata med fast layout. Sidinställningar som konfigurerats på kalkylbladet, såsom pappersstorlek, orientering och utskriftsområde, påverkar layouten för det resulterande OFD-dokumentet.

{{% /alert %}}
## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells for Python via Java låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt till OFD-format med hjälp av uppräkningen `SaveFormat.Ofd`. Följande exempel skapar en faktura från grunden. Det lägger till en företagslogotyp, rubrikinformation, en "faktura till"-sektion, radobjekt och beräknade summor, och exporterar sedan arbetsboken till ett OFD-dokument.
### **Bygga en faktura med en logotyp**
Exemplet konstruerar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra området, fylla i företagsnamn och kontaktuppgifter, lägga till en "FAKTURA"-titel över sammanslagna celler, registrera fakturanummer och datum, lista faktureringskund, bygga en tabell med radobjekt med kolumner för beskrivning, antal, enhetspris och total, samt beräkna delsumma, skatt och totalsumma med cellformler. Formatering som feta rubriker, valutaformat för priser, kanter och kolumnbredder tillämpas med hjälp av `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filtillägget `.ofd` med hjälp av `SaveFormat.Ofd`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Skapa en ny arbetsbok
workbook = Workbook()

# Hämta det första kalkylbladet
worksheet = workbook.getWorksheets().get(0)

# Ställ in kolumnbredder
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Infoga företagslogotyp
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Företagsnamn och kontaktuppgifter
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# INVOICE-titel - sammanfoga celler
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# Fakturanummer och datum
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# Faktureringssektion
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# Rubrik för artiklar
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# Valutastil med kanter
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Enkel kantstil för beskrivnings-/kvantitetsceller
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Rader för artiklar
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# Delsumma, skatt, totalsumma
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Fetstil + valutastil för totalvärden
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Fetstil för totaletiketter
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells for Python via Java kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart för batchkonverteringspipelines, arkiveringsarbetsflöden och scenarier där källarbetsboken producerades av ett annat verktyg och endast behöver återutges som en artefakt med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av sidinställningar och sparar resultatet som ett OFD-dokument.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# Öppna en befintlig Excel-arbetsbok från disk
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) Läs och visa värden från valda celler för att bekräfta att filen har laddats
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) Iterera över Worksheets-samlingen för att räkna upp tillgängliga ark
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) Valfritt: uppdatera en tidsstämpelcell för att återspegla konverteringen
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Lägg till en sammanfattningsrubrikrad överst i datablocket
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Konfigurera PageSetup-egenskaper på kalkylbladet
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) Valfritt: ställ in utskriftsområdet för OFD-utdata
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **Relaterade artiklar**
- [Dela upp Excel-filer i flera filer](/cells/sv/python-java/splitting-excel-files-into-multiple-files/)
- [Infoga en bild i en cell](/cells/sv/python-java/inserting-an-image-into-a-cell/)
- [Läsa och skriva DBF-filer](/cells/sv/python-java/dbf/)
- [Konvertera Sparkline till bild och HTML i Aspose.Cells for Python via Java](/cells/sv/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}