---
title: إدارة التعليقات والملاحظات باستخدام C++
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/cpp/comments-and-notes/
description: إدراج وإدارة التعليقات أو الملاحظات مع Aspose.Cells for C++.
keywords: إدراج تعليقات، إدراج ملاحظات
---

## **مقدمة**

يتم استخدام التعليقات لإضافة معلومات إضافية إلى الخلايا. يوفر Aspose.Cells طريقتين لإضافة تعليقات إلى الخلايا. الأولى هي إنشاء التعليقات في ملف مصمم يدويًا. يتم استيراد هذه التعليقات بعد ذلك باستخدام Aspose.Cells. الثانية هي إضافة التعليقات باستخدام واجهة برمجة التطبيقات Aspose.Cells أثناء التشغيل. يتناول هذا الموضوع إضافة التعليقات إلى الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيتم أيضًا شرح تنسيق التعليقات.

## **إضافة تعليق**

أضف تعليقًا إلى خلية عن طريق استدعاء الطريقة [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/add/) في تجميعة [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) (المغلفة في الكائن [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). يمكن الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) الجديد من تجميعة [**Comments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/) عن طريق تمرير مؤشر التعليق. بعد الوصول إلى الكائن [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/)، يمكن تخصيص ملاحظة التعليق باستخدام خاصية [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) لكائن [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add a comment to cell "F5"
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Access the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set the comment note
    comment.SetNote(u"Hello Aspose!");

    // Save the Excel file
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات عن طريق تكوين ارتفاعها، وعرضها وإعدادات الخط.

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

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding a comment to "F5" cell
    int32_t commentIndex = worksheet.GetComments().Add(u"F5");

    // Accessing the newly added comment
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Setting the comment note
    comment.SetNote(u"Hello Aspose!");

    // Setting the font size of a comment to 14
    comment.GetFont().SetSize(14);

    // Setting the font of a comment to bold
    comment.GetFont().SetIsBold(true);

    // Setting the height of the font to 10
    comment.SetHeightCM(10);

    // Setting the width of the font to 2
    comment.SetWidthCM(2);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إضافة صورة إلى التعليق**

مع Microsoft Excel 2007، من الممكن أيضًا وضع صورة كخلفية لتعليق الخلية. في Excel 2007، يمكن القيام بذلك من خلال الخطوات التالية. (يلزم أن يكون قد تم بالفعل إضافة تعليق للخلية.)

1. انقر بزر الماوس الأيمن فوق الخلية التي تحتوي على التعليق.
1. حدد **إظهار/إخفاء التعليقات**، وامسح أي نص من التعليق.
1. انقر على الحد للتعليق لتحديده.
1. حدد **تنسيق**، ثم **تعليق**.
1. على علامة تبويب **الألوان والخطوط**، قم بتوسيع قائمة **اللون**.
1. انقر على **ملء الآثار**.
1. على علامة تبويب **الصورة**، انقر على **تحديد صورة**.
1. العثور على الصورة وتحديدها.
1. انقر على **موافق** حتى يتم إغلاق جميع الحوارات.

توفر Aspose.Cells أيضًا هذه الميزة. فيما يلي عينة من الشفرة التي تنشئ ملف XLSX من البداية، مع إضافة تعليق إلى الخلية "A1" وتعيين صورة كخلفية لها.

```c++
#include <Aspose.Cells.h>
#include <fstream>
#include <vector>
#include <iostream>

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);
    CommentCollection comments = sheet.GetComments();

    int32_t commentIndex = comments.Add(0, 0);
    Comment comment = comments.Get(commentIndex);
    comment.SetNote(u"First note.");

    Font commentFont = comment.GetFont();
    commentFont.SetName(u"Times New Roman");

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData;
    std::ifstream file(imagePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (file)
    {
        std::streamsize size = file.tellg();
        file.seekg(0, std::ios::beg);
        imageData.resize(size);
        file.read(reinterpret_cast<char*>(imageData.data()), size);
    }
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));

    CommentShape shape = comment.GetCommentShape();
    shape.GetFill().SetImageData(data);

    U16String outputPath = outDir + u"book1.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook with image comment created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مواضيع متقدمة**
- [تغيير اتجاه النص للتعليق](/cells/ar/cpp/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/cpp/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/cpp/how-to-set-comment-background/)
- [تعليقات متداخلة](/cells/ar/cpp/threaded-comments/)
