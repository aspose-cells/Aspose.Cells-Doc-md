---
title: استخدام وظيفة FormulaText في Aspose.Cells باستخدام C++
linktitle: استخدام وظيفة FormulaText
description: يقدم هذا المقال كيفية استخدام وظيفة FormulaText في مكتبة Aspose.Cells لمعالجة الصيغ في Microsoft Excel. عن طريق تحميل ملف Excel الحالي أو إنشاء ملف Excel جديد ، يمكننا استخدام الطريقة المقدمة من Aspose.Cells للحصول على وتعيين نص الصيغة للخلية والحصول على النتيجة. في النهاية ، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، وظائف FormulaText
type: docs
weight: 60
url: /ar/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

وظيفة FormulaText هي وظيفة Excel 2013 والإصدارات اللاحقة. لا تدعم الإصدارات السابقة مثل Excel 2010 أو 2007 إلخ. كما يوحي اسمها ، فإنها تطبع النص الخاص بالصيغة الموجودة في الخلية المعطاة. سيوضح لك هذا المقال كيفية الاستفادة من هذه الوظيفة باستخدام Aspose.Cells.

{{% /alert %}} 

يوضح الكود المصدري العيني التالي استخدام FormulaText مع Aspose.Cells. يكتب الكود أولاً صيغة في الخلية A1 ثم يطبع نص الصيغة باستخدام FormulaText في الخلية A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
