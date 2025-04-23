---
title: دمج وفك دمج الخلايا باستخدام C++
linktitle: دمج وفك دمج الخلايا
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جدول البيانات، وتدعم دمج وفك دمج الخلايا. ستشرح هذه المقالة كيفية دمج وفك دمج الخلايا باستخدام مكتبة Aspose.Cells، وكيفية تخصيص نمط الخلية المندمجة.
keywords: Aspose.Cells، مكتبة C++، جدول البيانات، دمج الخلايا، فك دمج الخلايا، إعدادات النمط، الأنماط المخصصة
type: docs
weight: 190
url: /ar/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

تدعم Aspose.Cells هذه الميزة ويمكنها أيضًا دمج الخلايا في ورقة العمل. يمكنك فصل أو تقسيم الخلايا المدمجة أيضًا. الإشارة المرجعية للخلية المدمجة هي الإشارة المرجعية للخلية اليسرى العلوية في النطاق المحدد الأصلي.

{{% /alert %}} 

## **مقدمة**
غالبًا ما لا ترغب في نفس عدد الخلايا في كل صف أو عمود. على سبيل المثال، قد ترغب في وضع عنوان في خلية تمتد عبر عدة أعمدة. أو، إذا كنت تقوم بإنشاء فاتورة، قد ترغب في أقل عدد من الأعمدة للمجموع. لدمج خلية واحدة من خلايا أكثر من اثنين، قم بدمجهم. يتيح Microsoft Excel للمستخدمين تحديد الملفات ودمجها لتنظيم جدول البيانات بالطريقة التي يرغبون فيها.

{{% alert color="primary" %}} 

يرجى ملاحظة أنه عند دمج الخلايا، يتم الاحتفاظ بالبيانات فقط في الخلايا اليسرى العلوية. إذا كانت هناك بيانات في الخلايا الأخرى في النطاق، سيتم حذف هذه البيانات.
يعتمد التنسيق على الخلية المرجعية بالمثل، بحيث عندما تدمج الخلايا، يتم تطبيق إعدادات التنسيق للخلية اليسرى العلوية في النطاق على الخلية المدمجة. عند تقسيم الخلية، تحتفظ الخلايا الجديدة بإعدادات تنسيقها الأصلية.

{{% /alert %}} 

## **دمج الخلايا في ورقة العمل**
### **دمج الخلايا في Microsoft Excel**
الخطوات التالية تصف كيفية دمج الخلايا في ورق العمل باستخدام برنامج MS Excel.

1. قم بنسخ البيانات التي تريدها إلى أعلى يسار الخلية ضمن النطاق.
1. حدد الخلايا التي تريد دمجها.
1. لدمج الخلايا في صف أو عمود وتوسيط محتوى الخلية، انقر على أيقونة **دمج وتوسيط** في شريط الأدوات **التنسيق**.

### **دمج الخلايا باستخدام Aspose.Cells**
تحتوي فئة `Aspose::Cells::Cells` على بعض الطرق المفيدة للمهمة. على سبيل المثال، تقوم طريقة `Merge()` بدمج الخلايا في خلية واحدة ضمن النطاق المحدد.

المثال التالي يوضح كيفية دمج الخلايا (C6:E7) في ورق العمل.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **رفع الدمج (تقسيم) الخلايا المدمجة**
### **استخدام Microsoft Excel**
الخطوات التالية تصف كيفية تقسيم الخلايا المدمجة باستخدام Microsoft Excel.

1. حدد الخلية المدمجة.
   عندما يتم دمج الخلايا، يتم تحديد **دمج وتوسيط** في شريط الأدوات **التنسيق**.
1. انقر على **دمج وتوسيط** في شريط الأدوات **التنسيق**.

### **استخدام Aspose.Cells**
تحتوي فئة `Aspose::Cells::Cells` على طريقة تسمى `UnMerge()` والتي تفصل الخلايا إلى حالتها الأصلية. تقوم الطريقة بفصل الخلايا باستخدام مرجع الخلية في نطاق الخلايا المدمجة.

المثال التالي يوضح كيفية تقسيم الخلايا المدمجة (C6). يستخدم المثال الملف الذي تم إنشاؤه في المثال السابق ويقوم بتقسيم الخلايا المدمجة.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [كشف الخلايا المدمجة في ورقة العمل](/cells/ar/cpp/detect-merged-cells-in-a-worksheet/)
