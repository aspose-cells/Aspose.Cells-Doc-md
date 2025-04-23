---
title: تخصيص إعدادات التوطين لجدول محوري باستخدام C++
linktitle: تخصيص إعدادات العالمية لجدول محوري
type: docs
weight: 50
url: /ar/cpp/customize-globalization-settings-for-pivot-table/
description: تعلم كيفية تخصيص إعدادات التوطين في الجدول المحوري باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 أحيانًا تريد تخصيص نص *المجموع الكلي للجدول المحوري، المجموع الفرعي، المجموع الكلي، جميع العناصر، عناصر متعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة* وفقًا لمتطلباتك. يتيح لك Aspose.Cells for C++ تخصيص إعدادات التوطين للجدول المحوري للتعامل مع مثل هذه السيناريوهات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية، الهندية، البولندية، وغيرها.

## **تخصيص إعدادات العالمية لجدول محوري**

 يوضح الكود النموذجي التالي كيفية تخصيص إعدادات التوطين للجدول المحوري في C++. ينشئ فصل *CustomPivotTableGlobalizationSettings* المشتق من الفصل [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.settings/pivotglobalizationsettings/) ويجاوز جميع الأساليب الضرورية. تُرجع هذه الأساليب نصوصًا مخصصة لمختلف عناصر الجدول المحوري. ثم يُخصص هذا التنفيذ لخاصية [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). يقوم المثال بتحميل [ملف Excel المصدر](40468488.xlsx)، تحديث بيانات الجدول المحوري، وحفظه كـ [ملف PDF المخرجات](40468487.pdf). يُظهر لقطة الشاشة أدناه التسميات المخصصة في الإخراج.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **الكود المثالي**

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
