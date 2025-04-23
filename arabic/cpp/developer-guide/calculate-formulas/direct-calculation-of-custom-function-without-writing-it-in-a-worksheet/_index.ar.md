---
title: حساب مباشر لوظيفة مخصصة دون كتابتها في ورقة عمل باستخدام C++
linktitle: حساب مباشر لوظيفة مخصصة
description: تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لحساب الوظائف المخصصة مباشرة في Microsoft Excel دون كتابتها في ورقة عمل. من خلال تحميل ملف Excel القائم أو إنشاء واحد جديد، يمكننا استخدام الطرق المقدمة من Aspose.Cells لحساب الوظيفة المخصصة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، إكسل، وظائف مخصصة، حسابات مباشرة، لا حاجة للكتابة، ورق العمل
type: docs
weight: 90
url: /ar/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **حساب مباشر لوظيفة مخصصة بدون كتابتها في ورقة عمل**

يشرح هذا الموضوع كيف يمكنك حساب وظائفك المخصصة مباشرة دون كتابتها أولاً في ورقة عمل. يرجى استخدام طريقة [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) لهذا الغرض.

يرجى الاطلاع على الشفرة النموذجية التالية التي توضح استخدام هذه الطريقة. استخدمنا وظيفة مخصصة تسمى MyCompany::CustomFunction() ونحسب قيمتها بأنفسنا كـ "Aspose.Cells." ثم يتم دمج هذه القيمة تلقائيًا مع قيمة الخلية A1 وهي "مرحبًا بك في" بواسطة محرك الحساب، وتُرجع القيمة المحسوبة النهائية كـ "مرحبًا بك في Aspose.Cells.". كما يتضح في الشفرة، لم نكتب وظيفتنا المخصصة في أي مكان في ورقة عمل، وهي تحسب مباشرة بواسطة منطقنا المخصص.

### **نموذج برمجة**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ICustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Check the formula name and calculate it yourself
        if (data.GetFunctionName() == u"MyCompany.CustomFunction")
        {
            // This is our calculated value
            data.SetCalculatedValue(Aspose::Cells::Object(u"Aspose.Cells."));
        }
    }
};

class ImplementDirectCalculationOfCustomFunction
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        // Create a workbook
        Workbook wb;

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Add some text in cell A1
        ws.GetCells().Get(u"A1").PutValue(u"Welcome to ");

        // Create a calculation options with custom engine
        CalculationOptions opts;
        opts.SetCustomEngine(new ICustomEngine());

        // This line shows how you can call your own custom function without
        // a need to write it in any worksheet cell
        // After the execution of this line, it will return
        // Welcome to Aspose.Cells.
        Aspose::Cells::Object ret = ws.CalculateFormula(u"=A1 & MyCompany.CustomFunction()", opts);

        // Print the calculated value on Console
        std::cout << "Calculated Value: " << ret.ToString().ToUtf8() << std::endl;

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementDirectCalculationOfCustomFunction::Run();
    return 0;
}
```

### **مخرجات الوحدة**

فيما يلي إخراج وحدة التحكم للرمز العيني أعلاه.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **مقال ذو صلة**

{{% alert color="primary" %}}

[تطبيق محرك حساب مخصص لتمديد محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
