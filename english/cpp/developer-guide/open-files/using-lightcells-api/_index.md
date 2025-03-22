---
title: Using LightCells API with C++
linktitle: Using LightCells API
type: docs
weight: 160
url: /cpp/using-lightcells-api/
description: Learn how to use the LightCells API in C++ to efficiently read and write large Excel files with minimal memory usage.
---

{{% alert color="primary" %}} 

Sometimes you need to read and write large Microsoft Excel files with a huge list of data or content in the worksheet. The LightCells API is useful for creating huge Excel spreadsheets: with it, you need less memory and get better performance and efficiency.

{{% /alert %}} 

# Event Driven Architecture
Aspose.Cells provides the LightCells API, mainly designed to manipulate cell data one by one without building a complete data model block (using the Cell collection etc.) into memory. It works in an event-driven mode.

To save workbooks, provide the cell content cell by cell when saving, and the component saves it to the output file directly.

When reading template files, the component parses every cell and provides their value one by one.

In both procedures, one Cell object is processed and then discarded, the Workbook object does not hold the collection. In this mode, therefore, memory is saved when importing and exporting Microsoft Excel file that has a large data set which would otherwise use a lot of memory.

Even though the LightCells API processes the cells in the same way for XLSX and XLS files (it does not actually load all cells in memory but processes one cell and then discards it), it saves memory more effectively for XLSX files than XLS files because of the different data models and structures of the two formats.

However, **for XLS files**, to save more memory, developers can specify a temporary location for saving temporary data generated during the Save process. Commonly, **using LightCells API to save XLSX file may save 50% or more memory** than using the common way, **saving XLS may save about 20-40% memory**.

## Writing a Large Excel File
Aspose.Cells provides an interface, `LightCellsDataProvider`, that needs to be implemented in your program. The interface represents the data provider for saving large spreadsheet files in light-weight mode.

When saving a workbook by this mode, `StartSheet(int)` is checked when saving every worksheet in the workbook. For one sheet, if `StartSheet(int)` is true, then all the data and properties of rows and cells of this sheet to be saved is provided by this implementation. In the first place, `NextRow()` is called to get the next row index to be saved. If a valid row index is returned (the row index must be in ascending order for the rows to be saved), then a `Row` object representing this row is provided for implementation to set its properties by `StartRow(Row)`.

For one row, `NextCell()` is checked first. If a valid column index is returned (the column index must be in ascending order for all cells of one row to be saved), then a `Cell` object representing that cell is provided for implementation to set its data and properties by `StartCell(Cell)`. After the data of the cell is set, the cell is saved directly to the generated spreadsheet file and the next cell is checked and processed.

### Writing a Large Excel File: Example
Please see the following sample code to see the working of the LightCells API. Add and remove, or update the code segments according to your needs.

The program creates a huge file with **10,000 (10000x30 matrix) records** in a worksheet and fills them with dummy data. You can specify your own matrix by changing the `rowsCount` and `colsCount` variables in the `Main()` method.

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

## Reading Large Excel Files
Aspose.Cells provides an interface, `LightCellsDataHandler`, that needs to be implemented in your program. The interface represents Data provider for reading large spreadsheet files in light-weight mode.

When reading a workbook in this mode, `StartSheet` is checked when reading every worksheet in the workbook. For a sheet, if `StartSheet` returns true, then all the data and properties of the cells in rows and columns of the sheet are checked and processed by the implementation of this interface. For every row, `StartRow` is called to check whether it needs to be processed. If a row needs to be processed, its properties are read first and the developer can access its properties with `ProcessRow`. If the row's cells also need to be processed, then `ProcessRow` should return true and then `StartCell` is called for every existing cell in the row to check whether one cell needs to be processed. If one cell needs to be processed, then `ProcessCell` is called to process the cell by the implementation of this interface.

### Reading Large Excel Files: Example
Please see the following sample code to see the working of the LightCells API. Add and remove, or update the code segments according to your needs.

The program reads a huge file with millions of records in a worksheet. It takes a little time to read each sheet in the workbook. The sample code reads the file and retrieves the total number of cells, the string count and formula count in each worksheet.

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