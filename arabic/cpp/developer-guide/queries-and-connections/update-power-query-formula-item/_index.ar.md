---
title: تحديث عنصر صيغة Power Query باستخدام C++
linktitle: تحديث عنصر صيغة Power Query
type: docs
weight: 120
url: /ar/cpp/update-power-query-formula-item/
description: تعلم كيف تقوم بتحديث عناصر صيغة Power Query باستخدام Aspose.Cells for C++ لتعديل مواقع ملفات مصدر البيانات في ملفات إكسل.
---

## **سيناريو الاستخدام**

قد تكون هناك حالات حيث يتم نقل ملفات مصدر البيانات، ويصبح ملف إكسل غير قادر على تحديد الملف. في مثل هذه الحالات، توفر واجهة برمجة التطبيقات Aspose.Cells خيار تحديث عنصر صيغة Power Query باستخدام فئة [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) لتحديث موقع ملف المصدر.

## **تحديث عنصر صيغة Power Query**

توفر واجهة برمجة تطبيقات Aspose.Cells القدرة على تحديث عناصر صيغة Power Query. يوضح مقتطف الكود التالي تحديث موقع ملف مصدر البيانات في ملف إكسل باستخدام الخاصية [**PowerQueryFormulaItem.GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/getvalue/). الملفات المصدرية والإخراجية مرفقة للرجوع إليها.

- [ملف المصدر 1](106364953.xlsx)
- [ملف المصدر 2](106364954.xlsx)
- [ملف الناتج](106364955.xlsx)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SamplePowerQueryFormula.xlsx");
    DataMashup mashupData = workbook.GetDataMashup();

    PowerQueryFormulaCollection powerQueryFormulas = mashupData.GetPowerQueryFormulas();
    for (int i = 0; i < powerQueryFormulas.GetCount(); ++i)
    {
        PowerQueryFormula formula = powerQueryFormulas.Get(i);
        PowerQueryFormulaItemCollection powerQueryFormulaItems = formula.GetPowerQueryFormulaItems();
        for (int j = 0; j < powerQueryFormulaItems.GetCount(); ++j)
        {
            PowerQueryFormulaItem item = powerQueryFormulaItems.Get(j);
            if (item.GetName() == u"Source")
            {
                U16String newValue = u"Excel.Workbook(File.Contents(\"" + srcDir + u"SamplePowerQueryFormulaSource.xlsx" + u"\"), null, true)";
                item.SetValue(newValue);
            }
        }
    }

    workbook.Save(outDir + u"SamplePowerQueryFormula_out.xlsx");
    std::cout << "PowerQueryFormula updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
