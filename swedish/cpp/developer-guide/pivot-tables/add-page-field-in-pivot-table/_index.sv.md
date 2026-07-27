---
title: Lägga till filterfält i en pivottabell i Aspose.Cells för .NET
linktitle: Lägga till filterfält
description: Lär dig hur du lägger till och konfigurerar filterfält i pivottabeller med Aspose.Cells for C++, inklusive att lägga till filterfält, envalsfiltrering och flervalsfiltrering.
keywords: Aspose.Cells, C++, pivottabell, filterfält, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filter
type: docs
weight: 250
url: /sv/cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder hela livscykeln för filterfält i pivottabeller. Du kan lägga till ett filterfält via ett bekvämt högnivå-API eller via den lägre nivåns `PageFields`-samling, och du kan driva sidfiltret i envalsläge, rensa det för att visa alla sidobjekt, eller växla fältet till flerval så att användare kan välja flera sidobjekt samtidigt via kryssrutegränssnittet i Excel.
{{% /alert %}}

## **Introduktion**

Ett filterfält är ett pivotfält som styr *vilken delmängd* av källdatan pivotkroppen visar. Slutanvändare ser det som en rullgardinsmeny längst upp i en renderad pivot i Excel, och att välja ett av de tillgängliga sidobjekten bygger om pivotkroppen så att endast posterna som hör till det sidobjektet sammanfattas. Ett pivotfält blir ett filterfält när det registreras som `PivotFieldType.Page` snarare än `PivotFieldType.Row`, `PivotFieldType.Column` eller `PivotFieldType.Data`.

Ett filterfält kan fungera i två beteenden. I standardbeteendet **envals** är endast ett sidobjekt synligt åt gången, så pivotkroppen sammanfattar exakt en delmängd. I beteendet **flervals** exponerar fältet en kryssrutelista, och pivotkroppen sammanfattar föreningen av varje ikryssat sidobjekt. Samma källfält kan flyttas fram och tillbaka mellan dessa beteenden genom att växla en enskild egenskap.

Aspose.Cells for C++ exponerar två likvärdiga sätt att registrera ett filterfält. Det högnivå-API:et är `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, som tar källkolumnens namn och lägger till fältet i ett enda anrop. Det lägre nivåns API är `PivotTable.PageFields.Add(PivotField)`, som används när du redan har en `PivotField`-referens och vill lägga till samma fältinstans i filterområdet. Båda API:erna fyller slutligen samma `PageFields`-samling, och resten av den här artikeln visar hur du väljer mellan dem och hur du driver varje filtreringsläge.

## **Lägga till ett filterfält**

Det finns två sätt att registrera ett pivotfält i filterområdet. Högnivåanropet tar källkolumnens namn som en sträng och är den vanligaste vägen. Anropet på lägre nivå accepterar en befintlig `PivotField`-instans och är bekvämt när samma fältobjekt måste återanvändas i flera pivotområden. Båda anropen placerar fältet i `PivotTable.PageFields`, varefter det visas som sidans rullgardinsmeny längst upp i den renderade pivottabellen.

### Lägga till ett filterfält med AddFieldToArea

Följande exempel bygger en liten datamängd med Fruit / Year / Amount, placerar en pivottabell vid cell E3 med `Fruit` på radområdet, `Amount` på dataområdet och `Year` på filterområdet, uppdaterar pivoten och sparar arbetsboken.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // Skapa en ny arbetsbok
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();

    // Ställ in rubrikraden
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Fyll i 9 rader med exempeldata: Frukt, År, Belopp
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // Lägg till en pivottabell förankrad vid cell E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Lägg till fält i deras områden: Fruit som Rad, Amount som Data, Year som Sidfält
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // Uppdatera och beräkna pivottabellens data
    pivotTable.CalculateData();

    // Spara arbetsboken
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Lägga till ett filterfält med PageFields.Add

När du redan arbetar med en `PivotField`-instans kan du skicka den direkt till `PivotTable.PageFields.Add`. Pivottabellen och filterfältet konstrueras exakt som i föregående scenario; endast den slutliga registreringen i filterområdet ersätts med API-anropet på lägre nivå.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Rubriker
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Exempeldata (9 rader)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // Lägg till pivottabell vid E3 som täcker A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Frukt -> Rad, Belopp -> Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // Lågnivåstrategi: hitta det befintliga år-PivotField i BaseFields
    // och registrera det i sidområdet via PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // Uppdatera så att det nya sidfältet återspeglas i den sparade arbetsboken
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Envalsfiltrering (visa ett sidobjekt)**

I standardbeteendet för envals återges filterfältet som en enskild rullgardinsmeny och heltalet `PivotField.CurrentPageItem` väljer vilket sidobjekt som driver pivotkroppen. Att tilldela ett specifikt index väljer det objektet; att tilldela det speciella sentinelvärdet `0x7FFD` (decimalt 32765) rensar filtret så att alla sidobjekt sammanfattas på en gång. Envals är standard; du behöver inte aktivera det explicit.

### Visa alla objekt

Att ställa in `CurrentPageItem` till det magiska värdet `0x7FFD` är likvärdigt med att rensa sidfiltret: pivotkroppen sammanfattar varje sidobjekt som om inget filter tillämpades.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};

    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Visa ett specifikt objekt

Att ställa in `CurrentPageItem` till ett verkligt index väljer bara det sidobjektet. Indexet är objektets position i filterfältets sorterade objektlista, så till exempel `1` väljer det andra objektet efter sortering.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Flervalsfiltrering**

Flervalsfiltrering förvandlar sidans rullgardinsmeny till en kryssrutelista och låter slutanvändaren välja flera sidobjekt samtidigt. Aspose.Cells exponerar två egenskaper som fungerar tillsammans. `PivotField.IsMultipleItemSelectionAllowed` måste ställas in på `true` innan flervalsgränssnittet överhuvudtaget träder i kraft. När det är aktiverat styr `PivotItem.IsHidden` vilka objekt som visas i kryssrutelistan, så att du antingen kan visa varje objekt eller vitlista endast specifika objekt.

Koden nedan aktiverar flerval på samma Year-filterfält som byggdes i Scenario 1a, och visar sedan två mönster: Del A avslöjar varje sidobjekt genom att låta `IsHidden` vara satt till `false` för varje post, medan Del B vitlistar endast de källvärden du väljer och döljer allt annat via ett `switch (pivotItems[i].GetStringValue())`-block.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Exempeldata: Frukt | År | Belopp
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");

    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };

    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }

    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — Aktivera flerval på sidfältet
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // Del A — välj ALLA objekt (gör varje objekt synligt)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // Del B — välj endast specifika objekt efter källvärde
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Obs:** När du använder flervalsfiltrering via `PivotItem.IsHidden`, **måste minst en `PivotItem` förbli synlig** (`IsHidden == false`). Om varje objekt är dolt kraschar antingen Excel när filen öppnas eller så renderas en tom pivot. Verifiera alltid att din flervalsvitlista innehåller minst ett objekt från din källdata.

## **Vilket API och vilket läge ska jag använda?**

Tabellen nedan sammanfattar när du ska använda respektive API och läge, så att du kan välja rätt kombination utan att läsa varje scenario i detalj.

| Scenario / Användningsfall | Rekommenderat API | Använd egenskap | Anteckningar |
|---|---|---|---|
| Lägg till ett filterfält via källkolumnens namn (vanligaste) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Högnivå, en rad. Använd detta om du inte behöver en `PivotField`-referens. |
| Lägg till ett filterfält när du redan har ett `PivotField`-objekt | `PivotTable.PageFields.Add(PivotField)` | n/a | Använd när fältobjektet har hämtats någon annanstans eller behöver återanvändas. |
| Filtrera till ett enskilt sidobjekt (standardläge) | `PivotField.CurrentPageItem` | sätt till ett specifikt index | Till exempel visar `1` det andra objektet i den sorterade listan. |
| Visa alla objekt / rensa sidfiltret | `PivotField.CurrentPageItem` | sätt till `0x7FFD` | Det magiska värdet `0x7FFD` (decimalt 32765) är sentinelvärdet för "alla objekt". |
| Aktivera flervalsgränssnitt i Excel | `PivotField.IsMultipleItemSelectionAllowed` | sätt till `true` | Krävs innan några `IsHidden`-anrop träder i kraft. |
| Dölj / visa enskilda objekt i en flervalslista | `PivotItem.IsHidden` | sätt per objekt | Minst ett objekt måste förbli synligt (`IsHidden == false`). |

{{% alert color="primary" %}}
Kom alltid ihåg synlighetsbegränsningen när du konfigurerar flervalsfiltrering. Om varje `PivotItem` i ett flervalsfilterfält är dolt, kraschar Excel vid öppning eller renderar en tom pivot. Bygg din vitlista mot din källdata så att minst ett objekt förblir synligt, och dina sparade arbetsböcker öppnas tillförlitligt på varje maskin.
{{% /alert %}}



{{< app/cells/assistant language="cpp" >}}
