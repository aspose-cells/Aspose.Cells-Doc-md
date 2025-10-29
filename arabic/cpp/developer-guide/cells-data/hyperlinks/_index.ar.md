---
title: إدراج روابط تشعبية في Excel أو OpenOffice باستخدام C++
linktitle: إدارة الروابط التشعبية
type: docs
weight: 45
url: /ar/cpp/insert-hyperlinks-to-excel/
description: كيفية إدراج روابط تشعبية في ملف Excel باستخدام مكتبة Aspose.Cells بدون Microsoft Excel باستخدام C++.
keywords: إدراج الارتباطات التشعبية في Excel، إضافة أو إدراج الارتباطات، إضافة أو إدراج رابط إلى عنوان URL، إضافة أو إدراج رابط إلى خلية، إضافة رابط إلى ملف خارجي
---

{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.
باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 

## **إضافة الروابط المختصرة**
 تسمح Aspose.Cells للمطورين بإضافة روابط تشعبية إلى ملفات Excel إما باستخدام واجهة برمجة التطبيقات أو جداول البيانات المصممة (جداول البيانات التي يتم إنشاؤها يدويًا وتستخدم Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

 توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Excel من Microsoft. تحتوي فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) طرقًا مختلفة لإضافة روابط تشعبية مختلفة إلى ملفات Excel.

## **إضافة رابط إلى عنوان URL**
تحتوي فئة [ورقة العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) على مجموعة [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). كل عنصر في مجموعة [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) يمثل [عنوان URL](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink). أضف روابط تشعبية إلى عناوين URL عن طريق استدعاء طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) من مجموعة [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). تأخذ طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان URL, عنوان عنوان URL.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

في المثال أعلاه، يتم إضافة رابط تشعبي إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة فإن عنوان عنوان URL يتم أيضًا إضافته إلى تلك الخلية الفارغة كقيمتها. إذا لم تكن الخلية فارغة وتمت إضافة رابط تشعبي، فإن قيمة الخلية تبدو كنص عادي. لجعلها تبدو كرابط تشعبي، ضع إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 

## **إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط تشعبية إلى خلايا في نفس ملف إكسل عن طريق استدعاء طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) من مجموعة [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). تعمل طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) لكل من الروابط الداخلية والخارجية. نسخة من الطريقة التحميلية تتخذ المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إضافة رابط إلى ملف خارجي**
من الممكن إضافة روابط تشعبية إلى ملفات إكسل خارجية عن طريق استدعاء طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) من مجموعة [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). تأخذ طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/cpp/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/cpp/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/cpp/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/cpp/get-hyperlinks-in-range/)
{{< app/cells/assistant language="cpp" >}}
