---
title: Diskret gruppering av objekt i pivotfält
linktitle: Diskret gruppering
description: Lär dig hur du grupperar objekt i pivotfält till anpassade grupper med egna namn, till exempel frukt och grönsaker, med hjälp av DiscreteGroupItem och PivotFieldGroupOptions.getDiscreteGroupItems i Aspose.Cells for Python via Java.
keywords: Aspose.Cells, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera objekt i pivotfält, anpassade grupper, PivotField.group, Python via Java, Excel-pivottabell
type: docs
weight: 90
url: /sv/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering samlar objekt efter datatyp, till exempel datum till månader och kvartal eller tal till intervall. Diskret gruppering löser det motsatta problemet genom att samla specifika, orelaterade objekt i anpassade grupper med egna namn, till exempel produkter till frukt och grönsaker, butiker till regioner eller konton till zoner. Aspose.Cells erbjuder diskret gruppering med hjälp av klassen `DiscreteGroupItem` och metoden `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- En `DiscreteGroupItem` består av ett gruppnamn och de objekt som tillhör gruppen. Objekten kan identifieras på två sätt: med sina namn (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) eller med sina nollbaserade positioner i källdatan (`DiscreteGroupItem("fruit", [0, 3])`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i pivottabellens rad- eller kolumnområde genom att skicka grupperingsalternativet till `PivotField.group(PivotFieldGroupOptions)`.

## **Gruppera pivotfältsobjekt efter objektnamn**
Exemplet nedan bygger en liten försäljningslista (produkt, datum och belopp), skapar en pivottabell utifrån listan med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet och definierar sedan två anpassade grupper utifrån objektnamnen: frukt (druvor, körsbär) och grönsaker (morot, potatis). Resultatet visar en radlayout med två nivåer där gruppnamnet utgör den yttre nivån och de ursprungliga objekten är nästlade under den, så att trender kan läsas ut för varje anpassad grupp och varje objekt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

Efter `calculateData()` visar pivottabellens radområde frukt (druvor 50, körsbär 80) och grönsaker (morot 60, potatis 70) med en totalsumma på 260, och kolumnrubrikerna visar fortfarande de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera pivotfältsobjekt efter objektindex**
När objektnamnen är långa eller lokaliserade identifierar den andra konstruktorn för `DiscreteGroupItem` objekten med hjälp av index. Indexvärdena är nollbaserade positioner för objekten i den ordning de förekommer i källdatan, inte i alfabetisk ordning. I exempledata ovan är druvor objekt 0, morot objekt 1, potatis objekt 2 och körsbär objekt 3. Därför är frukt `{ 0, 3 }` och grönsaker `{ 1, 2 }`. Resultatet är identiskt med resultatet i exemplet baserat på namn.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Obs**

{{% alert color="primary" %}}
- Objekt som inte har tilldelats någon anpassad grupp behålls. De finns kvar i pivottabellen på samma nivå som de anpassade grupperna, med varje objekt som en separat post. I exemplet ovan innebär en definition av endast fruktgruppen att morot och potatis finns kvar i radområdet som fristående poster bredvid fruktgruppen.
- Metoderna `PivotFieldGroupOptions.getNewPivotField()` och `setNewPivotField()` styr layouten för diskret gruppering. `getNewPivotField()` har standardvärdet `true`, vilket lägger till det grupperade fältet som ett nytt yttre fält bredvid det ursprungliga fältet och skapar den layout med två nivåer som visas ovan (antalet fält som returneras av `getRowFields()` ökar till 2). Använd `setNewPivotField(false)` för att i stället ersätta det ursprungliga fältet. Radområdet visar då en enda nivå som endast innehåller gruppnamnen med deras aggregerade värden: frukt 130 (50 + 80) och grönsaker 130 (60 + 70).
- De namn- och indexbaserade konstruktorerna för `DiscreteGroupItem` kan kombineras i samma `getDiscreteGroupItems()`-samling.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/python-java/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa formatering på pivottabellen](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}