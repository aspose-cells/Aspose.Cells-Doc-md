---
title: الحصول على أقصى نطاق في ورقة عمل باستخدام C++
linktitle: الحصول على أقصى مجال في ورقة العمل
type: docs
weight: 360
url: /ar/cpp/get-max-range-in-a-worksheet/
description: تصف هذه المقالة كيفية الحصول على نطاق الحد الأقصى، نطاق البيانات الأقصى، ونطاق العرض الأقصى لملفات Excel باستخدام مكتبة Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

عند قراءة البيانات من ورقة العمل ، نحتاج إلى معرفة المساحة القصوى.

عند نسخ جميع البيانات من ورقة العمل ، نحتاج إلى معرفة المساحة القصوى.

عند تصدير منطقة محددة إلى HTML و PDF، نحتاج إلى معرفة المنطقة القصوى.

تحتوي Aspose.Cells for C++ على طرق مختلفة للعثور على أقصى نطاق في ورقة عمل. 

{{% /alert %}} 

## **الحصول على أقصى مجال**
في Aspose.Cells، إذا تم تهيئة كائنات [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) و [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/)، فسيتم حساب هذه الصفوف والأعمدة ضمن الحد الأقصى للمنطقة، حتى لو لم تكن هناك بيانات في الصفوف أو الأعمدة الفارغة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **الحصول على أقصى مجال للبيانات**
في معظم الحالات ، نحتاج إلى الحصول على جميع المجالات التي تحتوي على جميع البيانات ، حتى لو كانت الخلايا الفارغة خارج المجال مهيأة.
وستُتجاهل الإعدادات الخاصة بالأشكال، والجداول، والجداول المحورية.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **الحصول على أقصى مجال للعرض**
عند تصدير جميع البيانات من ورقة العمل إلى HTML ، PDF ، أو الصور ، نحتاج إلى الحصول على منطقة تحتوي على جميع الكائنات المرئية ، بما في ذلك البيانات والأنماط والرسومات والجداول والجداول المدورة.
توضح الرموز التالية كيفية عرض النطاق العرضي الأقصى في HTML:

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

هنا [ملف اكسل المصدر](Book1.xlsx).
{{< app/cells/assistant language="cpp" >}}
