---
title: Lägga till filterfält i en pivottabell i Aspose.Cells för .NET
linktitle: Lägga till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for .NET, inklusive att lägga till filterfält, enkelvalsfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, .NET, pivot table, filter field, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett högnivå-API eller via den lägre nivåns `PageFields`-samling, och du kan styra sidfiltret i enkelvalsläge, rensa det för att visa varje sidobjekt, eller växla fältet till flerval så att användare kan välja flera sidobjekt samtidigt via kryssrutogränssnittet i Excel.
{{% /alert %}}

## **Introduktion**

Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan pivottabellkroppen visar. Slutanvändare ser det som en rullgardinsmeny överst i en renderad pivottabell i Excel, och att välja ett av de tillgängliga sidobjekten bygger om pivottabellkroppen så att endast de poster som tillhör det sidobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.Page` istället för `PivotFieldType.Row`, `PivotFieldType.Column` eller `PivotFieldType.Data`.

Ett filterfält kan fungera i två beteenden. I standardbeteendet **enkelval** är endast ett sidobjekt synligt åt gången, så pivottabellkroppen sammanfattar exakt en delmängd. I beteendet **flerval** exponerar fältet en kryssrutelista, och pivottabellkroppen sammanfattar unionen av alla ikryssade sidobjekt. Samma källfält kan flyttas fram och tillbaka mellan dessa beteenden genom att växla en enskild egenskap.

Aspose.Cells for .NET exponerar två likvärdiga sätt att registrera ett filterfält. Det högnivå-API:t är `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, som tar källkolumnnamnet och lägger till fältet i ett enda anrop. Det lägre nivå-API:t är `PivotTable.PageFields.Add(PivotField)`, som används när du redan har en `PivotField`-referens och vill lägga till samma fältinstans i filterområdet. Båda API:erna slutar med att fylla samma `PageFields`-samling, och resten av denna artikel visar hur du väljer mellan dem och hur du styr varje filtreringsläge.

## **Lägga till ett filterfält**

Det finns två sätt att registrera ett pivotfält i filterområdet. Det högnivåanropet tar källkolumnnamnet som en sträng och är den vanligaste vägen. Det lägre nivåanropet accepterar en befintlig `PivotField`-instans och är bekvämt när samma fältobjekt måste återanvändas över flera pivotområden. Båda anropen placerar fältet i `PivotTable.PageFields`, varefter det visas som sidans rullgardinsmeny överst i den renderade pivottabellen.

### Lägga till ett filterfält med AddFieldToArea

Följande exempel bygger ett litet Fruit / Year / Amount-dataset, placerar en pivottabell vid cell E3 med `Fruit` på radområdet, `Amount` på dataområdet och `Year` på filterområdet, uppdaterar pivottabellen och sparar arbetsboken.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Skapa en ny arbetsbok
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Konfigurera rubrikraden
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Fyll i 9 rader med exempeldata: Frukt, År, Belopp
object[,] data = new object[,]
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

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// Lägg till en pivottabell förankrad vid cell E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Lägg till fält i deras områden: Frukt som Rad, Belopp som Data, År som Sidfält
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Uppdatera och beräkna pivottabellens data
pivotTable.CalculateData();

// Spara arbetsboken
workbook.Save("pageFieldSample.xlsx");
```

### Lägga till ett filterfält med PageFields.Add

När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.PageFields.Add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutliga registreringen i filterområdet ersätts med anropet på lägre nivå.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Pivottabellen och sidfältet konstrueras exakt som i
//   Scenario 1a (Frukt/År/Belopp-data, pivot vid E3, Frukt→Rad,
//   Belopp→Data). Nedan hämtar vi År-PivotField från
//   BaseFields-samlingen och skickar den till PageFields.Add — det
//   lågnivåalternativet till AddFieldToArea. Resultatet är
//   funktionellt identiskt med Scenario 1a.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Rubriker
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// Exempeldata (9 rader)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// Lägg till pivottabell vid E3 som täcker A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Frukt -> Rad, Belopp -> Data (År kommer att gå till Sida nedan)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Lågnivåmetod: hämta den befintliga År-PivotField från BaseFields
// och registrera den i Sid-området via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Enkelvalsfiltrering (visa ett sidobjekt)**

I standardbeteendet enkelval renderas filterfältet som en enda rullgardinsmeny och heltalet `PivotField.CurrentPageItem` väljer vilket sidobjekt som styr pivottabellkroppen. Att tilldela ett specifikt index väljer det specifika objektet; att tilldela det speciella sentinelvärdet `0x7FFD` (decimalt 32765) rensar filtret så att varje sidobjekt sammanfattas på en gång. Enkelval är standardinställningen; du behöver inte aktivera det uttryckligen.

### Visa alla objekt

Att sätta `CurrentPageItem` till det magiska värdet `0x7FFD` är likvärdigt med att rensa sidfiltret: pivottabellkroppen sammanfattar varje sidobjekt som om inget filter tillämpades.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // Skapa en ny arbetsbok
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Fylla i data för Frukt/År/Belopp
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // Skapa pivottabell vid E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // Konfigurera pivotfält: Frukt→Rad, Belopp→Data, År→Sida
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.CalculateData();

        // Rensa sidfiltret så att alla objekt i sidfältet syns.
        // 0x7FFD (decimal 32765) är det speciella sentinelvärdet som betyder "alla objekt" —
        // motsvarande att välja "(Alla)" i Excels sidfält-rullmeny.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### Visa ett specifikt objekt

Att sätta `CurrentPageItem` till ett verkligt index väljer bara det ena sidobjektet. Indexet är positionen för objektet i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Skapa arbetsbok
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Lägg till exempeldata (Frukt/År/Belopp)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// Lägg till pivottabell vid E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// Lägg till fält: Frukt→Rad, Belopp→Data, År→Sida
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Sidfältsspecifika operationer
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = andra objektet i sorterad ordning (t.ex. "2021")

// Uppdatera och beräkna pivottabell
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Flervalsfiltrering**

Flervalsfiltrering förvandlar sidans rullgardinsmeny till en kryssrutelista och låter slutanvändaren välja flera sidobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.IsMultipleItemSelectionAllowed` måste sättas till `true` innan flervalsgränssnittet överhuvudtaget får effekt. När det är aktiverat styr `PivotItem.IsHidden` vilka objekt som visas i kryssrutelistan, så du kan antingen visa varje objekt eller vitlista endast specifika objekt.

Koden nedan aktiverar flerval på samma Year-filterfält som byggdes i Scenario 1a, och visar sedan två mönster: Del A avslöjar varje sidobjekt genom att låta `IsHidden` vara satt till `false` för varje post, medan Del B vitlistar endast de källvärden du väljer och döljer allt annat via ett `switch (pivotItems[i].GetStringValue())`-block.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Pivottabellen och sidfältet konstrueras exakt som i
//   Scenario 1a (Fruit/Year/Amount-data, pivot vid E3, Fruit→Rad,
//   Amount→Data, Year→Sida via AddFieldToArea).
//   Nedan tillämpar vi flervalsfiltrering på sidfältet.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Exempeldata: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
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

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — Aktivera flerval på sidfältet
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// Del A — välj ALLA objekt (gör varje objekt synligt)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// Del B — välj endast specifika objekt efter källvärde
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **Obs!** När du använder flervalsfiltrering via `PivotItem.IsHidden` måste **minst en `PivotItem` förbli synlig** (`IsHidden == false`). Om varje objekt är dolt kraschar Excel antingen när filen öppnas eller renderar en tom pivottabell. Verifiera alltid att din flervalsvitlista innehåller minst ett objekt från din källdata.

## **Vilket API och vilket läge bör jag använda?**

Tabellen nedan sammanfattar när du ska använda varje API och läge så att du kan välja rätt kombination utan att läsa varje scenario i detalj.

| Scenario / användningsfall | Rekommenderat API | Använd egenskap | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält via källkolumnnamn (vanligast) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Hög nivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `PivotTable.PageFields.Add(PivotField)` | n/a | Använd när fältobjektet erhölls på annan plats eller behöver återanvändas. |
| Filtrera till ett enskilt sidobjekt (standardläge) | `PivotField.CurrentPageItem` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa sidfiltret | `PivotField.CurrentPageItem` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinelvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.IsMultipleItemSelectionAllowed` | sätt till `true` | Krävs innan några `IsHidden`-anrop får effekt. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.IsHidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`IsHidden == false`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervalsfilterfält är dolt kraschar Excel vid öppning eller renderar en tom pivottabell. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker kommer att öppnas tillförlitligt på varje maskin.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
