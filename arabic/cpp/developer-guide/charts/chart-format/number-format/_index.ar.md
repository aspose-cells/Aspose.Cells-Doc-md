---
title: تعيين رمز تنسيق القيم لمجموعة البيانات في الرسم البياني باستخدام C++
linktitle: تنسيق الأرقام
type: docs
weight: 100
url: /ar/cpp/set-the-values-format-code-of-chart-series/
description: تعلم كيفية تعيين رمز تنسيق القيم لسلسلة الرسم البياني في Aspose.Cells for C++. سيساعدك دليلنا على فهم كيفية تنسيق بيانات سلسلة الرسوم البيانية الخاصة بك باستخدام رمز التنسيق المناسب، مما يتيح لك عرض بياناتك بدقة واحترافية.
keywords: Aspose.Cells for C++، سلسلة الرسوم البيانية، رمز تنسيق القيم، التنسيق، عرض البيانات، الدقة، الاحترافية.
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك تعيين رمز تنسيق القيم لسلسلة الرسوم البيانية باستخدام الخاصية [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/). هذه الخاصية ليست مفيدة فقط للسلاسل المستندة إلى النطاق داخل ورقة العمل، ولكنها تعمل بشكل جيد أيضًا مع السلاسل التي تم إنشاؤها باستخدام مصفوفة من القيم.

## **تعيين رمز تنسيق القيم لسلاسل الرسم البياني**
 يضيف رمز العينة التالي سلسلة في الرسم البياني الفارغ الذي لم يكن لديه سابقًا. يضيف السلسلة باستخدام مصفوفة القيم. بمجرد إضافة السلسلة، يتم تنسيقها بالرمز `$#,##0` باستخدام الخاصية [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) وتتحول الرقم `10000` إلى `$10,000`. تظهر الصورة الملتقطة تأثير الكود على ملف إكسل العينة (51740712.xlsx) وملف إكسل الناتج (51740713.xlsx) بعد التنفيذ.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **الكود المثالي**
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
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
