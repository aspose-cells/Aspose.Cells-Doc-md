---
title: Formatera del av en pivottabell
linktitle: Formatera del av en pivottabell
description: Formatera del av en pivottabell i Aspose.Cells for Node.js via C++ genom att tillämpa stilar på semantiska PivotArea‑regioner eller CellArea‑rektanglar via PivotTable.format, med formaten lagrade i PivotTable.getPivotFormats() och bevarade när pivottabellen uppdateras.
keywords: Aspose.Cells, Node.js via C++, pivottabell, formatering, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /sv/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.formatAll` tillämpar en enda stil på hela pivottabellen och behandlas på den överordnade sidan. Den skiljer inte mellan etiketter, värden, totaler eller specifika områden i rapporten.  
I praktiken behöver vanligtvis bara en del av en pivottabell framhävas. Vanliga mål inkluderar etiketter som tillhör ett radfält, värdecellerna som produceras av ett fält, totalraden eller en godtycklig rektangel såsom de två första objektraderna.  
Att tillämpa en stil direkt på kalkylbladcellerna i en pivottabell är inte detsamma. Excel lagrar pivottabellens formatering som semantiska `PivotArea`‑regioner istället för vanliga cell‑stilsregister. En pivot‑area‑format förblir fäst vid en region, till exempel ett fälts etiketter eller datavärden, och den omvärderas när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell tillhör däremot den cellens position och spåras inte av pivottabellmodellen.  
Aspose.Cells exponerar hela `PivotTable.format`‑överladdningsfamiljen så att båda typerna av formatering är tillgängliga:
- `format(PivotArea, Style)` fäster en stil vid en semantisk region som byggs med `PivotArea.select` eller `PivotArea.selectField`.
- `format(CellArea, Style)` fäster en stil vid en kalkylbladrektangel inom pivottabellen.
- `format(number row, number column, Style)` riktar sig mot en enskild cell.
- `formatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Arbetssättet för semantiska områden är den rekommenderade metoden när en markering måste följa ett fält eller en region i rapporten.
1. Skapa en `PivotArea` med `new PivotArea(pivotTable)`. Objektet beskriver en semantisk region som tillhör den specifika pivottabellen.
1. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` väljer både fältets etiketter och data.
   - `PivotTableSelectionType.LabelOnly` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DataOnly` väljer endast fältets dataceller.
1. Välj ett fält efter namn med `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. När ett radfält väljs efter namn löser regionen upp till de värdeceller som produceras av fältets objekt.
1. Skapa en `Style` med `workbook.createStyle()`, konfigurera dess teckensnitt, förgrundsfärg och solitt bakgrundsmönster, och skicka stilen till `pivotTable.format(area, style)`.
1. Varje anrop av `PivotArea`‑överlagringen lägger till ett `PivotTableFormat`‑objekt i `pivotTable.getPivotFormats()`.
1. Fältanknutna format målas när pivot‑data beräknas. Därför bör du anropa `pivotTable.calculateData()` efter att formateringen har tillämpats så att stilarna blir synliga.  
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.select` och `PivotTableSelectionType.LabelOnly`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.selectField`, och beräknar sedan om pivottabellen så att båda stilarna målas.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formatera ett cellområde i pivottabellen**
Använd `PivotTable.format(CellArea, Style)` när det intressanta området är en vanlig kalkylbladrektangel snarare än ett semantiskt pivot‑område.  
`CellArea` beskrivs av egenskaperna `startRow`, `startColumn`, `endRow` och `endColumn`. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista raden och kolumnen som inkluderas i rektangeln, så området omfattar cellerna från startpositionen till slutpositionen inklusive.  
Till skillnad från ett fältanknutet format appliceras ett `CellArea`‑format på cellerna omedelbart. Ett ytterligare anrop av `pivotTable.calculateData()` behövs inte för att stilen ska visas.  
En `CellArea`‑rektangel kan innehålla både etikettceller och värdeceller samtidigt. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.  
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan ytterligare beräkning.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Hur Pivot‑områden och Cell‑områden mappar**
Excel lagrar pivottabellens formatering som `pivotArea`‑poster snarare än som vanliga kalkylblad‑cell‑stilsregister. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.  
Relationen mellan den `CellArea` som användaren tillhandahåller och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.  
- En `CellArea` kan producera flera pivot‑områden. Om rektangeln sträcker sig över både etikettceller och värdeceller delas den upp i separata etikett‑ och dataregler, eftersom pivot‑modellen behandlar etikettformatering och dataformatering oberoende.  
- Ett pivot‑område kan lösas upp till flera separata `CellArea`‑instanser. En semantisk region såsom en rad med totalsumma, eller ett fält vars objekt inte är sammanhängande, kan omfatta flera rektanglar. Detta är orsaken till att `PivotArea.getCellAreas()` returnerar en samling istället för en enda rektangel.  
Varje formateringsåtgärd som utförs via `pivotTable.format()` registreras i `pivotTable.getPivotFormats()`. Varje `PivotTableFormat`‑post visar den associerade `PivotArea` samt den `Style` som tillämpas på den. `PivotArea`‑överlagringen lägger till exakt en post per anrop, medan ett `CellArea`‑format som innehåller olika semantiska regioner kan lägga till flera poster.  
För att särskilja de lagrade regionerna exponerar varje `PivotArea` flaggorna `getOnlyLabel()` och `getOnlyData()`. Exemplet nedan formaterar en enda rektangel som omfattar både etiketter och värden, inspekterar `pivotTable.getPivotFormats()` och skriver ut de `CellArea`‑koordinater som varje lagrat pivot‑område löses upp till.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cellstilar, överlever de omberäkning och uppdatering. När pivottabellen uppdateras med `pivotTable.refreshData()`, beräknas om med `pivotTable.calculateData()`, eller sparas och laddas om, löser varje lagrat pivot‑område sig på nytt till den aktuella positionen för sin region och dess stil återappliceras.
{{% /alert %}}

Använd en `PivotArea` byggd med `select` eller `selectField` när en markering måste förbli fäst vid ett fält eller en semantisk region över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i den nuvarande pivottabellslayouten är tillräckligt. En‑cell‑överlagring `format(number row, number column, Style)` riktar sig mot en individuell cell. Använd `formatAll`, som behandlas på den överordnade sidan, när hela pivottabellen ska omformateras på en gång.

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)
- [Lägga till rad- och kolumnfält i pivottabell](/cells/sv/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-cpp/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}