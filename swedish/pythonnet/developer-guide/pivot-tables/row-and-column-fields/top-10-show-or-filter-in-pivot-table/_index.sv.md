---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig hur du endast visar de högst eller lägst rankade objekten i ett pivotfält i Aspose.Cells for Python via .NET. Den här artikeln beskriver metoden top_10_auto_show för Excel 97-2003, hur du läser alternativ med top_10_auto_show_settings och Top 10-filtret för Excel 2007-365 via filter_top10.
keywords: Aspose.Cells, Python via .NET, pivottabell, topp 10, automatisk visning, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /sv/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst om fältet innehåller tiotals objekt. En topp 10-rapport behåller endast de högst eller lägst rankade objekten, vilket är exakt vad rangordningsrapporter behöver – "de fem produkterna med högst intäkt" eller "de tre regionerna med minst antal försäljningar". Aspose.Cells stöder två mekanismer för detta, som motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – metoden `PivotField.top_10_auto_show()`. Detta är den klassiska inställningen "Visa de översta/nedersta N objekten" som lagras direkt på pivotfältet. Den fungerar i alla Excel-versioner, gamla som nya, eftersom den ingår i det ursprungliga formatet för pivottabeller.
- **Excel 2007-365 Top 10-filter** – metoden `PivotField.filter_top10()`. Detta är det moderna värdefiltret Top 10 som finns under Värdefilter i fältmenyn. Filtret lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rankning baserad på antal objekt eller procent.

## **Visa topp 10 i Excel 97-2003 (top_10_auto_show)**
Det klassiska AutoShow konfigureras med ett enda anrop till `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`:
- `is_auto_show` – aktiverar eller inaktiverar inställningen AutoShow för fältet.
- `is_top` – `True` behåller de högst rankade objekten (Topp), medan `False` behåller de lägst rankade objekten (Botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rank_by` – det nollbaserade indexet för det **datafält** vars värden används för att rangordna objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rangordningen kan baseras på ett värdefält eller på fältet självt. Här visas två möjliga varianter.

### **Rangordna efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel `Sum of Sales`. Följande exempel bygger en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`) och visar sedan de två sportsorterna med högst försäljning. `rank_by` är 0 eftersom `Sum of Sales` är datafältet på index 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Visa de 2 bästa objekten rankade efter "Sum of Sales" (datafältsindex 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Rangordna efter fältet självt**
Ett fält kan också rangordnas efter sig självt – ange -1 som `rank_by`. Inga extra datafält behövs för den här varianten; fältet behöver bara finnas i rad- eller kolumnområdet. Följande exempel visar de tre sportsorterna som rankas lägst enligt fältet självt. När den här inställningen sparas utelämnas attributet `rank_by` från pivottabellens XML eftersom -1 är formatets standardvärde, och `top_10_auto_show_settings.rank_by` returnerar -1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Läsa aktuella alternativ (top_10_auto_show_settings)**
Egenskapen `PivotField.top_10_auto_show_settings` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som innehåller de AutoShow-alternativ som för närvarande lagras på fältet. Använd det för att granska hur en befintlig arbetsbok eller en pivottabell som du nyligen har konfigurerat visar sina objekt, inklusive i arbetsböcker som har lästs in från en fil.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), så att de återlästa värden är de som alla Excel-versioner respekterar.

## **Obs**

{{% alert color="primary" %}}
- De direkta `PivotField`-egenskaperna `is_auto_show`, `is_ascend_show`, `auto_show_count` och `auto_show_field` är föråldrade. Använd objektet `top_10_auto_show_settings` i stället: `is_auto_show` motsvarar `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` motsvarar `top_10_auto_show_settings.is_top`, `auto_show_count` motsvarar `top_10_auto_show_settings.auto_show_count` och `auto_show_field` motsvarar `top_10_auto_show_settings.rank_by`. Använd metoden `top_10_auto_show()` för att ändra inställningarna.
- `top_10_auto_show` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidsområdet (filterområdet) kan inte rangordnas på detta sätt eftersom dess objekt inte är utplacerade i pivottabellens innehåll.
{{% /alert %}}

## **Excel 2007-365: Top 10-filter (filter_top10)**
I moderna Excel-versioner visas Top 10 som ett värdefilter i fältmenyn (Värdefilter, Topp 10...). Aspose.Cells representerar det med metoden `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)`, som returnerar det skapade `PivotFilter`-objektet:
- `value_field_index` – det nollbaserade indexet för datafältet vars aggregerade värden används för att rangordna objekten.
- `type` – vad `item_count` betyder. `PivotFilterType.COUNT` behåller ett bestämt antal objekt (alternativet Objekt i dialogrutan). `PivotFilterType.PERCENT` behåller en procentandel av objekten, så att `item_count` är själva procentandelen – 30 behåller de översta 30 procenten. `PivotFilterType.SUM` rangordnar utifrån den kumulativa värdevolym som omfattas.
- `is_top` – `True` för Topp, `False` för Botten.
- `item_count` – N i Topp N; enheten beror på `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Topp 10-filter — behåll de 2 bästa objekten enligt "Sum of Sales" (datfältsindex 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# För ett procentbaserat filter i stället, behåll de bästa 30 procent av objekten:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` och `filter_top10` är två separata funktioner. AutoShow skriver det klassiska `autoShow`-attributet till pivotfältet och respekteras av alla Excel-versioner ända tillbaka till Excel 97. `filter_top10` skriver en modern `PivotFilter`-post, vilket kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visar en pivottabell som använder det moderna filtret alla objekt i stället. För dokument som måste överföras fram och tillbaka med äldre verktyg bör du använda `top_10_auto_show`; för moderna arbetsböcker bör du använda `filter_top10` eftersom filtret kan kombineras med andra värdefilter.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/python-net/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/python-net/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/python-net/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/python-net/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}