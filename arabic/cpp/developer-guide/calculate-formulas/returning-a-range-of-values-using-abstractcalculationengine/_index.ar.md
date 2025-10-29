---
title: إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine مع C++
linktitle: إرجاع مجموعة من القيم باستخدام محرك الحساب النموذجي
description: تقدم هذه المقالة محرك حساب تجريدي يرجع مجموعة من القيم في مايكروسوفت إكسل باستخدام مكتبة Aspose.Cells مع C++. من خلال تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي توفرها Aspose.Cells للحصول على مجموعة من القيم وإرجاع النتيجة. أخيرًا، نحفظ ملف الإكسل المعدل على القرص.
keywords: Aspose.Cells ، Excel ، محرك حسابي نموذجي يرجع سلسلة من القيم
type: docs
weight: 55
url: /ar/cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

توفر Aspose.Cells فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) التي تستخدم لتنفيذ وظائف مخصصة غير مدعومة من قبل Microsoft Excel كوظائف مدمجة.

سيشرح هذا المقال كيفية إرجاع مجموعة القيم من [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

{{% /alert %}}

يوضح الكود التالي استخدام فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) ويعيد مجموعة القيم عبر طريقتها.

إنشاء فئة تحتوي على وظيفة `CalculateCustomFunction`. تنفذ هذه الفئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomFunctionStaticValue : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
		Vector<Object> row1{Object(Date{2015, 6, 12, 10, 6, 30}) ,Object(2)};
        Vector<Object> row2{ Object(3.0) ,Object(U16String(u"Test")) };

        Vector<Vector<Object>> values{ row1 , row2 };

        // Create Object with the 2D Vector and set as calculated value
        Object calculatedValue(values);

        // Set the calculated value in the CalculationData object
        data.SetCalculatedValue(calculatedValue);
    }
};

```

الآن استخدم الوظيفة أعلاه في برنامجك.

```c++
int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    Cell cell = cells.Get(0, 0);
    cell.SetArrayFormula(u"=MYFUNC()", 2, 2);

    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    CalculationOptions calculationOptions;

    // Create and set custom engine with proper memory management
    std::shared_ptr<CustomFunctionStaticValue> customEngine = 
        std::make_shared<CustomFunctionStaticValue>();
    calculationOptions.SetCustomEngine(customEngine.get());

    workbook.CalculateFormula(calculationOptions);

    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);
    workbook.Save(outDir + u"output_out.xlsx");
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
