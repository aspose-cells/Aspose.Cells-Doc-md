---
title: تحديث المراجع في أوراق عمل أخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة عمل باستخدام C++
linktitle: تحديث المراجع في أوراق عمل أخرى
type: docs
weight: 5000
url: /ar/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: تعلم كيف تقوم بتحديث المراجع في أوراق عمل أخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة عمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

عند حذف الأعمدة والصفوف الفارغة في ورقة عمل، تصبح مراجعها في أوراق عمل أخرى غير صالحة. إذا كنت تريد تجنب هذا السلوك والتأكد من تحديث المراجع إلى الورقة الحالية في أوراق عمل أخرى أيضًا، استخدم الخاصية [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) وضبطها على **true**.

{{% /alert %}}

## **تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل**

 يرجى مراجعة رمز العينة التالي وإخراجه في وحدة التحكم. يحتوي الخلية E3 في ورقة العمل الثانية على صيغة `=Sheet1!C3`، والتي تشير إلى الخلية C3 في ورقة العمل الأولى. إذا قمت بضبط الخاصية [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) على **true**، فستتم تحديث هذه الصيغة إلى `=Sheet1!A1` بعد حذف الأعمدة والصفوف الفارغة في ورقة العمل الأولى. ومع ذلك، إذا قمت بضبط الخاصية [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) على **false**، ستظل الصيغة في الخلية E3 من ورقة العمل الثانية `=Sheet1!C3` وتصبح غير صالحة.

### **نموذج برمجة**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Add second sheet with name Sheet2
    wb.GetWorksheets().Add(u"Sheet2");

    // Access first sheet and add some integer value in cell C1
    // Also add some value in any cell to increase the number of blank rows and columns
    Worksheet sht1 = wb.GetWorksheets().Get(0);
    sht1.GetCells().Get(u"C1").PutValue(4);
    sht1.GetCells().Get(u"K30").PutValue(4);

    // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
    Worksheet sht2 = wb.GetWorksheets().Get(1);
    sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
    std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
    DeleteOptions opts;
    opts.SetUpdateReference(true);

    // Delete all blank rows and columns with delete options
    sht1.GetCells().DeleteBlankColumns(opts);
    sht1.GetCells().DeleteBlankRows(opts);

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم الخاصة برمز العينة أعلاه عندما يتم ضبط الخاصية [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) على **true**.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4

{{< /highlight >}}

هذه هي مخرجات وحدة التحكم الخاصة برمز العينة أعلاه عندما يتم ضبط الخاصية [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) على **false**. كما ترى، لم يتم تحديث الصيغة في الخلية E3 من الورقة الثانية، وأصبح قيمة خلية الآن 0 بدلاً من 4، وهو غير صحيح.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
