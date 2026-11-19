---
title: Lägga till filterfält i en pivottabell i Aspose.Cells for Java
linktitle: Lägg till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for Java, inklusive att lägga till filterfält, enkelvalfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, Java, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett högnivå-bekvämlighets-API eller via den lägre nivåns `PageFields`-samling, och du kan styra filtret i enkelvalläge, rensa det för att visa varje filterobjekt, eller växla fältet till flerval så att användare kan välja flera filterobjekt samtidigt via kryssrutegränssnittet i Excel.
{{% /alert %}}

## **Introduktion**
Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan pivotkroppen visar. Slutanvändare ser det som en rullmeny överst i en renderad pivot i Excel, och att välja ett av de tillgängliga filterobjekten bygger om pivotkroppen så att endast de poster som tillhör det filterobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.Page` istället för `PivotFieldType.Row`, `PivotFieldType.Column` eller `PivotFieldType.Data`.

## **Lägga till ett filterfält**

### Lägga till ett filterfält med addFieldToArea
Följande exempel bygger en liten Fruit / Year / Amount-datamängd, placerar en pivottabell vid cell E3 med `Fruit` på radområdet, `Amount` på dataområdet och `Year` på filterområdet, uppdaterar pivoten och sparar arbetsboken.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Refresh and calculate the pivot table data
pivotTable.calculateData();
// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### Lägga till ett filterfält med PageFields.add
När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.PageFields.add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutgiltiga registreringen i filterområdet ersätts med anropet på lägre nivå.

```java
import com.aspose.cells.*;
// - The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit->Row,
//   Amount->Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add - the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Enkelvalfiltrering (visa ett filterobjekt)**
I standardbeteendet för enkelval renderas filterfältet som en enda rullmeny och heltalsvärdet i `PivotField.CurrentPageItem` väljer vilket filterobjekt som styr pivotkroppen. Att tilldela ett specifikt index väljer det ena objektet; att tilldela det speciella sentinellvärdet `0x7FFD` (decimalt 32765) rensar filtret så att varje filterobjekt sammanfattas på en gång. Enkelval är standard; du behöver inte aktivera det explicit.

### Visa alla objekt
Att sätta `CurrentPageItem` till det magiska värdet `0x7FFD` är likvärdigt med att rensa filtret: pivotkroppen sammanfattar varje filterobjekt som om inget filter tillämpades.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Create pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivot = pivotTables.add("=A1:C7", 2, 4);
// Configure pivot fields: Fruit to Row, Amount to Data, Year to Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items",
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Visa ett specifikt objekt
Att sätta `CurrentPageItem` till ett verkligt index väljer bara det ena filterobjektet. Indexet är positionen för objektet i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```java
import com.aspose.cells.*;
// Create workbook
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Add pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivotTable = pivotTables.add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Flervalsfiltrering**
Flervalsfiltrering förvandlar filterrullmenyn till en kryssrutelista och låter slutanvändaren välja flera filterobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.IsMultipleItemSelectionAllowed` måste sättas till `true` innan flervalsgränssnittet överhuvudtaget får effekt. När det är aktiverat styr `PivotItem.IsHidden` vilka objekt som visas i kryssrutelistan, så du kan antingen visa varje objekt eller vitlista endast specifika objekt.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
PivotTable pivotTable = pivots.add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Part A -- select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Part B -- select only specific items by source value
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Obs!** När du använder flervalsfiltrering via `PivotItem.IsHidden` måste **minst en `PivotItem` förbli synlig** (`IsHidden == false`). Om varje objekt är dolt kraschar antingen Excel när filen öppnas, eller så renderas pivoten tom. Verifiera alltid att din flervalsvitlista innehåller minst ett objekt från din källdata.

## **Vilket API och vilket läge ska jag använda?**
Tabellen nedan sammanfattar när du ska använda varje API och läge så att du kan välja rätt kombination utan att läsa varje scenario i detalj.
| Scenario / användningsfall | Rekommenderat API | Använd egenskap | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält med källkolumnnamn (vanligast) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | Högnivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `PivotTable.PageFields.add(PivotField)` | n/a | Använd när fältobjektet erhölls någon annanstans eller behöver återanvändas. |
| Filtrera till ett enskilt filterobjekt (standardläge) | `PivotField.CurrentPageItem` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa filtret | `PivotField.CurrentPageItem` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinellvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.IsMultipleItemSelectionAllowed` | sätt till `true` | Krävs innan några `IsHidden`-anrop får effekt. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.IsHidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`IsHidden == false`). |

{{% alert color="primary" %}}
Kom ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervalsfilterfält är dolt kraschar Excel vid öppning eller renderar en tom pivot. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker öppnas tillförlitligt på varje maskin.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}