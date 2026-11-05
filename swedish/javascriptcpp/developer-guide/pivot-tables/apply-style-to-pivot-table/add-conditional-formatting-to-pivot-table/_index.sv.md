---
title: Lägg till villkorsstyrd formatering i en pivottabell
linktitle: Lägg till villkorsstyrd formatering i en pivottabell
description: Lägg till villkorsstyrd formatering i en pivottabell i Aspose.Cells for JavaScript via C++ - förankra en regel till dataområdet med applyTo och en PivotConditionFormatScopeType-omfång, eller definiera målet med addCellArea och pivotAreas, och sedan bifoga regler och stilar via formatConditions.addCondition.
keywords: Aspose.Cells for JavaScript via C++, pivottabell, villkorsstyrd formatering, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /sv/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Stilarna som beskrivs på föräldrasidan och på syskonsidan är statiska – ett `PivotArea`- eller `CellArea`‑område målas en gång och behåller sin stil oavsett vilka värden som finns. Villkorsstyrd formatering är den regelbaserade motsvarigheten – markera varje belopp över 200, skugga de mittersta femtio procenten, eller flagga de lägst rankade objekten – och markeringen följer värdena när pivottabellen beräknas om eller uppdateras.
I Aspose.Cells, pivottabellens villkorsstyrda formatering finns i samlingen `pivotTable.conditionalFormats`. Varje post är ett `PivotConditionalFormat` som besvarar två frågor oberoende:
- **Var tillämpas regeln?** Målnområdet definieras antingen via `applyTo(row, column, scope)`, som speglar Excel‑gränssnittets omfångsväljare, eller via `addCellArea(cellArea)` och samlingen `pivotAreas`, som namnger området explicit.
- **Vad testar regeln?** En eller flera villkor läggs till i `formatConditions` med `addCondition(type, operatorType, formula1, formula2)`, och varje villkor har sin egen `style`.

{{% alert color="primary" %}}
Anropa inte `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` eller `formatConditions.addArea(cellArea)` på `formatConditions`‑objektet för ett pivottabell‑villkorsformat. Dessa två överlagringar är ärvda från det vanliga kalkylblads‑API:et för villkorsstyrd formatering och fungerar inte för pivottabeller – cellområdet konverteras aldrig till ett pivot‑område, så begäran ignoreras tyst. Definiera alltid området på själva `PivotConditionalFormat` (`applyTo`, `addCellArea` eller `pivotAreas`) och lägg till regeln med någon av `addCondition`‑överlagringarna.
{{% /alert %}}

## **Använd en regel med ett omfång (Excel‑gränssnittet)**
Det första sättet placerar regeln på samma sätt som Excel‑gränssnittet. En cell i pivottabellen namnges av sina nollbaserade kalkylbladskoordinater, och ett `PivotConditionFormatScopeType`‑omfång talar om för Aspose.Cells hur långt regeln ska sträcka sig från den cellen:
- `PivotConditionFormatScopeType.Data` – alla värdeceller som pivottabellen genererar, inklusive totaler.
- `PivotConditionFormatScopeType.Field` – värdecellerna som tillhör det fält som cellen identifierar, exklusive totaler. Cellen måste vara en fältcell, t.ex. en rad‑fält‑etikett; att skicka en värdecell resulterar i ett undantag.
- `PivotConditionFormatScopeType.Selection` – endast de värdeceller som ligger i den skärningspunkt som cellen väljer, vanligtvis en enda värdecell.
Exemplet nedan bygger en pivottabell för fruktförsäljning med övre vänstra hörnet i E3, förankrar en villkorsstyrd formatering i cell F4 (rad 3, kolumn 5) med `Data`‑omfånget, och markerar varje belopp över 200 med fet vit text på röd bakgrund. Med värdena Apple 220, Banana 330, Cherry 200 och totalen 750, målar regeln F4, F5 och F7 – det lösta området är hela datakolumnen F4:F7, och endast de celler vars värde uppfyller regeln lyser upp.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    // Pivot-tabell med dess övre vänstra hörn vid E3
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Fäst det villkorsstyrda formatet på F4 (rad 3, kolumn 5) med Data-omfång
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Regel - markera belopp större än 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) returnerar filen som bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Att förankra samma regel på rad‑fält‑etiketten E4 (rad 3, kolumn 4) med `Field`‑omfånget löser till F4:F6 istället – samma datakolumn utan totalraden – eftersom omfånget nu beskriver `Fruit`‑fältet snarare än hela värdeområdet. `Selection`‑omfånget som förankras i F4 löser till endast F4.

## **Definiera området manuellt**
Det andra sättet hoppar över omfångsväljaren och namnger området explicit på `PivotConditionalFormat`.

### **Ett kalkylbladsrektangel med addCellArea**
`addCellArea(cellArea)` registrerar den angivna rektangeln som regelns mål. Koordinaterna är nollbaserade kalkylbladskoordinater, och området är exakt den levererade rektangeln – ingen utökning till datakolumnen och ingen total‑logik. Använd den när de intressanta cellerna är en känd fast rektangel i den aktuella pivottabells‑layouten.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Måltavlan är rektangeln F4:F6 (värdecellerna utan totalen)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Regel - kursiv i ljusgul för belopp mellan 150 och 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **Ett semantiskt pivotområde med pivotAreas**
`pivotAreas` är samma semantiska regionsmodell som syskonsidan använder för statiska stilar. Bygg en `PivotArea`, välj ett fält eller område med `select` eller `selectField`, och lägg till det med `pivotAreas.addPivotArea(pivotArea)`. Ett semantiskt område förblir knutet till sitt fält, så den villkorsstyrda formateringen följer fältet när pivottabellen uppdateras och layouten förändras. `pivotAreas.add(pivotArea)`‑överlagringen fungerar fortfarande men är markerad som föråldrad – föredra `addPivotArea`.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Fäst regeln till Amount-datat fältet som ett semantiskt område
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Regel - grå text för belopp under 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Var reglerna lagras och hur de överlever en omläsning**
Varje anrop av `conditionalFormats.add()` lägger till ett `PivotConditionalFormat` i pivottabellen. Villkoren, deras formler och deras stilar sparas med arbetsboken – att öppna filen som sparades av det första exemplet i Node visar samma regel med sin typ, operator och formel intakta, och `getCellAreas()` rapporterar samma område. På den här plattformen visas `type`‑ och `operator`‑egenskaperna för ett villkor som numeriska enum‑värden. Poster som aldrig fick ett villkor tas bort när arbetsboken sparas, på samma sätt som Excel förkastar en villkorsstyrd formatering utan regel.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Ladda om filen som skrevs av det första exemplet
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // Det här skriver ut:
    // Villkorliga format: 1
    // Format 0: 1 2 formula1==200   (typ 1 = CellValue, operator 2 = Större än)
    //     rader 4-7, kolumner 6-6        (F4:F7, det lösta dataintervallet)
    process.exit(0);
});
```

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/javascript-cpp/apply-style-to-pivot-table/)
- [Formatera del av en pivottabell](/cells/sv/javascript-cpp/format-part-of-pivot-table/)
- [Topp 10 Visa eller filtrera i pivottabell](/cells/sv/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}