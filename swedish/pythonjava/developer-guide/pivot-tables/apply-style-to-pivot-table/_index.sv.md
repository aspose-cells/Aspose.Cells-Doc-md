---
title: Tillämpa stilar på pivottabeller
linktitle: Tillämpa stilar på pivottabeller
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for Python via Java, inklusive äldre XLS-autoformat, moderna namngivna stilar för Excel 2007+, anpassade pivottabellstilar och genvägen FormatAll.
keywords: Aspose.Cells Python via Java pivottabell stil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder tillämpning av både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du ska anropa beror på filformatet som arbetsboken sparas till, inte formatet den lästes från.

{{% /alert %}}

## **Introduktion**

Aspose.Cells tillhandahåller två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av filformatet du sparar arbetsboken till, inte av formatet du läser den från. En arbetsbok som lästs från en `.xls`-fil kan sparas om som `.xlsx`, och i så fall gäller det moderna stil-API:et snarare än det äldre.

För äldre `.xls`-utdata, använd metoden `pivotTable.setAutoFormatType(int)` tillsammans med enumerationen `com.aspose.cells.pivot.PivotTableAutoFormatType`. Detta API motsvarar den autoformatväljare som klassisk Excel erbjöd för pivottabeller.

För modern `.xlsx`-, `.xlsm`- och `.xlsb`-utdata finns två varianter av stil-API:er:

- `pivotTable.setPivotTableStyleType(int)` väljer en av de inbyggda namngivna stilarna (ljust och mörkt tema, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `pivotTable.setPivotTableStyleName(String)` väljer en anpassad stil som du själv definierar via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Anpassade stilar krävs när du vill ändra färger, kanter eller typsnitt utöver vad förinställningarna tillhandahåller.

Dessutom är `pivotTable.formatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen och åsidosätter vad som än har ställts in via något av stilnamns-API:erna ovan. Detta är användbart när ett enhetligt utseende krävs oavsett det underliggande temat.

## **Tillämpa ett äldre XLS-förinställt autoformat**

Metoden `setAutoFormatType` på en pivottabell accepterar ett värde från enumerationen `com.aspose.cells.pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `REPORT_1` till `REPORT_10`, `CLASSIC`, samt `TABLE_1` till `TABLE_10`.

{{% alert color="primary" %}}

`setAutoFormatType` respekteras endast när arbetsboken sparas som `.xls`. När samma arbetsbok sparas som `.xlsx`, `.xlsm` eller `.xlsb` ignorerar Excel denna inställning och faller tillbaka på inställningarna `setPivotTableStyleType` och `setPivotTableStyleName`.

{{% /alert %}}

Följande exempel laddar en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.REPORT_5` och sparar resultatet som `.xls`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Scenario 1: Tillämpa en äldre XLS-förinställd autoformat
# API som används: PivotTable.AutoFormatType
# Målfilformat: .xls (äldre)
# För fullständiga exempel och datafiler, vänligen gå till https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Skapa en ny arbetsbok
workbook = Workbook()

# Hämta det första arbetsbladet
sheet = workbook.getWorksheets().get(0)

# Fylla källdatan med rubrikrad (Fruit, Year, Amount)
# och 9 datarader som täcker grape, blueberry, kiwi, cherry över 2020 och 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")

sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)

sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)

sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)

sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)

sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)

sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)

sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)

sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)

sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)

# Lägg till en pivottabell vid destinationscell E3, med namnet "Pivot1", med källintervall A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Tilldela fält: Fruit -> Rader, Year -> Kolumner, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Tillämpa den äldre XLS-förinställda autoformaten "Report5"
# Obs: Den här egenskapen är endast meningsfull när man sparar som .xls.
# När det sparas som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
# och använder det som PivotTableStyleType / PivotTableStyleName anger.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Spara arbetsboken i äldre .xls-format
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Tillämpa en modern namngiven förinställd pivottabellstil**

Metoden `setPivotTableStyleType` på en pivottabell accepterar ett värde från enumerationen `com.aspose.cells.PivotTableStyleType`. Enumerationen omfattar ljusa teman `PIVOT_TABLE_STYLE_LIGHT_1` till `PIVOT_TABLE_STYLE_LIGHT_28` och mörka teman `PIVOT_TABLE_STYLE_DARK_1` till `PIVOT_TABLE_STYLE_DARK_28`. Stilarna som lades till i Excel 2017 (den andra vågen av ljusa och mörka teman) nås via samma enumeration.

Detta är det rekommenderade API:et för alla moderna filformat. Till skillnad från det äldre autoformatet återges stilen som väljs här troget av Excel och överlever rundresor genom andra Office-verktyg.

Följande exempel använder samma Fruit/Year/Amount-data, skapar en identisk pivottabell, tillämpar `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1` och sparar arbetsboken som `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Scenario 2: Tillämpa en modern namngiven förinställd stil för Excel 2007+ med PivotTableStyleType.
# Målfilformat: .xlsx. PivotTableStyleType-uppräkningen finns i Aspose.Cells-namnrymden
# (inte i Aspose.Cells.Pivot) — det är därför vi inte behöver någon extra using för det.
# GitHub-referens: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Huvudrad: Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 datarader med Frukt / År / Belopp
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)

# Lägg till en pivottabell vid E3 med namnet "Pivot1", baserad på A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Tilldela pivotfält: Frukt -> Rad-område, År -> Kolumn-område, Belopp -> Data-område
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Tillämpa en modern namngiven förinställd pivotstil för Excel 2007+.
# PivotTableStyleType är det korrekta API:et för .xlsx / .xlsm / .xlsb-filer; AutoFormatType
# ignoreras av Excel för dessa format. PivotTableStyleDark1 tillhör det mörka temat
# (PivotTableStyleDark1..PivotTableStyleDark28), och samma uppräkning exponerar också de
# nyare ljusa/mörka teman för Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Spara som modern .xlsx — detta är det format för vilket PivotTableStyleType är meningsfullt.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Definiera och tillämpa en anpassad pivottabellstil**

De inbyggda förinställningarna kan inte ändras. När du behöver åsidosätta färger, kanter eller typsnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:

1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WHOLE_TABLE` eller `GRAND_TOTAL_ROW`) via `tableStyle.getTableStyleElements().add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `tableStyleElement.setElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivoten genom att anropa `pivotTable.setPivotTableStyleName(String)` med stilens namn. Använd inte `setPivotTableStyleType` här, eftersom den metoden väljer inbyggda förinställningar.

{{% alert color="primary" %}}

`setPivotTableStyleName` och `setPivotTableStyleType` är inte utbytbara. Använd `setPivotTableStyleType` för inbyggda förinställningar, och `setPivotTableStyleName` för anpassade stilar som du har definierat via `addPivotTableStyle`. Att ställa in båda är ofarligt, men endast den som matchar den avsedda källan renderas.

{{% /alert %}}

De tillgängliga värdena för `TableStyleElementType` inkluderar `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` och `PAGE_FIELD_VALUES`.

Följande exempel definierar en anpassad pivotstil med en tunn svart kant på `WHOLE_TABLE` och ett fet rött typsnitt på `GRAND_TOTAL_ROW`, och tillämpar den sedan via `setPivotTableStyleName` och sparar som `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Populera källdata: rubrikrad + 9 datarader (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# Lägg till pivottabell från A1:C10, förankrad vid E3, namngiven "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Steg 1: registrera en ny anpassad pivottabellstil och fånga dess index
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# Steg 2: lägg till ett WholeTable-element och tillämpa tunna svarta kanter på alla fyra sidor
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd teckensnitt
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Steg 4: tillämpa den anpassade stilen med namn (INTE med PivotTableStyleType, vilket är för inbyggda förinställningar)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Tillämpa en stil på varje pivotcell med FormatAll**

`pivotTable.formatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totaler. Vad som tidigare ställts in via `setPivotTableStyleType` eller `setPivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}

`formatAll` åsidosätter både `setPivotTableStyleType` och `setPivotTableStyleName`. Använd det endast när ett enhetligt, temaneutralt utseende krävs över hela pivoten.

{{% /alert %}}

Följande exempel skapar en `Style` med gul solid fyllning, ett fet mörkblått typsnitt och tunna svarta kanter på alla sidor, och tillämpar den sedan med `formatAll` och sparar som `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Scenario 4: Tillämpa en enda Stil på varje pivottabellcell med hjälp av FormatAll
# API som används: PivotTable.FormatAll(Style)
# Målformat: .xlsx
# GitHub-referens: se Aspose.Cells-for-.NET repository — exempel på pivottabellformatering

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Fylla i källdata: rubrikrad (rad 1) + 9 datarader (rad 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)

# Lägg till pivottabell: källområde A1:C10, målcell E3, namn "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Tilldela pivotfält: Fruit -> Rad-område, Year -> Kolumn-område, Amount -> Data-område
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Bygg en Stil som kommer att tvingas på varje cell i pivottabellen
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# Tillämpa FormatAll: tvingar denna enda stil på varje cell i pivottabellen,
# åsidosätter alla PivotTableStyleType / PivotTableStyleName som tidigare satts
pivotTable.formatAll(style)

# Spara arbetsboken i det moderna .xlsx-formatet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Vilket stil-API ska jag använda?**

Valet av stil-API beror på filformatet du sparar till. Använd tabellen nedan som en snabbreferens.

| Filformat för mål | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `pivotTable.setAutoFormatType(int)` | Värden från `com.aspose.cells.pivot.PivotTableAutoFormatType` (t.ex. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoreras vid sparning som moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modernt, inbyggd stil) | `pivotTable.setPivotTableStyleType(int)` | Värden från `com.aspose.cells.PivotTableStyleType` (ljust/mörkt tema, inklusive tillägg i Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modernt, anpassad stil) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `tableStyleElement.setElementStyle(Style)`. |
| Valfritt format (enhetlig åsidosättning) | `pivotTable.formatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar över hela pivoten. |

Vid tveksamhet, spara som `.xlsx` och använd `setPivotTableStyleType` för inbyggda teman, eller `setPivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="python" >}}