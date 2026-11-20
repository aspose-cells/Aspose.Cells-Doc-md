---
title: Diskret gruppering av objekt i pivotfält
linktitle: Diskret gruppering
description: Lär dig hur du grupperar pivotfältets objekt i anpassade namngivna grupper, till exempel frukt och grönsaker, med hjälp av DiscreteGroupItem och PivotFieldGroupOptions.discreteGroupItems i Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera pivotobjekt, anpassade grupper, PivotField.group, Aspose.Cells for JavaScript via C++, Excel-pivottabell
type: docs
weight: 90
url: /sv/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
- Automatisk gruppering ordnar objekt efter datatyp, till exempel datum till månader och kvartal eller tal till intervall. Diskret gruppering hanterar i stället det motsatta problemet genom att samla specifika, orelaterade objekt i anpassade namngivna grupper, till exempel produkter i kategorierna frukt och grönsaker, butiker i regioner eller konton i zoner. Aspose.Cells erbjuder diskret gruppering med hjälp av klassen `DiscreteGroupItem` och egenskapen `PivotFieldGroupOptions.discreteGroupItems`.
- En `DiscreteGroupItem` består av ett gruppnamn och de objekt som tillhör gruppen. Objekten kan identifieras på två sätt: med sina namn (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) eller med sina nollbaserade index i källdatan (`new DiscreteGroupItem("fruit", [0, 3])`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i pivottabellens rad- eller kolumnområde genom att skicka grupperingsalternativet till `PivotField.group(PivotFieldGroupOptions)`.

## **Gruppera objekt i pivotfält efter objektnamn**
Det följande exemplet bygger en liten försäljningslista (produkt, datum och belopp) och skapar en pivottabell utifrån listan, med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet. Därefter definieras två anpassade grupper efter objektnamn: frukt (druva, körsbär) och grönsaker (morot, potatis). Resultatet visar en tvånivåstruktur där gruppnamnet utgör den yttre nivån och de ursprungliga objekten den inre, så att trender kan utläsas för varje anpassad grupp och varje objekt.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Efter `calculateData()` visar pivottabellens radområde frukt (druva 50, körsbär 80) och grönsaker (morot 60, potatis 70) med en totalsumma på 260. Kolumnetiketterna behåller de fyra datumvärdena (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera objekt i pivotfält efter objektindex**
När objektnamnen är långa eller lokaliserade används den andra konstruktören för `DiscreteGroupItem` för att identifiera objekten med index. Indexen är nollbaserade och bestäms av den ordning i vilken objekten förekommer i källdatan, inte av alfabetisk ordning. I exemplets data ovan är druva objekt 0, morot objekt 1, potatis objekt 2 och körsbär objekt 3. Därför är fruktgruppen `{ 0, 3 }` och grönsaksgruppen `{ 1, 2 }`. Resultatet är identiskt med det namnbaserade exemplet.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Obs**

{{% alert color="primary" %}}
- Objekt som inte har tilldelats någon anpassad grupp försvinner inte. De förblir i pivottabellen på samma nivå som de anpassade grupperna, där varje objekt utgör en egen post. Om endast fruktgruppen definieras i exemplet ovan ligger morot och potatis kvar i radområdet som fristående poster bredvid fruktgruppen.
- Egenskapen `PivotFieldGroupOptions.newPivotField` styr layouten för diskret gruppering. Standardvärdet är `true`, vilket lägger till det grupperade fältet som ett nytt yttre fält bredvid det ursprungliga fältet och skapar den tvånivåstruktur som visas ovan (`rowFields` växer till 2). Ange värdet till `false` för att det ursprungliga fältet i stället ska ersättas. Radområdet visar då en enda nivå med enbart gruppnamnen och deras aggregerade värden: frukt 130 (50 + 80) och grönsaker 130 (60 + 70).
- De konstruktorerna som baseras på namn respektive index kan kombineras i samma `discreteGroupItems`-array.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i en pivottabell](/cells/sv/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa format på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}