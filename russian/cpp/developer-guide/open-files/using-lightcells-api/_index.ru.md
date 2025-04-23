---
title: Использование API LightCells с C++
linktitle: Использование API LightCells
type: docs
weight: 160
url: /ru/cpp/using-lightcells-api/
description: Узнайте, как использовать API LightCells в C++ для эффективного чтения и записи больших файлов Excel с минимальным использованием памяти.
---

{{% alert color="primary" %}} 

Иногда вам необходимо читать и записывать большие файлы Microsoft Excel с огромным списком данных или контента на листе. API LightCells полезен для создания больших электронных таблиц Excel: благодаря этому, требуется меньше памяти, и достигается лучшая производительность и эффективность.

{{% /alert %}} 

# Архитектура, основанная на событиях
Aspose.Cells предоставляет API LightCells, преимущественно предназначенный для манипулирования данными ячейки одна за другой без построения полной модели данных (используя коллекцию Cell и т. д.) в памяти. Он работает в режиме событийного управления.

Для сохранения рабочих книг предоставьте содержание ячейки по ячейке при сохранении, и компонент сохранит его непосредственно в выходной файл.

При считывании файлов-шаблонов компонент анализирует каждую ячейку и предоставляет их значение по одной.

В обоих процедурах обрабатывается один объект ячейки, а затем он удаляется, объект Workbook не хранит коллекцию. В этом режиме, следовательно, память экономится при импорте и экспорте файлов Microsoft Excel с большим набором данных, который иначе использовал бы много памяти.

Несмотря на то, что API LightCells обрабатывает ячейки одинаково для файлов XLSX и XLS (он на самом деле не загружает все ячейки в память, а обрабатывает одну ячейку, а затем удаляет ее), он более эффективно экономит память для файлов XLSX, чем для файлов XLS из-за разных моделей данных и структур двух форматов.

Однако **для файлов XLS** для экономии памяти разработчики могут указать временное местоположение для сохранения временных данных, генерируемых в процессе сохранения. Обычно **использование API LightCells для сохранения файла XLSX может сэкономить 50% или более памяти** по сравнению с обычным способом, **сохранение XLS может сэкономить от 20 до 40% памяти**.

## Создание большого файла Excel
Aspose.Cells предоставляет интерфейс `LightCellsDataProvider`, который необходимо реализовать в вашей программе. Этот интерфейс представляет собой поставщика данных для сохранения больших файлов таблиц в легком режиме.

При сохранении рабочей книги в этом режиме проверяется `StartSheet(int)` при сохранении каждого листа рабочей книги. Для одного листа, если `StartSheet(int)` возвращает true, то все данные и свойства строк и ячеек этого листа предоставляются этой реализацией. В первую очередь вызывается `NextRow()`, чтобы получить следующий индекс строки для сохранения. Если возвращается действительный индекс строки (индекс строки должен быть в порядке возрастания для сохраняемых строк), то для реализации предоставляется объект `Row`, представляющий эту строку, для установки его свойств с помощью `StartRow(Row)`.

Для одной строки сначала проверяется `NextCell()`. Если возвращается действующий индекс столбца (индекс столбца должен быть в порядке возрастания для всех ячеек одной строки), то для реализации предоставляется объект `Cell`, представляющий эту ячейку, для установки данных и свойств с помощью `StartCell(Cell)`. После установки данных ячейки ячейка сохраняется напрямую в создаваемом файле таблицы, и далее проверяется и обрабатывается следующая ячейка.

### Запись большого Excel-файла: пример
Пожалуйста, ознакомьтесь со следующим образцовым кодом, чтобы увидеть работу API LightCells. Добавьте, удалите или обновите сегменты кода в соответствии с вашими потребностями.

Программа создает огромный файл с **10 000 (матрица 10000x30) записей** на листе и заполняет их тестовыми данными. Вы можете указать свою матрицу, изменяя переменные `rowsCount` и `colsCount` в методе `Main()`.

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

## Чтение больших файлов Excel
Aspose.Cells предоставляет интерфейс `LightCellsDataHandler`, который необходимо реализовать в вашей программе. Этот интерфейс представляет поставщика данных для чтения больших файлов таблиц в легком режиме.

При чтении рабочей книги в этом режиме проверяется `StartSheet` при чтении каждого листа. Для листа, если `StartSheet` возвращает true, все данные и свойства ячеек в строках и столбцах листа проверяются и обрабатываются этой реализацией. Для каждой строки вызывается `StartRow` для проверки необходимости обработки. Если строка должна быть обработана, её свойства сначала считываются, и разработчик может получить к ним доступ через `ProcessRow`. Если ячейки строки также нужно обработать, тогда `ProcessRow` возвращает true, и для каждой существующей ячейки строки вызывается `StartCell`, чтобы определить, нужно ли обрабатывать ячейку. Если обработка ячейки необходима, вызывается `ProcessCell`.

### Чтение больших Excel-файлов: пример
Пожалуйста, ознакомьтесь со следующим образцовым кодом, чтобы увидеть работу API LightCells. Добавьте, удалите или обновите сегменты кода в соответствии с вашими потребностями.

Программа считывает огромный файл с миллионами записей в листе Excel. На чтение каждого листа в книге требуется небольшое время. Ознакомьтесь с образцовым кодом чтения файла и получения общего количества ячеек, количества строк и формул в каждом листе.

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
