---
title: كيفية تغيير لون خط التعليق باستخدام C++
linktitle: كيفية تغيير لون الخط في التعليق
type: docs
weight: 180
url: /ar/cpp/how-to-change-the-comment-font-color/
description: تعلم كيفية تخصيص لون خط التعليق في Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بإضافة تعليقات إلى الخلايا لإضافة معلومات إضافية وتسليط الضوء على البيانات. قد تحتاج المطورون إلى تخصيص التعليق لتحديد إعدادات المحاذاة واتجاه النص ولون الخط وما إلى ذلك. توفر Aspose.Cells واجهات برمجة التطبيقات لإنجاز المهمة.

{{% /alert %}} 

تقدم Aspose.Cells خاصية [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) لضبط لون خط التعليق. يوضح الكود النموذجي التالي استخدام خاصية [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) لضبط اتجاه النص لتعليق ما.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some text in cell A1
    worksheet.GetCells().Get(u"A1").PutValue(u"Here");

    // Add a comment to A1 cell
    int commentIndex = worksheet.GetComments().Add(u"A1");
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is Test.");

    // Get the comment shape
    Shape shape = comment.GetCommentShape();

    // Set the fill color of the shape to black
    shape.GetFill().GetSolidFill().SetColor(Color::Black());

    // Get the font of the shape
    Font font = shape.GetFont();

    // Set the font color to white
    font.SetColor(Color::White());

    // Create a StyleFlag to apply font color changes
    StyleFlag styleFlag;
    styleFlag.SetFontColor(true);

    // Apply the font color changes to the shape's text
    shape.GetTextBody().Format(0, shape.GetText().GetLength(), font, styleFlag);

    // Save the Excel file
    workbook.Save(outDir + u"outputChangeCommentFontColor.xlsx");

    Aspose::Cells::Cleanup();
}
```

الملف الناتج (102662195.xlsx) الذي تم إنشاؤه بواسطة الكود أعلاه مرفق للرجوع إليه.
{{< app/cells/assistant language="cpp" >}}
