---
title: تلقائي يناسب الصفوف والأعمدة باستخدام C++
linktitle: ضبط تلقائي للصفوف والأعمدة
type: docs
weight: 20
url: /ar/cpp/autofit-rows-and-columns/
description: يوضح هذا المقال كيفية ضبط تلقائي للصفوف والأعمدة وصفوف الخلايا المدمجة وصفوف في نطاق خلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: ضبط تلقائي للصفوف، ضبط تلقائي للأعمدة، ضبط تلقائي للصف في مجموعة من الخلايا، ضبط تلقائي للصفوف في الخلايا المدمجة
---

{{% alert color="primary" %}}

 يتيح Microsoft Excel للمستخدمين تغيير حجم عرض وارتفاع الخلايا تلقائيًا وفقًا لمحتواها. تتوفر هذه الميزة أيضًا من خلال Aspose.Cells، بحيث يمكن للمطورين ضبط أبعاد الخلية تلقائيًا أثناء التشغيل.

{{% /alert %}}

## **ضبط تلقائي**

تقدم Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تُظهر ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الأساليب لإدارة ورقة العمل. يناقش هذا المقال استخدام فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) لضبط الصفوف أو الأعمدة تلقائيًا.

### **ضبط تلقائي للصف - بسيط**

أبسط طريقة لضبط عرض وارتفاع الصف تلقائيًا هي استدعاء طريقة [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) لفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). تأخذ طريقة [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) مؤشر صف (للصف الذي سيتم تغيير حجمه) كمعامل.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **كيفية ضبط صف تلقائيًا في مجموعة من الخلايا**

 يتكون الصف من العديد من الأعمدة. يسمح Aspose.Cells للمطورين بضبط صف تلقائيًا استنادًا إلى المحتوى في نطاق خلايا داخل الصف عن طريق استدعاء إصدار محمل زائد من طريقة [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/). وهي تأخذ المعاملات التالية:

- **فهرس الصف**, فهرس الصف المراد ضبطه تلقائياً.
- **فهرس العمود الأول**, فهرس العمود الأول للصف.
- **فهرس العمود الأخير**, فهرس العمود الأخير للصف.

 تتحقق طريقة [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) من محتويات جميع الأعمدة في الصف ثم تضبط الصف تلقائيًا.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية ضبط العمود تلقائيًا في مجموعة من الخلايا**

 يتكون العمود من العديد من الصفوف. من الممكن ضبط عمود تلقائيًا استنادًا إلى المحتوى في نطاق خلايا في العمود عن طريق استدعاء إصدار محمل زائد من طريقة [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) يأخذ المعاملات التالية:

- **فهرس العمود**: فهرس العمود الذي سيتم تلائم حجمه تلقائياً.
- **فهرس الصف الأول**: فهرس أول صف في العمود.
- **فهرس الصف الأخير**: فهرس آخر صف في العمود.

 تتحقق طريقة [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) من محتويات جميع الصفوف في العمود ثم تضبط العمود تلقائيًا.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية تلائم حجم الصفوف للخلايا المدمجة**

مع Aspose.Cells، من الممكن ضبط الصفوف تلقائيًا حتى للخلايا التي تم دمجها باستخدام واجهة برمجة التطبيقات [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/). توفر فئة [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) الخاصية [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) التي يمكن استخدامها لضبط صفوف الخلايا المدمجة تلقائيًا. يقبل [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) تعداد [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/) والتي تحتوي على الأعضاء التالية:

- لا شيء: تجاهل الخلايا المدمجة.
- السطر الأول: فقط يوسع ارتفاع الصف الأول.
- السطر الأخير: فقط يوسع ارتفاع الصف الأخير.
- كل سطر: يوسع ارتفاع كل صف.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يمكنك أيضًا محاولة استخدام الإصدارات المحملة الزائدة من طريقتي [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) و[**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) التي تقبل نطاق الصفوف/الأعمدة ونسخة من [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) لضبط الصفوف/الأعمدة المحددة وفقًا لـ [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) المطلوب.

التواقيع للطرق المذكورة سابقًا هي كما يلي:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **مهم معرفته**

{{% alert color="primary" %}}

إذا تم دمج خلية، لن يتم تطبيق طرق الضبط التلقائي، وهو نفس السلوك في مايكروسوفت إكسل. يمكنك تجنب ذلك باستخدام واجهة برمجة التطبيقات auto filter. علاوة على ذلك، إذا كان النص في خلية موجهًا، فلن يتم تطبيق طريقة [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) أيضًا. شيء آخر عليك معرفته هو أن طرق *AutoFit* تستغرق وقتًا. لذا، يجب استدعاؤها بأقل قدر ممكن لضمان كفاءة تطبيقك.

{{% /alert %}}

## **الموضوعات المتقدمة**
- [تلائم حجم الصفوف للخلايا المدمجة](/cells/ar/cpp/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="cpp" >}}
