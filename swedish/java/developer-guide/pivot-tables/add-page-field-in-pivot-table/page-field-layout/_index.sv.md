---
title: Ändra sidfältslayout i pivottabell
linktitle: Ändra sidfältslayout i pivottabell
description: Lär dig hur du styr layouten för sidfältsområdet i en pivottabell med Aspose.Cells for Java, inklusive inställning av visningsordning, radbrytningsantal och fältordning för sidfälten överst i pivottabellen.
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, pivottabell, sidfält, sidfältsordning, radbrytningsantal för sidfält, flytta sidfält
type: docs
weight: 191
url: /sv/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Den här artikeln är en fortsättning på ämnet **Lägg till sidfält i pivottabell**. Den visar hur du styr layouten för sidfältsområdet — remsan med filterkontroller överst i en pivottabell — inklusive visningsordning, radbrytningsantal och omordning av fält.
{{% /alert %}}
## **Introduktion**
En pivottabell i Microsoft Excel har ett dedikerat **sidfältsområde** som sitter ovanför tabellens rad-/kolumn-/datakropp. Detta område renderas som en remsa med rullgardinsfilterkontroller (en per sidfält) och det är vad slutanvändare klickar på för att skära pivoten efter kriterier som år eller region. Aspose.Cells modellerar detta område via samlingen `pivotTable.getPageFields()` och exponerar tre egenskaper som styr hur remsan visas visuellt:
- `pivotTable.getPageFieldOrder()` (ett `Aspose.Cells.PrintOrderType`-värde) avgör om ytterligare sidfält placeras *bredvid* de befintliga eller *under* dem.
- `pivotTable.getPageFieldWrapCount()` anger hur många sidfält som placeras per rad eller kolumn innan en radbrytning sker.
- `pivotTable.getPageFields().move(currIndex, destIndex)` omordnar sidfälten utan att ändra ordningsläget.
Den här artikeln går igenom tre kodexempel som demonstrerar var och en av dessa operationer på en delad datamängd, så att du kan jämföra de resulterande layouterna sida vid sida.
## **Källdata**
Alla tre exempel nedan läser in dessa åtta rader med försäljningsdata i ett kalkylblad som heter `PivotData`. Data innehåller två kandidater för sidfält (`Year`, `Region`), en kandidat för radfält (`Fruit`) och ett mått (`Amount`), vilket gör sidfältsremsan meningsfull att inspektera.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alla åtta rader fylls i i varje kodexempel, i identisk ordning, så att källdata aldrig skiljer sig mellan scenarierna — det är bara egenskaperna för sidfältslayout som gör det.
## **Exempel 1: Över sedan ned**
I det första scenariot konfigurerar vi de två sidfälten (`Year`, `Region`) så att de visas **sida vid sida i en enda rad** överst i pivottabellen. Vi tilldelar `Fruit` till radaxeln, placerar `Year` först och `Region` sedan på sidaxeln (ordningen på `addFieldToArea`-anropen avgör startindexet), lägger till `Amount` (Summa) som datafält och anger sedan `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` med `pivotTable.setPageFieldWrapCount(2)`. Med `OVER_THEN_DOWN` och ett radbrytningsantal på 2 läggs de två sidfälten ut horisontellt sida vid sida i en enda rad överst i pivottabellen, så att remsan upptar en rad med bredden två.
```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();

// Rubriker (rad 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Rad 1: Apple, 2022, Norr, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Rad 2: Apple, 2023, Norr, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Rad 3: Banan, 2022, Söder, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Rad 4: Banan, 2023, Söder, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Rad 5: Körsbär, 2022, Öst, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Rad 6: Körsbär, 2023, Öst, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Rad 7: Druva, 2022, Väst, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Rad 8: Druva, 2023, Väst, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Lägg till PivotTableReport-ark
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();

// Skapa pivottabell från PivotData!A1:D9 placerad vid A1 på PivotTableReport
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// Lägg till fält
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // Frukt
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // År
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // Belopp
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);

// Konfigurera sidfältsområdets layout: placera sidfält först horisontellt, radbryt efter varannan
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

// Uppdatera och beräkna
pivotTable.calculateData();

// Spara
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```
## **Exempel 2: Ned sedan över**
I det här exemplet placerar vi `Fruit` på radaxeln, `Year` och `Region` på sidaxeln (med `Year` först) och `Amount` (Summa) som datafält — exakt som i Exempel 1. Vi anger sedan `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` och `pivotTable.setPageFieldWrapCount(2)`. Med `DOWN_THEN_OVER` och ett radbrytningsantal på 2 staplas de två sidfälten vertikalt — `Year` överst, `Region` direkt under — och bildar en enda kolumn överst i pivottabellen. Remsan upptar därför två rader med bredden ett, i motsats till Exempel 1.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");

String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **Exempel 3: Flytta ett sidfält**
I det tredje scenariot behåller vi denna datamängd och fälttilldelning, anger en neutral layout (`OVER_THEN_DOWN` med radbrytningsantal `2`) och demonstrerar sedan operationen `pageFields.move`. Anropet `move(0, 1)` flyttar sidfältet på index 0 (`Year`) till position 1, och sidfältet som var på position 1 (`Region`) flyttas till position 0. Efter detta anrop är `Region` det första sidfältet och `Year` det andra. Radbrytningen och ordningsläget är oförändrade, så remsan renderas fortfarande horisontellt sida vid sida — det är bara ordningen på de två rullgardinerna som har bytts ut.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");

int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **Relaterade artiklar**
- [Lägg till sidfält i pivottabell](/cells/sv/java/add-page-field-in-pivot-table/) — föräldrasidan som introducerar hur sidfält läggs till i en pivottabell.
- [Rad- och kolumnfält i pivottabell](/cells/sv/java/row-and-column-fields/) — täcker tilldelning av fält till rad- och kolumnaxlarna, som kompletterar sidaxelarbetet som visas här.
- [Hantera värdefält i pivottabell](/cells/sv/java/manage-value-fields/) — beskriver hur man konfigurerar dataområdet (värde), inklusive `Sum`-aggregeringen som används i denna artikel.
- [Uppdatera pivottabell](/cells/sv/java/refresh-pivot-table/) — förklarar `refreshData()` och `calculateData()`, som krävs efter omordning av sidfält.
- [Tillämpa stil på pivottabell](/cells/sv/java/apply-style-to-pivot-table/) — visar hur man formaterar den renderade pivottabellen efter det att sidfältsremsan har lagts ut.
{{< app/cells/assistant language="java" >}}