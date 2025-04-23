---
title: Добавить ячейки в окно наблюдения формул Microsoft Excel с помощью C++
linktitle: Добавить ячейки в окно наблюдения формул
description: Узнайте, как использовать Aspose.Cells for C++ для добавления ячеек в окно наблюдения формул в Excel. Загрузите или создайте файл Excel, манипулируйте ячейками, задавайте формулы и сохраните изменённый файл.
keywords: Aspose.Cells, Excel, окно наблюдения формул, ячейки, добавление, C++
type: docs
weight: 60
url: /ru/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Возможные сценарии использования**

Окно наблюдения в Microsoft Excel — это полезный инструмент для удобного мониторинга значений ячеек и их формул в окне. Вы можете открыть *Окно наблюдения* в Microsoft Excel, выбрав *Формулы > Окно наблюдения*. В нем есть кнопка *Добавить наблюдение*, которая используется для добавления ячеек для проверки. Аналогично, вы можете использовать метод [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) для добавления ячеек в *Окно наблюдения* с помощью API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

Следующий пример кода устанавливает формулу ячеек C1 и E1 и добавляет обе ячейки в окно наблюдения. Затем он сохраняет книгу как [выходной файл Excel](67338481.xlsx). Если вы откроете выходной файл Excel и посмотрите *Окно наблюдения*, вы увидите обе ячейки, как показано на этом скриншоте.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
