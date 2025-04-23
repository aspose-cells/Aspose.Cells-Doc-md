---
title: تطبيق التنسيق الشرطي المتقدم باستخدام C++
linktitle: تطبيق التنسيق المشروط المتقدم
description: كيفية استخدام مكتبة Aspose.Cells في C++ لتطبيق التنسيق الشرطي المتقدم. من خلال تعديل هذه المعايير، يمكنك السيطرة بشكل أكبر على مظهر وتنسيق الخلايا.
keywords: Aspose.Cells، التنسيق الشرطي المتقدم، C++، الشرط، التنسيق
type: docs
weight: 70
url: /ar/cpp/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}}

إصدارات Microsoft Excel 2007 والأحدث (2010/2013/2016) توفر بعض الميزات المتقدمة لتنسيق المشروطات. على سبيل المثال، تتيح لك تطبيق تظليل الخلية والحدود والرموز الملونة والسهام والعلمات وتنسيق الخطوط، وما إلى ذلك، مما أصبح متطورًا تمامًا.

{{% /alert %}}

## **تطبيق تنسيق مشروط متقدم إلى ملفات Microsoft Excel**
يمكن للتنسيق المشروط:

- إضافة شريط بيانات مظللة لتحسين الأرقام الأساسية بشكل بصري من خلال تضمين مخطط بياني بسيط في الخلايا.
- تظليل الخلايا تلقائيًا بمقاييس الألوان بناءً على علاقتها بقيم في خلايا أخرى في النطاق. تظليل الإعدادات الافتراضية القيمة الأدنى باللون الأحمر متحركًا صعودًا إلى القيمة الأعلى باللون الأخضر.
- استخدام مجموعات الرموز بالطريقة نفسها كمقاييس الألوان، ولكن بدلاً من تظليل الخلايا، يضيف رموز صغيرة، مثل السهام وأضواء المرور، إلى الخلايا.

تدعم Aspose.Cells بشكل كامل التنسيق المشروط المقدم من Microsoft Excel 2007 والأحدث في تنسيق XLSX على الخلايا في وقت التشغيل. يوضح هذا المثال تمرينًا لأنواع التنسيق المشروط المتقدمة بما في ذلك مجموعات الرموز، أشرطة البيانات، مقاييس الألوان، فترات الزمن، القاع/القمة وقواعد أخرى بمجموعات مختلفة من السمات.

### **حساب اللون المختار من قبل Microsoft Excel لتنسيق المشروط مع المقياس اللوني**
تتيح لك Aspose.Cells حساب اللون الذي اختاره Microsoft Excel عند استخدام تنسيق مشروط بمقياس الألوان في ملف قالب. Consulte el código de ejemplo a continuación para aprender cómo calcular el color seleccionado por Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
