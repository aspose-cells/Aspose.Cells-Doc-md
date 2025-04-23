---
title: حذف الصفوف والأعمدة الفارغة في ورقة عمل باستخدام C++
linktitle: حذف الصفوف والأعمدة الفارغة في ورقة العمل
type: docs
weight: 300
url: /ar/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: حذف الصفوف والأعمدة الفارغة في ورقة العمل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

من الممكن حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل. هذا مفيد عند إنشاء ملف PDF من ملف Microsoft Excel وترغب في تحويل الصفوف والأعمدة التي تحتوي على بيانات أو كائنات ذات علاقة فقط.

استخدم وسائل Aspose.Cells التالية لحذف الصفوف والأعمدة الفارغة:

1. لحذف الصفوف الفارغة، استخدم الطريقة [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/). يرجى ملاحظة أنه من الضروري للصفوف الفارغة التي سيتم حذفها أن يكون [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) صحيحًا، وأيضًا يجب ألا يكون هناك تعليق مرئي معرف لأي خلية في تلك الصفوف، ولا جدول محوري يتقاطع نطاقه معها.
2. لحذف الأعمدة الفارغة، استخدم الطريقة [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/).

{{% /alert %}}

## كود C++ لحذف الصفوف الفارغة

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## كود C++ لحذف الأعمدة الفارغة

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
