---
title: Lägga till filterfält i en pivottabell i Aspose.Cells för .NET
linktitle: Lägga till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for Node.js via Java, inklusive att lägga till filterfält, enkelvalsfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, Node.js via Java, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stödjer hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett högnivå-API eller via den lägre nivåns `PageFields`-samling, och du kan styra sidfiltret i enkelvalsläge, rensa det för att visa alla sidobjekt, eller växla fältet till flerval så att användare kan välja flera sidobjekt samtidigt via kryssrutegränssnittet i Excel.
{{% /alert %}}

## **Introduktion**

Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan pivottabellens kropp visar. Slutanvändare ser det som en rullgardinsmeny överst i en renderad pivottabell i Excel, och valet av ett av de tillgängliga sidobjekten bygger om pivotkroppen så att endast de poster som tillhör det sidobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.Page` snarare än `PivotFieldType.Row`, `PivotFieldType.Column` eller `PivotFieldType.Data`.

Ett filterfält kan fungera i två beteenden. I standardbeteendet **enkelval** är endast ett sidobjekt synligt åt gången, så pivotkroppen sammanfattar exakt en delmängd. I beteendet **flerval** exponerar fältet en kryssrutelista, och pivotkroppen sammanfattar unionen av alla ikryssade sidobjekt. Samma källfält kan flyttas fram och tillbaka mellan dessa beteenden genom att växla en enskild egenskap.

Aspose.Cells for Node.js via Java exponerar två likvärdiga sätt att registrera ett filterfält. Det högnivå-API:et är `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, som tar källkolumnens namn och lägger till fältet i ett enda anrop. Det lägre nivåns API är `pivotTable.getPageFields().add(PivotField)`, som används när du redan har en `PivotField`-referens och vill lägga till samma fältinstans i filterområdet. Båda API:erna fyller slutligen samma `PageFields`-samling, och resten av denna artikel demonstrerar hur man väljer mellan dem och hur man styr varje filtreringsläge.

## **Lägga till ett filterfält**

Det finns två sätt att registrera ett pivotfält i filterområdet. Det högnivåanropet tar källkolumnens namn som en sträng och är den vanligaste vägen. Det lägre nivåns anrop accepterar en befintlig `PivotField`-instans och är praktiskt när samma fältobjekt måste återanvändas över flera pivotområden. Båda anropen placerar fältet i `pivotTable.getPageFields()`, varefter det visas som sidrullgardinsmenyn överst i den renderade pivottabellen.

### Lägga till ett filterfält med addFieldToArea

Följande exempel bygger en liten Fruit / Year / Amount-dataset, placerar en pivottabell vid cell E3 med `Fruit` i radområdet, `Amount` i dataområdet och `Year` i filterområdet, uppdaterar pivottabellen och sparar arbetsboken.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Ställ in rubrikraden
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Fyll i 9 rader med exempeldata: Frukt, År, Mängd
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Lägg till en pivottabell förankrad vid cell E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Lägg till fält i deras områden: Frukt som Rad, Mängd som Data, År som Sidfält
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Uppdatera och beräkna pivottabellens data
pivotTable.calculateData();

// Spara arbetsboken
workbook.save("pageFieldSample.xlsx");
```

### Lägga till ett filterfält med getPageFields().add

När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `pivotTable.getPageFields().add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutgiltiga registreringen i filterområdet ersätts med det lägre nivåns API-anrop.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

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
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Frukt -> Rad, Belopp -> Data (År hamnar på Sida nedan)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Lågnivåstrategi: hämta det befintliga År PivotField från BaseFields
// och registrera det i Sid-området via PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Enkelvalsfiltrering (visa ett sidobjekt)**

I standardbeteendet enkelval renderas filterfältet som en enda rullgardinsmeny och heltalet `PivotField.CurrentPageItem` väljer vilket sidobjekt som styr pivotkroppen. Om man tilldelar ett specifikt index väljs det objektet; om man tilldelar det speciella sentinelvärdet `0x7FFD` (decimalt 32765) rensas filtret så att alla sidobjekt sammanfattas på en gång. Enkelval är standardläget; du behöver inte aktivera det explicit.

### Visa alla objekt

Att sätta `CurrentPageItem` till det magiska värdet `0x7FFD` är likvärdigt med att rensa sidfiltret, pivotkroppen sammanfattar alla sidobjekt som om inget filter tillämpades.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// Fylla i Fruit/Year/Amount-data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Skapa pivottabell vid E3
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// Konfigurera pivotfält: Fruit→Rad, Amount→Data, Year→Sida
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// Rensa sidfiltret så att alla objekt i sidfältet syns.
// 0x7FFD (decimal 32765) är det speciella sentinelvärdet som betyder "alla objekt" —
// motsvarande att välja "(Alla)" i Excel:s sidfält-rullmenyn.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Visa ett specifikt objekt

Att sätta `CurrentPageItem` till ett verkligt index väljer bara det sidobjektet. Indexet är objektets position i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Lägg till exempeldata (Frukt/År/Belopp)
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// Lägg till pivottabell vid E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Lägg till fält: Frukt→Rad, Belopp→Data, År→Sida
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Sidfältsspecifika operationer
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = andra objektet i sorterad ordning (t.ex. "2021")

// Uppdatera och beräkna pivottabell
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Flervalsfiltrering**

Flervalsfiltrering förvandlar sidrullgardinsmenyn till en kryssrutelista och låter slutanvändaren välja flera sidobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.IsMultipleItemSelectionAllowed` måste sättas till `true` innan flervalsgränssnittet överhuvudtaget träder i kraft. När det är aktiverat styr `PivotItem.IsHidden` vilka objekt som visas i kryssrutelistan, så du kan antingen visa alla objekt eller vitlista endast specifika objekt.

Koden nedan aktiverar flerval på samma Year-filterfält som byggdes i Scenario 1a, och visar sedan två mönster, Del A visar alla sidobjekt genom att lämna `IsHidden` satt till `false` för varje post, medan Del B vitlistar endast de källvärden du väljer och döljer allt annat genom ett `switch (pivotItems[i].getStringValue())`-block.

```javascript
const AsposeCells = require("aspose.cells");

// — Pivottabellen och sidfältet konstrueras exakt som i
//   Scenario 1a (Fruit/Year/Amount-data, pivot vid E3, Fruit→Rad,
//   Amount→Data, Year→Sida via AddFieldToArea).
//   Nedan tillämpar vi flervalsfiltrering på sidfältet.

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// Exempeldata: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — Aktivera flerval på sidfältet
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Del A — välj ALLA objekt (gör varje objekt synligt)
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// Del B — välj endast specifika objekt efter källvärde
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
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

> **Obs:** När du använder flervalsfiltrering via `PivotItem.IsHidden`, **måste minst en `PivotItem` förbli synlig** (`IsHidden == false`). Om alla objekt är dolda kraschar antingen Excel när filen öppnas, eller så renderas en tom pivottabell. Verifiera alltid att din flervalsvitlista innehåller minst ett objekt från din källdata.

## **Vilket API och vilket läge ska jag använda?**

Tabellen nedan sammanfattar när du ska använda varje API och läge så att du kan välja rätt kombination utan att läsa varje scenario i detalj.

| Scenario / användningsfall | Rekommenderat API | Använd egenskap | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält efter källkolumnens namn (vanligast) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | ej tillämpligt | Högnivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `pivotTable.getPageFields().add(PivotField)` | ej tillämpligt | Använd när fältobjektet erhölls på annat håll eller behöver återanvändas. |
| Filtrera till ett enskilt sidobjekt (standardläge) | `PivotField.CurrentPageItem` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa sidfiltret | `PivotField.CurrentPageItem` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinelvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.IsMultipleItemSelectionAllowed` | sätt till `true` | Krävs innan några `IsHidden`-anrop träder i kraft. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.IsHidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`IsHidden == false`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervals-filterfält är dolt kraschar Excel vid öppning eller renderar en tom pivottabell. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker öppnas tillförlitligt på varje maskin.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}
