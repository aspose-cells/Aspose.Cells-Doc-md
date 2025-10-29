---
title: التوافق التلقائي للأعمدة والصفوف أثناء تحميل HTML في دفتر العمل باستخدام C++
linktitle: تناسب تلقائي للأعمدة والصفوف أثناء تحميل HTML في مصنف
type: docs
weight: 120
url: /ar/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: تعلم كيفية التوفيق التلقائي للأعمدة والصفوف أثناء تحميل HTML في دفتر العمل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تلائم الأعمدة والصفوف أثناء تحميل ملف HTML داخل كائن المفكرة. يرجى ضبط الخاصية [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) إلى **true** لهذا الغرض.

## **تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل**

الكود النموذجي التالي يقوم أولاً بتحميل HTML النموذجي في Workbook بدون أي خيارات تحميل وحفظه في تنسيق XLSX. ثم يقوم مرة أخرى بتحميل HTML النموذجي في Workbook ولكن هذه المرة، يقوم بتحميل الـ HTML بعد ضبط الخاصية [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) على **true** وحفظه في تنسيق XLSX. يرجى تنزيل كل من ملفات الإكسيل الناتجة، أي [ملف الإكسيل الناتج بدون تناسب الأعمدة والصفوف](outputWithout_AutoFitColsAndRows.xlsx) و [ملف الإكسيل الناتج مع تناسب الأعمدة والصفوف](outputWith_AutoFitColsAndRows.xlsx). اللقطة الشاشية التالية توضح تأثير الخاصية [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) على كل من ملفات الإكسيل الناتجة.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
