---
title: Lägga till filterfält i en pivottabell i Aspose.Cells for Java
linktitle: Lägga till filterfält i en pivottabell i Aspose.Cells for Java
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
// Skapa en ny arbetsbok
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Ställ in rubrikraden
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Fyll i 9 rader med exempeldata: Frukt, År, Belopp
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
// Lägg till en pivottabell förankrad vid cell E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Lägg till fält i deras områden: Frukt som Rad, Belopp som Data, År som Sidfält
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Uppdatera och beräkna pivottabellens data
pivotTable.calculateData();
// Spara arbetsboken
workbook.save("pageFieldSample.xlsx");
```

### Lägga till ett filterfält med PageFields.add
När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.PageFields.add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutgiltiga registreringen i filterområdet ersätts med anropet på lägre nivå.

```java
import com.aspose.cells.*;
// - Pivottabellen och sidfältet konstrueras exakt som i
//   Scenario 1a (Frukt/År/Belopp-data, pivot vid E3, Frukt->Rad,
//   Belopp->Data). Nedan hämtar vi År PivotField från
//   BaseFields-samlingen och skickar det till PageFields.Add - det
//   lågnivåalternativ till AddFieldToArea. Resultatet är
//   funktionellt identiskt med Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Rubriker
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Exempeldata (9 rader)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Lägg till pivottabell vid E3 som täcker A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Frukt -> Rad, Belopp -> Data (År kommer att läggas till Sida nedan)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Lågnivåmetod: hämta det befintliga År PivotField från BaseFields
// och registrera det i Sid-området via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
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
// Fylla i Frukt/År/Belopp-data
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
// Skapa pivottabell vid E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);
// Konfigurera pivotfält: Frukt till Rad, Belopp till Data, År till Sida
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Rensa sidfiltret så att varje objekt i sidfältet visas.
// 0x7FFD (decimal 32765) är det speciella sentinelvärdet som betyder "alla objekt",
// motsvarande att välja "(Alla)" i Excels sidfält-rullmeny.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Visa ett specifikt objekt
Att sätta `CurrentPageItem` till ett verkligt index väljer bara det ena filterobjektet. Indexet är positionen för objektet i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```java
import com.aspose.cells.*;
// Skapa arbetsbok
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Lägg till exempeldata (Fruit/Year/Amount)
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
// Lägg till pivottabell vid E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Lägg till fält: Fruit→Rad, Amount→Data, Year→Sida
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Sidfältsspecifika operationer
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = andra objektet i sorterad ordning (t.ex. "2021")
// Uppdatera och beräkna pivottabell
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
// Exempeldata: Frukt | År | Belopp
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
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Aktivera flerval på sidfältet
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Del A -- välj ALLA objekt (gör alla objekt synliga)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Del B -- välj endast specifika objekt efter källvärde
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