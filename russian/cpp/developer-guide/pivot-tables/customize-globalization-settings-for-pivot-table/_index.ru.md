---
title: Настройка глобальных настроек локализации для сводной таблицы с C++
linktitle: Настройка глобализации для сводной таблицы
type: docs
weight: 50
url: /ru/cpp/customize-globalization-settings-for-pivot-table/
description: Научитесь настраивать параметры глобализации сводной таблицы с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда вам нужно настроить текст *Общая сумма по сводной, Итоговая сумма, Общий итог, Все элементы, Несколько элементов, Метки столбцов, Метки строк, Пустые значения* в соответствии с вашими требованиями. Aspose.Cells for C++ позволяет настраивать параметры глобализации сводной таблицы для подобных сценариев. Вы также можете использовать эту функцию для изменения ярлыков на другие языки, такие как арабский, хинди, польский и др.

## **Настройка глобализации для сводной таблицы**

Следующий пример кода показывает, как настроить параметры глобализации для сводной таблицы на C++. Создается класс *CustomPivotTableGlobalizationSettings*, унаследованный от базового класса [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.settings/pivotglobalizationsettings/), и переопределяются все необходимые методы. Эти методы возвращают настроенный текст для различных элементов сводной таблицы. Затем эта реализация присваивается свойству [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). Пример загружает [исходный файл Excel](40468488.xlsx), обновляет данные сводной таблицы и сохраняет его как [выходной PDF](40468487.pdf). Ниже изображение с настройками ярлыков в выходном файле.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomPivotTableGlobalizationSettings : public PivotGlobalizationSettings {
public:
    virtual U16String GetTextOfTotal() override {
        std::cout << "---------GetPivotTotalName-------------" << std::endl;
        return u"AsposeGetPivotTotalName";
    }

    virtual U16String GetTextOfGrandTotal() override {
        std::cout << "---------GetPivotGrandTotalName-------------" << std::endl;
        return u"AsposeGetPivotGrandTotalName";
    }

    virtual U16String GetTextOfMultipleItems() override {
        std::cout << "---------GetMultipleItemsName-------------" << std::endl;
        return u"AsposeGetMultipleItemsName";
    }

    virtual U16String GetTextOfAll() override {
        std::cout << "---------GetAllName-------------" << std::endl;
        return u"AsposeGetAllName";
    }

    virtual U16String GetTextOfColumnLabels() override {
        std::cout << "---------GetColumnLabelsOfPivotTable-------------" << std::endl;
        return u"AsposeGetColumnLabelsOfPivotTable";
    }

    virtual U16String GetTextOfRowLabels() override {
        std::cout << "---------GetRowLabelsNameOfPivotTable-------------" << std::endl;
        return u"AsposeGetRowLabelsNameOfPivotTable";
    }

    virtual U16String GetTextOfEmptyData() override {
        std::cout << "---------GetEmptyDataName-------------" << std::endl;
        return u"(blank)AsposeGetEmptyDataName";
    }

    virtual U16String GetTextOfSubTotal(PivotFieldSubtotalType subTotalType) override {
        std::cout << "---------GetSubTotalName-------------" << std::endl;

        switch(subTotalType) {
            case PivotFieldSubtotalType::Sum:
                return u"AsposeSum";
            case PivotFieldSubtotalType::Count:
                return u"AsposeCount";
            case PivotFieldSubtotalType::Average:
                return u"AsposeAverage";
            case PivotFieldSubtotalType::Max:
                return u"AsposeMax";
            case PivotFieldSubtotalType::Min:
                return u"AsposeMin";
            case PivotFieldSubtotalType::Product:
                return u"AsposeProduct";
            case PivotFieldSubtotalType::CountNums:
                return u"AsposeCount";
            case PivotFieldSubtotalType::Stdev:
                return u"AsposeStdDev";
            case PivotFieldSubtotalType::Stdevp:
                return u"AsposeStdDevp";
            case PivotFieldSubtotalType::Var:
                return u"AsposeVar";
            case PivotFieldSubtotalType::Varp:
                return u"AsposeVarp";
            default:
                return u"AsposeSubTotalName";
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb(srcDir + u"samplePivotTableGlobalizationSettings.xlsx");

    CustomPivotTableGlobalizationSettings customSettings;
    wb.GetSettings().GetGlobalizationSettings()->SetPivotSettings(&customSettings);

    wb.GetWorksheets().Get(0).SetIsVisible(false);

    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);

    pt.SetRefreshDataFlag(true);
    pt.RefreshData();
    pt.CalculateData();
    pt.SetRefreshDataFlag(false);

    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);

    wb.Save(outDir + u"outputPivotTableGlobalizationSettings.pdf", options);

    std::cout << "Pivot table globalization settings applied successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
