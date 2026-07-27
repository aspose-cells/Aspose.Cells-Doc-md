---
title: Lägga till filterfält i en pivottabell i Aspose.Cells för .NET
linktitle: Lägga till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for Node.js via C++, inklusive att lägga till filterfält, enkelvalfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, Node.js via C++, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/nodejs-cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett högnivå-API eller via den lägre nivåns `PageFields`-samling, och du kan styra sidfiltret i enkelvalsläge, rensa det för att visa varje sidobjekt, eller växla fältet till flerval så att användare kan välja flera sidobjekt samtidigt via kryssrutegränssnittet i Excel.
{{% /alert %}}

## **Introduktion**

Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan pivotens innehåll visar. Slutanvändare ser det som en rullgardinsmeny överst i en renderad pivot i Excel, och att välja ett av de tillgängliga sidobjekten bygger om pivotens innehåll så att endast posterna som tillhör det sidobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.Page` snarare än `PivotFieldType.Row`, `PivotFieldType.Column` eller `PivotFieldType.Data`.

Ett filterfält kan fungera i två beteenden. I standardbeteendet **enkelval** är endast ett sidobjekt synligt åt gången, så pivotens innehåll sammanfattar exakt en delmängd. I beteendet **flerval** exponerar fältet en kryssrutelista, och pivotens innehåll sammanfattar unionen av varje markerat sidobjekt. Samma källfält kan flyttas fram och tillbaka mellan dessa beteenden genom att växla en enskild egenskap.

Aspose.Cells for Node.js via C++ exponerar två likvärdiga sätt att registrera ett filterfält. Det högnivå-API är `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, som tar källkolumnnamnet och lägger till fältet i ett enda anrop. Det lägre nivåns API är `PivotTable.pageFields.add(PivotField)`, som används när du redan har en `PivotField`-referens och vill lägga till samma fältinstans i filterområdet. Båda API:erna fyller slutligen samma `PageFields`-samling, och resten av denna artikel demonstrerar hur man väljer mellan dem och hur man styr varje filtreringsläge.

## **Lägga till ett filterfält**

Det finns två sätt att registrera ett pivotfält i filterområdet. Det högnivå-anropet tar källkolumnnamnet som en sträng och är den vanligaste vägen. Det lägre nivåns anrop accepterar en befintlig `PivotField`-instans och är bekvämt när samma fältobjekt måste återanvändas över flera pivotområden. Båda anropen placerar fältet i `PivotTable.pageFields`, varefter det visas som sidans rullgardinsmeny överst i den renderade pivoten.

### Lägga till ett filterfält med addFieldToArea

Följande exempel bygger ett litet Fruit / Year / Amount-dataset, placerar en pivottabell vid cell E3 med `Fruit` i radområdet, `Amount` i dataområdet och `Year` i filterområdet, uppdaterar pivoten och sparar arbetsboken.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Ställ in rubrikraden
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Fylla i 9 rader med exempeldata: Frukt, År, Belopp
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

// Lägg till fält i deras områden: Frukt som Rad, Belopp som Data, År som Sidfält
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Uppdatera och beräkna pivottabellens data
pivotTable.calculateData();

// Spara arbetsboken
workbook.save("pageFieldSample.xlsx");
```

### Lägga till ett filterfält med pageFields.add

När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.pageFields.add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutliga registreringen i filterområdet ersätts med det lägre nivåns API-anrop.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Rubriker
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Exempeldata (9 rader)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Lägg till pivottabell vid E3 som täcker A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Frukt -> Rad, Belopp -> Data (År kommer att läggas till Sida nedan)
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

## **Enkelvalsfiltrering (Visa ett sidobjekt)**

I standardbeteendet enkelval renderas filterfältet som en enda rullgardinsmeny och heltalsvärdet `PivotField.currentPageItem` väljer vilket sidobjekt som styr pivotens innehåll. Att tilldela ett specifikt index väljer det objektet; att tilldela den speciella sentinelvärdet `0x7FFD` (decimalt 32765) rensar filtret så att alla sidobjekt sammanfattas samtidigt. Enkelval är standard; du behöver inte aktivera det explicit.

### Visa alla objekt

Att sätta `currentPageItem` till det magiska värdet `0x7FFD` är likvärdigt med att rensa sidfiltret: pivotens innehåll sammanfattar alla sidobjekt som om inget filter tillämpades.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Fylla i Fruit/Year/Amount-data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Skapa pivottabell vid E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Konfigurera pivotfält: Fruit→Rad, Amount→Data, Year→Sida
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// Rensa sidfiltret så att alla objekt i sidfältet visas.
// 0x7FFD (decimal 32765) är det speciella sentinelvärdet som betyder "alla objekt" —
// motsvarande att välja "(Alla)" i Excels sidfält-rullgardinsmeny.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Visa ett specifikt objekt

Att sätta `currentPageItem` till ett riktigt index väljer bara det sidobjektet. Indexet är positionen för objektet i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Lägg till exempeldata (Frukt/År/Belopp)
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

Flervalsfiltrering förvandlar sidans rullgardinsmeny till en kryssrutelista och låter slutanvändaren välja flera sidobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.isMultipleItemSelectionAllowed` måste sättas till `true` innan flervalsgränssnittet över huvud taget aktiveras. När det är aktiverat styr `PivotItem.isHidden` vilka objekt som visas i kryssrutelistan, så du kan antingen visa varje objekt eller vitlista endast specifika objekt.

Koden nedan aktiverar flerval på samma Year-filterfält som byggdes i Scenario 1a, och visar sedan två mönster: Del A avslöjar alla sidobjekt genom att låta `isHidden` vara satt till `false` för varje post, medan Del B vitlistar endast de källvärden du väljer och döljer allt annat genom ett `switch (pivotItems[i].getStringValue())`-block.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Exempeldata: Frukt | År | Belopp
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Aktivera flerval på sidfältet
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Del A — välj ALLA objekt (gör alla objekt synliga)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Del B — välj endast specifika objekt efter källvärde
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Obs:** När du använder flervalsfiltrering via `PivotItem.isHidden`, **måste minst en `PivotItem` förbli synlig** (`isHidden == false`). Om varje objekt är dolt kraschar Excel antingen när filen öppnas eller renderar en tom pivot. Verifiera alltid att din flervalsvitlista inkluderar minst ett objekt från din källdata.

## **Vilket API och vilket läge ska jag använda?**

Tabellen nedan sammanfattar när du ska använda varje API och läge så att du kan välja rätt kombination utan att läsa varje scenario i detalj.

| Scenario / Användningsfall | Rekommenderat API | Använd egenskap | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält via källkolumnnamn (vanligast) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Högnivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `PivotTable.pageFields.add(PivotField)` | n/a | Använd när fältobjektet erhölls någon annanstans eller behöver återanvändas. |
| Filtrera till ett enskilt sidobjekt (standardläge) | `PivotField.currentPageItem` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa sidfiltret | `PivotField.currentPageItem` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinelvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.isMultipleItemSelectionAllowed` | sätt till `true` | Krävs innan några `isHidden`-anrop får effekt. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.isHidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`isHidden == false`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervals-filterfält är dolt, kraschar Excel vid öppning eller renderar en tom pivot. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker kommer att öppnas tillförlitligt på varje maskin.
{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}
