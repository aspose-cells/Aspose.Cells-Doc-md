---
title: تغيير اتجاه نص التعليق باستخدام C++
linktitle: تم إرفاق [ملف الإخراج](102662195.xlsx) الذي تم إنشاؤه بواسطة الرمز العينة أعلاه للإشارة الخاصة بك.
type: docs
weight: 10
url: /ar/cpp/change-text-direction-of-the-comment/
description: تعلم كيفية تغيير اتجاه نص التعليقات في Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يسمح Microsoft Excel للمستخدمين بإضافة تعليقات إلى الخلايا لإضافة معلومات إضافية وتسليط الضوء على البيانات. قد يحتاج المطورون إلى تخصيص التعليق لتحديد إعدادات التوجيه واتجاه النص. توفر Aspose.Cells واجهات برمجة التطبيقات لإنجاز المهمة.

{{% /alert %}}

تتيح Aspose.Cells خاصية [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) لضبط اتجاه النص لتعليق ما. يوضح الكود النموذجي التالي استخدام خاصية [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) لضبط اتجاه النص لتعليق ما.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add a comment to A1 cell
    int commentIndex = sheet.GetComments().Add(u"A1");
    Comment comment = sheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set its horizontal alignment setting
    comment.GetCommentShape().SetTextHorizontalAlignment(TextAlignmentType::Right);

    // Set the Text Direction - Right-to-Left
    comment.GetCommentShape().SetTextDirection(TextDirectionType::RightToLeft);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is test");

    // Save the Excel file
    U16String outputPath = outDir + u"OutCommentShape.out.xlsx";
    wb.Save(outputPath);

    std::cout << "Comment shape created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
