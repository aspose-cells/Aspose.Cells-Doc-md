---
title: Реализовать подписи подытогов или итогов в других языках с помощью C++
linktitle: Реализуйте метки Подитог или Итог в других языках
type: docs
weight: 50
url: /ru/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Узнайте, как реализовать подписи подытогов и итогов на нерусском языке с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда вам нужно отображать подписи подытогов и итогов на нерусском языке, например, на китайском, японском, арабском, хинди и т.д. Aspose.Cells позволяет делать это, используя класс [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) и свойство [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). См. эту статью, чтобы узнать, как использовать класс [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/):

- [Использование класса GlobalizationSettings для пользовательских меток итогов и других меток круговой диаграммы](/cells/ru/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## ** Реализуйте метки Подитог или Итог в других языках**

Следующий пример кода загружает [пробный файл Excel](5115151.xlsx) и реализует имена подытогов и итогов в китайском языке. Пожалуйста, ознакомьтесь с [выходным файлом Excel](5115152.xlsx), созданным этим кодом, для вашего ознакомления. Сначала мы создаем класс типа [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/), а затем используем его в нашем коде.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

Теперь используйте созданный выше класс в коде следующим образом:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
