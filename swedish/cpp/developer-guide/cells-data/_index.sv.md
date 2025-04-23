---
title: Hantera data i Excel filer med C++
linktitle: Cellers data
type: docs
weight: 110
url: /sv/cpp/view-and-edit-excel-data/
description: Denna artikel beskriver hur man visar och redigerar data i Excel filer med Aspose.Cells biblioteket med C++.
keywords: Aspose.Cells C++ Hantera data i Excel fil, lägg till data i Excel fil, hämta data från Excel fil, hur man förbättrar effektiviteten vid tillägg av data, hantera celldata, uppdatera celldata, hämta celldata, infoga celldata
---

{{% alert color="primary" %}}

I [Åtkomst till celler i ett kalkylblad](/cells/sv/cpp/accessing-cells-of-a-worksheet/), diskuterade vi grundläggande tillvägagångssätt för att komma åt celler på ett kalkylblad. Den här artikeln använder en av dessa tillvägagångssätt för att lägga till olika typer av data i celler.

{{% /alert %}}

## **Hur man lägger till data i celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en samling av typen [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en samling av typen [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Varje objekt i samlingen [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representerar en instans av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells möjliggör för utvecklare att lägga till data i cellerna i arbetsblad genom att anropa metoden [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) i klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Aspose.Cells tillhandahåller överbelastade versioner av metoden [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) som låter utvecklare lägga till olika typer av data i cellerna. Genom att använda dessa överbelastade versioner av metoden [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) är det möjligt att lägga till en boolean, sträng, dubbel, heltal eller datum/tid, etc. värden till cellen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Hur man förbättrar effektiviteten**

Om du använder metoden [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) för att lägga till en stor mängd data i ett arbetsblad, bör du först lägga till värden i cellerna rad för rad och sedan kolumn för kolumn. Detta tillvägagångssätt förbättrar avsevärt effektiviteten för dina applikationer.

## **Hur man hämtar data från celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en samling av typen [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som möjliggör åtkomst till arbetsbladen i filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en samling av typen [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Varje objekt i samlingen [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representerar en instans av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) tillhandahåller flera egenskaper som låter utvecklare hämta värden från cellerna enligt deras datatyper. Dessa egenskaper inkluderar:

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): returnerar cellens strängvärde.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): returnerar cellens dubbelvärde.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): returnerar cellens booleanvärde.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): returnerar cellens datum/tid-värde.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): returnerar cellens flyttalsvärde.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): returnerar cellens heltalsvärde.

När en värdetyp inte är ifylld, kastar celler med [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) eller [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) ett undantag.

Datatypen som finns i en cell kan också kontrolleras genom att använda egenskapen [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) i klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Faktum är att egenskapen [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) i klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) är baserad på uppräkningen [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) vars fördefinierade värden listas nedan:

|**Cellvärdestyper**|**Beskrivning**|
| :- | :- |
|IsBool| Specificerar att cellvärdet är Booleskt.
|IsDateTime| Specificerar att cellvärdet är datum/tid.
|IsNull| Representerar en tom cell.
|IsNumeric| Specificerar att cellvärdet är numeriskt.
|IsString| Specificerar att cellvärdet är en sträng.
|IsUnknown| Specificerar att cellvärdet är okänt.

Du kan också använda ovanstående fördefinierade cellvärdestyper för att jämföra med datatypen som finns i varje cell.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

När man arbetar med arbetsblad kan användare lägga till olika typer av data i cellerna. Dessa datatyper kan inkludera booleska, heltal, flyttal, text eller datum/tid-värden. Med Aspose.Cells kan du hämta lämpliga värden från cellerna enligt deras datatyper.

{{% /alert %}}

## **Fortsatta ämnen**
- [Tillgång till celler i ett arbetsblad](/cells/sv/cpp/accessing-cells-of-a-worksheet/)
- [Konvertera text numerisk data till nummer](/cells/sv/cpp/convert-text-numeric-data-to-number/)
- [Skapa delsummering](/cells/sv/cpp/creating-subtotals/)
- [Datafiltrering](/cells/sv/cpp/data-filtering/)
- [Data sortering](/cells/sv/cpp/sort-data-of-excel/)
- [Data validering](/cells/sv/cpp/data-validation/)
- [Hitta eller Sök Data](/cells/sv/cpp/find-or-search-data/)
- [Få cellsträngvärde med och utan formatering](/cells/sv/cpp/get-cell-string-value-with-and-without-formatting/)
- [Lägg till HTML Rich Text i cellen](/cells/sv/cpp/adding-html-rich-text-inside-the-cell/)
- [Infoga hyperlänkar i Excel eller OpenOffice](/cells/sv/cpp/insert-hyperlinks-to-excel/)
- [Hur och var man använder uppräknare](/cells/sv/cpp/how-and-where-to-use-enumerators/)
- [Mät bredden och höjden på cellvärdet i enheten pixlar](/cells/sv/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Läsa cellvärden i flera trådar samtidigt](/cells/sv/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertering mellan cellnamn och rad/kolumnindex](/cells/sv/cpp/names-and-indices/)
- [Fylla data först per rad och sedan per kolumn](/cells/sv/cpp/populate-data-first-by-row-then-by-column/)
- [Bevara enskild citattecken prefiks av cellvärde eller område](/cells/sv/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Åtkomst och uppdatering av delar av riktad text från cellen](/cells/sv/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
