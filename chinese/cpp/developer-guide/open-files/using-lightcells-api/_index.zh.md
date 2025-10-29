---
title: 使用 LightCells API 与 C++
linktitle: 使用 LightCells API
type: docs
weight: 160
url: /zh/cpp/using-lightcells-api/
description: 学习如何在 C++ 中使用 LightCells API 高效读取和写入大型 Excel 文件，且内存占用极少。
---

{{% alert color="primary" %}} 

有时您需要读写大量数据或工作表中的大量内容的大型Microsoft Excel文件。LightCells API 用于创建巨大的Excel电子表格非常有用：使用它，您需要更少的内存，并获得更好的性能和效率。

{{% /alert %}} 

# 事件驱动架构
Aspose.Cells 提供 LightCells API，主要设计用于逐个处理单元格数据，而无需将完整的数据模型块（使用 Cell 集合等）构建到内存中。它以事件驱动模式工作。

在保存工作簿时，保存组件会直接提供逐个单元格的单元格内容，然后将其保存到输出文件。

在读取模板文件时，组件会解析每个单元格，并逐个提供它们的值。

在这两个过程中，处理一个 Cell 对象然后丢弃它，Workbook 对象不会保留集合。因此，在导入和导出具有大数据集的 Microsoft Excel 文件时，将节省内存。

即使 LightCells API 在 XLSX 和 XLS 文件上以相同的方式处理单元格（它实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），但它对于 XLSX 文件比 XLS 文件更有效地节省内存，因为这两种格式的数据模型和结构不同。

但是，**对于 XLS 文件**，为了节省更多内存，开发人员可以指定在保存过程中保存生成的临时数据的临时位置。通常情况下，**使用 LightCells API 保存 XLSX 文件可能节省50%或更多内存**，**保存 XLS 可能节省大约20-40%内存**。

## 写一个大型的Excel文件
Aspose.Cells 提供接口 `LightCellsDataProvider`，需要在程序中实现该接口。该接口代表用于以轻量级模式保存大型电子表格文件的数据提供者。

使用此模式保存工作簿时，每次保存工作表时都会检查 `StartSheet(int)`。如果返回 true，则会调用此实现提供该工作表所有行列的所有数据和属性。在保存每一行时，都会调用 `NextRow()` 获取下一行的索引。如果返回有效行索引（行索引必须按递增顺序），则会调用 `StartRow(Row)` 以设置该行的属性。如需处理特定行，还可以调用 `ProcessRow`。

对于某一行，优先检查 `NextCell()`。如果返回有效列索引（列索引必须按递增顺序），则提供代表该单元格的 `Cell` 对象，供实现设置其数据和属性，调用 `StartCell(Cell)`。设置完后，单元格会直接保存到生成的电子表格文件中，接着检查并处理下一个单元格。

### 写入大型Excel文件示例
请查看以下示例代码，了解LightCells API的工作方式。根据您的需求添加和删除或更新代码段。

程序在工作表中创建一个包含10,000（10000x30矩阵）记录的大文件，并用虚拟数据填充。您可以通过修改 `Main()` 方法中的 `rowsCount` 和 `colsCount` 变量来指定不同的矩阵大小。

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

## 读取大型Excel文件
Aspose.Cells 提供接口 `LightCellsDataHandler`，需要在程序中实现。该接口表示用于读取大型电子表格文件的轻量级数据提供者。

在以轻量模式读取工作簿时，每次读取工作表时都会检查 `StartSheet`。如果返回 true，则会查阅和处理该工作表所有行列的单元格数据和属性。每处理一行时，都会调用 `StartRow`，判断是否需要处理该行。如果需要，则读取其属性以供处理。若该行的单元格也需要处理，则调用 `ProcessRow`。如果返回 true，则对每个存在的单元格调用 `StartCell`，判断是否需要处理该单元格。若需要，则调用 `ProcessCell`。

### 读取大型Excel文件示例
请查看以下示例代码，了解LightCells API的工作方式。根据您的需求添加和删除或更新代码段。

该程序读取一个worksheet中的数百万条记录的大文件。每个工作表的读取都需要一些时间。示例代码读取文件并检索每个工作表中的单元格总数，字符串计数和公式计数。

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
{{< app/cells/assistant language="cpp" >}}
