---
title: Lägg till filterfält i en pivottabell med Aspose.Cells for JavaScript via C++
linktitle: Lägg till filterfält i en pivottabell med Aspose.Cells for JavaScript via C++
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for JavaScript via C++, inklusive att lägga till filterfält och använda filtrering med enkelval och flerval.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält med hjälp av ett bekvämt API på hög nivå eller med hjälp av samlingen `getPageFields()` på lägre nivå. Du kan också styra filtret i läge för enkelval, rensa det för att visa alla filterposter eller växla fältet till flerval så att användare kan välja flera filterposter samtidigt via gränssnittet med krytrutor i Excel.
{{% /alert %}}

## **Introduktion**
Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan som pivottabellens dataområde visar. Slutanvändaren ser det som en rullmeny högst upp i den pivottabell som visas i Excel. När något av de tillgängliga filterposterna väljs byggs pivottabellens dataområde om så att endast de poster som hör till den valda filterposten sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.Page` i stället för `PivotFieldType.Row`, `PivotFieldType.Column` eller `PivotFieldType.Data`.

## **Lägga till ett filterfält**

### Lägga till ett filterfält med `addFieldToArea`
Det följande exemplet skapar en liten datamängd med `Fruit`, `Year` och `Amount`, placerar en pivottabell i cell E3 med `Fruit` i radområdet, `Amount` i dataområdet och `Year` i filterområdet, uppdaterar pivottabellen och sparar arbetsboken.

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
            worksheet.name = "Data";
            // Konfigurera rubrikraden
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Fyll i 9 rader med exempeldata: Fruit, Year, Amount
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // Lägg till en pivottabell med förankring vid cellen E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Lägg till fält i sina områden: Fruit som rad, Amount som data, Year som sidfält
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Uppdatera och beräkna pivottabellens data
            pivotTable.calculateData();
            // Spara arbetsboken
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### Lägga till ett filterfält med `getPageFields().add`
När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `pivotTable.getPageFields().add(pivotField)`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast registreringen i filterområdet ersätts med anropet till API:t på lägre nivå.

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
            // — Pivottabellen och sidfältet konstrueras exakt som i
            //   Scenario 1a (Fruit/Year/Amount-data, pivot i E3, Fruit→Rad,
            //   Amount→Data). Nedan hämtar vi Year PivotField från
            //   BaseFields-samlingen och skickar det till PageFields.Add — det
            //   lågnivåalternativet till AddFieldToArea. Resultatet är
            //   funktionellt identiskt med Scenario 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Rubriker
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Exempeldata (9 rader)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Lägg till pivottabell i E3 som täcker A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Fruit -> Rad, Amount -> Data (Year läggs till på Sida nedan)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Lågnivåmetod: hämta det befintliga Year PivotField från BaseFields
            // och registrera det i Sidområdet via PageFields.Add(PivotField).
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Klart! Klicka på nedladdningslänken för att hämta resultatfilen.</p>';
        });
    </script>
</html>
```

## **Enkelvalfiltrering (visar en filterpost)**
I standardläget för enkelval visas filterfältet som en enda rullmeny, och heltalet `pivotField.currentPageItem` avgör vilken filterpost som styr pivottabellens dataområde. Om du anger ett specifikt index väljs det motsvarande postet. Om du anger det särskilda reservvärdet `0x7FFD` (32765 i decimalform) rensas filtret så att alla filterposter tas med i pivottabellen samtidigt. Enkelval är standardläget och behöver inte aktiveras explicit.

### Visa alla poster
Att sätta `currentPageItem` till det särskilda värdet `0x7FFD` är likvärdigt med att rensa filtret: pivottabellens dataområde visar alla filterposter, som om inget filter hade tillämpats.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Skapa en ny arbetsbok
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Fyll i data för frukt/år/antal
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // Skapa en pivottabell vid E3
            const pivotTables = sheet.pivotTables;
            const pivotTableIndex = pivotTables.add("=A1:C7", "E3", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Konfigurera pivotfält: Fruit→Rad, Amount→Data, Year→Sida
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Rensa sidfiltret så att alla objekt i sidfältet är synliga.
            // 0x7FFD (decimal 32765) är det speciella kontrollvärdet som betyder "alla objekt" —
            // motsvarar att välja "(Alla)" i Excels rullmenü för sidfält.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
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

### Visa en specifik post
Att ange ett giltigt index för `currentPageItem` väljer endast den filterposten. Indexet anger postens position i filterfältets sorterade postlista. Exempelvis väljer `1` den andra posten efter sortering.

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
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // Skapa arbetsbok
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Lägg till exempeldata (Fruit/Year/Amount)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Lägg till pivottabell vid E3
                const pivotTables = sheet.pivotTables;
                const pivotTableIndex = pivotTables.add("=A1:C5", "E3", "PivotTable1");
                const pivotTable = pivotTables.get(pivotTableIndex);
                // Lägg till fält: Fruit→Rad, Amount→Data, Year→Sida
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Åtgärder specifika för sidfält
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = andra objektet i sorterad ordning (t.ex. "2021")
                // Uppdatera och beräkna pivottabellen
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Flervalfiltrering**
Vid flervalfiltrering visas filtrets rullmeny som en lista med krytrutor, och slutanvändaren kan välja flera filterposter samtidigt. Aspose.Cells exponerar två egenskaper som används tillsammans. `pivotField.isMultipleItemSelectionAllowed` måste sättas till `true` innan gränssnittet för flerval får någon effekt alls. När det är aktiverat avgör `pivotItem.isHidden` vilka poster som visas i listan med krytrutor, så att du antingen kan visa alla poster eller skapa en vitlista som endast innehåller specifika poster.

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
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — Pivottabellen och sidfältet konstrueras exakt som i
                //   Scenario 1a (Fruit/Year/Amount-data, pivot vid E3, Fruit→Rad,
                //   Amount→Data, Year→Sida via AddFieldToArea).
                //   Nedan tillämpar vi filter med flerval på sidfältet.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Exempeldata: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTableIndex = pivots.add("=A1:C10", "E3", "PivotTable1");
                const pivotTable = pivots.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Aktivera flerval på sidfältet
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Del A — välj ALLA objekt (gör varje objekt synligt)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Del B — välj endast specifika objekt baserat på källvärde
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Obs:** När du använder flervalfiltrering via `pivotItem.isHidden` måste **minst ett `PivotItem` vara synligt** (`isHidden === false`). Om alla poster är dolda kraschar Excel antingen när filen öppnas eller visar en tom pivottabell. Kontrollera alltid att din vitlista för flerval omfattar minst en post från källdatan.

## **Vilket API och vilket läge bör jag använda?**
Tabellen nedan sammanfattar när du bör använda varje API och läge, så att du kan välja rätt kombination utan att läsa varje scenario i detalj.
| Scenario / användningsfall | Rekommenderat API | Egenskap som används | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält med hjälp av källkolumnens namn (vanligast) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | Ej tillämpligt | API på hög nivå, ett anrop på en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `pivotTable.getPageFields().add(pivotField)` | Ej tillämpligt | Använd detta när fältsobjektet har hämtats någon annanstans eller behöver återanvändas. |
| Filtrera till en enda filterpost (standardläget) | `pivotField.currentPageItem` | Anges som ett specifikt index | Till exempel visar `1` den andra posten i den sorterade listan. |
| Visa alla poster / rensa filtret | `pivotField.currentPageItem` | Anges som `0x7FFD` | Det särskilda värdet `0x7FFD` (32765 i decimalform) är sentinelvärdet för ”alla poster”. |
| Aktivera gränssnittet för flerval i Excel | `pivotField.isMultipleItemSelectionAllowed` | Sätt till `true` | Krävs innan värden som tilldelas `isHidden` får effekt. |
| Dölj/visa enskilda poster i en lista med flerval | `pivotItem.isHidden` | Anges för varje post | Minst en post måste vara synlig (`isHidden === false`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsvillkoret när du konfigurerar flervalfiltrering. Om alla `PivotItem` i ett filterfält med flerval är dolda kraschar Excel antingen när filen öppnas eller visar en tom pivottabell. Bygg din vitlista utifrån källdatan så att minst en post förblir synlig. Då öppnas dina sparade arbetsböcker pålitet på alla datorer.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}