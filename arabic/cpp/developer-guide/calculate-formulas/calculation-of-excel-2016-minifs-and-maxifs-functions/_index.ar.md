---
title: حساب دوال MINIFS و MAXIFS في إكسل 2016 باستخدام C++
description: تقدم هذه المقالة طريقة استخدام مكتبة Aspose.Cells لحساب دوال MINIFS و MAXIFS في إكسل 2016 باستخدام C++.
keywords: Aspose.Cells، Excel، 2016، وظيفة MINIFS، وظيفة MAXIFS، حساب
type: docs
weight: 300
url: /ar/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **سيناريوهات الاستخدام المحتملة**
يدعم إكسل 2016 دوال MINIFS و MAXIFS. هذه الدوال غير مدعومة في إكسل 2013 أو الإصدارات الأقدم. كما يدعم Aspose.Cells حساب هذه الدوال. ت illustrating كيفية استخدامها في الصورة المأخوذة أدناه. يرجى قراءة التعليقات الحمراء داخل الصورة لمعرفة كيفية عمل هذه الدوال.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **حساب وظائف MINIFS و MAXIFS في Excel 2016**
الشفرة النموذجية التالية تقوم بتحميل [ملف إكسل النموذجي](5115149.xlsx) وتستدعي طريقة [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) لتنفيذ حساب الصيغة عبر Aspose.Cells ثم تحفظ النتائج في [ملف PDF الناتج](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
