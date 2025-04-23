---
title: Använder LightCells API med C++
linktitle: Användning av LightCells API
type: docs
weight: 160
url: /sv/cpp/using-lightcells-api/
description: Lär dig hur man använder LightCells API i C++ för att effektivt läsa och skriva stora Excel filer med minimal minnesanvändning.
---

{{% alert color="primary" %}} 

Ibland behöver du läsa och skriva stora Microsoft Excel-filer med en stor lista över data eller innehåll i kalkylarket. LightCells API är användbart för att skapa stora Exceldokument: med det behöver du mindre minne och får bättre prestanda och effektivitet.

{{% /alert %}} 

# Event Driven Architecture
Aspose.Cells tillhandahåller LightCells API, främst utformat för att manipulera celldata en i taget utan att bygga en komplett datamodellblock (med hjälp av Cell-samlingen etc.) i minnet. Det fungerar i ett händelsestyrt läge.

För att spara arbetsböcker, ange cellinnehållet cell för cell vid sparande, och komponenten sparar det till utdatafilen direkt.

När du läser mallfiler parsa komponenten varje cell och tillhandahåller deras värde en i taget.

I båda procedurerna bearbetas sedan en Cell-objekt och kastas sedan bort, Workbook-objektet håller inte samlingen. I detta läge sparas därför minnet när Microsoft Excel-fil med en stor datamängd importeras och exporteras, vilket annars skulle använda mycket minne.

Även om LightCells API bearbetar cellerna på samma sätt för XLSX- och XLS-filer (det läser inte faktiskt in alla celler i minnet utan bearbetar en cell och kastar sedan bort den), sparar det minnet effektivare för XLSX-filer än XLS-filer på grund av de olika datamodellerna och strukturerna för de två formaten.

För **XLS-filer** kan utvecklare dock för att spara minne specificera en temporär plats för att spara temporära data som genereras under sparandeprocessen. Vanligtvis kan **användning av LightCells API för att spara XLSX-fil spara 50 % eller mer minne** än att använda det vanliga sättet, **sparande XLS-fil kan spara cirka 20-40 % minne**.

## Skriver en stor Excel-fil
Aspose.Cells erbjuder ett gränssnitt, `LightCellsDataProvider`, som måste implementeras i ditt program. Gränssnittet representerar dataleverantören för att spara stora kalkylbladsfiler i lättviktläge.

När du sparar en arbetsbok med detta läge, kontrolleras `StartSheet(int)` när varje arbetsblad i arbetsboken sparas. För ett blad, om `StartSheet(int)` är sant, tillhandahålls all data och egenskaper för rader och celler i detta blad av denna implementation. Först, kallas `NextRow()` för att få nästa radindex att spara. Om ett giltigt radindex returneras (radens index måste vara i stigande ordning för raderna som ska sparas), tillhandahålls ett `Row`-objekt som representerar denna rad för att ställa in dess egenskaper med `StartRow(Row)`.

För en rad, kontrolleras först `NextCell()`. Om ett giltigt kolumnindex returneras (kolumnindex måste vara i stigande ordning för alla celler i en rad för att sparas), tillhandahålls ett `Cell`-objekt som representerar den cellen för implementation att ställa in dess data och egenskaper med `StartCell(Cell)`. Efter att cellens data har ställts in, sparas cellen direkt till den genererade kalkylbladsfilen och nästa cell kontrolleras och bearbetas.

### Skriv ut en stor Excel-fil: Exempel
Se följande exempelkod för att se arbete med LightCells API. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.

Programmet skapar en enorm fil med **10 000 (10000x30 matris) poster** i ett kalkylblad och fyller dem med dummy-data. Du kan specificera din egen matris genom att ändra variablerna `rowsCount` och `colsCount` i `Main()`-metoden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Läs stora Excel-filer
Aspose.Cells ger ett gränssnitt, `LightCellsDataHandler`, som behöver implementeras i ditt program. Gränssnittet representerar Data-leverantör för att läsa stora kalkylbladsfiler i lättviktsläge.

När du läser en arbetsbok i detta läge, kontrolleras `StartSheet` när varje arbetsblad i arbetsboken läses. För ett blad, om `StartSheet` returnerar true, kontrolleras och bearbetas all data och egenskaper för cellerna i rader och kolumner i bladet av denna gränssnittsimplementation. För varje rad, kallas `StartRow` för att kontrollera om den ska bearbetas. Om en rad ska bearbetas, läses dess egenskaper först och utvecklaren kan komma åt dess egenskaper med `ProcessRow`. Om radens celler också ska bearbetas, bör `ProcessRow` returnera true och `StartCell` kallas för varje befintlig cell i raden för att kontrollera om en cell ska bearbetas. Om en cell ska bearbetas, kallas `ProcessCell` för att bearbeta cellen genom denna gränssnittsimplementation.

### Läsa stora Excel-filer: Exempel
Se följande exempelkod för att se arbete med LightCells API. Lägg till och ta bort eller uppdatera kodsegmenten enligt dina behov.

Programmet läser en stor fil med miljontals poster i ett kalkylblad. Det tar lite tid att läsa varje blad i arbetsboken. Exempelkoden läser filen och hämtar det totala antalet celler, antalet strängar och antalet formler i varje kalkylblad.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
