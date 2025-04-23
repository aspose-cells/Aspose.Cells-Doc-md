---
title: الحصول على التحذيرات بشأن استبدال الخط أثناء عرض ملف إكسل باستخدام C++
linktitle: الحصول على تحذيرات استبدال الخط
type: docs
weight: 230
url: /ar/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: تعلم كيفية الحصول على تحذيرات استبدال الخط عند تحويل ملفات Excel إلى PDF باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، عند تقديم ملف Microsoft Excel إلى PDF، يقوم Aspose.Cells بتبديل الخطوط. توفر Aspose.Cells ميّزة تتيح للمطورين معرفة ما إذا كانت خطوط معينة قد تم تبديلها عن طريق إطلاق تحذير. هذه ميزة مفيدة يمكن أن تساعدك في تحديد سبب تباين ملف PDF الناتج من Aspose.Cells عن ملف Microsoft Excel الأصلي بحيث يمكنك اتخاذ الإجراءات اللازمة. على سبيل المثال، تثبيت الخطوط المفقودة حتى تبدو نتائج التقديم متطابقة.

{{% /alert %}}

للحصول على تحذيرات استبدال الخط عند تحويل ملفات Excel إلى PDF، قم بتنفيذ واجهة `IWarningCallback` واضبط الخاصية `PdfSaveOptions.WarningCallback` بواجهتك المنفذة.

تظهر اللقطة الشاشية أدناه ملف Excel مصدري سنستخدمه في الكود التالي. يحتوي على بعض النص في الخلايا A6 وA7 بخطوط لا تتميز بالتقديم الجيد بواسطة Microsoft Excel.

|**لا تتم تقديم جميع الخطوط بشكل صحيح**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

ستقوم Aspose.Cells بتعويض الخطوط في الخلايا A6 و A7 بخطوط مناسبة كما يظهر أدناه.

|**خطوط مستبدلة**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **تحميل ملف المصدر وملف PDF الناتج**
يمكنك تنزيل ملف Excel المصدر وملف PDF الناتج من الروابط التالية:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **الكود**
الكود التالي ينفذ `IWarningCallback` ويضبط الخاصية `PdfSaveOptions.WarningCallback` بواجهة التنفيذ. الآن، كلما تم استبدال أي خط في أي خلية، ستقوم Aspose.Cells بإطلاق تحذير داخل طريقة `WarningCallback.Warning()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الناتج**
بعد تحويل ملف Excel الأصلي إلى PDF، يتم إخراج التحذيرات إلى وحدة التحكم في التصحيح كالتالي:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، من الأفضل استدعاء طريقة `Workbook.CalculateFormula` قبل عرض الجدول بصيغة PDF. القيام بذلك سيضمن إعادة حساب القيم المعتمدة على الصيغة، ويتم عرض القيم الصحيحة في PDF.

{{% /alert %}}
