---
title: Transponera intervall
linktitle: Transponera intervall
description: Den här artikeln förklarar hur du transponerar eller roterar data från rader till kolumner eller vice versa i Excel‑filer med Aspose.Cells for JavaScript via C++ med tre olika tillvägagångssätt.
keywords: Aspose.Cells, JavaScript via C++, kalkylblad, transponera intervall, rotera data, transponera funktion, dynamisk array-formel, array-formel, Excel TRANSPOSE, rader till kolumner
type: docs
weight: 80
url: /sv/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ stödjer att transponera (rotera) data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Det första tillvägagångssättet använder den in‑place‑metod `range.transpose()` och fungerar i alla Excel‑versioner, medan det andra använder `cell.setDynamicArrayFormula()` för att skriva en modern dynamisk array‑formel `=TRANSPOSE(...)` som automatiskt sprider sig i Excel 365 eller Excel 2021. Det tredje tillvägagångssättet använder `cell.setArrayFormula()` för att skriva en klassisk Ctrl+Shift+Enter‑array‑formel (CSE) som är kompatibel med äldre Excel‑versioner. Den här artikeln går igenom varje tillvägagångssätt med steg‑för‑steg‑instruktioner och kompletta kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall betyder att rotera det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket i praktiken speglar datan över dess huvuddiagonal. I Microsoft Excel utför arbetsbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen finns dokumenterad på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Detta koncept kan appliceras programmässigt på ett cellintervall, vilket är användbart i många affärs‑ och rapporteringsscenarier.
- Att orientera om kvartals‑ eller årsrapporter där kvartalen normalt löper horisontellt över sidan och regionerna vertikalt ner på sidan, eller tvärtom.
- Att byta axelorientering i instrumentpaneler eller diagram så att en tidsserie löper vertikalt istället för horisontellt.
- Att omforma data som importeras från externa system så att den matchar den layout som förväntas av nedströmsanalys eller rapportmallar.
För att göra resten av artikeln konkret använder varje exempel den följande lilla tabellen med försäljning per region per kvartal. I exempelarbetsboken upptar tabellen intervallet **A1:D5**, med **A1** tomt som det övre‑vänstra hörnet, **B1:D1** som regionrubriker och **A2:A5** som kvartalsrubriker.
| Region | Europa | Asien | Nordamerika |
|--------|--------|------|---------------|
| Kvartal 1 | 21704714 | 8774099 | 12094215 |
| Kvartal 2 | 17987034 | 12214447 | 10873099 |
| Kvartal 3 | 19485029 | 14356879 | 15689543 |
| Kvartal 4 | 22567894 | 15763492 | 17456723 |
Artikeln presenterar sedan tre olika sätt att transponera dessa data med Aspose.Cells for JavaScript via C++, där varje metod är anpassad för en specifik Excel‑version och användningsfall.

## **Tillvägagångssätt 1 — Transponera intervall på plats (Range.transpose)**
Använd detta tillvägagångssätt när du vill transponera data utan att involvera `TRANSPOSE`‑arbetsbladsfunktionen. Det fungerar i **alla Excel‑versioner** och har inget beroende av dynamiska arrayer, vilket gör det till det säkraste alternativet med versionsöverkorskompatibilitet. Det är idealiskt när du bara behöver det slutgiltiga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`‑formeln i arbetsboken.

### **Använt API**
`Range.transpose()` är en instansmetod på klassen `Aspose.Cells.Range`. När den anropas vänds intervallet på plats genom att byta plats på rader och kolumner, så att en rad blir en kolumn och en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva någon formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`‑format genom att anropa `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.getWorksheets().get(0)`.
3. Få åtkomst till kalkylbladets cellsamling via `worksheet.getCells()`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.createRange("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats, vilket byter rader och kolumner.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen innehåller detta ankareintervall de roterade data. Den första raden blir (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen blir (tom, **Kvartal 1**, **Kvartal 2**, **Kvartal 3**, **Kvartal 4**). Varje ursprunglig försäljningskolumn blir en rad i det transponerade intervallet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Tillvägagångssätt 2 — Transponera med en dynamisk array‑formel (Excel 365 / 2021)**
Använd detta tillvägagångssätt när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en levande formel i den resulterande arbetsboken så att resultatet uppdateras automatiskt om källdata ändras, och mål‑Excel‑filen kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska arrayer och spill‑operatorn stöds.

### **Använt API**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` är en metod på klassen `Aspose.Cells.Cell` som sätter cellens formel som en **dynamisk array‑formel**. Excel utvärderar formeln en gång och sprider automatiskt resultatet till omgivande celler. Den tredje parametern, när den är `true`, instruerar Aspose.Cells att även beräkna de resulterande värdena vid skrivningstillfället.

### **Steg**
1. Läs in källarbetsboken med `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och få åtkomst till dess cellsamling.
3. Placera den dynamiska array‑formeln i cell **A6**, precis under källintervallet, genom att anropa `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. Argumentet `new FormulaParseOptions()` använder standardinställningarna för `FormulaParseOptions`, och det tredje argumentet `true` talar om för Aspose.Cells att behandla formeln som en dynamisk array och att utvärdera den så att de spredda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel sprider resultatet automatiskt till området **A6:E9**, ett block på 4 rader gånger 5 kolumner som motsvarar det transponerade datat.

{{% alert color="primary" %}}
Detta tillvägagångssätt fungerar **endast i Excel 365 / 2021 eller senare**. Äldre Excel‑versioner kommer inte att sprida dynamiska array‑formler korrekt.
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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Tillvägagångssätt 3 — Transponera med en klassisk array‑formel (CSE)**
Använd detta tillvägagångssätt när du vill ha en `TRANSPOSE`‑formel bevarad i arbetsboken men mål‑Excel‑filen kan öppnas i **äldre Excel‑versioner (före 2021, inklusive 2019, 2016, 2013 osv.)** där dynamisk array‑spilling inte stöds. Den klassiska CSE‑ (Ctrl+Shift+Enter) array‑formeln är det bakåtkompatibla alternativet som alla Excel‑versioner kan utvärdera.

### **Använt API**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` är en metod på klassen `Aspose.Cells.Cell` som tilldelar en **klassisk array (CSE)‑formel** till ankercellen och deklarerar dimensionerna för den resulterande arrayen. Aspose.Cells skriver en multi‑cell‑array‑formel‑markör så att Excel utvärderar formeln som ett enda array‑uttryck som fyller det deklarerade intervallet.

### **Steg**
1. Läs in källarbetsboken enligt de tidigare tillvägagångssätten.
2. Hämta det första kalkylbladet och få åtkomst till dess cellsamling.
3. Anropa `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsarrayen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankaret för array‑formeln och den utvärderade arrayen sträcker sig över 4 rader gånger 5 kolumner med början i A6, vilket matchar de transponerade dimensionerna för källintervallet A1:D5. Excel skriver en enda array‑formel‑markör över det resulterande intervallet så att äldre Excel‑versioner utvärderar den korrekt.

{{% alert color="primary" %}}
CSE‑array‑formler är det klassiska Excel‑sättet att utvärdera ett `TRANSPOSE`‑uttryck och detta tillvägagångssätt är universellt kompatibelt med alla Excel‑versioner.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Läs in källarboken med xlsx LoadOptions
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // Åtkomst till det första kalkylbladet och dess Cells-samling
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Ställ in den klassiska CSE-arrayformeln på cell A6.
                // Formeln =TRANSPOSE(A1:D5) roterar det 5-rader x 4-kolumners källintervallet
                // till en 4-rader x 5-kolumners array. Det andra argumentet (4) är antalet rader
                // och det tredje argumentet (5) är antalet kolumner i den resulterande arrayen.
                // Aspose.Cells skriver CSE-arrayformel-markören så att Excel utvärderar den som
                // en enda flercellsarrayformel, kompatibel med äldre Excel-versioner
                // (2019, 2016, 2013 osv.) som inte stöder dynamisk array-spillning.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Spara arbetsboken så att arrayformel-markören bevaras
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Jämförelse — När du ska använda varje tillvägagångssätt**
| Tillvägagångssätt | API / Metod | Excel‑version | Bevarad formel? | Utdata‑intervall |
|-------------------|-------------|----------------|-----------------|-------------------|
| Tillvägagångssätt 1 — In‑place‑transponering | `range.transpose()` | Alla Excel‑versioner | Nej (endast värden) | Ursprungligt ankareintervall, 5×4 |
| Tillvägagångssätt 2 — Dynamisk array‑formel | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Ja (spiller dynamiskt) | Spiller från ankare |
| Tillvägagångssätt 3 — Klassisk array‑formel (CSE) | `cell.setArrayFormula()` | Alla Excel‑versioner | Ja (multi‑cell‑array‑formel) | Explicit storlek, 4×5 |
Använd **Tillvägagångssätt 1** när du snabbt behöver en tvärversions‑transformation och bara behöver de transponerade värdena skrivna till filen. Använd **Tillvägagångssätt 2** när modern Excel är garanterad och du vill att formeln förblir levande och uppdateras om källdatan ändras. Använd **Tillvägagångssätt 3** när du behöver största möjliga kompatibilitet med en bevarad formel i alla Excel‑versioner, inklusive de äldre som saknar stöd för dynamiska arrayer.

{{< app/cells/assistant language="javascript-cpp" >}}