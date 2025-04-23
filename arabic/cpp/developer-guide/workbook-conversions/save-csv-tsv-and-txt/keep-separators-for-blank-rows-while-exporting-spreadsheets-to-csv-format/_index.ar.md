---
title: الاحتفاظ بالفواصل للفئات الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام C++
linktitle: الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير أوراق الجدول إلى تنسيق CSV
type: docs
weight: 160
url: /ar/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: تعلم كيف تحتفظ بالفواصل للفئات الفارغة عند تصدير الجداول إلى تنسيق CSV باستخدام Aspose.Cells مع C++.
---

## **الاحتفاظ بالفواصل للصفوف الفارغة أثناء تصدير جداول البيانات إلى تنسيق CSV**

توفر Aspose.Cells القدرة على الاحتفاظ بفواصل الأسطر أثناء تحويل جداول البيانات إلى تنسيق CSV. لهذا، يمكنك استخدام خاصية [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) من فئة [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) هي خاصية من نوع boolean. للحفاظ على الفواصل للفقرات الفارغة أثناء تحويل ملف Excel إلى CSV، اضبط الخاصية [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) على **true**.

يعرض الرمز النموذجي التالي تحميل ملف Excel [المصدر](84378743.xlsx). حيث يضبط الخاصية [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) على **true** ويحفظه كـ [ملف CSV الناتج](84378744.csv). تظهر الصورة المجمعة المقارنة بين ملف Excel المصدر، والناتج الافتراضي عند تحويل ورقة العمل إلى CSV، والناتج الناتج عن ضبط [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) على **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **الكود المثالي**

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
