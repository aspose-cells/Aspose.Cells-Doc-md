---
title: تنفيذ Cell.FormulaLocal مماثلة لـ Range.FormulaLocal في Excel VBA باستخدام C++
linktitle: تنفيذ Cell.FormulaLocal
type: docs
weight: 30
url: /ar/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: تعلم كيفية تنفيذ Cell.FormulaLocal مماثلة لـ Range.FormulaLocal في Excel باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

قد تكون للمعادلات في Microsoft Excel أسماء مختلفة في لغات أو مناطق أو لهجات مختلفة. على سبيل المثال، تسمى وظيفة **SUM** باسم **SUMME** في اللغة الألمانية. لا يمكن لـ Aspose.Cells العمل مع أسماء الوظائف غير الإنجليزية. في Microsoft Excel VBA، هناك خاصية **Range.FormulaLocal** التي تعيد اسم الوظيفة وفقًا للغتها أو منطقتها. كما يوفر Aspose.Cells أيضًا الخاصية [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) لهذا الغرض. ومع ذلك، ستعمل هذه الخاصية فقط عند تنفيذ الأسلوب [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **تنفيذ Cell.FormulaLocal مماثل لـ Excel VBA Range.FormulaLocal**

يوضح الكود البرنامج النموذجي التالي كيفية تنفيذ [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/). يُعيد الأسلوب اسم الوظيفة المحلية القياسية. إذا كان اسم الوظيفة القياسية هو **SUM**، فإنه يُعيد **UserFormulaLocal_SUM**. يمكنك تغيير الكود وفقًا لاحتياجاتك وإعادة أسماء الوظائف المحلية الصحيحة على سبيل المثال، **SUM** هي **SUMME** في اللغة الألمانية و**TEXT** هي **ТЕКСТ** في اللغة الروسية. يُرجى أيضًا الاطلاع على مخرجات وحدة التحكم في الكود البرنامجي المعطى أدناه للإشارة.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

// Implement GlobalizationSettings class
class GS : public GlobalizationSettings
{
public:
    virtual U16String GetLocalFunctionName(const U16String& standardName) override
    {
        // Change the SUM function name as per your needs.
        if (standardName == u"SUM")
        {
            return u"UserFormulaLocal_SUM";
        }

        // Change the AVERAGE function name as per your needs.
        if (standardName == u"AVERAGE")
        {
            return u"UserFormulaLocal_AVERAGE";
        }

        return u"";
    }
};

void Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal()
{
    // Create workbook
    Workbook wb;

    // Assign GlobalizationSettings implementation class
    wb.GetSettings().SetGlobalizationSettings(new GS());

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access some cell
    Cell cell = ws.GetCells().Get(u"C4");

    // Assign SUM formula and print its FormulaLocal
    cell.SetFormula(u"SUM(A1:A2)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;

    // Assign AVERAGE formula and print its FormulaLocal
    cell.SetFormula(u"=AVERAGE(B1:B2, B5)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
