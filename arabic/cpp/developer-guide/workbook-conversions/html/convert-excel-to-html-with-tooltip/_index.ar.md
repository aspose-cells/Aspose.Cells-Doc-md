---
title: تحويل إكسل إلى HTML مع تلميح باستخدام C++
linktitle: تحويل Excel إلى HTML مع تلميح سريع
type: docs
weight: 200
url: /ar/cpp/convert-excel-to-html-with-tooltip/
description: تحويل إكسل إلى HTML أثناء إضافة تلميحات باستخدام Aspose.Cells باستخدام C++.
---

## **تحويل Excel إلى HTML مع تلميحة**

 قد توجد حالات يتم فيها قطع النص في HTML الناتج وترغب في عرض النص الكامل كتلميح عند التمرير فوقه. تدعم Aspose.Cells ذلك عن طريق توفير خاصية [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/). تعيين الخاصية [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) إلى **true** سيضيف النص الكامل كتلميح في HTML الناتج.

تُظهر الصورة التالية التلميح السريع في ملف HTML المولد.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

الرمز التالي يحمل ملف Excel [المصدر](98107416.xlsx) ويولد ملف HTML [الناتج](98107417.zip) مع أداة التلميح.

الكود المثالي

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
