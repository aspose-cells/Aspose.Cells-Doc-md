---
title: تطبيق محرك حساب مخصص لتمديد محرك الحساب الافتراضي لـ Aspose.Cells باستخدام C++
linktitle: تطبيق محرك حساب مخصص
description: تصف هذه المقالة كيفية توسيع محرك الحساب الافتراضي عن طريق تنفيذ محرك حساب مخصص باستخدام مكتبة Aspose.Cells مع C++. من خلال تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي توفرها Aspose.Cells لتنفيذ محرك حساب مخصص والحصول على النتائج. أخيرًا، نحفظ ملف الإكسل المعدل على القرص.
keywords: Aspose.Cells، إكسل، محرك حساب مخصص، يمدد محرك الحساب الافتراضي، C++
type: docs
weight: 80
url: /ar/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **تنفيذ محرك الحساب المخصص**

Aspose.Cells يمتلك محرك حساب قوي يمكنه حساب معظم صيغ Microsoft Excel تقريبًا. على الرغم من ذلك، يسمح لك أيضًا بتوسيع محرك الحساب الافتراضي مما يمنحك قوة ومرونة أكبر.

يتم استخدام الخصائص والفئات التالية في تنفيذ هذه الميزة.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

ينفذ الكود التالي محرك الحساب المخصص. إنه ينفذ واجهة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) التي تحتوي على طريقة [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/). يتم استدعاء هذه الطريقة ضد جميع الصيغ. ضمن هذه الطريقة، نلتقط وظيفة **اليوم** ونضيف يوم واحد إلى تاريخ النظام. لذا، إذا كان التاريخ الحالي هو 27/07/2023، فسيقوم المحرك المخصص بحساب TODAY() كـ 28/07/2023.

### **نموذج برمجة**

```c++
#include <iostream>
#include <cwctype>
#include "Aspose.Cells.h"
#include <chrono>

using namespace Aspose::Cells;

class CustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        U16String funcName = data.GetFunctionName();
        std::u16string upperName;
        for (int i = 0; i < funcName.GetLength(); ++i)
        {
            upperName.push_back(std::towupper(funcName[i]));
        }
		if (upperName == u"TODAY")
		{
			auto now = std::chrono::system_clock::now();
			std::time_t now_time = std::chrono::system_clock::to_time_t(now);
			std::tm local_tm;

#ifdef _WIN32
			localtime_s(&local_tm, &now_time);
#else
			localtime_r(&now_time, &local_tm);
#endif

            Date today{ local_tm.tm_year + 1900, local_tm.tm_mon + 1, local_tm.tm_mday };
			data.SetCalculatedValue(Date{ today.year, today.month, today.day + 1 });
		}
    }

    bool GetProcessBuiltInFunctions() override { return true; }
};

class ImplementCustomCalculationEngine
{
public:
    static void Run()
    {
        Workbook workbook;
        Worksheet sheet = workbook.GetWorksheets().Get(0);
        Cell a1 = sheet.GetCells().Get(u"A1");
        Style style = a1.GetStyle();
        style.SetNumber(14);
        a1.SetStyle(style);
        a1.SetFormula(u"=TODAY()");
        workbook.CalculateFormula();
        std::cout << "The value of A1 with default calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        CustomEngine engine;
        CalculationOptions opts;
        opts.SetCustomEngine(&engine);
        workbook.CalculateFormula(opts);
        std::cout << "The value of A1 with custom calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }
};

int main()
{
    Aspose::Cells::Startup();
    ImplementCustomCalculationEngine::Run();
    Aspose::Cells::Cleanup();
    return 0;
}

```

### **النتيجة**

يرجى التحقق من إخراج الوحدة لمثال الشفرة أعلاه ، يجب أن يكون قيمة (التاريخ والوقت) لـ A1 مع محرك مخصص بعد يوم واحد عن النتيجة بدون محرك مخصص.

### **مقال ذو صلة**

{{% alert color="primary" %}}

[حساب مباشر لوظيفة مخصصة بدون كتابتها في ورقة عمل](/cells/ar/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
