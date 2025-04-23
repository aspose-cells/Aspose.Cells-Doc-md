---
title: تقليم الصفوف والأعمدة الفارغة في البداية أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام C++
linktitle: تقليم الصفوف والأعمدة الفارغة في البداية
type: docs
weight: 100
url: /ar/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: تعلم كيف تقليم الصفوف والأعمدة الفارغة في البداية أثناء تصدير جداول البيانات إلى تنسيق CSV باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يكون لملف Excel أو CSV الخاص بك أعمدة أو صفوف فارغة في البداية. على سبيل المثال، فكر في السطر التالي:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

هنا تكون الأعمدة الثلاثة الأولى فارغة. عند فتح مثل هذا الملف CSV في Microsoft Excel، فإن Microsoft Excel يتجاهل هذه الأعمدة الرئيسية والصفوف.

بشكل افتراضي، لا تقوم Aspose.Cells بتجاهل الأعمدة والصفوف الفارغة الرائدة عند الحفظ ولكن إذا كنت ترغب في إزالتها تمامًا كما يفعل Microsoft Excel، فإن Aspose.Cells توفر الخاصية  [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/). يرجى ضبطها على **true** ثم سيتم تجاهل كل الصفوف والأعمدة الفارغة الرائدة عند الحفظ.

{{% alert color="primary" %}}

قبل إصدار Aspose.Cells for C++ 20.4، كانت القيمة الافتراضية لـ [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) هي **false**. منذ إصدار 20.4، القيمة الافتراضية لـ [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) هي **true.**

{{% /alert %}}

## **تقليص الصفوف والأعمدة الخالية أثناء تصدير جداول البيانات إلى تنسيق CSV**

الكود النموذجي التالي يقوم بتحميل [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx) الذي يحتوي على عمودين فارغين رائدين. يقوم أولاً بحفظ ملف الإكسيل في تنسيق CSV دون أي تغييرات ومن ثم يضبط الخاصية [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) على **true** ويحفظه مرة أخرى. توضح اللقطة [ملف الإكسيل المصدر](sampleTrimBlankColumns.xlsx)، [ملف CSV الناتج بدون تقليم](outputWithoutTrimBlankColumns.csv)، و[ملف CSV الناتج بالتقليم](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **الكود المثالي**

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
