---
title: Uppdatera pivottabeller och pivotcacher i Aspose.Cells for Python via Java
linktitle: Uppdatera pivottabeller och pivotcacher i Aspose.Cells for Python via Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via Java med hjälp av pivotuppdaterings-API i v26.7+. Den här artikeln behandlar RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Python via Java, pivottabell, uppdatering, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett lagerindelat uppdaterings-API som låter dig ladda om pivotdata på fyra olika nivåer – från hela arbetsboken ned till en enda pivottabell. Från och med **Aspose.Cells for Python via Java v26.7** är den äldre metoden `PivotTable.refreshData()` markerad som obsolet och bör ersättas med de effektivare cachebaserade API:er som beskrivs i den här artikeln.
{{% /alert %}}

## Introduction
Att uppdatera en pivottabell är sällan en enda åtgärd. Aspose.Cells underhåller bakom kulisserna en lagerindelad datakedja som binder samman de ursprungliga källdata med de renderade värden som du ser i kalkylbladet. Att förstå den här kedjan är nyckeln till att välja rätt uppdaterings-API för varje situation.
Datalkedjan har fyra lager:
1. **Datakälla** – de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **`PivotCache`** – ögonblicksbilden av källdata i minnet. Varje pivottabell byggs ovanpå en `PivotCache`; här samlas och aggregeras all data.
3. **`PivotTable`** – vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **`Cells`** – kalkylbladets `Cells` dit `PivotTable` renderar sina beräknade värden och stilar.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enumet `PivotTableSourceType`) anger varifrån cacheladdan kom. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`SHEET`** och **`CONSOLIDATION`** – alltså data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) går inte att uppdatera via cache-API:et ännu.
På grund av den här kedjan finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculateData()`** – beräknar om en `PivotTable`s visning utifrån redan cachelagda data, utan någon tur och retur till datakällan.
Alla scenarier i den här artikeln använder källdata i kalkylbladsceller, så källtypen är `SHEET` och uppdateringsåtgärderna fungerar som beskrivs.
{{% /alert %}}

## Quick Start
Om du bara behöver den kortaste möjliga kod som uppdaterar alla pivottabeller i arbetsboken räcker ett enda anrop:

```python
import jpype
from asposecells.api import Workbook

workbook = Workbook("input.xlsx")
workbook.refreshAll()
workbook.save("output.xlsx")
```

Resten av den här artikeln förklarar när du i stället ska välja ett mer avgränsat API.

## Required Imports
Alla Python-exempel i den här artikeln är beroende av följande importer eftersom pivottyperna finns i namespace `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
Modulen `jpype` används för att initiera JVM, medan `aspose.cells` exponerar de typer för arbetsbok, kalkylblad, cell och pivot som används i hela artikeln.

## Refresh All Pivot Tables in the Workbook
Om du behöver säkerställa att alla pivotcacher och alla pivottabeller i arbetsboken återspeglar de senaste källdata är det enklaste och mest omfattande API:t `Workbook.refreshAll()`. Ett enda anrop går igenom hela arbetsboken – det uppdaterar varje `PivotCache` från sin källa och beräknar sedan om alla beroende `PivotTable`. Detta är den rekommenderade metoden för fullständiga dokumentuppdateringar när prestanda inte är en viktig faktor.
Det här exemplet skapar ett arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar vissa källvärden och använder sedan `refreshAll()` för att uppdatera allt med ett enda anrop.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll()
# Save the workbook
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh All Pivot Tables on a Single Worksheet
Ibland behöver du endast uppdatera pivottabellerna i ett visst kalkylblad, till exempel när pivottabeller i andra kalkylblad inte har någon koppling till den och inte ska ändras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, som är begränsad till en enda `Worksheet`-instans.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Refresh a Single Pivot Table
Om du vill ha detaljerad kontroll över en enda pivottabell ger cachebaserade API:t två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: källdatan under eller endast vy- och layoutinställningarna för pivottabellen själv.

### Source Data Changed — Use `PivotCache.refresh()`
Om källdatan underliggande har ändrats är rätt ingångspunkt `pivotTable.getPivotCache().refresh()`. Anropet läser in källdatan i cachen på nytt och beräknar sedan om varje `PivotTable` som är beroende av cachen.

### Only View/Layout Changed — Use `calculateData()`
Om källdatan *inte* har ändrats men endast pivottabellens vy- eller layoutinställningar har ändrats, till exempel om ett fält har flyttats till ett annat område eller en inställning för uppdatering vid öppning har växlat, finns inget behov av att gå tillbaka till datakällan. Cachen innehåller redan rätt data; endast den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.calculateData()` rätt val.
Det här exemplet ändrar en egenskap som inte hör till källan och anropar sedan `calculateData()` för att rendera om pivottabellen från den befintliga cachen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Modify a view/layout property — this is a presentation-only change,
# so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# calculateData() re-renders THIS pivot table's display (data + style) from the
# data already held in the PivotCache. Because the source data did not change,
# no round-trip to the source is performed — only the cached values are recalculated
# into worksheet cells.
pivotTable.calculateData()
# Save the workbook to disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Ett arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en och samma cache. Om du vill enumerera dem, till exempel före en batchuppdatering eller för att diagnostisera effekten av en delad cache, använder du `PivotCache.getPivotTables()`. Metoden returnerar samlingen av alla `PivotTable` som är beroende av den angivna cachen.

## Migrating from the Obsolete `PivotTable.refreshData()`
Före Aspose.Cells for Python via Java v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.refreshData()` separat för varje pivottabell. Från och med v26.7 är metoden markerad som **obsolet** och bör ersättas med de cachebaserade API:er som beskrivs ovan.
Det finns två skäl till att `refreshData()` per tabell är problematiskt i verkliga arbetsböcker:
- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
Rekommenderade ersättningar är:
Det här exemplet visar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Which Refresh API Should I Use?
Tabellen nedan sammanfattar tillgängliga uppdaterings-API:er och när du bör välja varje enskild.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller i ett kalkylblad | `Worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdatan har ändrats för en cache | `pivotTable.getPivotCache().refresh()` | Uppdaterar ALLA pivottabeller som använder den delade cachen. |
| Endast vy- eller layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödig tur och retur till källan. |
| Lista alla pivottabeller som använder en delad cache | `pivotCache.getPivotTables()` | Använd för att enumerera före massuppdatering. |
I praktiken bör du föredra cachebaserade API:er framför den obsoleta `refreshData()` per tabell. De är medvetna om delade cachar, undviker redundanta källhämtningar och låter dig välja den minsta omfattning som uppfyller ditt uppdateringsbehov.

## Common Pitfalls
- **Att glömma att uppdatera före sparande.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja har uppdaterats. Om du ändrar källceller anropar du `PivotCache.refresh()` (eller `Workbook.refreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Att anropa den obsoleta `RefreshData()` för varje tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som obsolet och hämtar källan på nytt vid varje anrop. Med flera pivottabeller som delar en cache innebär det N redundanta källhämtningar. Ersätt det med ett enda anrop till `PivotCache.refresh()` följt av `calculateData()` för varje tabell.
- **Att uppdatera när endast layouten har ändrats.** Om du bara har ändrat en pivottabells vy, till exempel kolumnordning eller `ConsolidationFunction`, utan att röra källdatan är `PivotCache.refresh()` onödig och långsam. Anropa `pivotTable.calculateData()` för att rendera om från den befintliga cachen.
- **Extern källa som inte stöds av `PivotCache.refresh()`.** Om pivottabellens källa kommer från en extern anslutning, till exempel en databas eller OLAP-kub, kan `PivotCache.refresh()` inte uppdatera den i v26.7 – den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor öppnar du arbetsboken på nytt eller bygger om cachen från källan.

{{< app/cells/assistant language="python" >}}