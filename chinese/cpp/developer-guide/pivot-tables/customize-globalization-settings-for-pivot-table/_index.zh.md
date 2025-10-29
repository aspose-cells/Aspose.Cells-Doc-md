---
title: 用C++自定义数据透视表的全球化设置
linktitle: 自定义数据透视表的全球化设置
type: docs
weight: 50
url: /zh/cpp/customize-globalization-settings-for-pivot-table/
description: 学习如何使用Aspose.Cells for C++自定义数据透视表的全球化设置。
---

## **可能的使用场景**

有时你想根据需要自定义*总计、子总计、总览、小计、多选项、列标签、行标签、空值*的文本。Aspose.Cells for C++允许你自定义数据透视表的全球化设置，以应对这些场景。你还能使用此功能将标签更改为阿拉伯语、印地语、波兰语等其他语言。

## **自定义数据透视表的全球化设置**

以下示例代码说明如何为 C++ 中的数据透视表自定义全球化设置。它创建一个派生自 [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.settings/pivotglobalizationsettings/) 基类的类 *CustomPivotTableGlobalizationSettings*，并重写所有必要的方法。这些方法返回各种数据透视表元素的自定义文本。然后，代码将此实现分配给 [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) 属性。示例加载一个 [源 Excel 文件](40468488.xlsx)，刷新数据透视表并保存为 [输出 PDF](40468487.pdf)。下方截图显示了输出中的自定义标签。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

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
{{< app/cells/assistant language="cpp" >}}
