---
title: Uppdatera pivottabeller i Aspose.Cells for Python via .NET
linktitle: Uppdatera pivottabeller i Aspose.Cells for Python via .NET
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via .NET med hjälp av pivot-refresh API,et i v26.7+. Den här artikeln tar upp RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Python via .NET, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett lagerindelat uppdaterings-API som låter dig läsa in pivotdata på fyra olika nivåer — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Python via .NET v26.7** är den äldre metoden `PivotTable.refresh_data()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:erna som beskrivs i den här artikeln.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enstaka operation. Bakom kulisserna upprätthåller Aspose.Cells en lagerindlad datakedja som kopplar samman dina ursprungliga källdata med de renderade värdena du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Den fyralagers datakedjan är:

1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Celler** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

Ett särskilt viktigt koncept är den **delade cachen**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enskild `PivotCache` kan refereras av många pivottabeller, och att uppdatera den cachen uppdaterar varje beroende `PivotTable` på en gång.

{{% alert color="primary" %}}

`PivotCache.source_type` (enum `PivotTableSourceType`) anger var cachedatan kom ifrån. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar etc.) är ännu inte möjliga att uppdatera via cache-API:et.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.refresh()`** — läser in källan → cache OCH beräknar om alla beroende `PivotTable`s i en enda operation.
- **`PivotTable.calculate_data()`** — beräknar om en `PivotTable`s vy från redan cachad data, utan att gå tillbaka till datakällan.

Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsoperationerna fungerar enligt beskrivningen.

## Nödvändiga importer

Alla Python-exempel i den här artikeln börjar med följande tre import-satser eftersom pivottyperna finns i namnrymden `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest heltäckande API:et `Workbook.refresh_all()`. Ett enda anrop går igenom hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmän, fullständig dokumentuppdatering där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `refresh_all()` för att uppdatera allt i ett enda anrop.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Skriv rubrikrad i cellerna A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Skriv datarader i cellerna A2:C9 (8 rader med fruktdata över 2020 och 2021)
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

# Uppdatera varje pivottabell / pivotcache i arbetsboken
workbook.refresh_all()

# Spara arbetsboken
workbook.save("output.xlsx")
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad

Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refresh_pivot_tables()`, som är begränsat till en enskild `Worksheet`-instans.

Detta är mer selektivt än `Workbook.refresh_all()`: endast pivottabellerna på det riktade kalkylbladet uppdateras, medan eventuella pivottabeller på andra kalkylblad förblir orörda.

Följande exempel fyller i samma källdata för Fruit/Year/Amount, lägger till en pivottabell på det första kalkylbladet, ändrar några källvärden och uppdaterar sedan bara pivottabellerna på det kalkylbladet.

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

## Uppdatera en enskild pivottabell

När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara vy-/layoutinställningarna för själva pivottabellen.

### Källdata har ändrats — Använd `PivotCache.refresh()`

Om den underliggande källdatan har ändrats är rätt startpunkt `pivot_table.pivot_cache.refresh()`. Detta anrop läser in källdatan i cachen igen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans gör ett anrop till `PivotCache.refresh()` att **alla** pivottabeller som är byggda på samma cache beräknas om — inte bara den du refererar till. Om två pivottabeller delar samma källintervall uppdateras båda när du uppdaterar en cache.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, ändrar några källvärden och uppdaterar sedan genom en cache-referens.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok och öppna det första kalkylbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Skriv rubrikrad: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Skriv ungefär 9 datarader (grape / blueberry / kiwi / cherry över 2020-2021)
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
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# Lägg till den första pivottabellen "Pivot1" förankrad vid cell E3, källintervall A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Tilldela fält för Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Lägg till en ANDRA pivottabell "Pivot2" förankrad vid E15 med SAMMA källintervall A1:C9
# Både Pivot1 och Pivot2 delar en enda PivotCache eftersom källintervallet är identiskt.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Tilldela samma fält för Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Ändra flera Amount-cellvärden i källdatan för att simulera en dataändring
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# Uppdatera den delade PivotCache.
# Eftersom Pivot1 och Pivot2 delar samma PivotCache, uppdaterar detta enda anrop
# BÅDA pivottabellerna (data + stil) från den uppdaterade källan.
pivotTable1.pivot_cache.refresh()

# Spara arbetsboken
workbook.save("output.xlsx")
```

### Endast vy/layout har ändrats — Använd `calculate_data()`

Om källdatan *inte* har ändrats men bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel att ett fält har flyttats till ett annat område, eller att en inställning för uppdatering vid öppning har växlats), finns det ingen anledning att gå tillbaka till datakällan. Cachen innehåller redan rätt data; bara den renderade `PivotTable` behöver beräknas om. I detta fall är `pivot_table.calculate_data()` rätt val.

Detta undviker det onödiga källhämtningen och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel modifierar en egenskap som inte är kopplad till källan för pivottabellen och anropar sedan `calculate_data()` för att rendera om den från den befintliga cachen.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Skriv rubrikraden Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Skriv 8 datarader (raderna 2-9, som passar källintervallet A1:C9)
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

# Lägg till en pivottabell med namnet "Pivot1" placerad vid destinationscell E3, med källa från A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Tilldela fält: Fruit till Rad, Year till Kolumn, Amount till Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Ändra en visnings-/layout-egenskap — detta är en presentationsförändring,
# så den kräver INTE att källdatan läses om via PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() återrenderar DENNA pivottabells visning (data + stil) från
# data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
# utförs ingen rundtur till källan — endast de cachelagrade värdena beräknas om
# till kalkylbladsceller.
pivot_table.calculate_data()

# Spara arbetsboken till disk
workbook.save("output.xlsx")
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en massuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.get_pivot_tables()`. Den här metoden returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cache-referenser, eller helt enkelt iterera samlingen som returneras av `get_pivot_tables()` och observera vilka pivottabeller som finns i den.

Följande exempel skapar två pivottabeller på samma källintervall, verifierar att de delar samma cache-instans och räknar sedan upp cachens pivottabeller.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

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
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## Migrera från den föråldrade `PivotTable.refresh_data()`

Före Aspose.Cells for Python via .NET v26.7 var standardsättet att uppdatera en pivottabell att anropa `PivotTable.refresh_data()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:erna som beskrivs ovan.

Det finns två anledningar till att `refresh_data()`-metoden per tabell är problematisk i verkliga arbetsböcker:

- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache gör upprepade anrop till `refresh_data()` per pivottabell att samma cache hämtas om och om igen, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.refresh_all();`
- **Uppdatera NÅGRA av dem** → använd `pivot_table.pivot_cache.refresh();` för en cache. Eftersom cachen delas uppdaterar detta enda anrop varje pivottabell som är byggd ovanpå den cachen. Andra pivottabeller som ligger på en redan uppdaterad cache kan säkert hoppas över.
- **Endast pivotvyn/layouten har ändrats** → använd `pivot_table.calculate_data();` för att rendera om från den befintliga cachen utan att hämta från källan.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok och hämta det första kalkylbladet
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Bygg källdata: Frukt / År / Belopp (rubrik + 9 rader) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- Lägg till den första pivottabellen (Pivot1) vid målcell E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Lägg till den ANDRA pivottabellen (Pivot2) på SAMMA källintervall ---
# Både Pivot1 och Pivot2 delar ETT underliggande PivotCache.
# Detta är exakt scenariot där den äldre per-tabell RefreshData()
# metoden blir ineffektiv: att uppdatera en tabell hämtar om hela
# delade cachen, så att uppdatera N tabeller gör samma dyra hämtning N gånger.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Ändra flera Belopp-värden i källdatan ---
sheet.cells["C2"].put_value(5000)   # Druva   2020
sheet.cells["C5"].put_value(7500)   # Körsbär 2020
sheet.cells["C9"].put_value(9500)   # Körsbär 2021

# --- FÖRÅLDRAD metod (före 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # hämtar om från källan, uppdaterar hela cachen
# pivot_table2.refresh_data();  # hämtar IGEN — cachen är redan färsk!
# Varje anrop bygger om den delade cachen, så N tabeller = N redundanta hämtningar.

# --- NYTT mönster v26.7+: uppdatera cachen EN GÅNG, rendera sedan om vid behov ---
# Ett anrop till PivotCache.Refresh() hämtar de ändrade värdena till den delade
# cachen OCH beräknar om visningen av VARJE pivottabell som refererar till den.
# Eftersom Pivot1 och Pivot2 delar en PivotCache, uppdaterar detta enda anrop
# båda tabellerna — ingen andra källhämtning behövs.
pivot_table1.pivot_cache.refresh()

# CalculateData() renderar bara om en pivottabells visning (data + stil)
# från data som redan finns i cachen — den rör INTE källan.
# Vi anropar den på Pivot2 här enbart för att demonstrera API:et: efter att cachen
# har uppdaterats en gång, kan vilken som helst beroende tabell renderas om utan
# att gå tillbaka till källan. Använd CalculateData() ensam när bara
# pivottabellens visnings-/layoutinställningar har ändrats och cachen är aktuell.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Vilket uppdaterings-API bör jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja varje enskilt.

| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refresh_all()` | Ett anrop; täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt ark | `Worksheet.refresh_pivot_tables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivot_table.pivot_cache.refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivot_table.calculate_data()` | Hoppar över onödig källhämtning. |
| Lista alla pivottabeller på en delad cache | `pivot_cache.get_pivot_tables()` | Använd för att räkna upp före massuppdatering. |

I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade `refresh_data()` per tabell. De är medvetna om delade cachar, de undviker redundanta källhämtningar och de låter dig välja den minsta omfattning som uppfyller ditt uppdateringskrav.

{{< app/cells/assistant language="python" >}}