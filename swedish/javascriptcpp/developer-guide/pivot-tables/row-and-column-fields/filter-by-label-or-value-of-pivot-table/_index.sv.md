---
title: Filtrering av pivottabeller efter etikett eller värde
linktitle: Filtrering av pivottabeller efter etikett eller värde
description: Aspose.Cells for JavaScript via C++ stöder omfattande filtreringsfunktioner för pivottabeller. Den här artikeln beskriver hur pivottabellens data kan filtreras med etikettfilter, datumfilter, värdefilter, topp 10-filter samt genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, JavaScript via C++-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölja pivotobjekt
type: docs
weight: 10
url: /sv/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datum- och tidsceller eller tomma celler, tillämpa värdefilter på aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `isHidden`. Varje strategi är tillgänglig via ett eget API på klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men råa sammanställningar innehåller ofta mycket mer information än vad du behöver presentera. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for JavaScript via C++ återger de filtreringsfunktioner som finns i Microsoft Excel och exponerar dem programmatiskt, så att rapportgenereringen kan automatiseras fullständigt.
De filtreringsstrategier som behandlas i den här artikeln är:
1. **Etikettfilter** — filtrerar pivotobjekt i rad- eller kolumnfält baserat på deras textetiketter.
2. **Datumfilter** — filtrerar rad- eller kolumnfält som endast innehåller datum- och tidsvärden (eller tomma värden).
3. **Värdefilter** — filtrerar pivotobjekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** — visar endast de N översta eller lägsta pivotobjekten, rangordnade efter ett värdefält.
5. **Dölja/visa pivotobjekt** — styr manuellt synligheten för varje enskilt pivotobjekt i ett fält.
Varje tillvägagångssätt använder en annan metod i klassen `PivotField` eller en egenskap i klassen `PivotItem`. När du har tillämpat ett filter måste du anropa `pivotCache.refresh()` på pivottabellen så att cachelagrade data och beräknade värden återspeglar filtrets nya läge.

## **Etikettfilter**
Ett etikettfilter gör det möjligt att filtrera pivotobjekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter med ett mönster. Det är användbart när du endast vill visa produkter vars namn börjar med en viss bokstav, innehåller ett visst ord eller uppfyller något annat kriterium baserat på etiketten.
Aspose.Cells exponerar etikettfiltrering via metoden `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. Argumentet `filterType` väljer jämförelseläge (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` med mera). Argumenten `label1` och `label2` anger jämförelsetexten. Ange `""` för `label2` när endast ett värde behöver jämföras, till exempel vid jämförelser av typen börjar med eller innehåller.
Det följande exemplet läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast pivotobjekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Ladda den befintliga arbetsboken som innehåller en pivottabell
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Få åtkomst till kalkylarket via index (första kalkylarket)
                    const worksheet = workbook.worksheets.get(0);
                    // Få åtkomst till pivottabellen via index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Hämta det första PivotField i radområdet
                    const rowField = pivotTable.rowFields.get(0);
                    // Tillämpa etikettfiltret — visa endast rader vars etiketter börjar med det angivna prefixet
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Uppdatera och beräkna om pivottabellens data så att filtret får effekt
                    pivotTable.refreshData();
                    // Spara arbetsboken tillbaka till disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Datumfilter**
Datumfilter gör det möjligt att begränsa en pivottabell med kriterier baserade på datum, till exempel i dag, förra veckan, denna månad, nästa kvartal eller ett visst datumintervall. Det är specialiserade filter som endast fungerar mot fält som lagrar datum- och tidsinformation.

{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet bara innehåller datum- och tidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper, till exempel tal eller text, ger datumfiltret inte det förväntade resultatet. Kontrollera att fältet är formaterat som ett datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar filtret.
Aspose.Cells exponerar datumfiltrering via metoden `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. Enumerationen `PivotFilterType` innehåller särskilda datumvärden, till exempel `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på den valda filtertypen anger du ett eller två `DateTime`-värden (för `Between` anger du start- och slutdatum).
Det följande exemplet läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga pivotobjekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

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
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Ladda den befintliga arbetsboken som innehåller pivottabellen
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Få åtkomst till kalkylbladet som innehåller pivottabellen (via index)
                const worksheet = workbook.worksheets.get(0);
                // Få åtkomst till pivottabellen via index
                const pivotTable = worksheet.pivotTables.get(0);
                // Hämta datumfältet PivotField från radområdet
                // (Datumfilter fungerar endast när rad-/kolumnområdet endast innehåller datum- och tidsceller eller tomma celler)
                const dateField = pivotTable.rowFields.get(0);
                // Definiera datumkriteriet för filtret Mellan
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Använd datumfiltret på pivotfältet
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Uppdatera och beräkna om pivottabellen så att filtret får effekt
                pivotTable.refreshData();
                // Spara arbetsboken
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Värdefilter**
Värdefilter fungerar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. I stället för att matcha textetiketter jämför de numeriska summor med ett tröskelvärde. Typiska användningsfall är att endast visa produkter vars summa av försäljning överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering via metoden `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Parametern `valueFieldIndex` anger vilket datafält som ska utvärderas (använd `pivotTable.getDataFields().indexOf(dataField)` eller iterera över samlingen för att hitta positionen). Parametern `filterType` anger jämförelsetyp, till exempel `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. De två `double`-argumenten anger tröskelvärdet eller tröskelvärdena.
Det följande exemplet läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller pivotobjekt vars aggregerade försäljning överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

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
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Hitta datafältets index manuellt eftersom PivotFieldCollection inte har IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.refreshData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **Topp 10-filter**
Ett topp 10-filter är en specialiserad form av värdefilter som endast behåller de N högsta eller lägsta pivotobjekten baserat på ett valt värdefält. Det används ofta för att skapa rankningar, till exempel ”topp 10 produkter efter intäkt” eller ”de 5 lägsta regionerna efter antal försäljningar”.

{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdefält i dataområdet. Utan minst ett värdefält finns inget aggregerat mått att rangordna pivotobjekten efter, och filtret kan inte tillämpas.
Aspose.Cells exponerar topp 10-filtrering via metoden `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Parametern `valueFieldIndex` är indexet för det datafält vars aggregerade värden används för att rangordna pivotobjekten. `filterType` avgör hur `itemCount` tolkas (`Count` behåller ett bestämt antal pivotobjekt, `Percent` behåller en procentandel av pivotobjekten så att `itemCount` är själva procentandelen), `isTop` anger om de översta pivotobjekten (true) eller de lägsta pivotobjekten (false) ska behållas, och `itemCount` anger hur många pivotobjekt, eller vilken procentandel, som ska behållas.
Det följande exemplet läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 högsta pivotobjekten baserat på summan av försäljningen, uppdaterar pivottabellen och sparar arbetsboken.
{{% /alert %}}

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
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Ladda den befintliga arbetsboken som innehåller pivottabellen
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Hämta kalkylarket som innehåller pivottabellen (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Hämta pivottabellen efter index
                const pivotTable = worksheet.pivotTables.get(0);
                // Kontrollera att det finns minst ett värdefält i dataområdet
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Hämta pivotfältet för målraden (det fält som vi vill tillämpa Top 10 på)
                const rowField = pivotTable.rowFields.get(0);
                // Det första (och enda) datafältet finns på index 0; Top 10 rangordnar efter det.
                const valueFieldIndex = 0;
                // Tillämpa Top 10-filtret på radfältet:
                //   - valueFieldIndex = 0 — datafältet som används för att rangordna objekt
                //   - filterType  = PivotFilterType.Count (behåll ett bestämt antal objekt;
                //     PivotFilterType.Percent skulle tolka 10 som "topp 10 procent")
                //   - isTop       = true (topp N; false skulle betyda botten N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Uppdatera pivottabellens data och beräkna om den så att filtret får effekt
                pivotTable.refreshData();
                // Spara arbetsboken
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Filtrera genom att dölja eller visa pivotobjekt**
Utöver de strukturerade API:erna för filtrering kan du med Aspose.Cells styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera över samlingen `pivotField.getPivotItems()` i en `PivotField` och växla egenskapen `isHidden` kan du selektivt dölja specifika pivotobjekt utan att tillämpa ett formelbaserat filter. Om du anger `pivotItem.isHidden = true` döljs pivotobjektet från pivottabellen. Om du anger `pivotItem.isHidden = false` visas det igen.
Den här metoden är användbar när filterregeln är oregelbunden eller specifik för en viss pivotpost, till exempel när ett fåtal namngivna kategorier som inte ska visas i en viss rapport ska döljas. Exemplet nedan läser in en arbetsbok med en pivottabell, döljer ett specifikt pivotobjekt efter namn, visar hur det kan visas igen, uppdaterar pivottabellen och sparar arbetsboken.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Ladda en befintlig arbetsbok som innehåller en pivottabell
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Hämta det första kalkylarket som innehåller pivottabellen
                const sheet = workbook.worksheets.get(0);
                // Hämta pivottabellen via index (den första pivottabellen på kalkylarket)
                const pivotTable = sheet.pivotTables.get(0);
                // Hämta mål-PivotField (det första fältet för radetiketter som vi ska dölja/visa objekt i)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterera genom PivotItems-samlingen för det valda PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Dölj pivotobjekt som matchar ett specifikt namn/kriterium
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrera att visa objekt: visa ett tidigare dolt pivotobjekt igen
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Uppdatera och beräkna om pivottabellen så att ändringarna träder i kraft
                pivotTable.refreshData();
                // Spara arbetsboken — dolda objekt förblir i underliggande data
                // men utesluts från pivottabellens visade resultat
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Sammanfattning**
Aspose.Cells for JavaScript via C++ erbjuder en komplett uppsättning filtreringsfunktioner för pivottabeller som motsvarar funktionerna i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filter används för att skapa rankningar. När filterregeln är oregelbunden erbjuder egenskapen `pivotItem.isHidden` ett flexibelt alternativ för enskilda pivotobjekt. Genom att kombinera dessa strategier – till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika pivotobjekt – kan du skapa precist avgränsade pivottabellrapporter helt med kod.

{{< app/cells/assistant language="javascript-cpp" >}}