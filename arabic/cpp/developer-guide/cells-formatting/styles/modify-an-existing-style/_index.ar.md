---
title: تعديل نمط موجود باستخدام C++
description: مكتبة Aspose.Cells هي مكتبة C++ للعمل مع ملفات الجدول الإلكتروني تتيح تعديل أنماط الخلايا الموجودة. ستوضح هذه المقالة كيفية تعديل نمط خلية موجود باستخدام مكتبة Aspose.Cells بحيث يمكن للمستخدمين تغيير مظهر الخلايا حسب الحاجة.
keywords: تعديل الأنماط الموجودة، تخصيص مظهر وشكل تطبيقك، دليل، تعليمات، مساعدة، وثائق التطوير، مستندات واجهة برمجة التطبيقات، رمز عينة، تنزيلات، الدعم.
type: docs
weight: 90
url: /ar/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

لتطبيق نفس الخيارات التنسيق على الخلايا، قم بإنشاء كائن نمط التنسيق جديد. كائن نمط التنسيق هو مزيج من الخصائص التنسيقية مثل الخط، حجم الخط، البدء، الرقم، الحدود، الأنماط الخطية وما إلى ذلك، مسمى ومخزن كمجموعة. عند التطبيق، يتم تطبيق كل من التنسيق في ذلك النمط.

يمكنك أيضا استخدام نمط موجود، حفظه مع الدفتر واستخدامه لتنسيق المعلومات بنفس السمات.

عندما لا تتم تنسيق الخلايا بشكل صريح، يتم تطبيق النمط العادي (نمط الافتراضي للدفتر). Microsoft Excel يعرف مسبقا العديد من الأنماط بالإضافة إلى النمط العادي بما في ذلك Comma و Currency و Percent.

تسمح Aspose.Cells بتعديل أي من هذه الأنماط أو أي نمط آخر تعرفه بالسمات المرغوبة.

{{% /alert %}}

## **استخدام Microsoft Excel**

لتحديث نمط في Microsoft Excel 97-2003:

1. في قائمة **تنسيق**، انقر على **نمط**.
1. حدد النمط الذي تريد تعديله من قائمة **اسم النمط**.
1. انقر على **تعديل**.
1. اختر خيارات النمط التي تريدها باستخدام علامات التبويب في مربع حوار تنسيق الخلايا.
1. انقر على **موافق**.
1. في **يتضمن النمط**, حدد ميزات النمط التي تريدها.
1. انقر **موافق** لحفظ النمط وتطبيقه على النطاق المحدد.

## **استخدام Aspose.Cells**

 توضح الأمثلة التالية كيفية استخدام طريقة [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/).

### **إنشاء وتعديل نمط**

يتم إنشاء كائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)، وتطبيقه على نطاق من الخلايا وتعديل كائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). يتم تطبيق التعديلات تلقائيًا على الخلية والنطاق الذي تم تطبيق النمط عليه.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تعديل نمط موجود**

يستخدم هذا المثال ملف Excel قالبي بسيط تم تطبيق نمط يُسمى النسبة على نطاق معين بالفعل. المثال:

1. يستلم النمط,
1. ينشئ كائن نمط و
1. يعدل تنسيق النمط.

يتم تطبيق التعديلات تلقائيًا على النطاق الذي تم تطبيق النمط عليه.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
