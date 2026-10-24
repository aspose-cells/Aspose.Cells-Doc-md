---
title: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Java
linktitle: Uppdatera pivottabeller och pivotcacheminnen i Aspose.Cells for Java
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for Java med v26.7+ pivot-uppdaterings-API,et. Den här artikeln tar upp RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData och GetPivotTables med praktiska kodexempel.
keywords: Aspose.Cells, Java, pivottabell, uppdatera, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /sv/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells tillhandahåller ett skiktat uppdaterings-API som låter dig ladda om pivotdata i fyra olika omfång — från hela arbetsboken ner till en enskild pivottabell. Från och med **Aspose.Cells for Java v26.7** är den äldre metoden `PivotTable.refreshData()` markerad som föråldrad och bör ersättas med de mer effektiva, cache-medvetna API:erna som beskrivs i den här artikeln.
{{% /alert %}}

## Introduction
Att uppdatera en pivottabell är sällan en enskild åtgärd. Bakom kulisserna upprätthåller Aspose.Cells en skiktad datakedja som kopplar samman dina ursprungliga källdata med de renderade värdena du ser i kalkylbladet. Att förstå denna kedja är nyckeln till att välja rätt uppdaterings-API för varje situation.
Datakedjan i fyra lager är:
1. **Datakälla** — de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** — ögonblicksbilden i minnet av källdatan. Varje pivottabell är byggd ovanpå en `PivotCache`; det är här all data samlas in och aggregeras.
3. **PivotTable** — vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *bara* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** — kalkylbladets `Cells` som `PivotTable` renderar sina beräknade värden och stilar till.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) anger var cache-datan kom ifrån. Från och med v26.7 stöder `PivotCache.refresh()` endast källtyperna **`Sheet`** och **`Consolidation`** — det vill säga data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) kan ännu inte uppdateras via cache-API:et.
På grund av denna kedja finns det två grundläggande uppdateringsvägar i Aspose.Cells:
- **`PivotTable.calculateData()`** — beräknar om en `PivotTable`s visning från redan cachad data, utan att gå tillbaka till datakällan.
Alla scenarier i den här artikeln använder kalkylbladscells-källdata, så källtypen är `Sheet` och uppdateringsåtgärderna beter sig enligt beskrivningen.
{{% /alert %}}

## Quick Start
Om du bara behöver den kortaste möjliga koden som uppdaterar varje pivot i arbetsboken räcker det med ett enda anrop:

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Allt annat i den här artikeln förklarar när du istället bör välja ett smalare API.

## Required Import Statements
Alla Java-exempel i den här artikeln inleds med följande import-satser eftersom pivottyperna ligger i paketet `com.aspose.cells.pivot`:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återspeglar de senaste källdatan är det enklaste och mest omfattande API:et `Workbook.refreshAll()`. Ett enda anrop traverserar hela arbetsboken — uppdaterar varje `PivotCache` från sin källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar där prestanda inte är ett bekymmer.
Följande exempel bygger en arbetsbok med ett Fruit/Year/Amount-källintervall, skapar en pivottabell, ändrar några källvärden och använder sedan `refreshAll()` för att uppdatera allt i ett enda anrop.

```java
import com.aspose.cells.*;
// Skapa en ny arbetsbok
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Skriv rubrikraden till cellerna A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Skriv datarader till cellerna A2:C9 (8 rader fruktdata för 2020 och 2021)
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
// Lägg till en pivottabell: källområde "A1:C9", destinationscell "E3", namn "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Tilldela pivotfält: Fruit till Rows, Year till Columns, Amount till Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Ändra flera Amount-värden i källdatan för att simulera ändringar
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Uppdatera alla pivottabeller/pivotcachar i arbetsboken
workbook.refreshAll();
// Spara arbetsboken
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
Ibland behöver du bara uppdatera de pivottabeller som finns på ett specifikt kalkylblad — till exempel när pivottabeller på andra kalkylblad är kända för att vara orelaterade och inte bör röras. För detta fall tillhandahåller Aspose.Cells `Worksheet.refreshPivotTables()`, som är begränsat till en enda `Worksheet`-instans.

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

## Refresh a Single Pivot Table
När du vill ha finkornig kontroll över en enskild pivottabell ger det cache-baserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: underliggande källdata, eller bara vy-/layoutinställningarna för pivottabellen i sig.

### Source Data Changed — Use `PivotCache.refresh()`
Om underliggande källdata har ändrats är rätt startpunkt `pivotTable.getPivotCache().refresh()`. Detta anrop läser om källdatan till cacheminnet och beräknar sedan om varje `PivotTable` som är beroende av det cacheminnet.

### Only View/Layout Changed — Use `calculateData()`
Om källdatan *inte* har ändrats utan bara pivottabellens vy- eller layoutinställningar har modifierats (till exempel har ett fält flyttats till ett annat område, eller en inställning för uppdatering vid öppning har växlats), finns det ingen anledning att gå tillbaka till datakällan. Cacheminnet innehåller redan rätt data; det är bara den renderade `PivotTable` som behöver beräknas om. I detta fall är `pivotTable.calculateData()` rätt val.
Följande exempel modifierar en icke-källrelaterad egenskap hos pivottabellen och anropar sedan `calculateData()` för att rendera om den från befintlig cache.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Skriv rubrikraden med Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Skriv 8 datarader (rader 2-9, som passar till källintervallet A1:C9)
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
// Lägg till en pivottabell med namnet "Pivot1" som är placerad på destinationscellen E3 och har A1:C9 som datakälla
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Tilldela fält: Fruit till rad, Year till kolumn, Amount till data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Ändra en egenskap för vy/layout -- detta är enbart en ändring av presentationen,
// så det kräver INTE att källdatan läses om via PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() renderar denna pivottabells visning (data + stil) på nytt utifrån
// de data som redan finns i PivotCache. Eftersom källdatan inte ändrades,
// sker ingen rundtur till källan -- endast de cachelagrade värdena beräknas om
// in i kalkylarkets celler.
pivotTable.calculateData();
// Spara arbetsboken till disk
workbook.save("output.xlsx");
```

En arbetsbok innehåller ofta många pivottabeller som alla ligger ovanpå ett delat cacheminne. För att räkna upp dem — till exempel innan du utför en batchuppdatering, eller för att diagnostisera påverkan av delad cache — använd `PivotCache.getPivotTables()`. Den här metoden returnerar samlingen av varje `PivotTable` som är beroende av det givna cacheminnet.

## Migrating from the Obsolete `PivotTable.refreshData()`
Före Aspose.Cells for Java v26.7 var standardmetoden för att uppdatera en pivottabell att anropa `PivotTable.refreshData()` på varje pivottabell individuellt. Från och med v26.7 är den metoden markerad som **föråldrad** och bör ersättas med de cache-medvetna API:erna som beskrivs ovan.
Det finns två anledelser till att per-tabell-metoden `refreshData()` är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
De rekommenderade ersättningarna är:
Följande exempel visar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar ett enda cacheminne.

## Which Refresh API Should I Use?
Tabellen nedan sammanfattar tillgängliga uppdaterings-API:er och när du ska välja var och en.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `Workbook.refreshAll()` | Ett anrop; täcker alla cacheminnen och tabeller. |
| Uppdatera endast pivottabeller på ett enskilt blad | `Worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för ett cacheminne | `pivotTable.getPivotCache().refresh()` | Uppdaterar ALLA pivottabeller på det delade cacheminnet. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödiga källresor. |
| Lista alla pivottabeller på ett delat cacheminne | `pivotCache.getPivotTables()` | Använd för att räkna upp före massuppdatering. |
I praktiken bör du föredra de cache-baserade API:erna framför den föråldrade per-tabell-metoden `refreshData()`. De är medvetna om delade cacheminnen, de undviker redundanta källhämtningar och de låter dig välja det minsta omfång som uppfyller ditt uppdateringskrav.

## Common Pitfalls
- **Glömmer att uppdatera innan du sparar.** En pivottabell skriver bara sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller, anropa `PivotCache.refresh()` (eller `Workbook.refreshAll()`) före `Workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Anropar den föråldrade `refreshData()` per tabell.** I v26.7 är `PivotTable.refreshData()` markerad som föråldrad och hämtar om källan för varje anrop. Med flera pivottabeller som delar ett cacheminne innebär detta N redundanta källhämtningar. Ersätt med ett enda `PivotCache.refresh()` följt av `calculateData()` per tabell.
- **Uppdaterar när bara layouten har ändrats.** Om du bara ändrade en pivottabells vy (kolumnordning, `ConsolidationFunction` osv.) utan att röra källdata är `PivotCache.refresh()` onödigt och långsamt. Anropa `pivotTable.calculateData()` för att rendera om från befintlig cache.
- **Extern källa stöds inte av `PivotCache.refresh()`.** Om pivottabellens källa kommer från en extern anslutning (databas, OLAP-kub osv.) kan `PivotCache.refresh()` inte uppdatera den i v26.7 — den stöder för närvarande endast källtyperna `Sheet` och `Consolidation`. För externa källor, öppna arbetsboken igen eller bygg om cacheminnet från källan.

{{< app/cells/assistant language="java" >}}