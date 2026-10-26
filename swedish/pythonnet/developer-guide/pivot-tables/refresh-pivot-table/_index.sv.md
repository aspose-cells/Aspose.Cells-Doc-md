---
title: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Python via .NET
linktitle: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Python via .NET
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via .NET med hjälp av v26.7+ pivot-uppdaterings-API,et. Den här artikeln täcker refresh_all, _refresh_pivot_tables, PivotCache.refresh, _calculate_data och _get_pivot_tables med praktiska kodexempel.
keywords: Aspose.Cells, Python via .NET, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett lagerindelat uppdaterings-API som låter dig ladda om pivotdata i fyra olika omfattningar — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Python via .NET v26.7** är den äldre metoden `PivotTable.refresh_data()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.
{{% /alert %}}

## Introduction
Att uppdatera en pivottabell är sällan en enskild åtgärd. Bakom kulisserna underhåller Aspose.Cells en lagerindelad datakedja som kopplar samman dina ursprungliga källdata till de renderade värdena du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyrlagers datakedjan är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallerna, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden av källdatan i minnet. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **Pivottabell** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Celler** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

{{% alert color="primary" %}}
`PivotCache.source_type` (enum `PivotTableSourceType`) anger var cachedatan kom ifrån. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar etc.) kan ännu inte uppdateras via cache-API:et.
På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculate_data()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i denna artikel använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar som beskrivs.
{{% /alert %}}

## Quick Start
Om du bara behöver den kortaste möjliga koden som uppdaterar varje pivot i arbetsboken, räcker det med ett enda anrop:

```python
import aspose.cells as ac

workbook = ac.Workbook("input.xlsx")
workbook.refresh_all()
workbook.save("output.xlsx")
```

Allt annat i denna artikel förklarar när du ska välja ett snävare API istället.

## Required Imports
Alla Python-exempel i denna artikel börjar med följande tre import-satser eftersom pivottyperna finns i namnrymden `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Refresh All Pivot Tables in the Workbook
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest omfattande API:et `Workbook.refresh_all()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett bekymmer.
Följande exempel bygger en arbetsbok med ett källintervall för Frukt/År/Belopp, skapar en pivottabell, ändrar några källvärden och använder sedan `refresh_all()` för att uppdatera allt i ett enda anrop.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
# Create a new workbook
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write header row into cells A1:C1
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(50)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(60)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(70)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(80)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(90)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(100)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(110)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(120)
# Add a pivot table: source range "A1:C9", destination cell "E3"
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.cells.get("C2").put_value(55)
worksheet.cells.get("C5").put_value(85)
worksheet.cells.get("C9").put_value(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refresh_all()
# Save the workbook
workbook.save("output.xlsx")
```

## Refresh All Pivot Tables on a Single Worksheet
Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refresh_pivot_tables()`, som är begränsat till en enskild `Worksheet`-instans.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("blueberry")
worksheet.cells.get("B3").put_value(2021)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("cherry")
worksheet.cells.get("B5").put_value(2021)
worksheet.cells.get("C5").put_value(120)
worksheet.cells.get("A6").put_value("grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(180)
worksheet.cells.get("A7").put_value("blueberry")
worksheet.cells.get("B7").put_value(2020)
worksheet.cells.get("C7").put_value(130)
worksheet.cells.get("A8").put_value("kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(220)
worksheet.cells.get("A9").put_value("cherry")
worksheet.cells.get("B9").put_value(2020)
worksheet.cells.get("C9").put_value(140)
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
worksheet.cells.get("C2").put_value(300)
worksheet.cells.get("C5").put_value(250)
worksheet.cells.get("C9").put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Refresh a Single Pivot Table
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt ändrades: underliggande källdata, eller bara vy-/layoutinställningarna för pivottabellen själv.

### Source Data Changed — Use `PivotCache.refresh()`
Om underliggande källdata har ändrats är rätt ingångspunkt `pivot_table.pivot_cache.refresh()`. Detta anrop läser om källdatan till cachen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Only View/Layout Changed — Use `calculate_data()`
Om källdatan *inte* har ändrats men bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en refresh-on-open-inställning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen har redan rätt data; bara den renderade `PivotTable` behöver beräknas om. I detta fall är `pivot_table.calculate_data()` rätt val.
Följande exempel modifierar en icke-källegenskap för pivottabellen och anropar sedan `calculate_data()` för att rendera om den från den befintliga cachen.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Write Fruit / Year / Amount header row
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(150)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(250)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(350)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(450)
# Add a pivot table placed at destination cell E3, sourcing from A1:C9
pivot_table = worksheet.pivot_tables.add("A1:C9", 2, 4)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivot_table.refresh_data_on_opening_file = False
# calculate_data() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivot_table.calculate_data()
# Save the workbook to disk
workbook.save("output.xlsx")
```

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.get_pivot_tables()`. Denna metod returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

## Migrating from the Obsolete `PivotTable.refresh_data()`
Före Aspose.Cells for Python via .NET v26.7 var standardmetoden att uppdatera en pivottabell att anropa `PivotTable.refresh_data()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.
Det finns två skäl till att `refresh_data()`-metoden per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Which Refresh API Should I Use?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refresh_all()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt kalkylblad | `Worksheet.refresh_pivot_tables()` | Begränsat till ett kalkylblad. |
| Källdata ändrades för en cache | `pivot_table.pivot_cache.refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar ändrades | `pivot_table.calculate_data()` | Hoppar över onödig källöverföring. |
| Lista alla pivottabeller på en delad cache | `pivot_cache.get_pivot_tables()` | Använd för att räkna upp innan bulkuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade per-tabell `refresh_data()`. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar, och de låter dig välja den minsta omfattning som uppfyller ditt uppdateringskrav.

## Common Pitfalls
- **Glömmer att uppdatera innan du sparar.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller, anropa `PivotCache.refresh()` (eller `Workbook.refresh_all()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `refresh_data()` per tabell.** I v26.7 är `PivotTable.refresh_data()` markerad som föråldrad och hämtar om källan för varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt med en enda `PivotCache.refresh()` följt av `calculate_data()` per tabell.
- **Uppdaterar när bara layouten ändrades.** Om du bara ändrade en pivottabells vy (kolumnordning, `ConsolidationFunction` etc.) utan att röra källdata är `PivotCache.refresh()` onödig och långsam. Anropa `pivotTable.calculate_data()` för att rendera om från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub etc.) kan `PivotCache.refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cachen från källan.

{{< app/cells/assistant language="python-net" >}}