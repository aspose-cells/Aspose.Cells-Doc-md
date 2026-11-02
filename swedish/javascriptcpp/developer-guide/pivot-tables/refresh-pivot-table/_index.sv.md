---
title: Uppdatera pivottabeller och pivotcachar i Aspose.Cells for JavaScript via C++
description: Lär dig hur du uppdaterar pivottabeller i Aspose.Cells for JavaScript via C++ med hjälp av pivotuppdaterings-API,t för v26.7+. Den här artikeln beskriver workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData och pivotCache.getPivotTables med praktiska kodexempel.
linktitle: Uppdatera pivottabeller
keywords: Aspose.Cells, JavaScript via C++, pivottabell, uppdatering, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /sv/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder ett lagerindelat uppdaterings-API som låter dig ladda om pivotdata inom fyra olika omfattningar – från hela arbetsboken ner till en enda pivottabell. Från och med **Aspose.Cells for JavaScript via C++ v26.7** är den äldre metoden `pivotTable.refreshData()` markerad som föråldrad och bör ersättas med de effektivare, cachebaserade API:erna som beskrivs i den här artikeln.
{{% /alert %}}

## Introduktion
Att uppdatera en pivottabell är sällan en enda åtgärd. Under huven underhåller Aspose.Cells en lagerindelad datakedja som kopplar den ursprungliga källdatan till de renderade värden som du ser i kalkylbladet. Att förstå den här kedjan är nyckeln till att välja rätt uppdaterings-API i varje situation.
Datakedjan har fyra lager:
1. **Datakälla** – de ursprungliga kalkylbladsintervallen, databasfrågan eller konsolideringsintervallet där råvärdena finns.
2. **PivotCache** – ögonblicksbilden av källdatan i minnet. Varje pivottabell byggs ovanpå en `PivotCache`; här samlas och aggregeras alla data.
3. **PivotTable** – vyobjektet som definierar rad-, kolumn-, värde- och filterfält. En `PivotTable` läser *endast* från sin `PivotCache`, aldrig direkt från datakällan.
4. **Cells** – kalkylbladscellerna som returneras av `getCells()`, där `PivotTable` renderar sina beräknade värden och format.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (enumen `PivotTableSourceType`) anger varifrån cachedata kom. Från och med v26.7 stöder `pivotCache.refresh()` endast källtyperna **`SHEET`** och **`CONSOLIDATION`** – alltså data som finns i kalkylbladsintervall. Externa källor (databaser, externa anslutningar osv.) kan ännu inte uppdateras via cache-API:et.
På grund av den här kedjan finns två grundläggande uppdateringsvägar i Aspose.Cells:
- **`pivotTable.calculateData()`** – beräknar om en `PivotTable`s visning från redan cachat data, utan någon tur och retur till datakällan.
Alla scenarier i den här artikeln använder kalkylbladsceller som källdata, så källtypen är `SHEET` och uppdateringsåtgärderna fungerar som beskrivs.
{{% /alert %}}

## Snabbstart
Om du bara behöver den kortast möjliga kod som uppdaterar alla pivottabeller i arbetsboken räcker ett enda anrop:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Allt annat i den här artikeln förklarar när du bör välja ett snävare API.

## Obligatoriska importer
Alla JavaScript-exempel i den här artikeln börjar med följande modulimport eftersom pivottyperna exponeras via namespace `Aspose.Cells.Pivot`:
- `const Aspose = require('aspose.cells');`

## Uppdatera alla pivottabeller i arbetsboken
När du behöver säkerställa att varje pivotcache och varje pivottabell i arbetsboken återger de senaste källdatan är det enklaste och mest omfattande API:et `workbook.refreshAll()`. Ett enda anrop går igenom hela arbetsboken – det uppdaterar varje `PivotCache` från dess källa och beräknar sedan om varje beroende `PivotTable`. Detta är den rekommenderade metoden för allmänna, fullständiga dokumentuppdateringar när prestanda inte är något hinder.
Exemplet nedan bygger en arbetsbok med ett källintervall för frukt, år och belopp, skapar en pivottabell, ändrar vissa källdata och använder sedan `refreshAll()` för att uppdatera allt med ett enda anrop.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Skapa en ny arbetsbok
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Skriv rubrikraden till cellerna A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Skriv datarader till cellerna A2:C9 (8 rader med fruktdata för 2020 och 2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Lägg till en pivottabell: källområdet "A1:C9", destinationscellen "E3"
            const pivotTableIndex = worksheet.pivotTables.add(
                "=A1:C9",
                "E3",
                "PivotTable1"
            );
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Tilldela pivotfält: Fruit till rader, Year till kolumner, Amount till data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Ändra flera Amount-värden i källdatan för att simulera ändringar
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Uppdatera alla pivottabeller och pivotcachar i arbetsboken
            workbook.refreshAll();
            // Spara arbetsboken
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Uppdatera alla pivottabeller i ett kalkylblad
I vissa fall behöver du endast uppdatera de pivottabeller som finns i ett visst kalkylblad – till exempel när pivottabeller i andra kalkylblad är kända att vara orelaterade och inte ska röras. För detta fall erbjuder Aspose.Cells `worksheet.refreshPivotTables()`, som är begränsad till en enda `Worksheet`-instans.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTableIndex = worksheet.pivotTables.add("=A1:C9", "E3", "PivotTable1");
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## Uppdatera en enda pivottabell
När du vill ha detaljerad kontroll över en enda pivottabell ger det cachebaserade API:et dig två alternativ. Valet mellan dem beror på vad som faktiskt har ändrats: källdata eller endast vy- och layoutinställningarna för pivottabellen.

### Källdata har ändrats – använd `pivotCache.refresh()`
Om källdata har ändrats är rätt startpunkt `pivotTable.getPivotCache().refresh()`. Anropet läser in källdatan i cachen på nytt och beräknar sedan om varje `PivotTable` som är beroende av den cachen.

### Endast vyn eller layouten har ändrats – använd `pivotTable.calculateData()`
Om källdata *inte* har ändrats men endast pivottabellens vy- eller layoutinställningar har ändrats, till exempel om ett fält har flyttats till ett annat område eller om en inställning för uppdatering vid öppning har växlat, finns inget behov av att gå tillbaka till datakällan. Cachen innehåller redan rätt data; endast den renderade `PivotTable` behöver beräknas om. I detta fall är `pivotTable.calculateData()` rätt val.
Exemplet nedan ändrar en egenskap som inte hör till källdatan och anropar sedan `calculateData()` för att rendera om pivottabellen från den befintliga cachen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Skriv rubrikraden Fruit / Year / Amount
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // Skriv 8 datarader (raderna 2–9, som passar till källintervallet A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Lägg till en pivottabell på destinationscellen E3 med A1:C9 som datakälla
                const pivotTableIndex = worksheet.pivotTables.add(
                    "=A1:C9",
                    "E3",
                    "PivotTable1"
                );
                const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
                // Tilldela fält: Fruit till Row, Year till Column, Amount till Data
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Ändra en egenskap för vy/layout – detta är endast en presentationsändring,
                // så källdatan behöver inte läsas om via PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() renderar om DENNA pivottabells visning (data + format) från de
                // data som redan finns i PivotCache. Eftersom källdatan inte har ändrats,
                // sker ingen tur och retur till källan – endast de cachelagrade värdena beräknas om
                // och skrivs till arbetsbladscellerna.
                pivotTable.calculateData();
                // Spara arbetsboken till disk
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

En arbetsbok innehåller ofta många pivottabeller som alla vilar på en och samma cache. Om du behöver enumerera dem – till exempel före en batchuppdatering eller för att diagnostisera effekterna av en delad cache – använder du `pivotCache.getPivotTables()`. Metoden returnerar samlingen av alla `PivotTable` som är beroende av den angivna cachen.

## Migrera från den föråldrade `pivotTable.refreshData()`
Före Aspose.Cells for JavaScript via C++ v26.7 var standardmetoden att uppdatera en pivottabell att anropa `pivotTable.refreshData()` för varje pivottabell. Från och med v26.7 är metoden markerad som **föråldrad** och bör ersättas med de cachebaserade API:erna som beskrivs ovan.
Det finns två skäl till att metoden `refreshData()` per tabell är problematisk i verkliga arbetsböcker:
- Den hämtar data från källan *varje* gång den anropas, även när källan inte har ändrats.
Rekommenderade ersättningar är:
Exemplet nedan visar det nya effektiva mönstret för arbetsböcker med flera pivottabeller som delar en enda cache.

## Vilket uppdaterings-API bör jag använda?
Tabellen nedan sammanfattar de tillgängliga uppdaterings-API:erna och när du bör välja varje enskilt API.
| Mål | Rekommenderat API | Anteckningar |
|------|-----------------|-------|
| Uppdatera allt i arbetsboken | `workbook.refreshAll()` | Ett anrop; täcker alla cachar och tabeller. |
| Uppdatera endast pivottabeller i ett kalkylblad | `worksheet.refreshPivotTables()` | Begränsat till ett kalkylblad. |
| Källdata har ändrats för en cache | `pivotTable.getPivotCache().refresh()` | Uppdaterar ALLA pivottabeller i den delade cachen. |
| Endast vy-/layoutinställningar har ändrats | `pivotTable.calculateData()` | Hoppar över onödig tur och retur till källan. |
| Lista alla pivottabeller i en delad cache | `pivotCache.getPivotTables()` | Använd för att enumerera före massuppdatering. |
I praktiken bör du föredra de cachebaserade API:erna framför den föråldrade `refreshData()` per tabell. De är medvetna om delade cachar, undviker redundanta hämtningar från källan och låter dig välja den minsta omfattning som uppfyller ditt uppdateringsbehov.

## Vanliga problem
- **Att glömma att uppdatera före sparande.** En pivottabell skriver endast sina renderade värden till kalkylbladet när dess datakedja uppdateras. Om du ändrar källceller anropar du `pivotCache.refresh()` (eller `workbook.refreshAll()`) före `workbook.save()`, annars innehåller den sparade filen fortfarande de gamla aggregerade värdena.
- **Att anropa den föråldrade `refreshData()` för varje tabell.** I v26.7 är `pivotTable.refreshData()` markerad som föråldrad och hämtar källan på nytt vid varje anrop. Med flera pivottabeller som delar en cache innebär det N redundanta hämtningar från källan. Ersätt med ett enda anrop till `pivotCache.refresh()` följt av `pivotTable.calculateData()` för varje tabell.
- **Att uppdatera när endast layouten har ändrats.** Om du endast har ändrat en pivottabells vy, till exempel kolumnordningen eller `getConsolidationFunction()`, utan att röra källdatan, är `pivotCache.refresh()` onödig och långsam. Anropa `pivotTable.calculateData()` för att rendera om från den befintliga cachen.
- **En extern källa stöds inte av `pivotCache.refresh()`.** Om pivottabellens källa kommer från en extern anslutning, till exempel en databas eller OLAP-kub, kan `pivotCache.refresh()` inte uppdatera den i v26.7 – den stöder för närvarande endast källtyperna `SHEET` och `CONSOLIDATION`. För externa källor kan du öppna arbetsboken på nytt eller bygga om cachen från källan.

{{< app/cells/assistant language="javascript-cpp" >}}