---
title: Konvertera Excel till OFD-format
linktitle: Konvertera Excel till OFD-format
description: Aspose.Cells for Python via .NET är ett kalkylbladsbibliotek som stöder konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document). Den här artikeln visar hur man skapar Excel-innehåll och exporterar det som OFD, samt hur man konverterar befintliga Excel-filer till OFD med hjälp av Aspose.Cells.
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, Excel till OFD, OFD-konvertering, SaveFormat.Ofd, dokument med fast layout, arbetsboksexport
type: docs
weight: 195
url: /sv/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder direkt konvertering av Excel-arbetsböcker till OFD-format (Open Fixed-layout Document) med hjälp av `SaveFormat.Ofd`-uppräkningsvärdet. Det resulterande OFD-dokumentet bevarar arbetsbokens synliga layout, innehåll, sammanfogade celler, kolumnbredder, radhöjder, typsnitt, färger, kanter och talformat. Detta gör Aspose.Cells lämpligt för arkivering, utskrift, regulatorisk inlämning och myndighetsinlämning som kräver en fast layout.

{{% /alert %}}
## **Introduktion**
OFD (Open Fixed-layout Document) är en kinesisk nationell standard (GB/T 33190-2016) för att representera digitala dokument i en fast, sidbaserad layout. Den fyller en roll som liknar PDF för användningsfall där det visuella utseendet på källdokumentet måste bevaras exakt som det skapades. OFD används i stor utsträckning för myndighetsinlämningar, regulatoriska inlämningar, elektroniska fakturor och långtidsarkivering i Folkrepubliken Kina.

Att konvertera Excel-arbetsböcker till OFD är ett vanligt krav i scenarier där kalkylbladsinnehåll måste distribueras som ett skrivskyddat, layoutlåst dokument snarare än som ett redigerbart kalkylblad. Exempel inkluderar att skicka en slutförd faktura till en kund, arkivera en kvartalsvis ekonomisk rapport eller lämna in ett budgetkalkylblad till en tillsynsmyndighet. Aspose.Cells hanterar detta krav genom `SaveFormat.Ofd`-uppräkningsvärdet, som skriver arbetsboken direkt till OFD utan att kräva ett mellanliggande konverteringssteg. OFD-utdata bevarar cellvärden, sammanfogade intervall, typsnitt, färger, kanter, talformat och sidlayoutsalternativ som konfigurerats på arbetsboken.

{{% alert color="primary" %}}

OFD-utdata som genereras av Aspose.Cells bevarar den synliga layouten för källarbetsboken, inklusive cellinnehåll, sammanfogade celler, kolumnbredder och radhöjder. Cellformatering som typsnitt, färger, kanter, justering och talformat renderas också i utdata med fast layout. Sidlayoutsalternativ som konfigurerats på kalkylbladet, såsom pappersstorlek, orientering och utskriftsområde, påverkar layouten för det resulterande OFD-dokumentet.

{{% /alert %}}
## **Skapa en Excel-arbetsbok och spara som OFD**
Aspose.Cells låter dig bygga en arbetsbok programmatiskt, fylla den med data och sedan spara den direkt i OFD-format med hjälp av `SaveFormat.Ofd`-uppräkningsvärdet. Följande exempel skapar en faktura från grunden. Den lägger till en företagslogotyp, rubrikinformation, en faktura-till-sektion, rader av artiklar och beräknade summor, och exporterar sedan arbetsboken till ett OFD-dokument.
### **Bygga en faktura med en logotyp**
Exemplet konstruerar ett fakturakalkylblad genom att infoga en logotypbild i det övre vänstra området, fylla i företagsnamn och kontaktuppgifter, lägga till en "INVOICE"-titel över sammanfogade celler, registrera fakturanummer och datum, lista fakturamottagaren, bygga en radartabell med beskrivning, kvantitet, styckpris och totalsumma-kolumner, samt beräkna delsumma, skatt och totalsumma med hjälp av cellformler. Formatering som feta rubriker, valutaformat för priser, kanter och kolumnbredder tillämpas med hjälp av `Style`- och `Font`-objekt. Slutligen sparas arbetsboken med filändelsen `.ofd` med hjälp av `SaveFormat.Ofd`.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# Skapa en ny arbetsbok
workbook = ac.Workbook()

# Hämta det första arbetsbladet
worksheet = workbook.worksheets[0]

# Ange kolumnbredder
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# Infoga företagslogotyp
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# Företagsnamn och kontaktuppgifter
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# FAKTURAtitel - sammanfoga celler
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# Fakturanummer och datum
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# Faktura till-sektion
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# Rubrik för radartiklar
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# Valutastil med kanter
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Enkel kantstil för beskrivnings-/kvantitetsceller
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Rader för radartiklar
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# Delsumma, skatt, totalsumma
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# Fetstil + valutastil för totalvärden
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# Fetstil för totaletiketter
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# Spara arbetsboken som en OFD-fil
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **Konvertera en befintlig Excel-fil till OFD**
Aspose.Cells kan också läsa in en befintlig Excel-arbetsbok från disk och exportera den direkt till OFD-format. Detta är användbart för batchkonverteringsflöden, arkiveringsflöden och scenarier där källarbetsboken producerades av ett annat verktyg och bara behöver återutges som ett dokument med fast layout. Följande exempel läser in en befintlig `.xlsx`-arbetsbok, läser data från dess celler, tillämpar valfria justeringar av sidlayouten och sparar resultatet som ett OFD-dokument.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# Öppna en befintlig Excel-arbetsbok från disk
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) Läs och visa värden från valda celler för att bekräfta att filen laddades
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Iterera över Worksheets-samlingen för att räkna upp tillgängliga blad
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) Valfritt: uppdatera en tidsstämpelcell för att återspegla konverteringen
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Lägg till en sammanfattningsrubrikrad överst i datablocket
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Konfigurera PageSetup-egenskaper på kalkylbladet
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) Valfritt: ställ in utskriftsområdet för OFD-utdata
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) Spara arbetsboken som en OFD-fil
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Relaterade artiklar**
- [Dela upp Excel-filer i flera filer](/cells/sv/python-net/splitting-excel-files-into-multiple-files/)
- [Infoga en bild i en cell](/cells/sv/python-net/inserting-an-image-into-a-cell/)
- [Läsa och skriva DBF-filer](/cells/sv/python-net/dbf/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Python via .NET](/cells/sv/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}