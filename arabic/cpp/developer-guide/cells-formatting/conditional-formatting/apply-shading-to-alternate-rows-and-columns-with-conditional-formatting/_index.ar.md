---
title: تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي مع C++
linktitle: تطبيق التظليل على الصفوف والأعمدة البديلة
description: كيفية استخدام مكتبة Aspose.Cells في C++ لتطبيق ظلال التنسيق الشرطي على الصفوف والأعمدة البديلة. من خلال ضبط هذه المعايير، لديك مزيد من السيطرة على مظهر وتنسيق الخلايا.
keywords: Aspose.Cells، التنسيق الشرطي، C++، الصفوف البديلة، الأعمدة البديلة، الظلال
type: docs
weight: 30
url: /ar/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

توفر واجهات برمجة التطبيقات Aspose.Cells الوسائل لإضافة وتعديل قواعد التنسيق الشرطي لـ [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) الكائن. يمكن تخصيص هذه القواعد بعدة طرق للحصول على التنسيق المطلوب استنادًا إلى الشروط أو القواعد. ستوضح هذه المقالة استخدام API Aspose.Cells for C++ لتطبيق الظلال على الصفوف والأعمدة البديلة بمساعدة قواعد التنسيق الشرطي ووظائف إكسل المدمجة.

{{% /alert %}}

تستخدم هذه المقالة وظائف Excel المدمجة مثل ROW، COLUMN و MOD. فيما يلي بعض التفاصيل حول هذه الوظائف لفهم أفضل لمقتطف الكود المقدم فيما بعد.

- تقوم الوظيفة **ROW()** بإرجاع رقم الصف لمرجع الخلية. إذا تم تغيير المعامل، يفترض أن المرجع هو عنوان الخلية التي تم إدخال وظيفة ROW فيها.
- تقوم الوظيفة **COLUMN()** بإرجاع رقم العمود لمرجع الخلية. إذا تم تغيير المعامل، يفترض أن المرجع هو عنوان الخلية التي تم إدخال وظيفة COLUMN فيها.
- تقوم وظيفة **MOD()** بإرجاع الباقي بعد قسمة العدد على المقسوم، حيث يكون العدد الأول للوظيفة هو القيمة العددية التي ترغب في العثور على باقيها والمعامل الثاني هو العدد المستخدم للقسمة في المعامل الأول للوظيفة. إذا كان المقسوم هو 0، فسيعيد الخطأ #DIV/0!.

لنبدأ بكتابة بعض الكود لتحقيق هذا الهدف بمساعدة API Aspose.Cells for C++.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

يوضح المثال التالي لقطة للجدول النهائي المحمّل في تطبيق Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

من أجل تطبيق التظليل على الأعمدة البديلة، كل ما عليك فعله هو تغيير الصيغة **=MOD(ROW(),2)=0** إلى **=MOD(COLUMN(),2)=0**، أي؛ بدلاً من الحصول على فهرس الصف، قم بتعديل الصيغة لاسترجاع فهرس العمود. 
جدول البيانات الناتج، في هذه الحالة، سيظهر كما يلي.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
