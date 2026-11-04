---
title: Formatera del av en pivottabell
description: Formatera en del av en pivottabell i Aspose.Cells for Java genom att applicera stilar på semantiska PivotArea-områden eller CellArea-rektanglar via PivotTable.format, där formaten lagras i PivotTable.getPivotFormats och bevaras när pivottabellen uppdateras.
linktitle: Formatera del av en pivottabell
keywords: Aspose.Cells for Java, pivottabell, formatering, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /sv/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
`PivotTable.formatAll` tillämpar en enda stil på hela pivottabellen och behandlas på föräldrasidan. Den skiljer inte mellan etiketter, värden, totaler eller specifika områden i rapporten.
I praktiken är det vanligt att endast en del av en pivottabell behöver framhävas. Vanliga mål inkluderar etiketter som tillhör ett radfält, värdeceller som produceras av ett fält, rad med total för hela tabellen eller en godtycklig rektangel såsom de två första objekt raderna.
Att applicera en stil direkt på kalkylbladets celler i en pivottabell är inte detsamma. Excel lagrar pivottabelformat som semantiska `PivotArea`-områden snarare än vanliga cell‑stilsregister. Ett pivot‑area‑format förblir fäst vid ett område såsom ett fälts etiketter eller datavärden, och det återupptäcks när pivottabellen beräknas om, uppdateras eller expanderas. En stil som skrivs direkt till en cell tillhör däremot den cellens position och spåras inte av pivot‑modellen.
Aspose.Cells exponerar den kompletta familjen av `PivotTable.format`‑överlagringar så att båda typerna av formatering är tillgängliga:
- `format(PivotArea, Style)` fäster en stil på ett semantiskt område som byggs med `PivotArea.select` eller `PivotArea.selectField`.
- `format(CellArea, Style)` fäster en stil på en kalkylbladsrektangel inom pivottabellen.
- `format(int row, int column, Style)` riktar sig mot en enda cell.
- `formatAll(Style)` formaterar hela pivottabellen.

## **Formatera ett Pivot‑område**
Arbetsflödet med semantiskt område är den rekommenderade metoden när en markering måste följa ett fält eller ett område i rapporten.
1. Skapa ett `PivotArea` med `new PivotArea(pivotTable)`. Objektet beskriver ett semantiskt område som tillhör den specifika pivottabellen.
1. Välj ett fält efter dess nollbaserade position på en given axel med `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` väljer både fältets etiketter och data.
   - `PivotTableSelectionType.LABEL_ONLY` väljer endast fältets etiketter.
   - `PivotTableSelectionType.DATA_ONLY` väljer endast fältets dataceller.
1. Välj ett fält efter namn med `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. När ett radfält väljs efter namn, löser området upp sig till de värdeceller som produceras av fältets objekt.
1. Skapa en `Style` med `Workbook.createStyle()`, konfigurera dess teckensnitt, förgrundsfärg och solid bakgrundsmall, och skicka stilen till `PivotTable.format(area, style)`.
1. Varje anrop av `PivotArea`‑överlagringen lägger till en `PivotTableFormat`‑post i `PivotTable.getPivotFormats()`.
1. Fält‑fästa format målas när pivot‑data beräknas. Därför bör du anropa `PivotTable.calculateData()` efter att formaten har tillämpats så att stilarna blir synliga.
Exemplet nedan bygger en liten pivottabell för fruktförsäljning, formaterar `Fruit`‑radetiketterna med `PivotArea.select` och `PivotTableSelectionType.LABEL_ONLY`, formaterar värdecellerna som produceras av samma radfält med `PivotArea.selectField`, och beräknar därefter pivottabellen på nytt så att båda stilarna målas.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formatera ett Cell‑område i pivottabellen**
Använd `PivotTable.format(CellArea, Style)` när det område som intresserar är en enkel kalkylbladsrektangel snarare än ett semantiskt pivot‑område.
Ett `CellArea` beskrivs av egenskaperna `getStartRow()`, `getStartColumn()`, `getEndRow()` och `getEndColumn()`. Värdena är nollbaserade kalkylbladskoordinater, och sluttkoordinaterna identifierar den sista raden och kolumnen som ingår i rektangeln, så området täcker cellerna från startpositionen till slutpositionen inklusive.
Till skillnad från ett fält‑fäst format appliceras ett `CellArea`‑format på cellerna omedelbart. Ett ytterligare anrop av `calculateData()` behövs inte för att stilen ska visas.
En `CellArea`‑rektangel kan innehålla både etikettceller och värdeceller. Nästa avsnitt beskriver hur Aspose.Cells och Excel representerar den rektangeln internt.
Exemplet nedan formaterar rektangeln `E4:F5` i pivottabellen med en kursiv, ljusblå stil och sparar arbetsboken utan någon ytterligare omberäkning.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Hur Pivot‑områden och Cell‑områden kartläggs**
Excel lagrar pivottabelformat som `pivotArea`-poster snarare än som vanliga kalkylblads‑cell‑stilsregister. Samma modell används av Aspose.Cells, så en formateringsbegäran översätts till pivot‑områden när den registreras.
Relationen mellan det `CellArea` som användaren tillhandahåller och de pivot‑områden som lagras internt är många‑till‑många i båda riktningarna.
- Ett `CellArea` kan generera flera pivot‑områden. Om rektangeln omfattar både etikettceller och värdeceller, delas den upp i separata etikett‑ och dataregler, eftersom pivot‑modellen behandlar etikettformatering och dataformatering oberoende.
- Ett pivot‑område kan lösa upp sig till flera skilda `CellArea`‑instanser. Ett semantiskt område såsom en rad för total summa, eller ett fält vars objekt inte är sammanhängande, kan omfatta flera rektanglar. Detta är anledningen till att `PivotArea.getCellAreas()` returnerar en samling istället för en enda rektangel.
Varje formatoperation som utförs via `PivotTable.format` registreras i `PivotTable.getPivotFormats()`. Varje `PivotTableFormat`‑post visar den associerade `PivotArea` och den `Style` som tillämpas på den. `PivotArea`‑överlagringen lägger till exakt en post per anrop, medan ett `CellArea` som innehåller olika semantiska regioner kan lägga till flera poster.
För att särskilja de lagrade regionerna visar varje `PivotArea` flaggorna `getOnlyLabel()` och `getOnlyData()`. Exemplet nedan formaterar en enskild rektangel som täcker både etiketter och värden, inspekterar `PivotTable.getPivotFormats()` och skriver ut `CellArea`‑koordinaterna som varje lagrat pivot‑område löser upp till.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
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
Eftersom formaten lagras som pivot‑områden snarare än som vanliga cellstilar, överlever de omberäkning och uppdatering. När pivottabellen uppdateras med `PivotTable.refreshData`, beräknas om med `calculateData`, eller sparas och läses in igen, löser varje lagrat pivot‑område upp sig till den aktuella positionen för sitt område och dess stil appliceras på nytt.
{{% /alert %}}

Använd ett `PivotArea` byggt med `select` eller `selectField` när en markering måste förbli fäst vid ett fält eller ett semantiskt område över uppdateringar, och använd ett `CellArea` när formatering av en fast rektangel i det aktuella pivottabelutseendet är tillräckligt. En‑cells‑överlagringen `format(int row, int column, Style)` riktar sig mot en enskild cell. Använd `formatAll`, som behandlas på föräldrasidan, när hela pivottabellen ska omformateras på en gång.

## **Relaterade artiklar**
- [Applicera stil på pivottabell](/cells/sv/java/apply-style-to-pivot-table/)
- [Lägga till rader- och kolumnfält i pivottabell](/cells/sv/java/pivot-table-add-row-and-column-fields/)
- [Hantera värdefält i pivottabell](/cells/sv/java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}