---
title: استخدام خيارات التحقق من الأخطاء مع C++
linktitle: استخدام خيارات التحقق من الأخطاء
type: docs
weight: 140
url: /ar/cpp/use-error-checking-options/
description: في هذا المقال، ستجد رمزًا برمجيًا يستخدم خيارات التحقق من الأخطاء في أوراق عمل إكسل برمجياً باستخدام واجهة برمجة التطبيقات أو المكتبة C++، مثل الأرقام المخزنة كنص.
keywords: رقم المتجر كنص في إكسل باستخدام C++، تحقق من خيارات إكسل C++
---

{{% alert color="primary" %}}

يسمح Microsoft Excel للمستخدمين بتعريف خيارات وقواعد التحقق من الأخطاء. يرى المستخدمون في كثير من الأحيان التحقق من الأخطاء عند إنشاء الصيغ، حيث يوضح مثلث صغير في الزاوية العلوية اليمنى للخلية عند وجود مشكلة في الخلية. يوفر Excel معلومات تساعد المستخدمين على تصحيح المشاكل الشائعة.

{{% /alert %}}

## **أنواع الأخطاء**

الأخطاء التي تعني أن الصيغة لا يمكن أن تُعيد نتيجة - مثل قسمة عدد على صفر - تتطلب اهتماماً فوريًا ويتم عرض قيمة خطأ في الخلية. يُظهر النقر على المثلث الأخضر علامة تعجب، والنقر على ذلك يفتح قائمة الخيارات.

يمكن حل الخطأ باستخدام الخيارات، أو تجاهله. تجاهل الخطأ يعني أن هذا الخطأ لن يظهر في عمليات التحقق من الأخطاء في المستقبل.

يوفر Aspose.Cells ميزات خيارات التحقق من الأخطاء. تدير فئة [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) أنواع مختلفة من التحقق من الأخطاء، على سبيل المثال، الأرقام المخزنة كنصوص، الأخطاء في حساب الصيغ، وأخطاء التحقق. استخدم تعداد [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/) لتعيين التحقق من الخطأ المطلوب.

## **الأرقام المخزنة كنص**

في بعض الأحيان، قد تكون الأرقام مهيأة ومخزنة في الخلايا كنص. يمكن أن يسبب هذا مشاكل في الحسابات أو إنتاج ترتيبات فرز مربكة. الأرقام التي تم تهيئتها كنص تكون محاذية إلى اليسار بدلاً من اليمين في الخلية. إذا لم تُعَد الصيغة التي يجب أن تقوم بعملية رياضية على الخلايا قيمة، فحقق محاذاة في الخلايا التي تشير إليها الصيغة - قد تكون بعض أو كل تلك الخلايا أرقامًا تم تهيئتها كنص.

يمكنك استخدام خيارات التحقق من الأخطاء لتحويل الأرقام المخزنة كنص إلى أرقام حقيقية بسرعة. في Microsoft Excel 2003:

1. على قائمة **الأدوات**، انقر على **خيارات**.
1. حدد علامة التبويب التحقق من الأخطاء.
   خيار **العدد المخزن كنص** يتم التحقق منه بشكل افتراضي.
1. قم بتعطيله.

يوضح الكود المصدري العينة التالي كيفية تعطيل خيار التحقق من الأخطاء للأرقام المخزنة كنص لورقة العمل في ملف XLS القالب باستخدام واجهات برمجة التطبيقات Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
