--- 
title: نسخ نطاقات إكسل باستخدام C++ 
linktitle: نسخ النطاقات 
type: docs 
weight: 105 
url: /ar/cpp/copy-ranges-of-excel/ 
description: تعلم كيفية نسخ النطاقات في إكسل باستخدام Aspose.Cells مع C++. 
--- 

## **مقدمة**

في اكسل، يمكنك تحديد نطاق، ونسخ النطاق، ثم لصقه بخيارات محددة إلى نفس ورقة العمل، أوراق العمل الأخرى، أو ملفات أخرى.

## **نسخ النطاقات باستخدام Aspose.Cells**

يسمح Aspose.Cells ببعض التحميلات الزائدة [Range.Copy](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) لنسخ النطاق. و [Range.CopyStyle](https://reference.aspose.com/cells/cpp/aspose.cells/range/copystyle/) لنسخ نمط النطاق فقط؛ [Range.CopyData](https://reference.aspose.com/cells/cpp/aspose.cells/range/copydata/) لنسخ قيمة النطاق فقط.

## **نسخ النطاق**

إنشاء نطاقين: النطاق المصدر، النطاق الهدف، ثم نسخ النطاق المصدر إلى النطاق الهدف باستخدام طريقة نطاق.نسخ.

انظر الكود التالي:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into
    // A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy source range to target range in the same worksheet 
    targetRange.Copy(sourceRange);

    // Create a new worksheet.
    worksheets.Add();
    worksheet = worksheets.Get(1);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another worksheet 
    targetRange.Copy(sourceRange);

    // Copy to another workbook
    Workbook anotherWorkbook;

    worksheet = workbook.GetWorksheets().Get(0);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another workbook 
    targetRange.Copy(sourceRange);

    std::cout << "Copy operations completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **لصق النطاق مع الخيارات**

تدعم Aspose.Cells لصق النطاق بنوع محدد.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Init paste options.
    PasteOptions options;
    // Set paste type.
    options.SetPasteType(PasteType::ValuesAndFormats);
    options.SetSkipBlanks(true);

    // Copy source range to target range
    targetRange.Copy(sourceRange, options);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **نسخ بيانات النطاق فقط**
أيضا يمكنك نسخ البيانات مع طريقة نطاق.نسخالبيانات كما في الشفرات التالية:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // A few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(123);

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy the data of source range to target range
    targetRange.CopyData(sourceRange);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [نسخ أطوال الصفوف من النطاق المصدر إلى النطاق الهدف](/cells/ar/cpp/copy-row-heights-of-source-range-to-destination-range/)
{{< app/cells/assistant language="cpp" >}}
