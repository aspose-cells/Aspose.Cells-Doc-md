---
title: Tillämpa stilar på pivottabeller i Aspose.Cells för .NET
linktitle: Tillämpa pivottabellstilar
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for Python via .NET, inklusive äldre XLS-autoformat, moderna namngivna stilar för Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells Python via .NET pivottabell stil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder tillämpning av både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du bör anropa beror på det filformat som arbetsboken sparas till, inte det format den laddades från.

{{% /alert %}}

## **Introduktion**

Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser från. En arbetsbok som laddats från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet gäller det moderna stil-API:et snarare än det äldre.

För äldre `.xls`-utdata använder du egenskapen `PivotTable.auto_format_type` tillsammans med enumerationen `aspose.cells.pivot.PivotTableAutoFormatType`. Detta API motsvarar den autoformatväljare som klassisk Excel erbjöd för pivottabeller.

För moderna `.xlsx`-, `.xlsm`- och `.xlsb`-utdata finns två varianter av stil-API:

- `PivotTable.pivot_table_style_type` väljer en av de inbyggda namngivna stilarna (ljusa och mörka teman, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `PivotTable.pivot_table_style_name` väljer en anpassad stil som du själv definierar via `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Anpassade stilar krävs när du vill ändra färger, kanter eller typsnitt utöver vad förinställningarna erbjuder.

Dessutom är `PivotTable.format_all(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivoten och åsidosätter vad som än ställts in via något av stil-namns-API:erna ovan. Detta är användbart när ett enhetligt utseende krävs oavsett det underliggande temat.

## **Tillämpa ett äldre XLS-förinställt autoformat**

`PivotTable.auto_format_type` accepterar ett värde från enumerationen `aspose.cells.pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `REPORT_1` till `REPORT_10`, `CLASSIC` och `TABLE_1` till `TABLE_10`.

{{% alert color="primary" %}}

`auto_format_type` respekteras endast när arbetsboken sparas som `.xls`. När samma arbetsbok sparas som `.xlsx`, `.xlsm` eller `.xlsb` ignorerar Excel denna egenskap och faller tillbaka på inställningarna `pivot_table_style_type` och `pivot_table_style_name`.

{{% /alert %}}

Följande exempel laddar en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.REPORT_5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}

**Varför inga kolumnfält?** Autoformaten i Report-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassiska Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd formatering för kolumnfält-rubriker. Om din pivottabell behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från Scenario 2 nedan istället, som är designade för den tvådimensionella layout som moderna Excel använder.

{{% /alert %}}

```python
import aspose.cells as ac

# Scenario 1: Tillämpa ett äldre XLS-förinställt autoformat
# API som används: PivotTable.AutoFormatType
# Målfilformat: .xls (äldre)
# För fullständiga exempel och datafiler, vänligen gå till https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Skapa en ny arbetsbok
workbook = ac.Workbook()

# Hämta det första kalkylbladet
sheet = workbook.worksheets[0]

# Fyll källdata med rubrikrad (Fruit, Year, Amount)
# och 9 datarader som täcker grape, blueberry, kiwi, cherry över 2020 och 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# Lägg till en pivottabell vid destinationscell E3, med namnet "Pivot1", med källintervall A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Tilldela fält: Fruit -> Rader, Year -> Kolumner, Amount -> Data
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Tillämpa det äldre XLS-förinställda autoformatet "Report5"
# Obs: Den här egenskapen är endast meningsfull när den sparas som .xls.
# När den sparas som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
# och använder det som PivotTableStyleType / PivotTableStyleName anger.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Spara arbetsboken i äldre .xls-format
workbook.save("output.xls")
```

## **Tillämpa en modern namngiven förinställd pivottabellsstil**

`PivotTable.pivot_table_style_type` accepterar ett värde från enumerationen `aspose.cells.PivotTableStyleType`. Enumerationen täcker ljusa teman `PIVOT_TABLE_STYLE_LIGHT_1` till `PIVOT_TABLE_STYLE_LIGHT_28` och mörka teman `PIVOT_TABLE_STYLE_DARK_1` till `PIVOT_TABLE_STYLE_DARK_28`. Stilarna som lades till i Excel 2017 (den andra vågen av ljusa och mörka teman) nås via samma enumeration.

Detta är det rekommenderade API:et för alla moderna filformat. Till skillnad från det äldre autoformatet återges stilen som väljs här troget av Excel och överlever rundresor genom andra Office-verktyg.

Följande exempel använder samma Fruit/Year/Amount-data, skapar en identisk pivottabell, tillämpar `PIVOT_TABLE_STYLE_DARK_1` och sparar arbetsboken som `.xlsx`.

```python
import aspose.cells as ac

# Scenario 2: Tillämpa en modern förinställd stil från Excel 2007+ med PivotTableStyleType.
# Målfilformat: .xlsx. PivotTableStyleType-enum finns i Aspose.Cells-namnområdet
# (inte i Aspose.Cells.Pivot) — det är därför vi inte behöver någon extra using för det.
# GitHub-referens: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Huvudrad: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 datarader med Fruit / Year / Amount
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# Lägg till en pivottabell vid E3 med namnet "Pivot1", med källa från A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Tilldela pivotfält: Fruit -> Rad-område, Year -> Kolumn-område, Amount -> Data-område
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Tillämpa en modern förinställd pivotstil från Excel 2007+.
# PivotTableStyleType är det korrekta API:et för .xlsx / .xlsm / .xlsb-filer; AutoFormatType
# ignoreras av Excel för dessa format. PivotTableStyleDark1 tillhör det mörka temat
# familjen (PivotTableStyleDark1..PivotTableStyleDark28), och samma enum exponerar också de
# nyare Excel 2017 ljusa/mörka teman (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Spara som modern .xlsx — det är formatet för vilket PivotTableStyleType är meningsfullt.
workbook.save("output.xlsx")
```

## **Definiera och tillämpa en anpassad pivottabellsstil**

De inbyggda förinställningarna kan inte modifieras. När du behöver åsidosätta färger, kanter eller typsnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:

1. Lägg till en anpassad stil i arbetsbokens `table_styles`-samling via `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WHOLE_TABLE` eller `GRAND_TOTAL_ROW`) via `table_style.table_style_elements.add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `table_style_element.set_element_style(Style)`.
3. Tillämpa den anpassade stilen på pivoten genom att sätta `PivotTable.pivot_table_style_name` till stilens namn. Använd inte `pivot_table_style_type` här, eftersom den egenskapen väljer inbyggda förinställningar.

{{% alert color="primary" %}}

`pivot_table_style_name` och `pivot_table_style_type` är inte utbytbara. Använd `pivot_table_style_type` för inbyggda förinställningar, och `pivot_table_style_name` för anpassade stilar som du har definierat via `add_pivot_table_style`. Att sätta båda är ofarligt, men det är bara den som matchar den avsedda källan som återges.

{{% /alert %}}

De tillgängliga `TableStyleElementType`-värdena inkluderar `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` och `PAGE_FIELD_VALUES`.

Följande exempel definierar en anpassad pivotstil med en tunn svart kant på `WHOLE_TABLE` och ett fetstilt rött typsnitt på `GRAND_TOTAL_ROW`, och tillämpar den sedan via `pivot_table_style_name` och sparar som `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fyll i källdata: rubrikrad + 9 datarader (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# Lägg till pivottabell med källa från A1:C10, förankrad vid E3, med namnet "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Steg 1: registrera en ny anpassad pivottabellstil och fånga dess index
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# Steg 2: lägg till ett WholeTable-element och tillämpa tunna svarta kanter på alla fyra sidor
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd text
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# Steg 4: tillämpa den anpassade stilen efter namn (INTE efter PivotTableStyleType, vilket är för inbyggda förinställningar)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **Tillämpa en stil på varje pivotcell med FormatAll**

`PivotTable.format_all(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totalsummor. Vad som tidigare ställts in via `pivot_table_style_type` eller `pivot_table_style_name` åsidosätts.

{{% alert color="primary" %}}

`format_all` åsidosätter både `pivot_table_style_type` och `pivot_table_style_name`. Använd det endast när ett enhetligt, temaoberoende utseende krävs över hela pivoten.

{{% /alert %}}

Följande exempel skapar en `Style` med en gul solid fyllning, ett fetstilt mörkblått typsnitt och tunna svarta kanter på alla sidor, och tillämpar den sedan med `format_all` och sparar som `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Scenario 4: Tillämpa en enda Stil på varje pivottabellcell med FormatAll
# API som används: PivotTable.FormatAll(Style)
# Målformat: .xlsx
# GitHub-referens: se Aspose.Cells-for-.NET-arkivet — exempel på pivottabellstil

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fyll i källdata: rubrikrad (rad 1) + 9 datarader (raderna 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Lägg till pivottabell: källområde A1:C10, målcell E3, namn "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Tilldela pivotfält: Fruit -> Rad-område, Year -> Kolumn-område, Amount -> Data-område
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Bygg en Stil som kommer att tvingas på varje cell i pivottabellen
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# Tillämpa FormatAll: tvingar denna enda stil på varje cell i pivottabellen,
# och åsidosätter eventuell PivotTableStyleType / PivotTableStyleName som tidigare ställts in
pivot_table.format_all(style)

# Spara arbetsboken i det moderna .xlsx-formatet
workbook.save("output.xlsx")
```

## **Vilket stil-API bör jag använda?**

Valet av stil-API beror på det filformat du sparar till. Använd tabellen nedan som en snabbreferens.

| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `PivotTable.auto_format_type` | Värden från `aspose.cells.pivot.PivotTableAutoFormatType` (t.ex. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoreras vid sparande som moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `PivotTable.pivot_table_style_type` | Värden från `aspose.cells.PivotTableStyleType` (ljusa/mörka teman, inklusive tillägg från Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `table_style_element.set_element_style(...)`. |
| Valfritt format (enhetlig åsidosättning) | `PivotTable.format_all(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivoten. |

Vid tveksamhet, spara som `.xlsx` och använd `pivot_table_style_type` för inbyggda teman, eller `pivot_table_style_name` för anpassade teman.

{{< app/cells/assistant language="python" >}}