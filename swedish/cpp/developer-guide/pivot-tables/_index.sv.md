---
title: Skapa pivottabell
linktitle: Skapa pivottabell
description: Skapa och formatera pivottabeller med Aspose.Cells for C++.
keywords: Skapa pivottabell, infoga pivottabell, formatera pivottabell.
type: docs
weight: 160
url: /sv/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den komprimerar ett stort block med rådata i radvis form till en kompakt matris utan en enda formel. Du bestämmer vilka kolumner som ska användas som radetiketter, vilka som ska användas som kolumnetiketter och vilka som ska aggregeras som värden – pivottabellen utför både grupperingen och beräkningen:
- **Sammanfatta** – total försäljning per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder på kolumnerna gör en platt lista till en korsrapport där trender blir uppenbara.
- **Visa detaljer** – dubbelklicka på valfritt sammanfattningsvärde för att granska källraderna bakom värdet.
- **Uppdatera** – när källdatan ändras räknas hela rapporten om med en enda uppdatering.
Vanliga användningsfall är säljdashboards, kostnadsfördelningar och lageranalys – alla frågor av typen ”hur fördelas dessa siffror per kategori och tid?”. I Aspose.Cells for C++ skapas en pivottabell med hjälp av metoden [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) i ett kalkylblad. När pivottabellen har skapats kan du arbeta med den via klassen [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/).

## **Skapa pivottabell**
Exempelkoden nedan visar hur du skapar en pivottabell och arbetar med den. Kontrollera [utdatafilen i Excel](23167010.xlsx) som genereras med koden nedan. Den följande skärmbilden visar utdatafilen i Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **Exempelkod**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Skapa en ny arbetsbok och hämta det första kalkylbladet
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Skriv källdata: försäljning per sport och kvartal
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // Lägg till en pivottabell vid destinationscellen E3, med A1:C8 som källa
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Tilldela pivotfält: Sport till rader, Quarter till kolumner och Sales till data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Spara arbetsboken
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}