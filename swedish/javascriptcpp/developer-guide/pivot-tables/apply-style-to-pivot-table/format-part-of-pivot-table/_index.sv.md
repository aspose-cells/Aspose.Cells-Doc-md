---
title: Formatera del av en pivottabell
linktitle: Formatera del av en pivottabell
description: Formatera en del av en pivottabell i Aspose.Cells for JavaScript via C++ genom att tillämpa stilar på semantiska PivotArea‑regioner eller CellArea‑rektanglar via PivotTable.Format, med format lagrade i PivotTable.PivotFormats och bevarade när pivottabellen uppdateras.
keywords: Aspose.Cells for JavaScript via C++, pivottabell, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /sv/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.FormatAll` tillämpar en enda stil på hela pivottabellen och behandlas på föräldrasidan. Den gör ingen skillnad mellan etiketter, värden, totaler eller specifika områden i rapporten.  
I praktiken behöver vanligtvis bara en del av en pivottabell framhävas. Vanliga mål inkluderar etiketterna som tillhör ett radfält, värdecellerna som produceras av ett fält, totalraden eller en godtycklig rektangel såsom de två första radposterna.  
Att tillämpa en stil direkt på kalkylbladscellerna i en pivottabell är inte detsamma. Excel lagrar pivottabellformatering som semantiska `PivotArea`‑regioner snarare än vanliga cell‑stilsregister. En pivot‑area‑format förblir knutet till en region såsom ett fälts etiketter eller datavärden, och den återupplöses när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell tillhör däremot den cellens position och spåras inte av pivot‑modellen.  
Aspose.Cells exponerar den kompletta `PivotTable.Format`‑överlagringsfamiljen så att båda typerna av formatering är tillgängliga:
- `Format(PivotArea, Style)` förankrar en stil till en semantisk region som byggs med `PivotArea.Select` eller `PivotArea.SelectField`.
- `Format(CellArea, Style)` förankrar en stil till en kalkylbladsrektangel inom pivottabellen.
- `Format(int row, int column, Style)` riktar sig mot en cell.
- `FormatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett pivot‑område**
Arbetssättet med semantiskt område är den rekommenderade metoden när en markering måste följa ett fält eller en region i rapporten.
1. Skapa ett `PivotArea` med `new PivotArea(pivotTable)`. Objektet beskriver en semantisk region som tillhör just den pivottabellen.
2. Välj ett fält enligt dess nollbaserade position på en given axel med `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` väljer både fältets etiketter och dess data.
   - `PivotTableSelectionType.LabelOnly` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DataOnly` väljer endast fältets dataceller.
3. Välj ett fält med namn med `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. När ett radfält väljs per namn löser regionen upp till värdecellerna som produceras av fältets objekt.
4. Skapa en `Style` med `Workbook.CreateStyle()`, konfigurera dess typsnitt, förgrundsfärg och solid bakgrundsmönster, och skicka stilen till `PivotTable.Format(area, style)`.
5. Varje anrop av `PivotArea`‑överlagringen lägger till en `PivotTableFormat`‑post i `PivotTable.PivotFormats`.
6. Fältförankrade format målas när pivottdata beräknas. Därför bör du anropa `PivotTable.CalculateData()` efter att formaten har tillämpats så att stilarna blir synliga.  
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.Select` och `PivotTableSelectionType.LabelOnly`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.SelectField`, och beräknar sedan pivottabellen på nytt så att båda stilarna målas.

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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Formatera ett cellområde i pivottabellen**
Använd `PivotTable.Format(CellArea, Style)` när det intressanta området är en vanlig kalkylbladsrektangel snarare än ett semantiskt pivot‑område.  
Ett `CellArea` beskrivs av fälten `startRow`, `startColumn`, `endRow` och `endColumn`. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista raden och kolumnen som ingår i rektangeln, så området omfattar cellerna från startpositionen till slutpositionen inklusive.  
Till skillnad från ett fältförankrat format appliceras ett `CellArea`‑format på cellerna omedelbart. Ett ytterligare anrop av `CalculateData()` behövs inte för att stilen ska visas.  
En `CellArea`‑rektangel kan innehålla både etikettceller och värdeceller tillsammans. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.  
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan någon ytterligare omräkning.

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
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Hur pivot‑områden och cellområden mappar**
Excel lagrar pivottabellformatering som `pivotArea`‑poster snarare än som vanliga kalkylblads‑cell‑stilsregister. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.  
Relationen mellan det `CellArea` som användaren anger och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.  
- Ett `CellArea` kan producera flera pivot‑områden. Om rektangeln sträcker sig både över etikettceller och värdeceller delas den upp i separata etikett‑ och dataregel, eftersom pivot‑modellen behandlar etikettformatering och dataformatering oberoende.  
- Ett pivot‑område kan lösa upp till flera separata `CellArea`‑instanser. En semantisk region såsom en totalrad, eller ett fält vars objekt inte är sammanhängande, kan omfatta flera rektanglar. Detta är anledningen till att `PivotArea.GetCellAreas()` returnerar en samling istället för en enskild rektangel.  
Varje formateringsoperation som utförs via `PivotTable.Format` registreras i `PivotTable.PivotFormats`. Varje `PivotTableFormat`‑post visar den associerade `PivotArea` samt den `Style` som appliceras på den. `PivotArea`‑överlagringen lägger till exakt en post per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera poster.  
För att särskilja de lagrade regionerna visar varje `PivotArea` flaggorna `OnlyLabel` och `OnlyData`. Exemplet nedan formaterar en enda rektangel som omfattar både etiketter och värden, inspekterar `PivotTable.PivotFormats` och skriver ut `CellArea`‑koordinaterna som varje lagrat pivot‑område löser upp till.

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
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cellstilar överlever de omräkningar och uppdateringar. När pivottabellen uppdateras med `PivotTable.RefreshData`, beräknas på nytt med `CalculateData`, eller sparas och laddas om, löser varje lagrat pivot‑område upp till den aktuella positionen för sin region och dess stil appliceras på nytt.
{{% /alert %}}

Använd ett `PivotArea` byggt med `Select` eller `SelectField` när en markering måste förbli knuten till ett fält eller en semantisk region över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i den aktuella pivottabells layout är tillräcklig. Den enskilda cell‑överlagringen `Format(int row, int column, Style)` riktar sig mot en individuell cell. Använd `FormatAll`, som behandlas på föräldrasidan, när hela pivottabellen ska omformateras på en gång.

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)
- [Lägga till rad- och kolumnfält i pivottabell](/cells/sv/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/javascript-cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}