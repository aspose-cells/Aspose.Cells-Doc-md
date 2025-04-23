---
title: إدراج أو حذف الصفوف في ورقة عمل Excel مع C++
linktitle: إدراج أو حذف الصفوف
type: docs
weight: 20
url: /ar/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: توفر هذه المقالة رمز C++ لإدراج وحذف الصفوف في ورقة عمل Excel.
keywords: إضافة أو حذف الصفوف في C++ في ورقة عمل Excel، إدراج أو حذف الصفوف في Excel باستخدام C++، إدراج صفوف في Excel باستخدام C++، حذف صفوف في Excel باستخدام C++، إدراج أو حذف الصفوف في ورقة عمل Excel باستخدام C++، إدراج أو حذف صفوف في Excel باستخدام C++، إدراج صفوف في Excel باستخدام C++، حذف صفوف في Excel باستخدام C++
---

{{% alert color="primary" %}}

عند إنشاء ورقة عمل جديدة أو العمل مع ورقة عمل موجودة، قد تحتاج في بعض الأوقات إلى إضافة صفوف أو أعمدة إضافية لاستيعاب البيانات. في أوقات أخرى، قد تحتاج إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.

{{% /alert %}}

تقدم Aspose.Cells طريقتين لإدراج الصفوف وحذفها: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) و [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). تم تحسين هذه الطرق لتحقيق أداء ممتاز ولإنجاز المهمة بسرعة كبيرة جدًا.

لإدراج أو إزالة عدد من الصفوف، نوصي دائمًا باستخدام ال[**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) و ال[**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) بدلاً من استخدام ال[**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) أو ال[**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) في حلقة.

تعمل Aspose.Cells بنفس الطريقة التي يعمل بها برنامج Microsoft Excel. عند إضافة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأسفل ولليمين. وعند إزالة صفوف أو أعمدة، يتم نقل محتوى ورقة العمل لأعلى أو لليسار. يتم تحديث أي مراجع في ورقات العمل والخلايا الأخرى عند إضافة أو إزالة الصفوف.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
