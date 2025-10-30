---
title: Skapa och hantera tabeller i Microsoft Excel filer med JavaScript via C++
linktitle: Tabeller
type: docs
weight: 150
url: /sv/javascript-cpp/create-and-format-table/
description: Infoga, resize, redigera, radera och formatera tabeller i Excel filer med Aspose.Cells for JavaScript via C++.
---

## **Skapa tabell**

En av fördelarna med kalkylblad är att de tillåter dig att skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan samarbeta för att använda, skapa och underhålla olika listor.

Aspose.Cells stödjer skapande och hantering av listor.

### **Fördelar med en List-objekt**

Det finns ganska många fördelar när du konverterar en lista med data till ett faktiskt List-objekt

- Nya rader och kolumner inkluderas automatiskt.
- En totalrad längst ner i din lista kan enkelt läggas till för att visa SUMMA, MEDELVÄRDE, ANTAL, osv.
- Kolumner som läggs till till höger inkorporeras automatiskt i listobjektet.
- Diagram baserade på rader och kolumner kommer att utökas automatiskt.
- Namngivna intervall tilldelade rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig rad- och kolumnradering.

### **Skapa ett List-objekt med hjälp av Microsoft Excel**

- Välj dataintervall för att skapa ett List-objekt
- Detta visar skapa List-dialogrutan.
- Implementera List-objektet för data och ange totalsraden (Välj **Data**, sedan **Lista**, och därefter **Totalrad**).

### **Använda Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) -samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att skapa ett [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) i ett kalkylblad, använd [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--)-samlingsegenskapen av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. Varje [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) är i själva verket ett objekt av [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/)-klassen, som vidare tillhandahåller [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-)-metoden för att lägga till ett List-objekt och ange ett cellområde för listan.

Enligt det angivna cellområdet skapas List-objektet av Aspose.Cells. Använd attribut (till exempel [**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--), [**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--) osv.) för [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)-klassen för att styra listan.

I exemplet nedan har vi skapat samma [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) med Aspose.Cells API som vi skapade med Microsoft Excel i föregående avsnitt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Formatera en tabell**

För att hantera och analysera en grupp relaterade data är det möjligt att göra om ett cellområde till ett listobjekt (även känt som en Exceltabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende från data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverat i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en specialrad i en lista som ger ett urval av aggregeringsfunktioner som är användbara för att arbeta med numeriska data) till listobjektet som ger en rullista med aggregeringsfunktioner för varje cell i totalraden. Aspose.Cells tillhandahåller alternativ för att skapa och hantera listor (eller tabeller).

### **Formatera ett Listobjekt**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) -samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa ett [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) i ett kalkylblad, använd [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--)-samlingsegenskapen av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen. Varje [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) är i själva verket ett objekt av [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/)-klassen, som vidare tillhandahåller [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-)-metoden för att lägga till ett List-objekt och specificera det cellområde det ska omfatta. Enligt det angivna cellområdet skapas ett [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) i kalkylbladet av Aspose.Cells. Använd attribut (till exempel [**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/)) för [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/)-klassen för att formatera tabellen efter dina behov.

Nedan följer ett exempel som lägger till exempeldata i ett kalkylblad, lägger till ett [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) och tillämpar standardstilar. [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) stilar stöds av Microsoft Excel 2007/2010.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Konvertera tabell till ODS](/cells/sv/javascript-cpp/convert-table-to-ods/)
- [Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar](/cells/sv/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Läs och skriv tabell med datakälla för frågetabell](/cells/sv/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [Ange kommentaren för tabell eller listobjekt inne i kalkylbladet](/cells/sv/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabeller och områden](/cells/sv/javascript-cpp/tables-and-ranges/)
