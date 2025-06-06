---
title: كيفية تنسيق الرقم كعملة باستخدام C++
linktitle: كيفية تنسيق الرقم كعملة
type: docs
weight: 10
url: /ar/cpp/format-number-to-currency/
description: ستقدم لك هذه المقالة كيفية تنسيق الرقم كعملة باستخدام API رقم Aspose.Cells for C++.
keywords: تنسيق الرقم كعملة، إعدادات رقم الخلية، تنسيق الرقم كعملة، إعدادات العملة، تنسيق العملة.
---

## **سيناريوهات الاستخدام المحتملة**
تنسيق الأرقام كعملة في إكسل مهم لعدة أسباب، خاصة عند العمل مع البيانات المالية. إليك سبب فائدته:

1. **توضيح القيم المالية**: يجعل تنسيق الرقم كعملة من الواضح أن القيمة تمثل مالًا. على سبيل المثال، بدلاً من رؤية 1000، والذي يمكن أن يعني أي شيء، يظهر $1,000 بوضوح أن القيمة مبلغ مالي.
1. **يشمل رموز العملة**: عند التعامل مع عملات دولية أو متعددة، يوفر تنسيق الأرقام برمز العملة المناسب (مثل $, €, £) توضيح نوع العملة المستخدمة، مما يقلل من الالتباس في التقارير أو المعاملات المالية متعددة الجنسيات.
1. **يعزز العرض الاحترافي**: تظهر القيم المالية بشكل منقح ومهني، وهو أمر مهم بشكل خاص للتقارير والعروض والوثائق التجارية. $10,000.00 تبدو أكثر مصداقية وتنظيمًا من رقم عادي 10000.
1. **تحسين قابلية القراءة**: يضيف تنسيق العملة فواصل الآلاف والأماكن العشرية، مما يجعل الأرقام الكبيرة أسهل في القراءة. على سبيل المثال، يصبح 1000000 على شكل $1,000,000.00، والذي يكون أكثر قابلية للفهم بسرعة.
1. **ضمان الاتساق**: من خلال تطبيق تنسيق عملة متسق، تضمن عرض جميع القيم النقدية في مجموعة البيانات بنفس التنسيق. هذا الاتساق مهم للدقة المالية وللتواصل المهني، خاصة في جداول بيانات كبيرة تحتوي على العديد من الأرقام.
1. **إظهار الدقة**: عادةً ما يتضمن تنسيق العملة مكانين عشريين، مما يسهل رؤية المبالغ المالية الدقيقة. على سبيل المثال، $100.50 يختلف بوضوح عن $100.00، وهو مهم في التقارير المالية حيث تتعلق الدقة بالأمر.
1. **تبسيط الحسابات المالية**: عند إجراء حسابات مالية (مثل جمع الإجماليات أو حساب المتوسط)، يساعد تنسيق العملة Excel والمستخدمين على فهم أن البيانات عبارة عن مبالغ مالية. يساعد Excel على تطبيق تنسيق مناسب في الصيغ والوظائف، وضمان استمرارية النتائج.
1. **تقليل سوء التفسير**: بدون تنسيق العملة، قد تُفسر الأرقام بشكل خاطئ على أنها قيم رقمية عامة بدلاً من مبالغ مالية. على سبيل المثال، يمكن اعتقاد أن 500 هو عدد العناصر أو الوحدات، في حين أن $500.00 يمثل بوضوح مبلغًا ماليًا.
1. **يعمل مع ميزات المحاسبة**: يتوافق تنسيق العملة بشكل جيد مع وظائف المحاسبة في Excel، مثل الميزانيات أو تقارير التدفقات النقدية. يجعل القيم أسهل في الاستخدام في البيانات المالية التي تكون النقود محورًا رئيسيًا.
<br>
باختصار، يساعد تنسيق الأرقام كعملة على تمييز القيم المالية عن الأنواع الأخرى من الأرقام، ويزيد من الوضوح، ويسهل تفسير البيانات، خاصة في السياقات المالية.

## **كيفية تنسيق الرقم إلى عملة في Excel**
ل تنسيق الأرقام كعملة في Excel، اتبع الخطوات التالية:

### **باستخدام خيار تنسيق العملة**
1. حدد الخلايا التي تريد تنسيقها كعملة.
1. انتقل إلى علامة التبويب الصفحة الرئيسية على الشريط.
1. في مجموعة الأرقام، انقر على السهم المنسدل بجانب مربع تنسيق الأرقام (قد يعرض "عام" بشكل افتراضي).
<br>
<img src="1.png" width=60% />
1. اختر العملة من القائمة.

### **استخدام مربع حوار تنسيق الخلايا**
1. حدد الخلايا التي تريد تنسيقها.
1. انقر بزر الماوس الأيمن على الخلايا المحددة واختر تنسيق الخلايا لفتح مربع الحوار تنسيق الخلايا.
1. في علامة التبويب الرقم، اختر العملة من القائمة على اليسار.
<br>
<img src="2.png" width=60% />
1. يمكنك تخصيص التالي: أماكن الفاصلة العشرية، الرمز، الأرقام السالبة.
1. انقر موافق لتطبيق التنسيق.

## **كيفية تنسيق الرقم إلى عملة في Aspose.Cells**

لتنسيق الأرقام كعملة في مكتبة Aspose.Cells for C++ للعمل مع ملفات Excel، يمكنك تطبيق تنسيق العملة على الخلايا برمجياً. إليك كيفية القيام بذلك باستخدام C++ مع Aspose.Cells:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the currency format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value to the cell
    a1.PutValue(1234.56);

    // Create a style object to apply the currency format
    Style a1Style = a1.GetStyle();
    // "7" is the currency format in Excel
    a1Style.SetNumber(7);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(3456.78);

    // Create a style object to apply the currency format
    Style a2Style = a2.GetStyle();
    // Custom format for dollar currency
    a2Style.SetCustom(u"$#,##0.00");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"CurrencyFormatted.xlsx");

    std::cout << "Workbook saved successfully with currency formatting!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
