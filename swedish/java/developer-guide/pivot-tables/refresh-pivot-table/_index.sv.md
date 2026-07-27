---
title: Uppdatera pivottabeller i Aspose.Cells for Java
linktitle: Uppdatera pivottabeller i Aspose.Cells for Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Java med pivot-uppdaterings-API,et i v26.7+. Den här artikeln tar upp RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Java, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells tillhandahåller ett lagerindelat uppdaterings-API som låter dig läsa in pivotdata igen på fyra olika omfång — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Java v26.7** är den äldre metoden `PivotTable.refreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:er som beskrivs i den här artikeln.

{{% /alert %}}

## Introduktion

Att uppdatera en pivottabell är sällan en enskild åtgärd. Bakom kulisserna underhåller Aspose.Cells en lagerindelad datakedja som kopplar ihop dina ursprungliga källdata med de renderade värdena du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.

Den fyrlagers datakedjan är:

1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där de råa värdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

Ett särskilt viktigt koncept är den **delade cachen**. När flera pivottabeller i en arbetsbok refererar till samma källintervall delar de *en* `PivotCache`-instans. En enskild `PivotCache` kan refereras av många pivottabeller, och att uppdatera den cachen uppdaterar alla beroende `PivotTable`r på en gång.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) anger var cachedatan kom ifrån. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa kopplingar etc.) är ännu inte möjliga att uppdatera via cache-API:et.

{{% /alert %}}

På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:

- **`PivotCache.refresh()`** — läser in källa → cache igen OCH beräknar om alla beroende `PivotTable`r i en enda åtgärd.
- **`PivotTable.calculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.

Alla scenarier i den här artikeln använder kalkylbladscells-källdata, så källtypen är `Sheet` och uppdateringsåtgärder beter sig enligt beskrivningen.

## Obligatoriska import-satser

Alla Java-exempel i den här artikeln inleds med följande import-satser eftersom pivottyperna ligger i paketet `com.aspose.cells.pivot`:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Uppdatera alla pivottabeller i arbetsboken

När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar den senaste källdatan är det enklaste och mest heltäckande API:et `Workbook.refreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett problem.

Följande exempel bygger en arbetsbok med ett källintervall för Fruit/Year/Amount, skapar en pivottabell, ändrar några källvärden och använder sedan `refreshAll()` för att uppdatera allt i ett enda anrop.

```java
import com.aspose.cells.*;

// Skapa en ny arbetsbok
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Skriv rubrikrad i cellerna A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Skriv datarader i cellerna A2:C9 (8 rader med fruktdata över 2020 och 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);

// Lägg till en pivottabell: källintervall "A1:C9", målcell "E3", namn "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Tilldela pivotfält: Fruit till Rader, Year till Kolumner, Amount till Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Ändra flera Amount-värden i källdatan för att simulera ändringar
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// Uppdatera varje pivottabell / pivotcache i arbetsboken
workbook.refreshAll();

// Spara arbetsboken
workbook.save("output.xlsx");
```

## Uppdatera alla pivottabeller på ett enskilt kalkylblad

Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, som är begränsat till en enskild `Worksheet`-instans.

Detta är mer selektivt än `Workbook.refreshAll()`: endast pivottabellerna på det riktade kalkylbladet uppdateras, medan pivottabeller på andra kalkylblad lämnas orörda.

Följande exempel fyller i samma Fruit/Year/Amount-källdata, lägger till en pivottabell på det första kalkylbladet, ändrar några källvärden och uppdaterar sedan endast pivottabellerna på det kalkylbladet.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## Uppdatera en enskild pivottabell

När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: den underliggande källdatan, eller bara vy-/layoutinställningarna för pivottabellen i sig.

### Källdata har ändrats — Använd `PivotCache.refresh()`

Om den underliggande källdatan har ändrats är rätt startpunkt `pivotTable.getPivotCache().refresh()`. Detta anrop läser in källdatan till cachen igen och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

{{% alert color="primary" %}}

Eftersom pivottabeller delar en enda `PivotCache`-instans beräknar ett anrop till `PivotCache.refresh()` om **alla** pivottabeller som är byggda på samma cache — inte bara den du refererar till. Om två pivottabeller delar samma källintervall uppdaterar en cache-uppdatering båda.

{{% /alert %}}

Följande exempel skapar två pivottabeller på samma källintervall för att demonstrera detta delade cache-beteende, ändrar några källvärden och uppdaterar sedan genom en cache-referens.

```java
import com.aspose.cells.*;

// Skapa en ny arbetsbok och öppna det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Skriv rubrikrad: Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Skriv ungefär 9 datarader (druva / blåbär / kiwi / körsbär över 2020-2021)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// Lägg till den första pivottabellen "Pivot1" förankrad vid cell E3, källintervall A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Tilldela fält för Pivot1
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// Lägg till en ANDRA pivottabell "Pivot2" förankrad vid E15 med SAMMA källintervall A1:C9
// Både Pivot1 och Pivot2 delar en enda PivotCache eftersom källintervallet är identiskt.
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Tilldela samma fält för Pivot2
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// Ändra flera Belopp-cellvärden i källdatan för att simulera en dataändring
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// Uppdatera den delade PivotCachen.
// Eftersom Pivot1 och Pivot2 delar samma PivotCache, uppdaterar detta enda anrop
// BÅDA pivottabellerna (data + stil) från den uppdaterade källan.
pivotTable1.refreshData();

// Spara arbetsboken
workbook.save("output.xlsx");
```

### Endast vy/layout har ändrats — Använd `calculateData()`

Om källdatan *inte* har ändrats men bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel att ett fält har flyttats till ett annat område, eller att en inställning för uppdatering vid öppning har växlats), finns det inget behov av att gå tillbaka till datakällan. Cachen har redan rätt data; bara den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.calculateData()` rätt val.

Detta undviker det onödiga källhämtningen och är avsevärt snabbare när många pivottabeller delar samma cache.

Följande exempel modifierar en egenskap som inte är källa för pivottabellen och anropar sedan `calculateData()` för att rendera om den från den befintliga cachen.

```java
ells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Skriv rubrikrad för Frukt / År / Belopp
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Skriv 8 datarader (raderna 2-9, som passar källintervallet A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// Lägg till en pivottabell med namnet "Pivot1" placerad vid destinationscell E3, med källa från A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Tilldela fält: Frukt till Rad, År till Kolumn, Belopp till Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Ändra en visnings-/layout-egenskap -- detta är en presentationsförändring,
// så det kräver INTE att källdatan läses igen via PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() återrenderar DENNA pivottabells visning (data + stil) från den
// data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
// utförs ingen tur och retur till källan -- endast de cachelagrade värdena beräknas om
// in i arbetsbladets celler.
pivotTable.calculateData();

// Spara arbetsboken till disk
workbook.save("output.xlsx");
```

## Hämta alla pivottabeller som delar samma PivotCache

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå en delad cache. För att räkna upp dem — till exempel innan du utför en batch-uppdatering, eller för att diagnostisera påverkan från delad cache — använd `PivotCache.getPivotTables()`. Den här metoden returnerar samlingen av alla `PivotTable`r som är beroende av den givna cachen.

Detta är också det mest direkta sättet att bekräfta att två pivottabeller verkligen delar samma `PivotCache`-instans: du kan jämföra cache-referenser (med operatorn `==`), eller helt enkelt iterera samlingen som returneras av `getPivotTables()` och observera vilka pivottabeller som finns i den.

Följande exempel skapar två pivottabeller på samma källintervall, verifierar att de delar samma cache-instans och räknar sedan upp cachens pivottabeller.


## Migrera från den föråldrade `PivotTable.refreshData()`

Före Aspose.Cells for Java v26.7 var standard sättet att uppdatera en pivottabell att anropa `PivotTable.refreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:er som beskrivs ovan.

Det finns två anledningar till att per-tabell-metoden `refreshData()` är problematisk i verkliga arbetsböcker:

- Den hämtar data från källan *varje gång* den anropas, även när källan inte har ändrats.
- Varje anrop uppdaterar hela den delade cachen. När många pivottabeller delar en cache, gör upprepade anrop till `refreshData()` per pivottabell att samma cache hämtas om och om igen, vilket är mycket långsamt.

De rekommenderade ersättningarna är:

- **Uppdatera ALLA pivottabeller i arbetsboken** → använd `workbook.refreshAll();`
- **Uppdatera NÅGRA av dem** → använd `pivotTable.getPivotCache().refresh();` för en cache. Eftersom cachen är delad uppdaterar detta enda anrop varje pivottabell som är byggd ovanpå den cachen. Andra pivottabeller som ligger på en redan uppdaterad cache kan tryggt hoppas över.
- **Endast pivotvyn/layouten har ändrats** → använd `pivotTable.calculateData();` för att rendera om från den befintliga cachen utan någon källhämtning.

Följande exempel demonstrerar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- Bygg källdatan: Frukt / År / Belopp (rubrik + 9 rader) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- Lägg till den första pivottabellen (Pivot1) vid målcell E3 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Lägg till den ANDRA pivottabellen (Pivot2) på SAMMA källintervall ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- Ändra flera beloppsvärden i källdatan ---
sheet.getCells().get("C2").putValue(5000);   // Druva  2020
sheet.getCells().get("C5").putValue(7500);   // Körsbär 2020
sheet.getCells().get("C9").putValue(9500);   // Körsbär 2021

// --- NYTT v26.7+ mönster: uppdatera cachen EN GÅNG, rendera sedan om efter behov ---
pivotTable1.getPivotCache().refresh();

// Rendera om den andra pivottabellens vy/layout utan att röra källan
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## Vilket uppdaterings-API ska jag använda?

Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du ska välja var och en.

| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop; täcker alla cacher och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt ark | `Worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.getPivotCache().refresh()` | Uppdaterar ALLA pivottabeller på den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödig källhämtning. |
| Lista alla pivottabeller på en delad cache | `pivotCache.getPivotTables()` | Använd för att räkna upp före bulk-uppdatering. |

I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade per-tabell-metoden `refreshData()`. De är medvetna om delade cacher, de undviker redundanta källhämtningar och de låter dig välja det minsta omfång som uppfyller ditt uppdateringskrav.

{{< app/cells/assistant language="java" >}}
