---
title: Diskret gruppering av pivotfältsobjekt
linktitle: Diskret gruppering
description: Lär dig hur du grupperar pivotfältsobjekt i anpassade grupper med egna namn, till exempel frukt och grönsaker, med DiscreteGroupItem och pivot_field_group_options.discrete_group_items i Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppering av pivotobjekt, anpassade grupper, PivotField.group, Python, Excel-pivottabell
type: docs
weight: 90
url: /sv/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering grupperar objekt efter datatyp, till exempel datum i månader och kvartal eller tal i intervall. Diskret gruppering löser det motsatta problemet genom att samla specifika, orelaterade objekt i anpassade grupper med egna namn, till exempel produkter i frukt och grönsaker, butiker i regioner eller konton i zoner. Aspose.Cells erbjuder diskret gruppering via klassen `DiscreteGroupItem` och egenskapen `pivot_field_group_options.discrete_group_items`.
- En `DiscreteGroupItem` består av ett gruppnamn och de objekt som tillhör gruppen. Objekten kan identifieras på två sätt: med sina namn (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) eller med sina nollbaserade positioner i källdatan (`DiscreteGroupItem("fruit", [0, 3])`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i rad- eller kolumnområdet i pivottabellen genom att skicka grupperingsalternativen till `pivot_field.group(PivotFieldGroupOptions)`.

## **Gruppera objekt i pivotfält efter objektnamn**
Följande exempel bygger en liten försäljningslista (produkt, datum och belopp), skapar en pivottabell från den med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet och definierar sedan två anpassade grupper utifrån objektnamnen: `fruit` (`grape`, `cherry`) och `vegetables` (`carrot`, `potato`). Resultatet visar en tvånivåindelning i radområdet där gruppnamnet utgör den yttre nivån och de ursprungliga objekten är nästlade under gruppnamnet, så att trender kan utläsas för varje anpassad grupp och varje objekt.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

Efter att `calculate_data()` har körts visar pivottabellens radområde `fruit` (`grape` 50, `cherry` 80) och `vegetable` (`carrot` 60, `potato` 70), och totalsumman är 260. Kolumnrubrikerna visar fortfarande de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera objekt i pivotfält efter objektindex**
När objektnamnen är långa eller lokaliserade identifierar den andra konstruktorn för `DiscreteGroupItem` objekten med index. Indexen anger de nollbaserade positionerna för objekten i den ordning de förekommer i källdatan, inte i alfabetisk ordning. I exemplets datamängd ovan har `grape` index 0, `carrot` index 1, `potato` index 2 och `cherry` index 3, så att `fruit` är `{ 0, 3 }` och `vegetable` är `{ 1, 2 }`. Resultatet är detsamma som i exemplet baserat på namn.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Anmärkning**

{{% alert color="primary" %}}
- Objekt som inte tilldelas någon anpassad grupp förloras inte. De förblir i pivottabellen på samma nivå som de anpassade grupperna, där de förekommer som egna poster med ett objekt vardera. I exemplet ovan lämnar definitionen av endast gruppen `fruit` `carrot` och `potato` kvar i radområdet som fristående poster bredvid gruppen `fruit`.
- Egenskapen `pivot_field_group_options.new_pivot_field` styr layouten för diskret gruppering. Standardvärdet är `True`, vilket lägger till det fält som grupperats som ett nytt yttre fält bredvid originalfältet och skapar den tvånivåindelning som visas ovan (`row_fields` växer till 2). Ange värdet till `False` för att i stället ersätta originalfältet. Radområdet visar då en enda nivå med endast gruppnamnen och deras aggregerade värden: `fruit` 130 (50 + 80) och `vegetable` 130 (60 + 70).
- De namnbaserade och indexbaserade konstruktorerna för `DiscreteGroupItem` kan kombineras i samma `discrete_group_items`-lista.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/python-net/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabellen](/cells/sv/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-net/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa format på pivottabell](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}