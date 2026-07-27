---
title: Uppdatera pivottabeller i Aspose.Cells for Python via .NET
linktitle: Uppdatera pivottabeller i Aspose.Cells for Python via .NET
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Python via .NET med hjälp av v26.7+ pivot-uppdaterings-API,et. Denna artikel täcker RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel
keywords: Aspose.Cells, Python via .NET, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett skiktat uppdaterings-API som låter dig läsa in pivotdata på fyra olika omfång — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Python via .NET v26.7** är den äldre metoden `PivotTable.refresh_data()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i denna artikel.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enskild åtgärd. Bakom kulisserna underhåller Aspose.Cells en skiktad datakedja som kopplar samman dina ursprungliga källdata med de renderade värden du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Den fyra nivåer djupa datakedjan är:

1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell byggs ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

Ett särskilt viktigt koncept är **delad cache**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enskild `PivotCache` kan refereras till av många pivottabeller, och om du uppdaterar den cachen uppdateras alla beroende `PivotTable`s på en gång.

{{% alert color="primary" %}}

`PivotCache.source_type` (uppräkning `PivotTableSourceType`) anger var cache-datan kom ifrån. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) kan ännu inte uppdateras via cache-API:et.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.refresh()`** — läser in källa → cache OCH beräknar om alla beroende `PivotTable`s i en enda åtgärd.
- **`PivotTable.calculate_data()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan någon tur-och-retur till datakällan.

Alla scenarier i denna artikel använder kalkylbladsceller som källdata, så källtypen är `Sheet` och uppdateringsåtgärderna fungerar enligt beskrivningen.

## Nödvändiga importer

Alla Python-exempel i denna artikel inleds med följande tre importsatser eftersom pivottyperna finns i namnrymden `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest heltäckande API:et `Workbook.refresh_all()`. Ett enda anrop traverserar hela arbetsboken — varje `PivotCache` uppdateras från sin källa och sedan beräknas varje beroende `PivotTable` om. Detta är den rekommenderade metoden för generella, dokumentövergripande uppdateringar där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, modifierar några källvärden och använder sedan `refresh_all()` för att uppdatera allt i ett enda anrop.

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

# Ändra flera Amount-värden i källdatan för att simulera förändringar
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# Uppdatera varje pivottabell / pivotcache i arbetsboken
workbook.refresh_all()

# Spara arbetsboken
workbook.save("output.xlsx")
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad

Ibland behöver du bara uppdatera de pivottabeller som finns på ett visst kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refresh_pivot_tables()`, som är begränsat till en enskild `Worksheet`-instans.

Detta är mer selektivt än `Workbook.refresh_all()`: endast pivottabellerna på det målsökta kalkylbladet uppdateras, medan pivottabeller på andra kalkylblad lämnas orörda.

Följande exempel fyller i samma Fruit/Year/Amount-källdata, lägger till en pivottabell på det första kalkylbladet, modifierar några källvärden och uppdaterar sedan endast pivottabellerna på det kalkylbladet.

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

När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara pivottabellens vy-/layoutinställningar.

### Källdata har ändrats — Använd `PivotCache.refresh()`

Om den underliggande källdatan har ändrats är rätt startpunkt `pivot_table.pivot_cache.refresh()`. Detta anrop läser om källdatan in i cachen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans beräknar ett anrop till `PivotCache.refresh()` om **alla** pivottabeller som är byggda på den cachen — inte bara den du refererar till. Om två pivottabeller delar samma källintervall uppdaterar en cache-uppdatering båda.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, modifierar några källvärden och uppdaterar sedan genom en cache-referens.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok och kom åt det första kalkylbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Skriv rubrikrad: Frukt / År / Belopp
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# Skriv ungefär 9 datarader (druva / blåbär / kiwi / körsbär över 2020-2021)
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

# Ändra flera belopps cellvärden i källdatan för att simulera en dataändring
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

Om källdatan *inte* har ändrats men endast pivottabellens vy- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en uppdaterings-vid-öppning-inställning har växlats), finns det ingen anledning att göra en tur-och-retur tillbaka till datakällan. Cachen innehåller redan rätt data; det är bara den renderade `PivotTable` som behöver beräknas om. I detta fall är `pivot_table.calculate_data()` rätt val.

Detta undviker det onödiga källhämtningen och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel modifierar en icke-källrelaterad egenskap hos pivottabellen och anropar sedan `calculate_data()` för att rendera om den från den befintliga cachen.

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

# Lägg till en pivottabell med namnet "Pivot1" placerad i destinationscell E3, med källa från A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Tilldela fält: Fruit till Rad, Year till Kolumn, Amount till Data
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# Ändra en egenskap för vy/layout — detta är en presentation-förändring,
# så den kräver INTE att källdata läses igen via PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() renderar om DEN HÄR pivottabellens visning (data + stil) från
# datan som redan finns i PivotCache. Eftersom källdatan inte ändrades,
# görs ingen tur och retur till källan — endast de cachade värdena beräknas om
# till arbetsbladets celler.
pivot_table.calculate_data()

# Spara arbetsboken till disk
workbook.save("output.xlsx")
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera delad cache-påverkan — använd `PivotCache.get_pivot_tables()`. Denna metod returnerar samlingen av varje `PivotTable` som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cache-referenser, eller helt enkelt iterera samlingen som returneras av `get_pivot_tables()` och observera vilka pivottabeller som förekommer i den.

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

Före Aspose.Cells for Python via .NET v26.7 var standardmetoden för att uppdatera en pivottabell att anropa `PivotTable.refresh_data()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.

Det finns två skäl till att den tabellvisa `refresh_data()`-metoden är problematisk i verkliga arbetsböcker:

- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache, gör upprepade anrop till `refresh_data()` per pivottabell att samma cache hämtas om och om igen, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.refresh_all();`
- **Uppdatera NÅGRA av dem** → använd `pivot_table.pivot_cache.refresh();` för en cache. Eftersom cachen delas, uppdaterar detta enda anrop varje pivottabell som är byggd ovanpå den cachen. Andra pivottabeller som sitter på en redan uppdaterad cache kan tryggt hoppas över.
- **Endast pivotvyn/layouten har ändrats** → använd `pivot_table.calculate_data();` för att rendera om från den befintliga cachen utan någon källtur-och-retur.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok och öppna det första kalkylbladet
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- Bygg källdatan: Frukt / År / Belopp (rubrik + 9 rader) ---
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
# Både Pivot1 och Pivot2 delar EN underliggande PivotCache.
# Detta är exakt scenariot där det äldre per-tabell RefreshData()-tillvägagångssättet
# blir ineffektivt: att uppdatera en tabell hämtar om hela
# delade cachen, så att uppdatera N tabeller gör samma dyra hämtning N gånger.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- Ändra flera beloppsvärden i källdatan ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- FÖRÅLDRAD mönster (före 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # hämtar om från källan, uppdaterar hela cachen
# pivot_table2.refresh_data();  # hämtar om IGEN — cachen är redan färsk!
# Varje anrop bygger om den delade cachen, så N tabeller = N redundanta hämtningar.

# --- NYTT v26.7+ mönster: uppdatera cachen EN GÅNG, rendera sedan om efter behov ---
# Ett anrop till PivotCache.Refresh() hämtar de ändrade värdena till den delade
# cachen OCH beräknar om visningen av VARJE pivottabell som refererar till den.
# Eftersom Pivot1 och Pivot2 delar en PivotCache, uppdaterar detta enda anrop
# båda tabellerna — ingen andra källomgång krävs.
pivot_table1.pivot_cache.refresh()

# CalculateData() renderar bara om en pivottabells vy (data + stil)
# från data som redan finns i cachen — den rör INTE källan.
# Vi anropar det på Pivot2 här enbart för att demonstrera API:et: efter att cachen
# har uppdaterats en gång, kan vilken som helst beroende tabell renderas om utan att
# gå tillbaka till källan. Använd CalculateData() ensamt när bara
# pivottabellens vy/layoutinställningar har ändrats och cachen är aktuell.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## Vilket uppdaterings-API bör jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du bör välja var och en.

| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refresh_all()` | Ett anrop; täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.refresh_pivot_tables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivot_table.pivot_cache.refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivot_table.calculate_data()` | Hoppar över onödig källtur-och-retur. |
| Lista alla pivottabeller på en delad cache | `pivot_cache.get_pivot_tables()` | Använd för att räkna upp före bulkuppdatering. |

I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade tabellvisa `refresh_data()`. De är medvetna om delade cachar, de undviker redundanta källhämtningar, och de låter dig välja det minsta omfång som uppfyller ditt uppdateringskrav.

## Relaterade artiklar

- [Sparklines i Aspose.Cells for Python via .NET](/cells/sv/python-net/sparkline/)

{{< app/cells/assistant language="python" >}}