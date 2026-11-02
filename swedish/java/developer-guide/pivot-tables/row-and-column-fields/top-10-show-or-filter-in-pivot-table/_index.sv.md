---
title: Visa eller filtrera topp 10 i pivottabell
linktitle: Visa eller filtrera topp 10 i pivottabell
description: Lär dig hur du endast visar de högst eller lägst rangordnade objekten i ett pivotfält i Aspose.Cells for Java. Den här artikeln beskriver metoden Top10AutoShow för Excel 97-2003, hur du läser alternativ med Top10AutoShowSettings och filtret Topp 10 för Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Java, pivottabell, topp 10, automatisk visning, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /sv/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell som listar varje objekt i ett radfält kan vara svårläst när fältet har dussintals medlemmar. En topp 10-rapport behåller endast de högst eller lägst rangordnade objekten, vilket är precis vad rapporter med rangordning behöver – ”topp 5 produkter efter intäkt” eller ”de tre lägst rangordnade regionerna efter antal försäljningar”. Aspose.Cells stöder två mekanismer för detta, och de motsvarar två generationer av Microsoft Excel.
- **Excel 97-2003 AutoShow** – metoden `PivotField.top10AutoShow()`. Den klassiska inställningen ”Visa de översta/understa N objekten” lagras direkt i pivotfältet. Den fungerar i alla Excel-versioner, gamla som nya, eftersom den ingår i det ursprungliga pivottabellformatet.
- **Excel 2007-365 topp 10-filter** – metoden `PivotField.filterTop10()`. Detta är det moderna topp 10-värdefilter som finns under Värdefilter i fältmenyn. Det lagras som ett `PivotFilter`-objekt kopplat till fältet och erbjuder rangordning baserad på antal objekt och procentandel.

## **Visa topp 10 i Excel 97-2003 (top10AutoShow)**
Den klassiska AutoShow-inställningen konfigureras med ett enda anrop till `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` – aktiverar eller inaktiverar AutoShow-inställningen i fältet.
- `isTop` – `true` behåller de högst rangordnade objekten (Topp), medan `false` behåller de lägst rangordnade (Botten).
- `count` – hur många objekt som ska behållas, till exempel 10 för en klassisk topp 10-rapport.
- `rankBy` – det nollbaserade indexet till **datafältet** vars värden rangordnar objekten. Ange -1 för att rangordna objekten efter fältet självt.
Rangordningen kan bestämmas av ett värdefält eller av fältet självt. Det finns två naturliga varianter, som visas nedan.

### **Rangordna efter ett värdefält**
Rangordna radfältets objekt efter ett vanligt värdefält, till exempel Summa av försäljning. I följande exempel skapas en pivottabell med ett radfält (`Sport`) och ett datafält (`Sales`), och därefter visas de två högst rangordnade sporterna enligt försäljningen. `rankBy` är 0 eftersom ”Summa av försäljning” är datafältet med index 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Visa de 2 högsta objekten rankade efter "Summa av försäljning" (datafältindex 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Rangordna efter fältet självt**
Ett fält kan också rangordnas efter sig självt – ange -1 som `rankBy`. För den här varianten behövs inget extra datafält; fältet behöver bara placeras i rad- eller kolumnområdet. I följande exempel visas de tre lägst rangordnade sporterna, där rangordningen görs efter fältet självt. När inställningen sparas utelämnas attributet `rankBy` från pivottabellens XML eftersom -1 är formatets standardvärde, och `Top10AutoShowSettings.getRankBy()` läser tillbaka värdet -1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Visa de 3 lägsta objekten rankade efter fältet självt (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Läsa aktuella alternativ (Top10AutoShowSettings)**
Metoden `PivotField.getTop10AutoShowSettings()` returnerar ett `PivotFieldTop10AutoShowSettings`-objekt som exponerar de AutoShow-alternativ som för närvarande lagras i fältet. Använd det för att undersöka hur en befintlig arbetsbok eller en pivottabell som du nyss har konfigurerat kommer att visa sina objekt – även när arbetsboken har lästs in från en fil.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

De fyra egenskaperna motsvarar de klassiska AutoShow-attributen som skrivs till pivottabellens XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). De värden som läses tillbaka är därför desamma värden som alla Excel-versioner respekterar.

## **Obs**

{{% alert color="primary" %}}
- De direkta egenskaperna i `PivotField` som exponeras av `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` och `getAutoShowField()` är markerade som föråldrade. Använd i stället objektet `Top10AutoShowSettings`: `Top10AutoShowSettings.isAutoShow()` ersätter `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` ersätter `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` ersätter `PivotField.getAutoShowCount()` och `Top10AutoShowSettings.getRankBy()` ersätter `PivotField.getAutoShowField()`. Metoden `PivotField.top10AutoShow()` är den metod som bör användas för att ändra inställningarna.
- `top10AutoShow` fungerar med rad- och kolumnfält. Ett fält som endast finns i sidfältsområdet (filterområdet) kan inte rangordnas på det här sättet, eftersom dess objekt inte placeras i pivottabellens tabellområde.
{{% /alert %}}

## **Excel 2007-365: topp 10-filter (filterTop10)**
Moderna Excel-versioner exponerar topp 10 som ett värdefilter i fältmenyn (Värdefilter, Topp 10...). Aspose.Cells modellerar det med metoden `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, som returnerar det skapade `PivotFilter`-objektet:
- `valueFieldIndex` – det nollbaserade indexet till datafältet vars aggregerade värden rangordnar objekten.
- `type` – vad `itemCount` betyder. `PivotFilterType.COUNT` behåller ett bestämt antal objekt (alternativet Objekt i dialogrutan). `PivotFilterType.PERCENT` behåller en viss procentandel av objekten, så att `itemCount` anger procenttalet – 30 behåller alltså de översta 30 procenten. `PivotFilterType.SUM` rangordnar utifrån den kumulativa andelen av det totala värdet som filtreringen omfattar.
- `isTop` – `true` för Topp, `false` för Botten.
- `itemCount` – N i Topp N; enheten beror på `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Top 10-filter - behåll de 2 bästa objekten baserat på "Sum of Sales" (index 0 för datafältet)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// För ett procentbaserat filter behålls i stället de översta 30 procenten av objekten:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` och `filterTop10` är två separata funktioner. AutoShow skriver det klassiska `autoShow`-attributet på pivotfältet, och det respekteras av alla Excel-versioner från och med Excel 97. `filterTop10` skriver en modern `PivotFilter`-post, vilket kräver Excel 2007 eller senare. När en arbetsbok öppnas i en äldre Excel-version visar en pivottabell som använder det moderna filtret alla objekt i stället. För dokument som måste gå fram och tillbaka via äldre verktyg bör du föredra `top10AutoShow`; för moderna arbetsböcker bör du föredra `filterTop10` eftersom det kan kombineras med de övriga värdefiltren.
{{% /alert %}}

## **Relaterade artiklar**
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/java/filter-by-label-or-value-of-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabell](/cells/sv/java/pivot-table-add-row-and-column-fields/)
- [Gruppera pivotfält i pivottabellen](/cells/sv/java/group-pivot-fields-in-the-pivot-table/)
- [Uppdatera pivottabell](/cells/sv/java/refresh-pivot-table/)
- [Lägg till sidfält i pivottabell](/cells/sv/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}