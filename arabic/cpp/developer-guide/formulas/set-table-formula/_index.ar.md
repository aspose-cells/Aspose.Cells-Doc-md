---
title: نشر الصيغة في جدول أو كائن قائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة باستخدام ++C
linktitle: يحدد صيغة الجدول
type: docs
weight: 260
url: /ar/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: تعلم كيفية نشر الصيغ تلقائيًا في الجداول أو كائنات القائمة عند إدخال بيانات جديدة باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، تريد أن تنتشر صيغة في جدولك أو كائن القائمة تلقائيًا إلى صفوف جديدة أثناء إدخال بيانات جديدة. هذه هي السلوك الافتراضي لمصنفات Microsoft Excel. لتحقيق نفس الوظيفة مع Aspose.Cells، استخدم طريقة [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/).

## **نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة**
يخلق رمز المثال التالي جدول أو كائن قائمة بحيث تنتشر الصيغة في العمود ب تلقائيًا إلى الصفوف الجديدة عند إدخال بيانات جديدة. يرجى التحقق من [ملف إكسل الناتج](5115469.xlsx) الذي تم توليده بهذا الرمز. إذا أدخلت أي رقم في الخلية A3، سترى أن الصيغة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.

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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
