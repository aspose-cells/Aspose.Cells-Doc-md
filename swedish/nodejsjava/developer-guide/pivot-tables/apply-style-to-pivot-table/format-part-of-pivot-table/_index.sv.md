---
title: Formatera del av en pivottabell
linktitle: Formatera del av en pivottabell
description: Formatera en del av en pivottabell i Aspose.Cells for Node.js via Java genom att tillämpa stilar på semantiska PivotArea‑regioner eller CellArea‑rektanglar via PivotTable.format, där formaten lagras i PivotTable.getPivotFormats() och bevaras när pivottabellen uppdateras.
keywords: Aspose.Cells for Node.js via Java, pivottabell, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /sv/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.formatAll` tillämpar en enda stil på hela pivottabellen och behandlas på överordnad sida. Den skiljer inte mellan etiketter, värden, totaler eller specifika områden i rapporten.
I praktiken är det vanligt att endast en del av en pivottabell behöver framhävas. Vanliga mål inkluderar etiketter som tillhör ett radfält, värdeceller som produceras av ett fält, totalraden eller en godtycklig rektangel som t.ex. de två första objekt‑raderna.
Att tillämpa en stil direkt på kalkylbladets celler i en pivottabell är inte likvärdigt. Excel lagrar pivottabellformatering som semantiska `PivotArea`‑regioner istället för vanliga cellstil‑poster. En pivot‑area‑format förblir kopplad till en region, exempelvis ett fälts etiketter eller datavärden, och den omtolkas när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell däremot tillhör den specifika cellpositionen och spåras inte av pivot‑modellen.
Aspose.Cells exponerar hela `PivotTable.format`‑överlagringsfamiljen så att båda typerna av formatering är tillgängliga:
- `format(PivotArea, Style)` fäster en stil på en semantisk region som byggs med `PivotArea.select` eller `PivotArea.selectField`.
- `format(CellArea, Style)` fäster en stil på en kalkylbladsrektangel inom pivottabellen.
- `format(int row, int column, Style)` riktar in sig på en enskild cell.
- `formatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Arbetsflödet med semantiskt område är den rekommenderade metoden när en markering måste följa ett fält eller ett område i rapporten.
1. Skapa ett `PivotArea` med `new PivotArea(pivotTable)`. Objektet beskriver en semantisk region som tillhör just den pivottabellen.
1. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` väljer både fältets etiketter och data.
   - `PivotTableSelectionType.LABEL_ONLY` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DATA_ONLY` väljer endast fältets dataceller.
1. Välj ett fält efter namn med `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. När ett radfält väljs efter namn löser regionen upp till de värdeceller som produceras av fältets objekt.
1. Skapa en `Style` med `Workbook.createStyle()`, konfigurera dess teckensnitt, förgrundsfärg och solid bakgrundsmönster, och skicka stilen till `PivotTable.format(area, style)`.
1. Varje anrop av `PivotArea`‑överlagringen lägger till ett `PivotTableFormat`‑inlägg i `PivotTable.getPivotFormats()`.
1. Fält‑ankrade format målas när pivot‑datat beräknas. Därför bör du anropa `PivotTable.calculateData()` efter att formaten har tillämpats så att stilarna blir synliga.
Följande exempel bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.select` och `PivotTableSelectionType.LABEL_ONLY`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.selectField`, och beräknar sedan pivottabellen på nytt så att båda stilarna målas.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formatera ett Cell‑område i pivottabellen**
Använd `PivotTable.format(CellArea, Style)` när det område som intresserar dig är en vanlig kalkylbladsrektangel snarare än ett semantiskt pivotoområde.
`CellArea` beskrivs av de publika fälten `StartRow`, `StartColumn`, `EndRow` och `EndColumn`. Värdena är nollbaserade kalkylbladskoordinater, och slutkoordinaterna identifierar den sista raden och kolumnen som ingår i rektangeln, så området omfattar cellerna från startpositionen till slutpositionen inklusive.
Till skillnad från ett fält‑ankrat format appliceras ett `CellArea`‑format på cellerna omedelbart. Ett ytterligare anrop av `calculateData()` behövs inte för att stilen ska visas.
En `CellArea`‑rektangel kan innehålla både etikettceller och värdeceller. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.
Följande exempel formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan ytterligare omberäkning.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Hur PivotArea‑ och CellArea‑områden mappar**
Excel lagrar pivottabellformatering som `pivotArea`‑poster istället för vanliga kalkylblads‑cellstil‑poster. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivotoområden när den registreras.
Sambandet mellan den `CellArea` som användaren tillhandahåller och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan generera flera pivotoområden. Om rektangeln sträcker sig över både etikettceller och värdeceller delas den upp i separata etikett‑ och dataregler, eftersom pivottomodellen behandlar etikett‑ och dataformatering oberoende.
- Ett pivot‑område kan lösa upp till flera separata `CellArea`‑instanser. En semantisk region såsom en totalsumma‑rad, eller ett fält vars objekt inte är sammanhängande, kan omfatta flera rektanglar. Detta är varför `PivotArea.getCellAreas()` returnerar en samling istället för en enda rektangel.
Varje formateringsoperation som utförs via `PivotTable.format` lagras i `PivotTable.getPivotFormats()`. Varje `PivotTableFormat`‑post visar den associerade `PivotArea` och den `Style` som tillämpas på den. `PivotArea`‑överlagringen lägger till exakt ett inlägg per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera inlägg.
För att särskilja de lagrade regionerna visar varje `PivotArea` flaggorna `getOnlyLabel()` och `getOnlyData()`. Exemplet nedan formaterar en enskild rektangel som omfattar både etiketter och värden, undersöker `PivotTable.getPivotFormats()` och skriver ut `CellArea`‑koordinaterna som varje lagrat pivot‑område löser upp till.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
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
Eftersom formaten lagras som pivotoområden snarare än som vanliga cellstilar, överlever de omberäkning och uppdatering. När pivottabellen uppdateras med `PivotTable.refreshData()`, beräknas om med `calculateData()`, eller sparas och laddas om, löser varje lagrat pivotoområde upp till den aktuella positionen för sin region och dess stil återappliceras.
{{% /alert %}}

Använd ett `PivotArea` byggt med `select` eller `selectField` när en markering måste förbli kopplad till ett fält eller en semantisk region över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i den aktuella pivottabellens layout är tillräckligt. Enstaka‑cell‑överlagringen `format(int row, int column, Style)` riktar in sig på en individuell cell. Använd `formatAll`, som behandlas på överordnad sida, när hela pivottabellen ska återformateras på en gång.

## **Related Articles**
- [Tillämpa stil på pivottabell](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/nodejs-java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}