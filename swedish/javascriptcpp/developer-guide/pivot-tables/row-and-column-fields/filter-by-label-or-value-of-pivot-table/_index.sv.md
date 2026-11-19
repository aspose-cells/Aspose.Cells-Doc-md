---
title: Filtrera pivottabeller efter etikett eller värde
linktitle: Filtrera pivottabeller efter etikett eller värde
description: Aspose.Cells for JavaScript via C++ stöder omfattande filtreringsfunktioner för pivottabeller. Den här artikeln förklarar hur du filtrerar data i pivottabeller med etikettfilter, datumfilter, värdefilter, topp 10-filter och genom att dölja eller visa pivotobjekt.
keywords: Aspose.Cells, JavaScript via C++-bibliotek, kalkylblad, pivottabell, filter, etikettfilter, värdefilter, datumfilter, topp 10-filter, pivotobjekt, dölja pivotobjekt
type: docs
weight: 10
url: /sv/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder fem praktiska strategier för att filtrera de data som visas i en pivottabell. Du kan tillämpa etikettfilter på textbaserade rad- eller kolumnfält, använda datumfilter när fältet endast innehåller datumtidsceller eller tomma celler, tillämpa värdefilter på aggregerade tal, använda topp 10-filter för att rangordna efter ett värdefält eller manuellt dölja och visa enskilda pivotobjekt med egenskapen `isHidden`. Varje strategi exponeras via dedikerade API:er i klasserna `PivotField` och `PivotItem`.
{{% /alert %}}

## **Introduktion**
Pivottabeller är kraftfulla analysverktyg, men deras råa sammanställningar innehåller ofta mycket mer information än du behöver visa. Filtrering är den primära mekanismen för att begränsa en pivottabell till de rader, kolumner eller värden som är relevanta för en specifik rapport. Aspose.Cells for JavaScript via C++ motsvarar de filtreringsfunktioner som finns i Microsoft Excel och exponerar dem programmatiskt, så att rapportgenereringen kan automatiseras fullständigt.
Följande filtreringsstrategier behandlas i den här artikeln:
1. **Etikettfilter** – filtrerar objekt i ett rad- eller kolumnfält baserat på deras textetiketter.
2. **Datumfilter** – filtrerar rad- eller kolumnfält som endast innehåller datumtidsvärden eller tomma celler.
3. **Värdefilter** – filtrerar objekt baserat på de aggregerade värdena i ett datafält.
4. **Topp 10-filter** – visar endast de N högsta eller lägsta objekten, rangordnade efter ett värdefält.
5. **Dölja/visa pivotobjekt** – styr manuellt synligheten för varje enskilt objekt i ett fält.
Varje tillvägagångssätt använder en separat metod i klassen `PivotField` eller en egenskap i klassen `PivotItem`. När du har tillämpat ett filter måste du anropa `pivotCache.refresh()` på pivottabellen, så att de cachelagrade data och de beräknade värdena återspeglar den nytillkomna filtreringen.

## **Etikettfilter**
Ett etikettfilter låter dig filtrera objekten i ett rad- eller kolumnfält genom att jämföra deras textetiketter med ett mönster. Det är användbart när du endast vill visa produkter vars namn börjar med en viss bokstav, innehåller ett visst ord eller uppfyller något annat kriterium som baseras på etiketten.
Aspose.Cells exponerar etikettfiltrering via metoden `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. Argumentet `filterType` väljer jämförelseläge (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` med flera andra). Argumenten `label1` och `label2` anger texten som ska jämföras – ange `""` för `label2` när endast en jämförelse med ett värde behövs, till exempel för att filtrera på börjar med eller innehåller.
Exemplet nedan läser in en arbetsbok som innehåller en befintlig pivottabell, tillämpar ett etikettfilter så att endast objekt vars etiketter börjar med ett angivet prefix förblir synliga, uppdaterar pivottabellen och sparar resultatet.

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
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
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
Datumfilter låter dig begränsa en pivottabell med datumbaserade kriterier som i dag, förra veckan, denna månad, nästa kvartal eller ett visst datumintervall. De är specialiserade filter som endast fungerar på fält som lagrar datumtidsinformation.

{{% alert color="primary" %}}
Datumfiltret fungerar endast när rad- eller kolumnområdet innehåller enbart datumtidsceller eller tomma värden. Om det underliggande fältet innehåller andra datatyper, till exempel tal eller text, ger datumfiltret inte det förväntade resultatet. Se till att fältet är formaterat som datum och att alla värden är giltiga `DateTime`-instanser eller tomma celler innan du tillämpar filtret.
Aspose.Cells exponerar datumfiltrering via metoden `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. Enumerationen `PivotFilterType` innehåller särskilda filtertyper för datum, som `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` och `Between`. Beroende på den valda filtertypen anger du ett eller två `DateTime`-värden (för `Between` anger du start- och slutdatum).
Exemplet nedan läser in en arbetsbok med en pivottabell vars radområde innehåller ett datumfält, tillämpar ett datumfilter som begränsar de synliga objekten till ett visst datumintervall, uppdaterar pivottabellen och sparar arbetsboken.
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
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
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
Värdefilter fungerar på de aggregerade värden som en pivottabell beräknar i sitt dataområde. I stället för att matcha textetiketter jämför de numeriska summorna med ett tröskelvärde. Typiska användningsfall är att endast visa produkter vars summa av försäljningen överstiger ett målbelopp eller endast regioner vars antal transaktioner ligger inom ett intervall.
Aspose.Cells exponerar värdefiltrering via metoden `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. Parametern `valueFieldIndex` anger vilket datafält som ska utvärderas (använd `pivotTable.getDataFields().indexOf(dataField)` eller iterera över samlingen för att hitta positionen). Parametern `filterType` kan ha värden som `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` och `ValueLessThanOrEqual`. De två `double`-argumenten anger tröskelvärdet eller tröskelvärdena.
Exemplet nedan läser in en arbetsbok med en pivottabell, tillämpar ett värdefilter som endast behåller objekt vars sammanlagda försäljningsvärde överstiger ett numeriskt tröskelvärde, uppdaterar pivottabellen och sparar arbetsboken.

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
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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
                pivotTable.pivotCache.refresh();
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
Topp 10-filtret är en specialiserad form av värdefilter som endast behåller de N högsta eller lägsta objekten baserat på ett valt värdefält. Det används ofta för rankningsrapporter som ”de 10 produkterna med högst intäkt” eller ”de 5 regionerna med lägst antal försäljningar”.

{{% alert color="primary" %}}
Topp 10-filtret är endast effektivt när pivottabellen har ett eller flera värdefält i dataområdet. Utan minst ett värdefält finns det ingen aggregerat mått att rangordna objekten efter, och filtret kan inte tillämpas.
Aspose.Cells exponerar topp 10-filtrering via metoden `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. Parametern `valueFieldIndex` är indexet för det datafält vars aggregerade värden används för att rangordna objekten, `filterType` anger hur `itemCount` ska tolkas (`Count` behåller ett fast antal objekt, medan `Percent` behåller en procentandel av objekten, så att `itemCount` själv anges som procent), `isTop` anger om de högsta objekten (true) eller de lägsta objekten (false) ska behållas, och `itemCount` anger hur många objekt, eller vilken procentandel, som ska behållas.
Exemplet nedan läser in en arbetsbok med en pivottabell som innehåller ett värdefält, tillämpar ett topp 10-filter för att endast behålla de 10 högsta objekten baserat på summan av försäljningen, uppdaterar pivottabellen och sparar arbetsboken.
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
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
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
Förutom de strukturerade filter-API:erna tillåter Aspose.Cells dig att styra synligheten för varje enskilt pivotobjekt direkt. Genom att iterera över samlingen `pivotField.getPivotItems()` i ett `PivotField`-objekt och växla egenskapen `isHidden` kan du dölja utvalda objekt utan att tillämpa ett formelbaserat filter. Om du anger `pivotItem.isHidden = true` döljs objektet från pivottabellen; om du anger `pivotItem.isHidden = false` visas objektet igen och blir synligt.
Det här tillvägagångssättet är användbart när filterregeln är oregelbunden eller objektspecifik, till exempel när ett litet antal namngivna kategorier som inte ska förekomma i en viss rapport ska döljas. Exemplet nedan läser in en pivottabell, döljer ett specifikt objekt efter namn, visar hur det kan visas igen, uppdaterar pivottabellen och sparar arbetsboken.

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
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
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
Aspose.Cells for JavaScript via C++ erbjuder en komplett uppsättning filtreringsfunktioner för pivottabeller som motsvarar funktionerna i Microsoft Excel. Etikett-, datum- och värdefilter täcker de vanligaste analysscenarierna, medan topp 10-filtret hanterar rankningsrapporter. När filterregeln är oregelbunden erbjuder egenskapen `pivotItem.isHidden` ett flexibelt alternativ på objektnivå. Genom att kombinera dessa strategier – till exempel genom att tillämpa ett etikettfilter och sedan dölja specifika objekt – kan du skapa exakt avgränsade pivottabellrapporter helt programmatiskt.

{{< app/cells/assistant language="javascript-cpp" >}}