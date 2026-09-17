---
title: Uppdatera pivottabeller och pivotcachar i Aspose.Cells for Python via Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via Java med hjälp av v26.7+ pivot-uppdaterings-API,et. Den här artikeln behandlar RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
linktitle: Uppdatera pivottabeller
keywords: Aspose.Cells, Python via Java, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett lagerbaserat uppdaterings-API som låter dig läsa in pivotdata igen i fyra olika omfattningar — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Python via Java v26.7** är den äldre metoden `PivotTable.refreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.
{{% /alert %}}

## Introduktion
Att uppdatera en pivottabell är sällan en enskild åtgärd. Bakom kulisserna underhåller Aspose.Cells en lagerbaserad datakedja som kopplar samman dina ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.
Den fyra-lagers datakedjan är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — den minneslagrade ögonblicksbilden av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar i.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) anger var cache-datan kom ifrån. Från och med v26.7 stödjer `PivotCache.refresh()` endast källtyperna **`SHEET`** och **`CONSOLIDATION`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) kan ännu inte uppdateras via cache-API:et.
{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculateData()`** — beräknar om en `PivotTable`:s visning från redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `SHEET` och uppdateringsåtgärderna fungerar enligt beskrivningen.

## Snabbstart
Om du bara behöver den kortaste möjliga koden som uppdaterar varje pivot i arbetsboken räcker ett enda anrop:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Skapa en ny arbetsbok
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Skriv rubrikrad i cellerna A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Skriv datarader i cellerna A2:C9 (8 rader fruktdata över 2020 och 2021)
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
# Lägg till en pivottabell: källområde "A1:C9", målcell "E3", namn "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Ändra flera Amount-värden i källdatan för att simulera ändringar
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# Uppdatera varje pivottabell/pivotcache i arbetsboken
workbook.refreshAll()
# Spara arbetsboken
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

Allt annat i den här artikeln förklarar när du bör välja ett snävare API istället.

## Obligatoriska importer
Alla Python-exempel i den här artikeln är beroende av följande importer eftersom pivottyperna finns i namnrymden `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
Modulen `jpype` används för att starta upp JVM, medan `aspose.cells` exponerar arbetsboks-/kalkylblads-/cell-/pivottyperna som används igenom hela texten.

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återger den senaste källdatan är det enklaste och mest omfattande API:et `Workbook.refreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från dess källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för generella, heltäckande uppdateringar där prestanda inte är ett problem.
Följande exempel bygger en arbetsbok med ett källintervall Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `refreshAll()` för att uppdatera allt i ett enda anrop.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
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

## Uppdatera alla pivottabeller på ett enskilt kalkylblad
Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, som är begränsat till en enskild `Worksheet`-instans.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Skriv rubrikrad för Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Skriv 8 datarader (raderna 2–9, som passar källintervallet A1:C9)
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
# Lägg till en pivottabell med namnet "Pivot1" placerad vid målcell E3, med källa från A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Tilldela fält: Frukt till Rad, År till Kolumn, Belopp till Data
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Ändra en egenskap för vy/layout — detta är en ändring som endast påverkar presentationen,
# så den kräver INTE att källdatan läses igen via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# CalculateData() renderar om DENNA pivottabells visning (data + stil) från
# data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
# utförs ingen rundtur till källan — endast de cachelagrade värdena beräknas om
# till kalkylbladsceller.
pivotTable.calculateData()
# Spara arbetsboken till disk
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## Uppdatera en enskild pivottabell
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: underliggande källdata, eller bara pivottabellens visnings-/layoutinställningar.

### Källdata har ändrats — använd `PivotCache.refresh()`
Om de underliggande källdatan har ändrats är rätt startpunkt `pivotTable.getPivotCache().refresh()`. Detta anrop läser om källdatan till cachen och beräknar sedan om alla `PivotTable` som är beroende av den cachen.

### Endast visning/layout har ändrats — använd `calculateData()`
Om källdatan *inte* har ändrats men endast pivottabellens visnings- eller layoutinställningar har modifierats (till exempel att ett fält har flyttats till ett annat område, eller att en inställning för uppdatering-vid-öppning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen har redan rätt data; bara den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.calculateData()` rätt val.
Följande exempel modifierar en icke-källegenskap hos pivottabellen och anropar sedan `calculateData()` för att rendera om den från den befintliga cachen.
En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att enumerera dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.getPivotTables()`. Den här metoden returnerar samlingen av alla `PivotTable` som är beroende av den givna cachen.

## Migrera från den föråldrade `PivotTable.refreshData()`
Före Aspose.Cells for Python via Java v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.refreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.
Det finns två anledningar till att `refreshData()`-metoden per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Vilket uppdaterings-API bör jag använda?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja varje.
| Mål | Rekommenderat API | Anteckningar |
|------|-------------------|-------------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop; täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.getPivotCache().refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast visnings-/layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödiga källanrop. |
| Lista alla pivottabeller på en delad cache | `pivotCache.getPivotTables()` | Använd för att enumerera före bulkuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade `refreshData()` per tabell. De är medvetna om delade cachar, de undviker redundanta källhämtningar och de låter dig välja den minsta omfattning som uppfyller ditt uppdateringsbehov.

## Vanliga fallgropar
- **Glömmer att uppdatera innan du sparar.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du modifierar källceller, anropa `PivotCache.Refresh()` (eller `Workbook.RefreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `RefreshData()` per tabell.** I v26.7 är `PivotTable.RefreshData()` markerad som föråldrad och hämtar om källan vid varje anrop. Med flera pivottabeller som delar en cache innebär detta N redundanta källhämtningar. Ersätt med ett enda `PivotCache.Refresh()` följt av `CalculateData()` per tabell.
- **Uppdaterar när bara layouten har ändrats.** Om du bara ändrade en pivottabells visning (kolumnordning, `ConsolidationFunction` osv.) utan att röra källdatan, är `PivotCache.Refresh()` onödigt och långsamt. Anropa `pivotTable.CalculateData()` för att rendera om från den befintliga cachen.
- **Extern källa stöds inte av `PivotCache.Refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub osv.) kan `PivotCache.Refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cachen från källan.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}