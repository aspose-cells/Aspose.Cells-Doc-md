---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for Node.js via C++ - fäst en regel till dataområdet med applyTo och ett PivotConditionFormatScopeType‑omfång, eller definiera målet med addCellArea och pivotAreas, och sedan bifoga regler och format via formatConditions.addCondition.
keywords: Aspose.Cells for Node.js via C++, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /sv/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea`‑ eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp som är över 200, skugga de mittersta femtio procenten eller flagga de lägst rankade objekten – och markeringen följer värdena när pivottabellen omberäknas eller uppdateras.
I Aspose.Cells lever villkorsstyrd formatering för pivottabeller i samlingen `pivotTable.getConditionalFormats()` . Varje post är en `PivotConditionalFormat` som svarar på två frågor oberoende:
- **Var gäller regeln?** Målet definieras antingen via `applyTo(row, column, scope)`, vilket speglar urvalet av omfång i Excel‑gränssnittet, eller via `addCellArea(cellArea)` och samlingen `pivotConditionalFormat.getPivotAreas()`, som namnger regionen explicit.
- **Vad testar regeln?** En eller flera villkor läggs till i `formatConditions`, erhållna via `pivotConditionalFormat.getFormatConditions()`, med `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, och varje villkor har sin egen stil via `getStyle()`.

{{% alert color="primary" %}}
Anropa inte `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` eller `formatConditions.addArea(cellArea)` på `formatConditions`‑objektet för ett pivottabellvillkorsformat. Dessa två överlagringar ärvs från det vanliga kalkylblads‑API‑et för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivåområde, så förfrågan ignoreras tyst. Definiera alltid regionen på `pivotConditionalFormat`‑objektet själv (`applyTo`, `addCellArea` eller `getPivotAreas()`) och lägg till regeln med en av `addCondition`‑överlagringarna.
{{% /alert %}}

## **Applicera en regel med ett omfång (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑gränssnittet. En cell i pivottabellen namnges av sina nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑omfång talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.DATA` – alla värdeceller som pivottabellen skapar, inklusive totalsummor.
- `PivotConditionFormatScopeType.FIELD` – värdecellerna som tillhör fältet som cellen identifierar, exklusive totalsummor. Cellen måste vara en fältcell, t.ex. en rad‑fältetikett; att skicka en värdecell resulterar i ett undantag.
- `PivotConditionFormatScopeType.SELECTION` – endast värdecellerna i skärningspunkten som cellen väljer, vanligtvis en enskild värdecell.
Exemplet nedan bygger en frukt‑försäljnings‑pivottabell vars övre vänstra hörn är på E3, fäster ett villkorsformat på cell F4 (rad 3, kolumn 5) med `DATA`‑omfånget, och markerar varje belopp över 200 med fet vit text på röd bakgrund. Med värdena Apple 220, Banana 330, Cherry 200 och totalsumman 750 målar regeln F4, F5 och F7 – den lösta regionen är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

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
// Pivottabell med dess övre vänstra hörn vid E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Förankra det villkorsstyrda formatet vid F4 (rad 3, kolumn 5) med Data-omfånget
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Regel - markera belopp som är större än 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Att fästa samma regel på rad‑fältetiketten E4 (rad 3, kolumn 4) med `FIELD`‑omfånget löser till F4:F6 istället – samma datakolumn utan totalsumman – eftersom omfånget nu beskriver `Fruit`‑fältet snarare än hela värdeområdet. `SELECTION`‑omfånget som fästs på F4 löser bara till F4.

## **Definiera regionen manuellt**
Det andra sättet hoppar över omfångsväljaren och namnger regionen explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med addCellArea**
`addCellArea(cellArea)` registrerar den angivna rektangeln som målet för regeln. Koordinaterna är nollbaserade kalkylbladskoordinater, och regionen är exakt den medföljande rektangeln – ingen utvidgning till datakolumnen och ingen totalsummalogik. Använd den när de intressanta cellerna är en känd fast rektangel i den aktuella pivottabellens layout.

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
// Måla in rektangeln F4:F6 (värdecellerna utan totalen)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Regel - kursiv på ljusgul för belopp mellan 150 och 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Ett semantiskt pivåområde med getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` är samma semantiska regionsmodell som syskonsidan använder för statiska format. Bygg ett `PivotArea`, välj ett fält eller område med `select` eller `selectField`, och lägg till det med `pivotAreas.addPivotArea(pivotArea)`. Ett semantiskt område förblir knutet till sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten förändras. `pivotAreas.add(pivotArea)`‑överlagringen kompilerar fortfarande men är markerad som föråldrad – föredra `addPivotArea`.

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
// Fäst regeln på Amount-datatfältet som ett semantiskt område
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regel - grå text för belopp under 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje anrop till `conditionalFormats.add()` lägger till en `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – att öppna filen igen i exemplet nedan visar samma regel med sin typ, operator och förmler intakta, och `getCellAreas()` rapporterar samma regioner. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel kastar ett villkorsformat som saknar regel.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// Detta skriver ut:
// Villkorliga format: 1
// Format 0: CellValue GreaterThan formula1==200
//     rader 4-7, kolumner 6-6        (F4:F7, det bestämda dataintervallet)
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/nodejs-cpp/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/nodejs-cpp/format-part-of-pivot-table/)
- [Topp 10 Visa eller filtrera i pivottabell](/cells/sv/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}