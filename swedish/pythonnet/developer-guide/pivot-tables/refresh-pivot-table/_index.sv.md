---
title: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Python via .NET
linktitle: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Python via .NET
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via .NET med hjälp av v26.7+ pivot-uppdaterings-API,et. Den här artikeln täcker RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
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

## Introduktion
Att uppdatera en pivottabell är sällan en enskild åtgärd. Bakom kulisserna underhåller Aspose.Cells en lagerindelad datakedja som kopplar samman dina ursprungliga källdata till de renderade värdena du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyrlagers datakedjan är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallerna, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden av källdatan i minnet. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **Pivottabell** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Celler** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

{{% alert color="primary" %}}
`PivotCache.source_type` (enum `PivotTableSourceType`) anger var cachedatan kom ifrån. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar etc.) kan ännu inte uppdateras via cache-API:et.
{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculate_data()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i denna artikel använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar som beskrivs.

## Snabbstart
Om du bara behöver den kortaste möjliga koden som uppdaterar varje pivot i arbetsboken, räcker det med ett enda anrop:

```python
import aspose.cells as ac
# Skapa en ny arbetsbok
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Skriv rubrikraden till cellerna A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Skriv datarader till cellerna A2:C9 (8 rader med fruktdata för 2020 och 2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)
# Lägg till en pivottabell: källområde "A1:C9", målcell "E3", namn "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Ändra flera Amount-värden i källdatan för att simulera ändringar
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# Uppdatera varje pivottabell/pivotcache i arbetsboken
workbook.refresh_all()
# Spara arbetsboken
workbook.save("output.xlsx")
```

Allt annat i denna artikel förklarar när du ska välja ett snävare API istället.

## Nödvändiga importer
Alla Python-exempel i denna artikel börjar med följande tre import-satser eftersom pivottyperna finns i namnrymden `aspose.cells.pivot`:
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest omfattande API:et `Workbook.refresh_all()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett bekymmer.
Följande exempel bygger en arbetsbok med ett källintervall för Frukt/År/Belopp, skapar en pivottabell, ändrar några källvärden och använder sedan `refresh_all()` för att uppdatera allt i ett enda anrop.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad
Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refresh_pivot_tables()`, som är begränsat till en enskild `Worksheet`-instans.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Skriv rubrikraden Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# Skriv 8 datarader (rad 2-9, som passar källintervallet A1:C9)
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
worksheet.cells["C6"].put_value(150)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)
# Lägg till en pivottabell med namnet "Pivot1" placerad vid målcell E3, med källa från A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Tilldela fält: Fruit till Rad, Year till Kolumn, Amount till Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# Ändra en visnings-/layout-egenskap — detta är en presentationsförändring,
# så den KRÄVER INTE att källdatan läses igen via PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False
# CalculateData() renderar DEN HÄR pivottabellens visning (data + stil) från
# data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
# utförs ingen tur och retur till källan — endast de cachade värdena beräknas om
# till kalkylbladsceller.
pivot_table.calculate_data()
# Spara arbetsboken till disk
workbook.save("output.xlsx")
```

## Uppdatera en enskild pivottabell
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt ändrades: underliggande källdata, eller bara vy-/layoutinställningarna för pivottabellen själv.

### Källdata har ändrats — Använd `PivotCache.refresh()`
Om underliggande källdata har ändrats är rätt ingångspunkt `pivot_table.pivot_cache.refresh()`. Detta anrop läser om källdatan till cachen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Endast vy/layout har ändrats — Använd `calculate_data()`
Om källdatan *inte* har ändrats men bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en refresh-on-open-inställning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen har redan rätt data; bara den renderade `PivotTable` behöver beräknas om. I detta fall är `pivot_table.calculate_data()` rätt val.
Följande exempel modifierar en icke-källegenskap för pivottabellen och anropar sedan `calculate_data()` för att rendera om den från den befintliga cachen.
En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.get_pivot_tables()`. Denna metod returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

## Migrera från den föråldrade `PivotTable.refresh_data()`
Före Aspose.Cells for Python via .NET v26.7 var standardmetoden att uppdatera en pivottabell att anropa `PivotTable.refresh_data()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.
Det finns två skäl till att `refresh_data()`-metoden per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Vilket uppdaterings-API ska jag använda?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refresh_all()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt kalkylblad | `Worksheet.refresh_pivot_tables()` | Begränsat till ett kalkylblad. |
| Källdata ändrades för en cache | `pivot_table.pivot_cache.refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar ändrades | `pivot_table.calculate_data()` | Hoppar över onödig källöverföring. |
| Lista alla pivottabeller på en delad cache | `pivot_cache.get_pivot_tables()` | Använd för att räkna upp innan bulkuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade per-tabell `refresh_data()`. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar, och de låter dig välja den minsta omfattning som uppfyller ditt uppdateringskrav.

## Vanliga fallgropar
- **Glömmer att uppdatera innan du sparar.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller, anropa `PivotCache.Refresh()` (eller `Workbook.RefreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `RefreshData()` per tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar om källan för varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt med en enda `PivotCache.Refresh()` följt av `CalculateData()` per tabell.
- **Uppdaterar när bara layouten ändrades.** Om du bara ändrade en pivottabells vy (kolumnordning, `ConsolidationFunction` etc.) utan att röra källdata är `PivotCache.Refresh()` onödig och långsam. Anropa `pivotTable.CalculateData()` för att rendera om från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.Refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub etc.) kan `PivotCache.Refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cachen från källan.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python-net" >}}