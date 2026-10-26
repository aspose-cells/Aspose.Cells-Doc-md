---
title: Tillämpa stilar på pivottabeller i Aspose.Cells for Python via Java
linktitle: Tillämpa stilar på pivottabeller i Aspose.Cells for Python via Java
description: Lär dig hur du tillämpar inbyggda och anpassade stilar på pivottabeller i Aspose.Cells for Python via Java, inklusive äldre XLS-autoformat, moderna namngivna stilar för Excel 2007+, anpassade pivottabellstilar och genvägen formatAll.
keywords: Aspose.Cells Python via Java pivottabell stil, PivotTableStyleType, AutoFormatType, FormatAll, anpassad stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /sv/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder tillämpning av både äldre pivot-autoformat (avsedda för `.xls`-filer) och moderna namngivna eller anpassade pivottabellstilar (avsedda för `.xlsx`-, `.xlsm`- och `.xlsb`-filer). Vilket API du ska anropa beror på det filformat som arbetsboken sparas till, inte det format den lästes in från.
{{% /alert %}}

## **Introduktion**
Aspose.Cells exponerar två parallella stil-API:er för pivottabeller. Valet mellan dem styrs av det filformat du sparar arbetsboken till, inte av det format du läser in den från. En arbetsbok som lästs in från en `.xls`-fil kan sparas om som `.xlsx`, och i det fallet används det moderna stil-API:t istället för det äldre.
- `pivotTable.setPivotTableStyleType(int)` väljer en av de inbyggda namngivna stilarna (ljust och mörkt tema, inklusive de stilar som lades till i Excel 2017). Dessa förinställningar är skrivskyddade.
- `pivotTable.setPivotTableStyleName(String)` väljer en anpassad stil som du definierar själv via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Anpassade stilar krävs när du vill ändra färger, kanter eller teckensnitt utöver vad förinställningarna erbjuder.
Dessutom är `pivotTable.formatAll(Style)` en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen och åsidosätter det som har ställts in via någon av stilnamns-API:erna ovan. Detta är användbart när ett enhetligt utseende krävs oavsett underliggande tema.

## **Tillämpa ett äldre förinställt XLS-autoformat**
Metoden `setAutoFormatType` på en pivottabell accepterar ett värde från uppräkningen `com.aspose.cells.pivot.PivotTableAutoFormatType`. De tillgängliga värdena är `REPORT_1` till `REPORT_10`, `CLASSIC` och `TABLE_1` till `TABLE_10`.
Följande exempel läser in en ny arbetsbok, fyller i exempeldata för Fruit/Year/Amount, lägger till en pivottabell, tillämpar `PivotTableAutoFormatType.REPORT_5` och sparar resultatet som `.xls`.

{{% alert color="primary" %}}
**Varför inga kolumnfält?** Autoformat i rapport-serien (`Report1` till `Report10`, `Table1` till `Table10`) designades i klassisk Excel för **endimensionella pivottabeller** med endast radfält och värden — de har ingen inbyggd stil för kolumnfältsrubriker. Om din pivottabell behöver kolumnfält, använd de moderna `PivotTableStyleType`-förinställningarna från [Scenario 2](#tillämpa-en-modern-namngiven-förinställd-pivottabellstil) istället, som är designade för den tvådimensionella layout som modern Excel använder.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Scenario 1: Tillämpa ett äldre XLS förinställt autoformat
# API som används: PivotTable.AutoFormatType
# Målfilformat: .xls (äldre)
# För fullständiga exempel och datafiler, vänligen gå till https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Skapa en ny arbetsbok
workbook = Workbook()
# Hämta det första kalkylbladet
sheet = workbook.getWorksheets().get(0)
# Fylla källdata med rubrikrad (Frukt, År, Belopp)
# och 9 datarader som täcker druva, blåbär, kiwi, körsbär över 2020 och 2021
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
# Lägg till en pivottabell vid destinationscell E3, namngiven, med källintervall A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# Tilldela fält: Frukt -> Rader, Belopp -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Tillämpa det äldre XLS förinställda autoformatet "Report5"
# Obs: Den här egenskapen är endast meningsfull när du sparar som .xls.
# När det sparas som .xlsx/.xlsm/.xlsb ignorerar Excel AutoFormatType
# och använder det som PivotTableStyleType / PivotTableStyleName anger.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# Spara arbetsboken i äldre .xls-format
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Tillämpa en modern namngiven förinställd pivottabellstil**
`pivotTable.setPivotTableStyleType(int)` väljer en av de inbyggda namngivna stilen som Excel 2007 introducerade för pivottabeller. `PivotTableStyleType`-enumerationen erbjuder tre temafamiljer: ljusfamiljen från `PIVOT_TABLE_STYLE_LIGHT1` till `PIVOT_TABLE_STYLE_LIGHT28`, medelfamiljen från `PIVOT_TABLE_STYLE_MEDIUM1` till `PIVOT_TABLE_STYLE_MEDIUM28` och mörkfamiljen från `PIVOT_TABLE_STYLE_DARK1` till `PIVOT_TABLE_STYLE_DARK_28`. Den definierar även `None` och `Custom`. De högre numrerade medlemmarna i varje familj är de stilar som lades till i Excel 2017.
Dessa förinställda värden är skrivskyddade. Så snart du behöver ändra färger, linjer eller teckensnitt bort från det som en förinställning tillåter, måste du i stället definiera en anpassad pivotstil, som visas i [Scenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Varför de moderna förinställningarna och inte rapportseriens automatformat?** Värdena `Report1` till `Report10` och `Table1` till `Table10` i `PivotTableAutoFormatType` är äldre än pivotkolumnfält, så de innehåller ingen formatering för kolumnfältsrubriker, och Excel visar dessa rubriker utan formatering. `PivotTableStyleType`-förinställningarna togs fram för den tvådimensionella layout som modern Excel använder och formaterar både radfälts- och kolumnfältsrubriker.
{{% /alert %}}

Detta scenario återanvänder datasetet för Frukt/År/Mängd från scenario 1, lägger till `Year` i kolumnområdet vid sidan av radfältet `Fruit` via `PivotFieldType.COLUMN`, tillämpar mörktidsförinställningen `PIVOT_TABLE_STYLE_DARK1` med `pivotTable.setPivotTableStyleType` och sparar resultatet som `.xlsx` – formatet för vilket `PivotTableStyleType` har betydelse.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
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
# Add a pivot table at E3, sourced from A1:C10
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Definiera och tillämpa en anpassad pivottabellstil**
De inbyggda förinställningarna kan inte ändras. När du behöver åsidosätta färger, kanter eller teckensnitt måste du definiera en anpassad pivotstil. Arbetsflödet har tre steg:
1. Lägg till en anpassad stil i arbetsbokens `TableStyles`-samling via `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Detta returnerar indexet för den nyskapade stilen.
2. Konfigurera stilen genom att lägga till element (såsom `WHOLE_TABLE` eller `GRAND_TOTAL_ROW`) via `tableStyle.getTableStyleElements().add(TableStyleElementType)`, och tilldela sedan en `Style` till varje element via `tableStyleElement.setElementStyle(Style)`.
3. Tillämpa den anpassade stilen på pivottabellen genom att anropa `pivotTable.setPivotTableStyleName(String)` med stilens namn. Använd inte `setPivotTableStyleType` här, eftersom den metoden väljer inbyggda förinställningar.

{{% alert color="primary" %}}
`setPivotTableStyleName` och `setPivotTableStyleType` är inte utbytbara. Använd `setPivotTableStyleType` för inbyggda förinställningar och `setPivotTableStyleName` för anpassade stilar som du har definierat via `addPivotTableStyle`. Att ställa in båda är ofarligt, men endast den som matchar den avsedda källan renderas.
De tillgängliga `TableStyleElementType`-värdena inkluderar `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` och `PAGE_FIELD_VALUES`.
Följande exempel definierar en anpassad pivotstil med en tunn svart kant på `WHOLE_TABLE` och ett fetstilt rött teckensnitt på `GRAND_TOTAL_ROW`, tillämpar den sedan via `setPivotTableStyleName` och sparar som `.xlsx`.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Fyll i källdata: rubrikrad + 9 datarader (A1:C10)
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
# Lägg till pivottabell från A1:C10, förankrad vid E3, med namnet
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
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
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# Steg 3: lägg till ett GrandTotalRow-element och tillämpa fet röd text
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# Steg 4: tillämpa den anpassade stilen med namn (INTE via PivotTableStyleType, som är för inbyggda förinställningar)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Tillämpa en stil på varje pivotcell med formatAll**
`pivotTable.formatAll(Style)` är en genväg som tillämpar ett enda `Style`-objekt på varje cell i pivottabellen, inklusive dataområdet, rad- och kolumnrubriker samt totaler. Det som tidigare ställts in via `setPivotTableStyleType` eller `setPivotTableStyleName` åsidosätts.

{{% alert color="primary" %}}
`formatAll` åsidosätter både `setPivotTableStyleType` och `setPivotTableStyleName`. Använd det endast när ett enhetligt, temaoberoende utseende krävs i hela pivottabellen.
Följande exempel skapar en `Style` med gul solid fyllning, ett fetstilt mörkblått teckensnitt och tunna svarta kanter på alla sidor, tillämpar den sedan med `formatAll` och sparar som `.xlsx`.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Scenario 4: Tillämpa en enda Style på varje pivottabellcell med hjälp av formatAll
# API som används: PivotTable.formatAll(Style)
# Målformat: .xlsx
# GitHub-referens: se Aspose.Cells-for-.NET repository — exempel på pivottabellformatering
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Fylla på källdata: rubrikrad (rad 1) + 9 datarader (raderna 2-10)
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
# Lägg till pivottabell: källintervall A1:C10, målcell E3, namn
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Tilldela pivotfält: Fruit -> Radområde, Year -> Kolumnområde, Amount -> Dataområde
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Bygg en Style som tvingas på varje cell i pivottabellen
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# Tillämpa formatAll: tvingar denna enda stil på varje cell i pivottabellen,
# åsidosätter eventuell PivotTableStyleType / PivotTableStyleName som tidigare ställts in
pivotTable.formatAll(style)
# Spara arbetsboken i det moderna .xlsx-formatet
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Vilket stil-API ska jag använda?**
Valet av stil-API beror på vilket filformat du sparar till. Använd tabellen nedan som en snabbreferens.
| Målfilformat | API att använda | Anteckningar |
|---|---|---|
| `.xls` (äldre) | `pivotTable.setAutoFormatType(int)` | Värden från `com.aspose.cells.pivot.PivotTableAutoFormatType` (t.ex. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignoreras vid sparning som moderna format. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, inbyggd stil) | `pivotTable.setPivotTableStyleType(int)` | Värden från `com.aspose.cells.PivotTableStyleType` (ljust/mörkt tema, inklusive tillägg i Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, anpassad stil) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Använd när de inbyggda förinställningarna inte räcker. Konfigurera via `tableStyleElement.setElementStyle(Style)`. |
| Valfritt format (enhetlig åsidosättning) | `pivotTable.formatAll(Style)` | Genväg som åsidosätter alla andra stilinställningar i hela pivottabellen. |
Vid tvivel, spara som `.xlsx` och använd `setPivotTableStyleType` för inbyggda teman, eller `setPivotTableStyleName` för anpassade teman.

{{< app/cells/assistant language="python" >}}