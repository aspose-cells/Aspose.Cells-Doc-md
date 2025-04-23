---
title: حذف جدول محوري من ورقة عمل باستخدام C++
linktitle: حذف جدول محوري
type: docs
weight: 60
url: /ar/cpp/delete-pivot-table-from-a-worksheet/
description: الكود C++ لإزالة الجداول المحورية من أوراق عمل Excel باستخدام Aspose.Cells.
keywords: إزالة الجدول المحوري من ورقة عمل باستخدام c++، حذف جدول محوري من Excel، كيفية حذف جدول محوري باستخدام c++، حذف جدول محوري مع c++، حذف جدول محوري من Excel باستخدام c++, حذف جدول محوري، إزالة الجدول المحوري، حذف الجدول المحوري، كيفية حذف الجدول المحوري
---

{{% alert color="primary" %}}

توفر Aspose.Cells ميزة لحذف أو إزالة جدول الدوران من ورقة عمل. يمكنك حذف جدول الدوران باستخدام كائن جدول الدوران أو موضع جدول الدوران. يرجى استخدام الطريقة [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) لحذف جدول الدوران باستخدام كائن جدول الدوران والطريقة [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) لحذف كائن جدول الدوران باستخدام موضعه داخل مجموعة جدول الدوران.

{{% /alert %}}

 يزيل المقتطف التالي جدولين محوريين من ورقة العمل. أولاً يزيل الجدول المحوري باستخدام [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/)، ثم يزيل الجدول باستخدام [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
