---
title: ضبط وضع حساب الصيغة لدفتر العمل باستخدام C++
linktitle: ضبط وضع حساب الصيغ لسجل العمل
description: تقدم هذه المقالة شرحًا لكيفية ضبط وضع حساب الصيغة في دفتر عمل في مايكروسوفت إكسل باستخدام مكتبة Aspose.Cells باستخدام C++. عن طريق تحميل ملف إكسل موجود أو إنشاء ملف جديد، يمكننا استخدام الطريقة التي توفرها Aspose.Cells لضبط وضع حساب الصيغة والحصول على النتيجة. وأخيرًا، نحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، إكسل، دفتر العمل، وضع حساب الصيغة، الإعدادات، C++
type: docs
weight: 110
url: /ar/cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

يتيح Microsoft Excel لك تعيين وضع حساب الصيغة، أي الطريقة التي يتم بها حساب الصيغ. هناك ثلاثة قيم ممكنة:

- تلقائي - إعادة الحساب كلما تم تغيير شيء ما، وفي كل مرة يتم فيها فتح دفتر العمل.
- تلقائي ما عدا الجداول البيانية - إعادة الحساب كلما تم تغيير شيء ما، ولكن دون الجداول البيانية.
- يدوي - إعادة الحساب فقط عندما يطلب المستخدم ذلك صراحة عن طريق الضغط على F9 أو CTRL+ALT+F9، أو عند حفظ دفتر العمل.

{{% /alert %}}

لتعيين وضع حساب الصيغ في Microsoft Excel:

1. حدد **الصيغ** ثم **خيارات الحساب**.
1. حدد أحد الخيارات.

تسمح Aspose.Cells أيضًا لك بتعيين وضع حساب الصيغة باستخدام [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getcalculationmode/) خاصية الوضع. يمكنك تعيينها لتحقيق [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) التعداد الذي يحتوي على إحدى القيم التالية:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Set the Formula Calculation Mode to Manual
    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);

    // Save the workbook
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with manual calculation mode!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
