---
title: تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط أدناه التفاصيل باستخدام C++
linktitle: تطبيق الإجمالي الجزئي وتغيير اتجاه الصفوف الجملية تحت البيانات الدقيقة
type: docs
weight: 100
url: /ar/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: تعلم كيفية تطبيق الإجمالي الفرعي وتغيير اتجاه صفوف ملخص المخطط أدناه التفاصيل باستخدام API رقم Aspose.Cells for C++.
keywords: تطبيق الإجمالي الجزئي، إضافة الإجمالي الجزئي، تغيير اتجاه صفوف الملخص الإطاري أدناه، تغيير اتجاه أعمدة الملخص الإطاري إلى اليمين من التفاصيل، إنشاء الإجمالي الجزئي وتغيير اتجاه صفوف الملخص التفصيلي.
---

{{% alert color="primary" %}}

 ستشرح هذه المقالة كيفية تطبيق الإجمالي الفرعي على البيانات وتغيير اتجاه صفوف ملخص المخطط أدناه التفاصيل.

 يمكنك تطبيق الإجمالي الفرعي على البيانات باستخدام طريقة [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/). وتقبل المعلمات التالية:

- **منطقة الخلية** - النطاق الذي سيتم تطبيق الإجمالي عليه
- **التجميع حسب** - الحقل الذي يتم التجميع حسبه، كتعويض صفري مبني
- **الوظيفة** - الوظيفة الإجمالي
- **قائمة الإجمالي** - مصفوفة من الحقول المبنية على التعويض الصفري، تشير إلى الحقول التي يتم إضافة الإجمالي لها
- **استبدال** - يشير إلى ما إذا كنت ترغب في استبدال الإجمالي الفرعي الحالي
- **فواصل الصفحة** - يشير إلى ما إذا كنت ستضيف فاصل صفحة بين المجموعات
- **ملخص أدناه البيانات** - يشير إلى ما إذا كنت ستضيف ملخصًا أسفل البيانات.

أيضًا، يمكنك التحكم في اتجاه **ملخص الصفوف أسفل التفاصيل** للمخطط باستخدام خاصية `Worksheet.Outline.SummaryRowBelow`. يمكنك فتح إعدادات هذا في Microsoft Excel باستخدام **البيانات > المخطط > الإعدادات**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## صور ملفات المصدر والإخراج

تظهر اللقطة الشاشية التالية ملف Excel الأصلي المستخدم في الشفرة المثالية أدناه والذي يحتوي على بعض البيانات في الأعمدة A و B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

تظهر اللقطة الشاشة التالية ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود النموذجي. كما ترون، تم تطبيق الإجمالي إلى النطاق A2:B11 واتجاه المخطط هو صفوف ملخص أدناه للتفاصيل.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## كود C++ لتطبيق الإجمالي الفرعي وتغيير اتجاه الصفوف الملخصة للمخطط

إليك الشيفرة المثالية لتحقيق الإخراج كما هو موضح أعلاه.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the Cells collection in the first worksheet
    Cells cells = worksheet.GetCells();

    // Create a cellarea i.e.., A2:B11
    CellArea ca = CellArea::CreateCellArea(u"A2", u"B11");

    // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, { 1 }, true, false, true);

    // Set the direction of outline summary
    worksheet.GetOutline().SetSummaryRowBelow(true);

    // Save the excel file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
