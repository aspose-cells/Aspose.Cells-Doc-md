---
title: Uppdatera pivottabeller i Aspose.Cells for Python via Java
linktitle: Uppdatera pivottabeller i Aspose.Cells for Python via Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via Java med hjälp av v26.7+ pivot-refresh API,t. Den här artikeln tar upp RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Python via Java, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett lagerbaserat uppdaterings-API som låter dig ladda om pivotdata i fyra olika omfattningar — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Python via Java v26.7** markeras den äldre metoden `PivotTable.refreshData()` som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:erna som beskrivs i den här artikeln.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enstaka åtgärd. Bakom kulisserna upprätthåller Aspose.Cells en lagerbaser datakedja som kopplar samman dina ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Den fyrlagriga datakedjan är:

1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallen där råvärdena finns.
2. **PivotCache** — den minnesbaserade ögonblicksbilden av källdatan. Varje pivottabell bygger ovanpå en `PivotCache`; det är här all data samlas och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Celler** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

Ett särskilt viktigt koncept är den **delade cachen**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enda `PivotCache` kan refereras av många pivottabeller, och att uppdatera den cachen uppdaterar alla beroende `PivotTable` samtidigt.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) anger varifrån cachedatan kom. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`SHEET`** och **`CONSOLIDATION`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) är ännu inte uppdateringsbara via cache-API:t.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.refresh()`** — läser in källa → cache OCH beräknar om alla beroende `PivotTable` i en enda åtgärd.
- **`PivotTable.calculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan någon tur och retur till datakällan.

Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `SHEET` och uppdateringsåtgärderna fungerar enligt beskrivningen.

## Nödvändiga importer

Alla Python-exempel i den här artikeln är beroende av följande importer eftersom pivottyperna finns i namnrymden `aspose.cells.pivot`:

- `import jpype`
- `import aspose.cells as cells`

Modulen `jpype` används för att starta JVM, medan `aspose.cells` exponerar arbetsboks-/kalkylblads-/cell-/pivottyper som används genomgående.

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återger de senaste källdatan, är det enklaste och mest heltäckande API:t `Workbook.refreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett källintervall Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `refreshAll()` för att uppdatera allt med ett enda anrop.

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

# Lägg till en pivottabell: källintervall "A1:C9", destinationscell "E3", namn "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Ändra flera Amount-värden i källdatan för att simulera förändringar
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# Uppdatera varje pivottabell / pivotcache i arbetsboken
workbook.refreshAll()

# Spara arbetsboken
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad

Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, vilken är begränsad till en enda `Worksheet`-instans.

Detta är mer selektivt än `Workbook.refreshAll()`: endast pivottabellerna på det riktade kalkylbladet uppdateras, vilket lämnar pivottabeller på andra kalkylblad orörda.

Följande exempel fyller i samma källdata Fruit/Year/Amount, lägger till en pivottabell på det första kalkylbladet, ändrar några källvärden och uppdaterar sedan endast pivottabellerna på det kalkylbladet.

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

## Uppdatera en enskild pivottabell

När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:t dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: de underliggande källdatan eller bara vy-/layoutinställningarna för pivottabellen i sig.

### Källdata har ändrats — använd `PivotCache.refresh()`

Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.getPivotCache().refresh()`. Detta anrop läser om källdatan till cachen och beräknar sedan om alla `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans, beräknar anropet av `PivotCache.refresh()` om **alla** pivottabeller som bygger på samma cache — inte bara den du refererar till. Om två pivottabeller delar samma källintervall, uppdaterar en cache-uppdatering båda.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, ändrar några källvärden och uppdaterar sedan via en cache-referens.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Skapa en ny arbetsbok och kom åt det första kalkylbladet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Skriv rubrikrad: Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Skriv ungefär 9 datarader (druva / blåbär / kiwi / körsbär över 2020-2021)
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

# Lägg till den första pivottabellen "Pivot1" förankrad vid cell E3, källområde A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Tilldela fält för Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# Lägg till en ANDRA pivottabell "Pivot2" förankrad vid E15 med SAMMA källområde A1:C9
# Både Pivot1 och Pivot2 delar en enda PivotCache eftersom källområdet är identiskt.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Tilldela samma fält för Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# Ändra flera beloppscellvärden i källdatan för att simulera en dataändring
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# Uppdatera den delade PivotCache.
# Eftersom Pivot1 och Pivot2 delar samma PivotCache, uppdaterar detta enda anrop
# uppdaterar BÅDA pivottabellerna (data + stil) från den uppdaterade källan.
pivotTable1.getPivotCache().refresh()

# Spara arbetsboken
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Endast vy/layout har ändrats — använd `calculateData()`

Om källdatan *inte* har ändrats utan bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel att ett fält har flyttats till ett annat område, eller en uppdaterings-vid-öppning-inställning har växlats), finns det ingen anledning att gå tur och retur till datakällan. Cachen har redan rätt data; det är bara den renderade `PivotTable` som behöver omberäkning. I detta fall är `pivotTable.calculateData()` rätt val.

Detta undviker det onödiga källhämtandet och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel ändrar en icke-källegenskap hos pivottabellen och anropar sedan `calculateData()` för att rendera om den från den befintliga cachen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Skriv rubrikrad med Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Skriv 8 datarader (raderna 2-9, som passar källintervallet A1:C9)
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

# Lägg till en pivottabell med namnet "Pivot1" placerad vid destinationscell E3, med källa från A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Tilldela fält: Fruit till Rad, Year till Kolumn, Amount till Data
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Ändra en egenskap för vy/layout — detta är enbart en presentationsändring,
# så det kräver INTE att källdatan läses om via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() renderar om DEN HÄR pivottabellens visning (data + stil) från
# data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
# görs ingen rundresa till källan — endast de cachade värdena räknas om
# till celler i kalkylbladet.
pivotTable.calculateData()

# Spara arbetsboken till disk
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera delad cache-påverkan — använd `PivotCache.getPivotTables()`. Den här metoden returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cache-referenser, eller helt enkelt iterera samlingen som returneras av `getPivotTables()` och observera vilka pivottabeller som visas i den.

Följande exempel skapar två pivottabeller på samma källintervall, verifierar att de delar samma cache-instans och räknar sedan upp cachers pivottabeller.


## Migrera från den föråldrade `PivotTable.refreshData()`

Innan Aspose.Cells for Python via Java v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.refreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.

Det finns två anledningar till att metoden per tabell `refreshData()` är problematisk i verkliga arbetsböcker:

- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache, gör upprepade anrop av `refreshData()` per pivottabell att samma cache hämtas om och om igen, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.refreshAll();`
- **Uppdatera NÅGRA av dem** → använd `pivotTable.getPivotCache().refresh();` för en cache. Eftersom cachen är delad, uppdaterar detta enda anrop varje pivottabell som bygger ovanpå den cachen. Andra pivottabeller som ligger på en redan uppdaterad cache kan säkert hoppas över.
- **Endast pivotvyn/layouten har ändrats** → använd `pivotTable.calculateData();` för att rendera om från den befintliga cachen utan någon källtur och retur.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Skapa en ny arbetsbok och öppna det första kalkylbladet
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- Bygg källdata: Fruit / Year / Amount (rubrik + 9 rader) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- Lägg till den första pivottabellen (Pivot1) vid destinationscell E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Lägg till den ANDRA pivottabellen (Pivot2) på SAMMA källintervall ---
# Både Pivot1 och Pivot2 delar ETT underliggande PivotCache.
# Detta är exakt scenariot där den äldre per-tabell-metoden RefreshData()
# blir ineffektiv: att uppdatera en tabell hämtar om hela
# delade cachen, så att uppdatera N tabeller gör samma dyra hämtning N gånger.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- Ändra flera Amount-värden i källdatan ---
sheet.getCells().get("C2").putValue(5000)   # Grape  2020
sheet.getCells().get("C5").putValue(7500)   # Cherry 2020
sheet.getCells().get("C9").putValue(9500)   # Cherry 2021

# --- FÖRÅLDRAT mönster (före 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // hämtar om från källan, uppdaterar hela cachen
# pivotTable2.RefreshData();  // hämtar om IGEN — cachen är redan färsk!
# Varje anrop bygger om den delade cachen, så N tabeller = N redundanta hämtningar.

# --- NYTT v26.7+ mönster: uppdatera cachen EN GÅNG, återrendera sedan vid behov ---
# Ett anrop till PivotCache.Refresh() hämtar de ändrade värdena till den delade
# cachen OCH beräknar om visningen av VARJE pivottabell som refererar till den.
# Eftersom Pivot1 och Pivot2 delar en PivotCache, uppdaterar detta enda anrop
# båda tabellerna — ingen andra källtur behövs.
pivotTable1.getPivotCache().refresh()

# CalculateData() återrenderar bara en pivottabells vy (data + stil)
# från datan som redan finns i cachen — den rör INTE källan.
# Vi anropar den på Pivot2 här enbart för att demonstrera API:et: efter att cachen
# har uppdaterats en gång kan vilken beroende tabell som helst återrenderas utan
# att gå tillbaka till källan. Använd CalculateData() ensamt när bara
# pivottabellens vy-/layoutinställningar har ändrats och cachen är aktuell.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## Vilket uppdaterings-API bör jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.

| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop; täcker alla cacher och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt ark | `Worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.getPivotCache().refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödig källturstur. |
| Lista alla pivottabeller på en delad cache | `pivotCache.getPivotTables()` | Använd för att räkna upp före bulkuppdatering. |

I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade per tabell `refreshData()`. De är medvetna om delade cacher, undviker redundanta källhämtningar och låter dig välja det minsta omfånget som uppfyller ditt uppdateringskrav.

{{< app/cells/assistant language="python" >}}
