---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for Node.js via Java, ankra en regel till dataområdet med applyTo och en PivotConditionFormatScopeType‑omfattning, eller definiera målet med addCellArea och getPivotAreas, och sedan fästa regler och stilar via getFormatConditions().addCondition.
keywords: Aspose.Cells, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /sv/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea`‑ eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mittersta femtio procenten av värdena, eller flagga de lägst rankade objekten – och markeringen följer värdena när pivottabellen återberäknas eller uppdateras.

{{% alert color="primary" %}}
Anropa inte `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` eller `FormatConditionCollection.addArea(CellArea)` på `getFormatConditions()`‑objektet för ett pivottabell‑villkorsformat. Dessa två överlagringar är ärvda från den vanliga kalkylblads‑API:n för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivotområde, så begäran ignoreras tyst. Definiera alltid området på själva `PivotConditionalFormat` (`applyTo`, `addCellArea` eller `getPivotAreas()`) och lägg till regeln med någon av `addCondition`‑överlagringarna.
{{% /alert %}}

## **Applicera en regel med en omfattning (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑användargränssnittet. En cell i pivottabellen namnges av sina nollbaserade kalkylbladskoordinater, och en `PivotConditionFormatScopeType`‑omfattning talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.DATA` – alla värdeceller som pivottabellen genererar, inklusive totaler.
- `PivotConditionFormatScopeType.FIELD` – värdeceller som tillhör det fält som cellen identifierar, exklusive totaler. Cellen måste vara en fältcell, t.ex. en rad‑fältetikett; att skicka en värdecell kastar ett undantag.
- `PivotConditionFormatScopeType.SELECTION` – endast de värdeceller som finns i skärningspunkten som cellen väljer, vanligtvis en enstaka värdecell.
Exemplet nedan skapar en pivottabell för fruktförsäljning med övre vänstra hörnet i E3, ankrar ett villkorsformat på cell F4 (rad 3, kolumn 5) med `DATA`‑omfattning, och markerar varje belopp över 200 med fet vit text på röd bakgrund. Med värdena Apple 220, Banana 330, Cherry 200 och totalen 750 målar regeln F4, F5 och F7 – det upplösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

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
// Pivottabell med dess övre vänstra hörn vid E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Ankrona det villkorsstyrda formatet vid F4 (rad 3, kolumn 5) med Data-omfånget
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Regel - markera belopp som är större än 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Att ankra samma regel på rad‑fältetiketten E4 (rad 3, kolumn 4) med `FIELD`‑omfattning ger F4:F6 istället – samma datakolumn utan total‑rad – eftersom omfattningen nu beskriver `Fruit`‑fältet snarare än hela värdeområdet. `SELECTION`‑omfattningen som ankras på F4 ger bara F4.

## **Definiera området manuellt**
Det andra sättet hoppar över omfattningsväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med addCellArea**
`addCellArea(CellArea)` registrerar den angivna rektangeln som regelns mål. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen utökning till datakolumnen och ingen total‑logik. Använd den när de intressanta cellerna är ett känt fast rektangel i den aktuella pivottabellens layout.

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
// Mål rektangeln F4:F6 (värdecellerna utan total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regel - kursiv på ljusgul för belopp mellan 150 och 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Ett semantiskt pivåtområde med PivotAreas**
`getPivotAreas()` är samma semantiska områdesmodell som syskonsidan använder för statiska stilar. Bygg en `PivotArea`, välj ett fält eller område med `select` eller `selectField`, och lägg till det med `getPivotAreas().addPivotArea(PivotArea)`. Ett semantiskt område förblir knutet till sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten ändras. Överlagringen `getPivotAreas().add(PivotArea)` kompilerar fortfarande men är markerad som föråldrad – föredra `addPivotArea`.

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
// Bifoga regeln till datafältet Amount som ett semantiskt område
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regel - grå text för belopp under 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Var reglerna lagras och hur de överlever en omladdning**
Varje `add()`‑anrop på `getConditionalFormats()` lägger till en `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och stilar sparas i arbetsboken – när filen öppnas igen i exemplet nedan visas samma regel med sin typ, operator och formel intakt, och `getCellAreas()` rapporterar samma områden. Poster som aldrig fått ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel förkastar ett villkorsformat utan regel.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// Detta skriver ut:
// Villkorsformat: 1
// Format 0: CellValue GreaterThan formula1==200
//     rader 4-7, kolumner 6-6        (F4:F7, det upplösta dataområdet)
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/nodejs-java/format-part-of-pivot-table/)
- [Topp 10 visa eller filtrera i pivottabell](/cells/sv/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}